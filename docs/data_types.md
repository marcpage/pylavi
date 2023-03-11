# LabVIEW Data Types

## Byte prefixed string

| Field  | Offset | Size | Type         | Description                       |
|--------|-------:|-----:|--------------|-----------------------------------|
| Length | 0      | 1    | unsigned int | The number of bytes in the string |
| String | 1      | N    | byte         | The characters of the string      |

