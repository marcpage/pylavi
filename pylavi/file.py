"""
    Parses a LabVIEW resource file
"""


from pylavi.data_types import Structure, Array, FourCharCode, PString, UInt16, UInt32


# pylint: disable=no-member
class Header(Structure):
    """Resource header."""

    FILE_TYPES = [
        "LVIN",  # VI
        "LVAR",  # LLB
        "LVCC",  # template VI?
        "LMNU",  # menu
        "LVRS",  # menu
        "LVSB",  # lsb
        "\\x00\\x00\\x00\\x00",  # menu
        "iUWl",  # LabWindows/CVI user interface resource file .uir
    ]
    FILE_CREATORS = [
        "LBVW",  # usual
        "WLin",  # LabWindows/CVI user interface resource file .uir
        "\\x00\\x00\\x00\\x00",  # older .uir and .mnu files
    ]
    VERSION = 3
    SIGNATURE = FourCharCode().from_bytes(b"RSRC")
    CORRUPTION_CHECK = b"\r\n"

    def __init__(self, file_type: str = None, file_creator: str = None):
        file_type = file_type or Header.FILE_TYPES[0]
        file_creator = file_creator or Header.FILE_CREATORS[0]
        super().__init__(
            "file_format",
            FourCharCode(),
            "corruption_check",
            UInt16(),
            "format_version",
            UInt16(),
            "file_type",
            FourCharCode(file_type),
            "file_creator",
            FourCharCode(file_creator),
            "metadata_offset",
            UInt32(),
            "metadata_size",
            UInt32(),
            "data_offset",
            UInt32(),
            "data_size",
            UInt32(),
        )

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

    def validate(self, file_size: int = None):
        """ensured the header data makes sense"""
        assert (
            self.file_format == Header.SIGNATURE
        ), f"Invalid Signature {self.file_format}"
        assert self.corruption_check == b"\r\n", f"Corrupt {self.corruption_check}"
        assert self.format_version == Header.VERSION, f"Version {self.format_version}"
        assert (
            self.file_type.to_value() in Header.FILE_TYPES
        ), f"Type {[self.file_type]}"
        assert (
            self.file_creator.to_value() in Header.FILE_CREATORS
        ), f"Creator {[self.file_creator]}"
        assert (
            self.size() == self.data_offset
        ), f"post-header gap {self.data_offset - self.size()}"
        assert (
            self.data_offset + self.data_size == self.metadata_offset
        ), f"post-data gap {self.metadata_offset - (self.data_offset + self.data_size)}"
        assert self.data_size.value % 4 == 0
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
            + UInt32().size()
            + TypeInfo().size()
        )
        assert (
            self.metadata_size.value >= minimum_metadata_size
        ), f"metadata size too small {self.metadata_size}"
        assert self.metadata_offset == (self.data_offset + self.data_size), (
            f"metadata should be right after data: metadata = {self.metadata_offset}"
            + f" data end = {self.data_offset + self.data_size}"
        )
        return self


class MetadataHeader(Structure):
    """header for the metadata section"""

    def __init__(self):
        header_size = Header().size()
        super().__init__(
            "unused_8",
            UInt32(0),
            "unused_16",
            UInt32(0),
            "file_header_size",
            UInt32(header_size),
            "metadata_header_size",
            UInt32(),
            "names_offset",
            UInt32(),
        )
        self.metadata_header_size.value = header_size + self.size()

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
        assert file_size >= (
            file_header.metadata_offset.value + self.names_offset.value
        ), (
            f"File too small {file_size} <"
            + f" {file_header.metadata_offset + self.names_offset}"
            + f" file_header.metadata_offset = {file_header.metadata_offset}"
            + f" names_offset = {self.names_offset}"
        )
        return self


class TypeInfo(Structure):
    """Structure for the list of resource types."""

    def __init__(
        self,
        resource_type: str = "\0\0\0\0",
        resource_count: int = 1,
        list_offset: int = 0,
    ):
        super().__init__(
            "resource_type",
            FourCharCode(resource_type),
            "resource_count",
            UInt32(resource_count - 1),
            "list_offset",
            UInt32(list_offset),
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


class TypeList(Array):
    """Fixed size list of types"""

    def __init__(self, *elements, length: int = 0):
        assert not elements or all(isinstance(e, TypeInfo) for e in elements)
        super().__init__(TypeInfo, *elements, data_count=length)

    def from_bytes(self, data: bytes, offset: int = 0):
        """fill in data from bytes"""
        length = UInt32().from_bytes(data, offset) + 1
        offset += UInt32().size()
        assert offset + length * TypeInfo().size() <= len(data), [
            offset,
            length,
            offset + length * TypeInfo().size(),
            len(data),
            data,
        ]
        self.set_length(length)
        super().from_bytes(data, offset)
        return self

    def to_bytes(self) -> bytes:
        """get the binary version"""
        return UInt32(self.length() - 1).to_bytes() + super().to_bytes()

    def __repr__(self):
        return f"TypeList({', '.join(repr(v) for v in self.value)})"


class ResourceMetadata(Structure):
    """Structure for the RsrcEntry Entry in the resource map."""

    NO_NAME = 0xFFFFFFFF

    def __init__(
        self, res_id: int = None, name_offset: int = None, data_offset: int = None
    ):
        super().__init__(
            "resource_id",
            UInt32(res_id),
            "name_offset",
            UInt32(ResourceMetadata.NO_NAME if name_offset is None else name_offset),
            "unused_8",
            UInt32(0),
            "data_offset",
            UInt32(data_offset),
            "unused_16",
            UInt32(0),
        )
        assert (
            self.name_offset.value is None
            or self.name_offset.value % 4 == 0
            or self.name_offset.value == ResourceMetadata.NO_NAME
        )
        assert self.data_offset.value is None or self.data_offset.value % 4 == 0

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


class ResourceList(Array):
    """Fixed size list of types"""

    def __init__(self, *elements, length: int = 0):
        assert not elements or all(isinstance(e, ResourceMetadata) for e in elements)
        super().__init__(ResourceMetadata, *elements, data_count=length)

    def __repr__(self):
        return f"ResourceList({', '.join(repr(v) for v in self.value)})"


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
            r[0].value for t in self.__resources if t[0] == resource_type for r in t[1]
        )

    def get_names(self, resource_type: str) -> [str]:
        """Get the names of the resources"""
        return list(
            r[1] for t in self.__resources if t[0] == resource_type for r in t[1]
        )

    def get_resources(self, resource_type: str) -> [(int, str, bytes)]:
        """Gets all resources of a given type with their name and id"""
        return list(
            (r[0].value, r[1], r[2])
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

        with_name = list(
            r[2]
            for t in self.__resources
            if t[0] == resource_type
            for r in t[1]
            if r[1] == name.encode("ascii")
        )
        return None if not with_name else with_name[0]

    @staticmethod
    def __load_file_header(contents: bytes) -> Header:
        return Header().from_bytes(contents).validate(len(contents))

    @staticmethod
    def __validate_2nd_file_header(contents: bytes, header: Header) -> int:
        offset = header.metadata_offset.value
        second_header = Header().from_bytes(contents, offset).validate(len(contents))
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
            .from_bytes(contents, offset)
            .validate(header, len(contents))
        )
        offset += metadata_header.size()
        return offset, metadata_header

    @staticmethod
    def __load_typelist(contents: bytes, offset: int) -> any:
        return TypeList().from_bytes(contents, offset)

    @staticmethod
    def __load_resource_name(
        header: Header,
        metadata_header: MetadataHeader,
        resource_info: ResourceMetadata,
        contents: bytes,
    ) -> str:
        if resource_info.name_offset != ResourceMetadata.NO_NAME:
            name_offset = (
                header.metadata_offset.value
                + metadata_header.names_offset.value
                + resource_info.name_offset.value
            )
            name = PString().from_bytes(contents, name_offset)
            assert len(name.value) > 0, f"name_size = {len(name.value)}"
            return name.value

        return None

    @staticmethod
    def __load_resource_data(header, resource_info, contents):
        data_offset = header.data_offset + resource_info.data_offset
        data_size = UInt32().from_bytes(contents, data_offset)
        data_offset += data_size.size()
        offset_past_data = data_offset + data_size.value
        return contents[data_offset:offset_past_data]

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

        for entry in data_types:
            assert entry.resource_count < int(header.metadata_size.value / ResourceMetadata().size()), "Corrupted"
            assert (
                entry.list_offset > last_offset
            ), f"Unordered type table {entry.list_offset} vs {last_offset}"
            last_offset = entry.list_offset
            resource_list = ResourceList(length=entry.number_of_resources())
            offset = header.metadata_offset
            offset += Header().size() + MetadataHeader().size()
            offset += entry.list_offset.value
            resource_list.from_bytes(contents, offset)
            resources = [
                (
                    r.resource_id,
                    Resources.__load_resource_name(
                        header, metadata_header, r, contents
                    ),
                    Resources.__load_resource_data(header, r, contents),
                )
                for r in resource_list
            ]
            resource_types.append((entry.resource_type.to_string(), resources))

        return Resources(
            file_type=header.file_type,
            file_creator=header.file_creator,
            description=resource_types,
        )
