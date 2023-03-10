# LabVIEW Data Types

## Byte prefixed string

| Field  | Offset | Size | Type         | Description                       |
|--------|-------:|-----:|--------------|-----------------------------------|
| Length | 0      | 1    | unsigned int | The number of bytes in the string |
| String | 1      | N    | byte         | The characters of the string      |


## Version

[Semantic Version](https://semver.org)

| Field                   | Bit Offset | Bits | Type         |
|-------------------------|-----------:|-----:|--------------|
| Major (tens)            |      28    |  4   | unsigned BCD |
| Major (ones)            |      24    |  4   | unsigned BCD |
| Minor                   |      20    |  4   | unsigned BCD |
| Patch                   |      16    |  4   | unsigned BCD |
| [Stage](#version-stage) |      13    |  3   | unsigned int |
| Build (thousands)       |      12    |  1   | unsigned BCD |
| Build (hundreds)        |       8    |  4   | unsigned BCD |
| Build (tens)            |       4    |  4   | unsigned BCD |
| Build (ones)            |       0    |  4   | unsigned BCD |

### Version Stage

| Value | Description |
|------:|-------------|
| 0     | Undefined   |
| 1     | Development |
| 2     | Alpha       |
| 3     | Beta        |
| 4     | Release     |
| 5-7   | Undefined   |
