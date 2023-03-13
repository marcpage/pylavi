![status sheild](https://img.shields.io/static/v1?label=status&message=Milestone+1&color=inactive&style=plastic)
![GitHub](https://img.shields.io/github/license/marcpage/pylavi?style=plastic)
[![commit sheild](https://img.shields.io/github/last-commit/marcpage/pylavi?style=plastic)](https://github.com/marcpage/pylavi/commits)
[![activity sheild](https://img.shields.io/github/commit-activity/m/marcpage/pylavi?style=plastic)](https://github.com/marcpage/pylavi/commits)
![GitHub top language](https://img.shields.io/github/languages/top/marcpage/pylavi?style=plastic)
[![size sheild](https://img.shields.io/github/languages/code-size/marcpage/pylavi?style=plastic)](https://github.com/marcpage/pylavi)
[![issues sheild](https://img.shields.io/github/issues-raw/marcpage/pylavi?style=plastic)](https://github.com/marcpage/pylavi/issues)
[![follow sheild](https://img.shields.io/github/followers/marcpage?label=Follow&style=social)](https://github.com/marcpage?tab=followers)
[![watch sheild](https://img.shields.io/github/watchers/marcpage/pylavi?label=Watch&style=social)](https://github.com/marcpage/pylavi/watchers)

# pylavi
Python LabVIEW resource file parser

## Description

This project was inspired by [pylabview by mefistotelis](https://github.com/mefistotelis/pylabview) (which was originally forked from [pylabview by jcreigh](https://github.com/jcreigh/pylabview)).
The idea was to reverse engineer the LabVIEW VI file format.
This project is designed to be a reboot, taking the incredible discovery done by the pylabview projects and simplifying the structure of the code.

This starts with a conceptual model of the [LabVIEW resource file](https://github.com/marcpage/pylavi/blob/main/docs/file.md) and treats the binary resources files as just collections of resources.
Once the API for working with the file format itself is solidified, then code can be added to work with resources of specific types.

Along the way discoveries will be [documented](https://github.com/marcpage/pylavi/tree/main/docs).
