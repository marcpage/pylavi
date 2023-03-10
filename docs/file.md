# LabVIEW Resource File Format

- [LabVIEW Resource File Format](#labview-resource-file-format)
  * [Origins](#origins)
  * [General LabVIEW resource file layout](#general-labview-resource-file-layout)
    + [File Header](#file-header)
      - [File Types](#file-types)
      - [File Creators](#file-creators)
    + [Resource Data](#resource-data)
    + [Resource Metadata](#resource-metadata)
      - [Metadata Header](#metadata-header)
      - [Type List](#type-list)
        * [Type Info](#type-info)
      - [Specific Resource Metadata](#specific-resource-metadata)
      - [Name Table](#name-table)

## Origins

The LabVIEW resource file format appears to be a replication of the 1980's era [Macintosh resource fork](https://formats.kaitai.io/resource_fork/resource_fork.svg) (at least in behavior).
From an interface standpoint, the resource file is a collection of resource types (identified by a four character code).
Resources of a given type can be identified by name or id number.
You can query for what types are available, fetch all resources for a given type, or fetch a single resource by type/id or type/name pair.


## General LabVIEW resource file layout

| Section | Description                                                   |
|---------|---------------------------------------------------------------|
| [Header](#file-header)  | Verification of file format and offset to sections            |
| [Data](#resource-data)    | The contents of the resources                                 |
| [Metadata](#resource-metadata) | The data that ties type, id, and name to a block of data      |
| Padding | There appears to be unnecessary data at the end of some files |


### File Header

The File Header is found at offset 0 in the file and is 32 bytes in length.

| Field            | Offset | Size | Type                  | Comments |
|------------------|-------:|-----:|-----------------------|----------|
| File Format      | 0      | 4    | Four ASCII Characters | Always `RSRC` |
| Corruption Check | 4      | 2    | Two ASCII Characters  | Always `\r\n`, checks for common text conversion corrption (similar to [PNG header](http://www.libpng.org/pub/png/spec/1.2/PNG-Rationale.html#R.PNG-file-signature)) |
| Format Version   | 6      | 2    | unsigned integer      | Always 3 |
| File Type        | 8      | 4    | Four ASCII Characters | Type of file (see [notes below](#file-types)) |
| File Creator     | 12     | 4    | Four ASCII Characters | Creator of the file (see [notes below](#file-creators)) |
| Metadata Offset  | 16     | 4    | unsigned integer      | Offset in the file of the metadata section |
| Metadata Size    | 20     | 4    | unsigned integer      | Size of the metadata section |
| Data Offset      | 24     | 4    | unsigned integer      | Offset in the file of the resource data (always right after this header) |
| Data Size        | 28     | 4    | unsigned integer      | The size of the data section |


#### File Types

1. `LVIN` - Virtual Instrument (.vi, .vit, .vim files)
2. `LVAR` - Container (.llb files)
3. `LVCC` - Control (.ctl, .ctt files)
4. `LVMNU` - Menu file (.mnu)
5. `LVRS` - Resource file (seen in .mnu files)
6. `LVSB` - External code (.lvsb files)
7. `iuWl` - LabWindows/CVI user interface resource file (.uir)
8. `\0\0\0\0` - Resource file (seen in .mnu files)


#### File Creators

1. `LBVW` - LabVIEW
2. `WLin` - LabVIEWs/CVI
3. `\0\0\0\0` - Unknown (seen in .uir and .mnu files)


### Resource Data

The Resource Data section is found at the offset indicated by `Data Offset` in the [File Header](#file-header).
This offset is always right after the header (at offset 32).
The size of the Resource Data section is indicated by `Data Size` in the [File Header](#file-header).
There may be gaps between actual resource data.
The location and metadata for each resource can be found in the [Resource Metadata](#resource-metadata) section of the file.

| Field            | Offset | Size | Type                  | Comments                    |
|------------------|-------:|-----:|-----------------------|-----------------------------|
| Data Size        | 0      | 4    | unsigned integer      | The number of bytes of data |
| Data             | 4      | N    | binary data           | The resource data           |


### Resource Metadata

The Resource Metadata section is found at the offset indicated by `Metadata Offset` in the [File Header](#file-header).
The offset is always right after the [Resource Data](#resource-data) section (at offset `Data Offset` (32) + `Data Size`).

| Section                                      | Description                                                   |
|----------------------------------------------|---------------------------------------------------------------|
| [Metadata Header](#metadata-header)          | Offsets of sections in the Metadata section                   |
| [Type List](#type-list)                      | List of all resource types                                    |
| [Resource Info](#specific-resource-metadata) | Information about specific resources                          |
| [Name Table](#name-table)                    | List of names used in resources (not-deduplicated)            |


#### Metadata Header

| Field                | Offset | Size | Type                        | Comments                         |
|----------------------|-------:|-----:|-----------------------------|----------------------------------|
| File Header          | 0      | 32   | [File Header](#file-header) | An exact copy of the file header |
| Unused               | 32     | 8    | bytes                       | May be safely set to all 0's     |
| File Header Size     | 40     | 4    | unsigned integer            | Always 32                        |
| Metadata Header Size | 44     | 4    | unsigned integer            | Always 52                        |
| Names Offset         | 48     | 4    | unsigned integer            | Offset in the [Resource Metadata](#resource-metadata) section of the [names list](#name-table). If no names, this is 0. |


#### Type List

| Field                | Offset | Size   | Type                    | Comments                              |
|----------------------|-------:|-------:|-------------------------|---------------------------------------|
| Type Count           | 0      | 4      | unsigned integer        | Number of types less one (need to +1) |
| Type Blocks          | 4      | 12 x N | [Type Info](#type-info) | Repeated entries for each type        |

##### Type Info

| Field                | Offset | Size   | Type                  | Comments                                               |
|----------------------|-------:|-------:|-----------------------|--------------------------------------------------------|
| Resource Type        | 0      | 4      | Four ASCII Characters | The code for the data type                             |
| Resource Count       | 4      | 4      | unsigned integer      | Number of resources of this type less one (need to +1) |
| List Offset          | 8      | 4      | unsigned integer      | Offset after [Metadata Header](#metadata-header)       |


#### Specific Resource Metadata

| Field                | Offset | Size   | Type                  | Comments                                                           |
|----------------------|-------:|-------:|-----------------------|--------------------------------------------------------------------|
| Resource ID          | 0      | 4      | signed integer        | Identifying number for this resource                               |
| Name Offset          | 4      | 4      | unsigned integer      | Index of name in the [Name Table](#name-table) or FFFFFFFF is none |
| Unused               | 8      | 4      | bytes                 | May safely be set to all 0's                                       |
| Data Offset          | 12     | 4      | unsigned integer      | Offset in the [Resource Data](#resource-data) section              |
| Unused               | 16     | 4      | bytes                 | May safely be set to all 0's                                       |

#### Name Table

The name table is a concatenated list of [byte-prefixed strings](data_types.md#byte-prefixed-string) starting at `Names Offset` from the [Metadata Header](#metadata-header).
