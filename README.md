# pylavi
Python LabVIEW resource file parser

## Description

This project was inspired by [pylabview by mefistotelis](https://github.com/mefistotelis/pylabview) (which was originally forked from [pylabview by jcreigh](https://github.com/jcreigh/pylabview).
The idea was to reverse engineer the LabVIEW VI file.
This project is designed to be a reboot, taking the incredible discovery done by the pylabview projects and simplifying the structure of the code.

This starts with a conceptual model of the [LabVIEW resource file](docs/file.md) and treats the binary resources files as just collections of resources.
Once the API for working with the file format itself is solidified, then code can be added to work with resources of specific types.

Along the way discoveries will be [documented](docs/).
