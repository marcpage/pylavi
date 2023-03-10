# LabVIEW Resource File Format

## Origins

The LabVIEW resource file format appears to be a replication of the 1980's era [Macintosh resource fork](https://formats.kaitai.io/resource_fork/resource_fork.svg) (at least in behavior). 
From an interface standpoint, the resource file is a collection of resource types (identified by a four character code).
Resources of a given type can be identified by name or id number.
You can query for what types are available, fetch all resources for a given type, or fetch a single resource by type/id or type/name pair.


## General LabVIEW resource file layout

| Section | Description                                              |
|---------|----------------------------------------------------------|
| Header  | Verification of file format and offset to sections       |
| Data    | The contents of the resources                            |
| Metadata| The data that ties type, id, and name to a block of data |

### File Header


### Resource Data

### Ressource Metadata
