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

The File Header is found at offset 0 in the file.

| Field            | Offset | Size | Type                  | Comments |
|------------------|-------:|-----:|-----------------------|----------|
| File Format      | 0      | 4    | Four ASCII Characters | Always 'RSRC' |
| Corruption Check | 4      | 2    | Two ASCII Characters  | Always '\r\n', checks for common text conversion corrption (similar to [PNG header](http://www.libpng.org/pub/png/spec/1.2/PNG-Rationale.html#R.PNG-file-signature)) |
| File Type        | 6      | 4    | Four ASCII Characters | Type of file (see notes below) |
| File Creator     | 10     | 4    | Four ASCII Characters | Creator of the file (see notes below) |
| Metadata Offset  | 14     | 4    | unsigned integer      | Offset in the file of the metadata section |
| Metadata Size    | 18     | 4    | unsigned integer      | Size of the metadata section |
| Data Offset      | 22     | 4    | unsigned integer      | Offset in the file of the resource data (always right after this header) |
| Data Size        | 26     | 4    | unsigned integer      | The size of the data section |


#### File Types

1. **'LVIN'** - Virtual Instrument (.vi, .vit, .vim files)
2. **'LVAR'** - Container (.llb files)
3. **'LVCC'** - Control (.ctl, .ctt files)
4. **'LVMNU'** - Menu file (.mnu)
5. **'LVRS'** - Resource file (seen in .mnu files)
6. **'LVSB'** - External code (.lvsb files)
7. **'iuWl'** - LabWindows/CVI user interface resource file (.uir)
8. **'\0\0\0\0'** - Resource file (seen in .mnu files)

#### File Creators

1. **'LBVW'** - LabVIEW
2. **'WLin'** - LabVIEWs/CVI
3. **'\0\0\0\0'** - Unknown (seen in .uir and .mnu files)


### Resource Data

### Ressource Metadata
