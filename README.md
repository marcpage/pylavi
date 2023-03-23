[![status sheild](https://img.shields.io/static/v1?label=released&message=v0.2.0&color=active&style=plastic)](https://pypi.org/project/pylavi/)
![status sheild](https://img.shields.io/static/v1?label=test+coverage&message=99%&color=active&style=plastic)
![GitHub](https://img.shields.io/github/license/marcpage/pylavi?style=plastic)
[![commit sheild](https://img.shields.io/github/last-commit/marcpage/pylavi?style=plastic)](https://github.com/marcpage/pylavi/commits)
[![activity sheild](https://img.shields.io/github/commit-activity/m/marcpage/pylavi?style=plastic)](https://github.com/marcpage/pylavi/commits)
![GitHub top language](https://img.shields.io/github/languages/top/marcpage/pylavi?style=plastic)
[![size sheild](https://img.shields.io/github/languages/code-size/marcpage/pylavi?style=plastic)](https://github.com/marcpage/pylavi)
[![issues sheild](https://img.shields.io/github/issues-raw/marcpage/pylavi?style=plastic)](https://github.com/marcpage/pylavi/issues)
[![follow sheild](https://img.shields.io/github/followers/marcpage?label=Follow&style=social)](https://github.com/marcpage?tab=followers)
[![watch sheild](https://img.shields.io/github/watchers/marcpage/pylavi?label=Watch&style=social)](https://github.com/marcpage/pylavi/watchers)

# pylavi

Python LabVIEW VI file checker.

There are many valuable checks that should be done on LabVIEW source code. 
While you can perform all these checks via running LabVIEW, `vi_validate` command can validate over a thousand VIs before LabVIEW can even launch (and only requires that Python be installed and not all of LabVIEW).

Checks:
- Dependency paths are not absolute paths (this can cause long mass compile times)
- Version of LabVIEW the file was saved in (do you test with beta versions of LabVIEW?)
- Separate source code (you don't want to add the bulk of binary code to source code control, right?)
- Password check (you want to make sure your IP is protected)
- Auto Error Handling turned off (what a pain when an unexpected error comes out of an error terminal and halts you program)
- No breakpoints (again, production code that just halts on a breakpoint can be a big bummer)
- Suspend on run (you mean there is an actual flag that pauses a VI when you run it?)
- No debugging (speed up your production code by disabling debugging)
- and many more ...


## Notice

This code is not endorsed, supported, or encouraged by National Instruments (NI).
This is a clean-room examiniation of LabVIEW files and using information from [pylabview by mefistotelis](https://github.com/mefistotelis/pylabview).
There is no guarantee of this tool working as designed with any particular LabVIEW files.
You should validate that this tool will work for your use case and re-verify with each new version of LabVIEW.

## Description

This tool is designed to quickly validate large groups of VIs for common problems.
This could be used in a Pull Request build to verify the LabVIEW files are saved in the correct version.

You could perform the same check using LabVIEW, but this tool can often verify thousands of files in the time it takes to launch LabVIEW (~1,200 files/second on an M2 macBook Pro while LabVIEW takes 1.8 seconds to launch and quit).
For a Pull Request build, you want to make sure your builds are as short as possible, hence, this tool.


## Validating VIs

### Install

`pip3 install pylavi`

### Validate VIs


`vi_validate --path lv_source --no_beta --gt 21.0`

This command will validate that all LabVIEW files in this directory (deep scan) were saved in a LabVIEW version greater than 21.0.0f0.
If any VIs were saved in a previous version, it will print the path to the VI and return a non-zero exit code.

You can validate the following:

- **version** greater than, less than, or equal to a specific version (any part of the version not specified is assumed to be zero or f (final))
- **version phase** disallow VIs saved in developer, alpha, beta, or release version of LabVIEW.
- **code** disallow VIs with or without the `Separate compiled code from source file` setting (--no-code means only allow VIs with separated compiled code set)
- **breakpoints** disallow VIs with breakpoints saved
- **locked** require all VIs to be locked (with or without a password) or not locked
- **password** require VIs to be locked with a password or not locked with a password or require the be locked with a specific password
- **clear indicators** require VIs be saved with the `Clear indiciators when called` or require they not be saved with this setting
- **run on open** require VIs be saved with the `Run when opened` or require they not be saved with this setting
- **suspend on run** require VIs be saved with the `Suspend when called` or require they not be saved with this setting
- **debuggable** require VIs be saved with the `Allow debugging` or require they not be saved with this setting
- **autoerror** require VIs have the `Enable automatic error handling` flag be turned off
- **path length** require that the path to the VI (including the `--path` length) be less than the given length
- **absolute dependency paths** require that all paths are relative to the VI or a known LabVIEW location (ie `<vilib>`)

If none of these are specified, then the following settings are defaulted: `--no-absolute-path` `--no-beta` `--no-alpha` `--no-development` `--no-invalid` `--path-length 260`

You may specify multiple `--path` or `--skip`. `--path` will never override `--skip`. 

You may also specify multiple paths and associate different settings with each by passing a yaml file to `--config`.

```yaml
public api:
    path:
        - ..
    skip:
        - ../tests/*
    gt: 8.0f
    lt: 23.0f
    no_code: true
    no_beta: true
    no_alpha: true
    no_development: true
    no_invalid: true
    no_breakpoints: true
    password_match: Setec Astronomy
    clear_indicators: true
    no_run_on_open: true
    no_suspend_on_run: true
    not_debuggable: true
    no_absolute_path: true
    autoerror: true
    path_length: 128

test code:
    path:
        - ../tests
    extension:
        - .vi
    eq: 21.0f
    path_length: 128
```

Each entry in the yaml file is treated as a separate call to `vi_validate`.
The `--verbose` and `--quiet` flags (or lack of them) on the command line override the .yaml file.
The top level is the name of the set (displayed if `--verbose` is passed).
Each key underneath is the `--` name with hyphens converted to underscores (eg `--no-absolute-path` -> `no_absolute_path`).
`path`, `skip`, and `extension` are lists.
`path_length` and `password_match` are values.
All enable flags are set to `true` to enable.
`path` and `skip` paths are relative to the directory that the config file is in.

```
usage: vi_validate [-h] [-l LT] [-g GT] [-e EQ] [-r] [-b] [-a] [-d] [-i] [-c] [--code] [--breakpoints] [--locked] [--not-locked]
                   [--password-match PASSWORD_MATCH] [--password] [--no-password] [--clear-indicators] [--no-clear-indicators]
                   [--run-on-open] [--no-run-on-open] [--suspend-on-run] [--no-suspend-on-run] [--debuggable] [--not-debuggable]
                   [--no-absolute-path] [--autoerror] [--path-length PATH_LENGTH] [-p PATH] [-s SKIP] [-x EXTENSION] [-q] [-v]
                   [--config CONFIG]

Validates LabVIEW resource files

optional arguments:
  -h, --help            show this help message and exit
  -l LT, --lt LT        LabVIEW version must be less than this
  -g GT, --gt GT        LabVIEW version must be greater than this
  -e EQ, --eq EQ        LabVIEW version must this
  -r, --no-release      LabVIEW version must not be release
  -b, --no-beta         LabVIEW version must not be beta
  -a, --no-alpha        LabVIEW version must not be alpha
  -d, --no-development  LabVIEW version must not be development
  -i, --no-invalid      LabVIEW version must be a valid phase
  -c, --no-code         Saved without code
  --code                Saved with code
  --breakpoints         Not saved with breakpoints
  --locked              File is locked (maybe with password)
  --not-locked          File is not locked
  --password-match PASSWORD_MATCH
                        Ensure the password is exactly
  --password            File is locked with a password
  --no-password         File is not saved with a password
  --clear-indicators    VI will clear indicators on run
  --no-clear-indicators
                        VI will not clear indicators on run
  --run-on-open         VI will run when opened
  --no-run-on-open      VI will not run when opened
  --suspend-on-run      VI will suspend on run
  --no-suspend-on-run   VI will not suspend on run
  --debuggable          VI is debuggable
  --not-debuggable      VI is not debuggable
  --no-absolute-path    Does not reference links by absolute path
  --autoerror           Not saved with auto error handling turned on
  --path-length PATH_LENGTH
                        Maximum number of characters for the path
  -p PATH, --path PATH  Path to scan for files (or a file path) (defaults to current directory)
  -s SKIP, --skip SKIP  Path to not scan for files (or a file to ignore)
  -x EXTENSION, --extension EXTENSION
                        File extensions to evaluate (defaults to all known)
  -q, --quiet           Reduce the output (multiple times reduces output more)
  -v, --verbose         Increase the output (multiple times increases output more)
  --config CONFIG       Path to a .yaml file with collections of arguments
```

## Credits

This project was inspired by [pylabview by mefistotelis](https://github.com/mefistotelis/pylabview) (which was originally forked from [pylabview by jcreigh](https://github.com/jcreigh/pylabview)).
The idea was to reverse engineer the LabVIEW VI file format.
The `pylavi` project is designed to be a reboot, taking the incredible discovery done by the `pylabview` projects and simplifying the structure of the code.

This starts with a conceptual model of the [LabVIEW resource file](https://github.com/marcpage/pylavi/blob/main/docs/file.md) and treats the binary resources files as just collections of resources.
Once the API for working with the file format itself is solidified, then code can be added to work with resources of specific types.

Along the way discoveries will be [documented](https://github.com/marcpage/pylavi/tree/main/docs).

