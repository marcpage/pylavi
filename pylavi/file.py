"""
    Parses a LabVIEW resource file
"""


import ctypes
import string


class FileStructure(ctypes.BigEndianStructure):
    """Common parent of all structures in the resource file"""

    def to_bytes(self):
        """Get the raw bytes as they are in the file"""
        data = ctypes.create_string_buffer(self.size())
        ctypes.memmove(data, ctypes.addressof(self), self.size())
        return data.raw

    def from_bytes(self, data: bytes, offset: int = 0):
        """Take raw bytes from the file and interpret them.
        offset - the offset in data to start parsing the bytes
        """
        size = self.size()
        subset = data[offset : offset + size]
        assert len(subset) >= size, f"Expected {size} bytes: found {len(subset)}"
        ctypes.memmove(ctypes.addressof(self), subset, size)
        return self

    def size(self) -> int:
        """the number of bytes in the file"""
        return ctypes.sizeof(self)

    def __repr__(self) -> str:
        return self.to_string()

    def __str__(self) -> str:
        return self.to_string()


class FourCharCode(FileStructure):
    """Four-byte ascii code"""

    DISPLAYABLE = (string.ascii_letters + string.digits + " ").encode("ascii")
    _pack_ = 1
    _fields_ = [
        ("b1", ctypes.c_byte),
        ("b2", ctypes.c_byte),
        ("b3", ctypes.c_byte),
        ("b4", ctypes.c_byte),
    ]

    def __init__(self, value: str = None):
        if value is not None:
            value_bytes = value.encode("ascii")
            assert len(value_bytes) == 4
            kwargs = {
                "b1": value_bytes[0],
                "b2": value_bytes[1],
                "b3": value_bytes[2],
                "b4": value_bytes[3],
            }
        else:
            kwargs = {}

        super().__init__(**kwargs)

    def to_string(self):
        """Get the four characters as a string"""
        if any(
            (256 + b) % 256 not in FourCharCode.DISPLAYABLE
            for b in [self.b1, self.b2, self.b3, self.b4]
        ):
            return (
                f"x{(256 + self.b1)%256:02x}"
                + f"{(256 + self.b2)%256:02x}"
                + f"{(256 + self.b3)%256:02x}"
                + f"{(256 + self.b4)%256:02x}"
            )

        return bytes([self.b1, self.b2, self.b3, self.b4]).decode("ascii")

    def __repr__(self) -> str:
        return f"FourCharCode('{self.to_string()}')"

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.to_string() == other

        if isinstance(other, bytes):
            return self.to_bytes() == other

        return (
            self.b1 == other.b1
            and self.b2 == other.b2
            and self.b3 == other.b3
            and self.b4 == other.b4
        )


class Header(FileStructure):
    """Resource header."""

    FILE_TYPES = [
        "LVIN",  # VI
        "LVAR",  # LLB
        "LVCC",  # template VI?
        "LMNU",  # menu
        "LVRS",  # menu
        "LVSB",  # lsb
        "\0\0\0\0",  # menu
        "iUWl",  # LabWindows/CVI user interface resource file .uir
    ]
    FILE_CREATORS = [
        "LBVW",  # usual
        "WLin",  # LabWindows/CVI user interface resource file .uir
        "\0\0\0\0",  # older .uir and .mnu files
    ]
    VERSION = 3
    SIGNATURE = FourCharCode().from_bytes(b"RSRC")
    CORRUPTION_CHECK = b"\r\n"

    _pack_ = 1
    _fields_ = [
        ("file_format", FourCharCode),
        ("corruption_check", ctypes.c_char * 2),
        ("format_version", ctypes.c_short),
        ("file_type", FourCharCode),
        ("file_creator", FourCharCode),
        ("metadata_offset", ctypes.c_uint),
        ("metadata_size", ctypes.c_uint),
        ("data_offset", ctypes.c_uint),
        ("data_size", ctypes.c_uint),
    ]

    def __init__(self, **kwargs):
        assert kwargs.get("file_type", None) is None or isinstance(
            kwargs["file_type"], str
        )
        assert kwargs.get("file_creator", None) is None or isinstance(
            kwargs["file_creator"], str
        )
        kwargs["file_format"] = kwargs.get("file_format", Header.SIGNATURE)
        kwargs["corruption_check"] = kwargs.get(
            "corruption_check", Header.CORRUPTION_CHECK
        )
        kwargs["format_version"] = kwargs.get("format_version", Header.VERSION)
        kwargs["file_type"] = FourCharCode(
            kwargs.get("file_type", Header.FILE_TYPES[0])
        )
        kwargs["file_creator"] = FourCharCode(
            kwargs.get("file_creator", Header.FILE_CREATORS[0])
        )
        kwargs["data_offset"] = kwargs.get("data_offset", self.size())
        super().__init__(**kwargs)

    def to_string(self):
        """String representation of the header"""
        return (
            "{"
            + f"file_type={self.file_type.to_string()}, "
            + f"file_creator={self.file_creator.to_string()}, "
            + f"metadata_offset={self.metadata_offset}, metadata_size={self.metadata_size}, "
            + f"data_offset={self.data_offset}, data_size={self.data_size}"
            + "}"
        )

    def __repr__(self) -> str:
        return f"Header({self.to_string()})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Header):
            return False

        return (
            self.file_type == other.file_type
            and self.file_creator == other.file_creator
            and self.metadata_offset == other.metadata_offset
            and self.metadata_size == other.metadata_size
            and self.data_offset == other.data_offset
            and self.data_size == other.data_size
        )

    def validate(self, file_size: int = None):
        """ensured the header data makes sense"""
        assert (
            self.file_format == Header.SIGNATURE
        ), f"Invalid Signature {self.file_format}"
        assert self.corruption_check == b"\r\n", f"Corrupt {self.corruption_check}"
        assert self.format_version == Header.VERSION, f"Version {self.format_version}"
        assert (
            bytes(self.file_type).decode("ascii") in Header.FILE_TYPES
        ), f"Type {[self.file_type]}"
        assert (
            bytes(self.file_creator).decode("ascii") in Header.FILE_CREATORS
        ), f"Creator {[self.file_creator]}"
        assert (
            self.size() == self.data_offset
        ), f"post-header gap {self.data_offset - self.size()}"
        assert (
            self.data_offset + self.data_size == self.metadata_offset
        ), f"post-data gap {self.metadata_offset - (self.data_offset + self.data_size)}"
        assert self.data_size % 4 == 0
        assert (
            file_size is None or file_size >= self.metadata_offset + self.metadata_size
        ), (
            f"file_size={file_size} expected="
            + f"{self.metadata_offset + self.metadata_size}\n"
            + f"\t metadata offset = {self.metadata_offset}\n"
            + f"\t metadata size = {self.metadata_size}"
        )
        minimum_metadata_size = (
            Header().size()
            + MetadataHeader().size()
            + TypeCount().size()
            + TypeInfo().size()
        )
        assert (
            self.metadata_size >= minimum_metadata_size
        ), f"metadata size too small {self.metadata_size}"
        assert self.metadata_offset == (self.data_offset + self.data_size), (
            f"metadata should be right after data: metadata = {self.metadata_offset}"
            + f" data end = {self.data_offset + self.data_size}"
        )
        return self


class MetadataHeader(FileStructure):
    """header for the metadata section"""

    _pack_ = 1
    _fields_ = [
        ("unused_8", ctypes.c_uint),
        ("unused_16", ctypes.c_uint),
        ("file_header_size", ctypes.c_uint),
        ("metadata_header_size", ctypes.c_uint),
        ("names_offset", ctypes.c_uint),
    ]

    def __init__(self, **kwargs):
        kwargs["unused_8"] = kwargs.get("unused_8", 0)
        kwargs["unused_16"] = kwargs.get("unused_16", 0)
        kwargs["file_header_size"] = kwargs.get("file_header_size", Header().size())
        kwargs["metadata_header_size"] = kwargs.get(
            "metadata_header_size", Header().size() + self.size()
        )
        super().__init__(**kwargs)

    def to_string(self):
        """String representation of the header"""
        return (
            "{"
            + f"unused_8 = {self.unused_8}, "
            + f"unused_16 = {self.unused_16}, "
            + f"file_header_size = {self.file_header_size}, "
            + f"metadata_header_size = {self.metadata_header_size}, "
            + f"names_offset = {self.names_offset}"
            + "}"
        )

    def __repr__(self) -> str:
        return f"MetadataHeader({self.to_string()})"

    def validate(self, file_header: Header, file_size: int):
        """validate that the data makes sense"""
        assert (
            self.file_header_size == Header().size()
        ), f"types header incorrect size: {self.file_header_size}"
        assert (
            self.metadata_header_size == Header().size() + self.size()
        ), f"type info not where it should be {self.metadata_header_size}"
        assert file_size >= (file_header.metadata_offset + self.names_offset), (
            f"File too small {file_size} <"
            + f" {file_header.metadata_offset + self.names_offset}"
            + f" file_header.metadata_offset = {file_header.metadata_offset}"
            + f" names_offset = {self.names_offset}"
        )
        return self


class TypeInfo(FileStructure):
    """Structure for the list of resource types."""

    _pack_ = 1
    _fields_ = [
        ("resource_type", FourCharCode),
        ("resource_count", ctypes.c_uint),
        ("list_offset", ctypes.c_uint),
    ]

    def __init__(
        self,
        resource_type: str = "\0\0\0\0",
        resource_count: int = 1,
        list_offset: int = 0,
    ):
        super().__init__(
            resource_type=FourCharCode(resource_type),
            resource_count=(resource_count - 1),
            list_offset=list_offset,
        )

    def to_string(self):
        """get string values"""
        return (
            "TypeInfo{"
            + f"resource_type = {self.resource_type.to_string()}, "
            + f"resource_count = {self.resource_count} (+1), "
            + f"list_offset = {self.list_offset}"
            + "}"
        )

    def __repr__(self) -> str:
        return f"TypeInfo({self.to_string()})"

    def number_of_resources(self) -> int:
        """Get the number of resources for the given type"""
        return self.resource_count + 1


class TypeCount(FileStructure):
    """Header for the list of type lists."""

    _pack_ = 1
    _fields_ = [
        ("num_types", ctypes.c_uint),
    ]

    def __init__(self, num_types: int = 0):
        super().__init__(num_types=num_types - 1)

    def number_of_types(self) -> int:
        """Get the number of types"""
        return self.num_types + 1


class DataSize(FileStructure):
    """Header for the resource data block."""

    _pack_ = 1
    _fields_ = [
        ("byte_count", ctypes.c_uint),
    ]

    def __init__(self, byte_count: int = 0):
        super().__init__(byte_count=byte_count)


def create_type_list(count: int):
    """Create a structure for a list Resource based on the count found in the type map."""

    class TypeList(FileStructure):
        """Fixed size list of types"""

        _pack_ = 1
        _fields_ = [
            ("type", TypeInfo * count),
        ]

        def to_string(self):
            """Convert to string"""
            return f"[{', '.join(e.to_string() for e in self.type)}]"

        def __repr__(self) -> str:
            return "TypeList({self.to_string()})"

    return TypeList()


class ResourceMetadata(FileStructure):
    """Structure for the RsrcEntry Entry in the resource map."""

    NO_NAME = 0xFFFFFFFF

    _pack_ = 1
    _fields_ = [
        ("resource_id", ctypes.c_uint),
        ("name_offset", ctypes.c_uint),
        ("unused_8", ctypes.c_uint),
        ("data_offset", ctypes.c_uint),
        ("unused_16", ctypes.c_uint),
    ]

    def __init__(self, **kwargs):
        kwargs["unused_8"] = kwargs.get("unused_8", 0)
        kwargs["unused_16"] = kwargs.get("unused_16", 0)
        kwargs["name_offset"] = kwargs.get("name_offset", ResourceMetadata.NO_NAME)
        assert (
            "name_offset" not in kwargs
            or kwargs["name_offset"] % 4 == 0
            or kwargs["name_offset"] == ResourceMetadata.NO_NAME
        )
        assert "data_offset" not in kwargs or kwargs["data_offset"] % 4 == 0
        super().__init__(**kwargs)

    def to_string(self):
        """Convert to a string"""
        return (
            "{"
            + f"resource_id = {self.resource_id}, "
            + f"unused_8 = {self.unused_8}, "
            + f"unused_16 = {self.unused_16}, "
            + f"name_offset = {self.name_offset}, "
            + f"data_offset = {self.data_offset}"
            + "}"
        )

    def __repr__(self) -> str:
        return f"ResourceMetadata({self.to_string()})"


class Resources:
    """Resources from a LabVIEW resource file"""

    EXTENSIONS = [
        ".vi",
        ".vit",
        ".ctl",
        ".ctt",
        ".llb",
        ".vim",
        ".mnu",
        ".uir",
        ".lsb",
        ".rtexe",
        ".gbl",
        ".glb",
    ]

    def __init__(
        self, file_type: str = None, file_creator: str = None, description: list = None
    ):
        self.file_type = file_type
        self.file_creator = file_creator
        self.__resources = description

    def types(self) -> [str]:
        """Get the types contained in the resource file"""
        return list(t[0] for t in self.__resources)

    def count_type(self, resource_type: str) -> int:
        """Get the number of resources of the given type"""
        return sum(len(t[1]) for t in self.__resources if t[0] == resource_type)

    def get_ids(self, resource_type: str) -> [int]:
        """Get the id of the resources"""
        return list(
            r[0] for t in self.__resources if t[0] == resource_type for r in t[1]
        )

    def get_names(self, resource_type: str) -> [int]:
        """Get the names of the resources"""
        return list(
            r[1] for t in self.__resources if t[0] == resource_type for r in t[1]
        )

    def get_resources(self, resource_type: str) -> [(int, str, bytes)]:
        """Gets all resources of a given type with their name and id"""
        return list(
            (r[0], r[1], r[2])
            for t in self.__resources
            if t[0] == resource_type
            for r in t[1]
        )

    def get_resource(
        self, resource_type: str, resource_id: int = None, name: str = None
    ) -> bytes:
        """Get a resource either by name of id"""
        assert resource_id is not None or name is not None

        if name is None:
            return list(
                r[2]
                for t in self.__resources
                if t[0] == resource_type
                for r in t[1]
                if r[0] == resource_id
            )[0]

        return list(
            r[2]
            for t in self.__resources
            if t[0] == resource_type
            for r in t[1]
            if r[1] == name
        )[0]

    @staticmethod
    def __load_file_header(contents: bytes) -> Header:
        return Header().from_bytes(contents).validate(len(contents))

    @staticmethod
    def __validate_2nd_file_header(contents: bytes, header: Header) -> int:
        offset = header.metadata_offset
        second_header = Header().from_bytes(contents[offset:]).validate(len(contents))
        assert (
            second_header == header
        ), f"headers don't match {header} vs {second_header}"
        return offset + second_header.size()

    @staticmethod
    def __load_metadata_header(
        contents: bytes, header: Header, offset: int
    ) -> (int, MetadataHeader):
        metadata_header = (
            MetadataHeader()
            .from_bytes(contents[offset:])
            .validate(header, len(contents))
        )
        offset += metadata_header.size()
        return offset, metadata_header

    @staticmethod
    def __load_typelist(contents: bytes, offset: int) -> any:
        type_count = TypeCount().from_bytes(contents[offset:])
        offset += type_count.size()
        return create_type_list(type_count.number_of_types()).from_bytes(
            contents[offset:]
        )

    @staticmethod
    def __load_resource_name(
        header: Header,
        metadata_header: MetadataHeader,
        resource_info: ResourceMetadata,
        contents: bytes,
    ) -> str:
        if resource_info.name_offset != ResourceMetadata.NO_NAME:
            name_offset = (
                header.metadata_offset
                + metadata_header.names_offset
                + resource_info.name_offset
            )
            name_size = contents[name_offset]
            assert name_size > 0, f"name_size = {name_size}"
            name_offset += 1
            offset_past_name = name_offset + name_size
            return contents[name_offset:offset_past_name]

        return None

    @staticmethod
    def __load_resource(
        header: Header,
        metadata_header: MetadataHeader,
        type_entry: TypeInfo,
        type_index: int,
        contents: bytes,
    ) -> (int, str, bytes):
        base_offset = header.metadata_offset + Header().size() + MetadataHeader().size()
        resource_offset = type_index * ResourceMetadata().size()
        offset = base_offset + type_entry.list_offset + resource_offset
        resource_info = ResourceMetadata().from_bytes(contents[offset:])
        data_offset = header.data_offset + resource_info.data_offset
        data_size = DataSize().from_bytes(contents[data_offset:])
        data_offset += data_size.size()
        offset_past_data = data_offset + data_size.byte_count
        data = contents[data_offset:offset_past_data]
        name = Resources.__load_resource_name(
            header, metadata_header, resource_info, contents
        )
        return resource_info.resource_id, name, data

    @staticmethod
    def load(path: str):
        """Loads the resources from the LabVIEW resource file"""
        with open(path, "rb") as resource_file:
            contents = resource_file.read()

        assert len(contents) >= 2 * Header().size(), "File too small"
        header = Resources.__load_file_header(contents)
        offset = Resources.__validate_2nd_file_header(contents, header)
        offset, metadata_header = Resources.__load_metadata_header(
            contents, header, offset
        )
        data_types = Resources.__load_typelist(contents, offset)
        resource_types = []
        last_offset = 0

        for entry in data_types.type:
            assert entry.list_offset > last_offset, "Unordered type table"
            last_offset = entry.list_offset
            resources = []

            for type_index in range(0, entry.number_of_resources()):
                resources.append(
                    Resources.__load_resource(
                        header, metadata_header, entry, type_index, contents
                    )
                )

            resource_types.append((entry.resource_type.to_string(), resources))

        return Resources(
            file_type=header.file_type,
            file_creator=header.file_creator,
            description=resource_types,
        )


def handle_file(file_path, extensions, types):
    """temporary function that attempts to open a resource file"""
    known_file_extensions = Resources.EXTENSIONS
    extension = os.path.splitext(file_path)[1].lower()

    if extension not in known_file_extensions:
        return

    try:
        resources = Resources.load(file_path)

        for resource_type in resources.types():
            types[resource_type] = types.get(
                resource_type, {"extensions": set(), "types": set()}
            )
            types[resource_type]["extensions"].add(extension)
            types[resource_type]["types"].add(resources.file_type.to_string())

        extensions[extension] = extensions.get(extension, 0) + 1

    except AssertionError as error:
        print(f"{file_path} : {error}")


if __name__ == "__main__":
    import os
    import sys
    import time

    seen_extensions = {}
    all_resource_types = {}
    start = time.time()

    for argument in sys.argv[1:]:
        if os.path.isfile(argument):
            handle_file(argument, seen_extensions, all_resource_types)
        else:
            for root, dirs, files in os.walk(sys.argv[1]):
                for file in files:
                    handle_file(
                        os.path.join(root, file), seen_extensions, all_resource_types
                    )

    total = sum(seen_extensions.values())
    assert total > 0, "No actual resource files found"
    duration = time.time() - start
    print(
        "\n".join(
            f"{s}: {100*seen_extensions[s]/total:0.1f}%"
            for s in sorted(
                seen_extensions, reverse=True, key=lambda x: seen_extensions[x]
            )
        )
    )
    print(
        f"{total} resource files in {duration:0.1f} seconds {total/duration:0.2f} files/sec"
    )
    print("Resource Types")
    print(
        "\n".join(
            f"## {t} "
            + f"(extensions = {', '.join(all_resource_types[t]['extensions'] - {None})}, "
            + f"file types = {', '.join(all_resource_types[t]['types'] - {None})})"
            for t in sorted(all_resource_types)
        )
    )
