# LabVIEW Resource File Format

- [LabVIEW Resource File Format](#labview-resource-file-format)
  * [Origins](#origins)
  * [General LabVIEW resource file layout](#general-labview-resource-file-layout)
    + [File Header](#file-header)
      - [File Types](#file-types)
      - [File Creators](#file-creators)
    + [Resource Data](#resource-data)
    + [Metadata](#metadata)
      - [Metadata Header](#metadata-header)
      - [Type List](#type-list)
        * [Type Info](#type-info)
      - [Resource Metadata](#resource-metadata)
      - [Name List](#name-list)

## Origins

The LabVIEW resource file format appears to be a replication of the 1980's era [Macintosh resource fork](https://formats.kaitai.io/resource_fork/resource_fork.svg) (at least in behavior).
From an interface standpoint, the resource file is a collection of resource types (identified by a four character code).
Resources of a given type can be identified by name or id number.
You can query for what types are available, fetch all resources for a given type, or fetch a single resource by type/id or type/name pair.


## File Types


| Extension | % | Description |
|-----------|--:|-------------|
| .vi       | 90% | Virtual Instrument |
| .ctl      | 10% | Control |
| .mnu      | 1%  | Menu |
| .llb      | .   | Container |
| .vit      | .   | Virtual Instrument Template |
| .vim      | .   | Virtual Instrument Macro |
| .ctt      | .   | Control Template |
| .lsb      | .   | User Compiled Code |
| .rtexe    | .   | ??? |
| .glb      | .   | Globals |
| .gbl      | .   | Globals |


## General LabVIEW resource file layout

| Section | Description                                                   |
|---------|---------------------------------------------------------------|
| [Header](#file-header)  | Verification of file format and offset to sections            |
| [Data](#resource-data)    | The contents of the resources                                 |
| [Metadata](#metadata) | The data that ties type, id, and name to a block of data      |
| Padding | There appears to be unnecessary data at the end of some files |


### File Header

|  |  |  |  |
|---|---|---|---|
| Offset | 0 | Size | 32 |


| Field            | Offset | Size | Type                  | Comments |
|------------------|-------:|-----:|-----------------------|----------|
| File Format      | 0      | 4    | Four ASCII Characters | Always `RSRC` |
| Corruption Check | 4      | 2    | Two ASCII Characters  | Always `\r\n`, checks for common text conversion corrption (similar to [PNG header](http://www.libpng.org/pub/png/spec/1.2/PNG-Rationale.html#R.PNG-file-signature)) |
| Format Version   | 6      | 2    | unsigned integer      | Always 3 |
| File Type        | 8      | 4    | Four ASCII Characters | Type of file (see [notes below](#file-types)) |
| File Creator     | 12     | 4    | Four ASCII Characters | Creator of the file (see [notes below](#file-creators)) |
| Metadata Offset  | 16     | 4    | unsigned integer      | Offset in the file of the metadata section (always Data Offset + Data Size) |
| Metadata Size    | 20     | 4    | unsigned integer      | Size of the metadata section |
| Data Offset      | 24     | 4    | unsigned integer      | Offset in the file of the resource data (always right after this header which is 32) |
| Data Size        | 28     | 4    | unsigned integer      | The size of the data section |


#### File Types

1. `LVIN` - Virtual Instrument (`.vi`, `.vit`, `.vim` files)
2. `LVAR` - Container (`.llb` files)
3. `LVCC` - Control (`.ctl`, `.ctt` files)
4. `LVMNU` - Menu file (`.mnu`)
5. `LVRS` - Resource file (seen in `.mnu` files)
6. `LVSB` - External code (`.lvsb` files)
7. `iuWl` - LabWindows/CVI user interface resource file (`.uir`)
8. `\0\0\0\0` - Resource file (seen in `.mnu` files)


#### File Creators

1. `LBVW` - LabVIEW
2. `WLin` - LabVIEWs/CVI
3. `\0\0\0\0` - Unknown (seen in .uir and .mnu files)


### Resource Data

This section is always right after the header (at offset 32).
The size of the Resource Data section is indicated by `Data Size` in the [File Header](#file-header).
There may be gaps between actual resource data blocks.
The location and metadata for each resource can be found in the [Metadata](#metadata) section of the file.

#### Resource Data Block

|  |  |  |  |
|---|---|---|---|
| Offset | [Resource Metadata](#resource-metadata).`Data Offset` | Size | 4 + `Resource Data`.`Data Size` |


| Field            | Offset | Size | Type                  | Comments                    |
|------------------|-------:|-----:|-----------------------|-----------------------------|
| Data Size        | 0      | 4    | unsigned integer      | The number of bytes of data |
| Data             | 4      | N    | binary data           | The resource data           |


### Metadata

The Metadata section is found at the offset indicated by `Metadata Offset` in the [File Header](#file-header).
The offset is always right after the [Resource Data](#resource-data) section (at offset `Data Offset` (32) + `Data Size`).

| Section                                      | Description                                                   |
|----------------------------------------------|---------------------------------------------------------------|
| [Metadata Header](#metadata-header)          | Offsets of sections in the Metadata section                   |
| [Type List](#type-list)                      | List of all resource types                                    |
| [Resource Metadata](#resource-metadata) | Information about specific resources                          |
| [Name List](#name-list)                    | List of names used in resources (not-deduplicated)            |


#### Metadata Header

|  |  |  |  |
|---|---|---|---|
| Offset | [File Header](#file-header).`Metadata Offset` | Size | 52 |

| Field                | Offset | Size | Type                        | Comments                         |
|----------------------|-------:|-----:|-----------------------------|----------------------------------|
| File Header          | 0      | 32   | [File Header](#file-header) | An exact copy of the file header |
| Unused               | 32     | 8    | bytes                       | May be safely set to all 0's     |
| File Header Size     | 40     | 4    | unsigned integer            | Always 32                        |
| Metadata Header Size | 44     | 4    | unsigned integer            | Always 52                        |
| Names Offset         | 48     | 4    | unsigned integer            | Offset in the [Metadata](#metadata) section of the [names list](#name-list). If no names, this is 0. |


#### Type List

|  |  |  |  |
|---|---|---|---|
| Offset | [File Header](#file-header).`Metadata Offset` + 52 | Size | 4 + 12 x number of types |

| Field                | Offset | Size   | Type                    | Comments                              |
|----------------------|-------:|-------:|-------------------------|---------------------------------------|
| Type Count           | 0      | 4      | unsigned integer        | Number of types less one (need to +1) |
| Type Blocks          | 4      | 12 x N | [Type Info](#type-info) | Repeated entries for each type        |

##### Type Info

|  |  |  |  |
|---|---|---|---|
| Offset | [File Header](#file-header).`Metadata Offset` + 56 + 12 x type index | Size | 12 |

| Field                | Offset | Size   | Type                  | Comments                                               |
|----------------------|-------:|-------:|-----------------------|--------------------------------------------------------|
| Resource Type        | 0      | 4      | Four ASCII Characters | The code for the data type                             |
| Resource Count       | 4      | 4      | unsigned integer      | Number of resources of this type less one (need to +1) |
| List Offset          | 8      | 4      | unsigned integer      | Offset after [Metadata Header](#metadata-header)       |


#### Resource Metadata

|  |  |  |  |
|---|---|---|---|
| Offset | [File Header](#file-header).`Metadata Offset` + 52 + [Type Info](#type-info).`List Offset` + 20 x resource index | Size | 20 |

| Field                | Offset | Size   | Type                  | Comments                                                           |
|----------------------|-------:|-------:|-----------------------|--------------------------------------------------------------------|
| Resource ID          | 0      | 4      | signed integer        | Identifying number for this resource                               |
| Name Offset          | 4      | 4      | unsigned integer      | Offset of name in the [Name List](#name-list) or FFFFFFFF is none |
| Unused               | 8      | 4      | bytes                 | May safely be set to all 0's                                       |
| Data Offset          | 12     | 4      | unsigned integer      | Offset of the [Resource Data Block](#resoure-data-block) in the [Resource Data](#resource-data) section              |
| Unused               | 16     | 4      | bytes                 | May safely be set to all 0's                                       |

**Note**: Resources of a given type are always in the order in which they are in the file

#### Name List

|  |  |  |  |
|---|---|---|---|
| Offset | [File Header](#file-header).`Metadata Offset` + [Metadata Header](#metadata-header).`Names Offset` | Size | variable |

The name list is a concatenated list of [byte-prefixed strings](data_types.md#byte-prefixed-string) starting at `Names Offset` from the [Metadata Header](#metadata-header).
