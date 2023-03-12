"""
    Common data types for LabVIEW resources
"""


import ctypes


class Structure(ctypes.BigEndianStructure):
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

    def __str__(self) -> str:
        return self.to_string()
