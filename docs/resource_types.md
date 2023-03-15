# Resource Types

In a [LabVIEW Resource File](file.md) there are resources of various types.
Each resource type is identified by a four character ascii code.

- [Resource Types](#resource-types)
  * [Common to many file types](#common-to-many-file-types)
    + [BDEx](#bdex), [BDHB](#bdhb), [BDHP](#bdhp), [BDHX](#bdhx), [BDHb](#bdhb), [BDHc](#bdhc), [BDSE](#bdse), [BDTS](#bdts)
      [BFAL](#bfal), [BKMK](#bkmk), [BNID](#bnid), [CCSG](#ccsg), [CCST](#ccst), [CGRS](#cgrs), [CNST](#cnst), [CONP](#conp), [COUT](#cout)
      [CPC2](#cpc2), [CPCT](#cpct), [CPD2](#cpd2), [CPDI](#cpdi), [CPMp](#cpmp), [CPSP](#cpsp), [CPST](#cpst), [CPTM](#cptm), [DFDS](#dfds)
      [DLDR](#dldr), [DLLP](#dllp), [DSIM](#dsim), [DSTM](#dstm), [DTHP](#dthp), [DsEL](#dsel), [EXPR](#expr), [FPEx](#fpex), [FPHB](#fphb)
      [FPHP](#fphp), [FPHX](#fphx), [FPHb](#fphb), [FPHc](#fphc), [FPRT](#fprt), [FPSE](#fpse), [FPTD](#fptd), [FPTS](#fpts), [FTAB](#ftab)
      [GCDI](#gcdi), [GCPR](#gcpr), [GTMI](#gtmi), [HBIN](#hbin), [HBUF](#hbuf), [HIDL](#hidl), [HIST](#hist), [HLPP](#hlpp), [HLPT](#hlpt)
      [HLPU](#hlpu), [HLPW](#hlpw), [HLPX](#hlpx), [HOBJ](#hobj), [HOMp](#homp), [ICON](#icon), [IPSR](#ipsr), [L2FG](#l2fg), [LBDP](#lbdp)
      [LFPP](#lfpp), [LIBN](#libn), [LIbd](#libd), [LIds](#lids), [LIfp](#lifp), [LIvi](#livi), [LPIN](#lpin), [LVIN](#lvin), [LVSB](#lvsb)
      [MNGI](#mngi), [MUID](#muid), [NUID](#nuid), [OBSG](#obsg), [OMId](#omid), [PICC](#picc), [PLAT](#plat), [PRIM](#prim)
      [PRT](#prt), [PsEL](#psel), [RSID](#rsid), [RTMP](#rtmp), [RTSG](#rtsg), [SBSP](#sbsp), [SCSR](#scsr), [STR](#str), [STRG](#strg)
      [SUID](#suid), [TITL](#titl), [TM80](#tm80), [TRec](#trec), [VAST](#vast), [VCTP](#vctp), [VICD](#vicd), [VIMS](#vims), [VINS](#vins)
      [VITS](#vits), [VPDP](#vpdp), [WEMF](#wemf), [XFlg](#xflg), [icl4](#icl4), [icl8](#icl8)
    + [BDPW - Block Diagram Password](#bdpw---block-diagram-password)
    + [LVSR - Save Record](#lvsr---save-record)
    + [vers - LabVIEW Editor Version](#vers---labview-editor-version)
  * [Non-VI types](#non-vi-types)
    + [ADir](#adir)
    + [CPRF](#cprf)
    + [FLAG](#flag)
    + [LPTH](#lpth)
    + [LVzp](#lvzp)
    + [PALM](#palm)
    + [PATH](#path)
    + [PLM2](#plm2)
    + [TMPL](#tmpl)
    + [UCRF](#ucrf)
  * [LabWindows/CVI](#labwindowscvi)
    + [DLG3](#dlg3)
    + [cALs](#cals)
    + [cANv](#canv)
    + [cARR](#carr)
    + [cDVl](#cdvl)
    + [cLSt](#clst)
    + [cTRl](#ctrl)
    + [cUS2](#cus2)
    + [dBNd](#dbnd)
    + [dGRF](#dgrf)
    + [gRAf](#graf)
    + [iLSt](#ilst)
    + [lCHk](#lchk)
    + [lISt](#list)
    + [mBAr](#mbar)
    + [mBR2](#mbr2)
    + [mBRf](#mbrf)
    + [mENu](#menu)
    + [mITm](#mitm)
    + [mLSt](#mlst)
    + [pANl](#panl)
    + [pBUt](#pbut)
    + [pVAl](#pval)
    + [pXT2](#pxt2)
    + [pXTr](#pxtr)
    + [sPLt](#splt)
    + [sTRn](#strn)
    + [tAB2](#tab2)
    + [tABl](#tabl)
    + [tABp](#tabp)
    + [tABs](#tabs)
    + [tEXt](#text)
    + [tIMr](#timr)
    + [uIRe](#uire)
    + [uIRf](#uirf)
    + [uIRr](#uirr)

## Common to many file types

### BDEx

- **extensions** .vim, .vi, .ctl, .ctt, .vit
- **file types** LVCC, LVIN

### BDHB

- **extensions** .ctl, .vi
- **file types** LVCC, LVIN

### BDHP

- **extensions** .ctl, .vi, .vit
- **file types** LVCC, LVIN

### BDHX

- **extensions** .vi
- **file types** LVIN

### BDHb

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

### BDHc

- **extensions** .ctl, .vi, .vit
- **file types** LVCC, LVIN

### BDPW - Block Diagram Password

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVIN

Not sure of the format, but this appears to be related to the password feature.
It appears that it also changes based on other criteria.
The first 16 bytes are the Hex MD5 digits of the password.
If no password is set, the first 16 bytes are: d41d8cd98f00b204e9800998ecf8427e
This is the MD5 hash of an empty string.

The size is either 32 or 48.

### BDSE

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

### BDTS

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVCC, LVIN

### BFAL

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVIN

### BKMK

- **extensions** .ctl, .vi, .vit
- **file types** LVCC, LVIN

### BNID

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVIN

**Note:** This resources is missing when **Separate compiled code from source** is turned on

### CCSG

- **extensions** .ctl, .vit, .vi, .ctt
- **file types** LVCC, LVIN

### CCST

- **extensions** .vim, .vi, .ctl, .ctt, .vit
- **file types** LVCC, LVIN

**Note:** This resources is missing when **Separate compiled code from source** is turned on

### CGRS

- **extensions** .ctl, .vi
- **file types** LVCC, LVIN

### CNST

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVCC, LVIN

### CONP

- **extensions** .vim, .llb, .vi, .glb, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVAR, LVIN

### COUT

- **extensions** .ctl, .vi
- **file types** LVCC, LVIN

### CPC2

- **extensions** .vim, .llb, .vi, .glb, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVAR, LVIN

### CPCT

- **extensions** .ctl, .llb, .vi
- **file types** LVCC, LVAR, LVIN

### CPD2

- **extensions** .llb, .vi
- **file types** LVAR, LVIN

### CPDI

- **extensions** .llb, .vi
- **file types** LVAR, LVIN

### CPMp

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVIN

**Note:** This resources is missing when **Separate compiled code from source** is turned on

### CPSP

- **extensions** .vi, .vit
- **file types** LVIN

### CPST

- **extensions** .llb, .vi, .ctl, .vit, .mnu
- **file types** LVRS, LMNU, LVAR, LVIN, LVCC

### CPTM

- **extensions** .ctl, .llb, .vi, .vit
- **file types** LVCC, LVAR, LVIN

### DFDS

- **extensions** .vim, .vi, .ctl, .ctt, .vit
- **file types** LVCC, LVIN

**Note:** This resources is missing when **Separate compiled code from source** is turned on

### DLDR

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVIN

**Note:** This resources is missing when **Separate compiled code from source** is turned on

### DLLP

- **extensions** .vi
- **file types** LVIN

### DSIM

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVCC, LVIN

### DSTM

- **extensions** .ctl, .vi, .vit
- **file types** LVCC, LVIN

### DTHP

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

### DsEL

- **extensions** .vi
- **file types** LVIN

### EXPR

- **extensions** .vi
- **file types** LVIN

### FPEx

- **extensions** .vim, .vi, .ctl, .ctt, .vit
- **file types** LVCC, LVIN

### FPHB

- **extensions** .ctl, .vi
- **file types** LVCC, LVIN

### FPHP

- **extensions** .ctl, .vi, .vit
- **file types** LVCC, LVIN

### FPHX

- **extensions** .vi
- **file types** LVIN

### FPHb

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

### FPHc

- **extensions** .ctl, .vi, .vit
- **file types** LVCC, LVIN

### FPRT

- **extensions** .vi, .vit
- **file types** LVIN

### FPSE

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

### FPTD

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVIN

**Note:** This resources is missing when **Separate compiled code from source** is turned on

### FPTS

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVCC, LVIN

### FTAB

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

### GCDI

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVCC, LVIN

**Note:** This resources is missing when **Separate compiled code from source** is turned on

### GCPR

- **extensions** .vim, .vi, .ctl, .ctt, .vit
- **file types** LVCC, LVIN

**Note:** This resources is missing when **Separate compiled code from source** is turned on

### GTMI

- **extensions** .ctl, .vi, .vit
- **file types** LVCC, LVIN

### HBIN

- **extensions** .vim, .vi, .ctl, .vit, .gbl
- **file types** LVCC, LVIN

### HBUF

- **extensions** .vim, .vi, .ctl, .vit, .gbl
- **file types** LVCC, LVIN

### HIDL

- **extensions** .vi
- **file types** LVIN

### HIST

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

### HLPP

- **extensions** .vim, .llb, .vi, .ctl, .vit, .mnu
- **file types** LVRS, LMNU, LVAR, LVIN, LVCC

### HLPT

- **extensions** .vim, .llb, .vi, .ctl, .vit, .mnu
- **file types** LVRS, LMNU, LVAR, LVIN, LVCC

### HLPU

- **extensions** .ctl, .vim, .vi
- **file types** LVCC, LVIN

### HLPW

- **extensions** .ctl, .vim, .vi
- **file types** LVCC, LVIN

### HLPX

- **extensions** .vim, .llb, .vi
- **file types** LVAR, LVIN

### HOBJ

- **extensions** .vi
- **file types** LVIN

### HOMp

- **extensions** .ctl, .vi
- **file types** LVCC, LVIN

### ICON

- **extensions** .vim, .llb, .vi, .glb, .ctl, .ctt, .vit, .gbl, .mnu
- **file types** LVRS, LMNU, LVAR, LVIN, LVCC

### IPSR

- **extensions** .ctl, .vi, .vit
- **file types** LVCC, LVIN

### L2FG

- **extensions** .ctl, .vi
- **file types** LVCC, LVIN

### LBDP

- **extensions** .ctl, .vi
- **file types** LVCC, LVIN

### LFPP

- **extensions** .ctl, .vi
- **file types** LVCC, LVIN

### LIBN

- **extensions** .vim, .vi, .ctl, .ctt, .vit
- **file types** LVCC, LVIN

### LIbd

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

### LIds

- **extensions** .vim, .vi, .ctl, .ctt, .vit
- **file types** LVCC, LVIN

**Note:** This resources is missing when **Separate compiled code from source** is turned on

### LIfp

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

### LIvi

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

### LPIN

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVCC, LVIN

### LVIN

- **extensions** .vi
- **file types** LVIN

### LVSB

- **extensions** .vi, .lsb
- **file types** LVIN, LVSB

### LVSR - Save Record

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

| Field    | Offset   | Size  | Type         | Description                                 |
|----------|---------:|------:|--------------|---------------------------------------------|
| Version  | 0        | 4     | unsigned int | LabVIEW [Version](data_types.md#version)    |
| Basic    | 4        | 4     | unsigned int | [Basic Flags](#lvsr-basic-flags)            |
| Flags    | 8        | 4     | unsigned int | [Flags](#lvsr-flags)                        |
| Unknown  | 12       | 12    | unsigned int | |
| Code     | 24       | 4     | unsigned int | [Code Flags](#lvsr-code-flags)              |
| Unknown  | 28       | 40    | unsigned int | |
| -------  | -------- | ----- | ------------ | End of some                                 |
| Unknown  | 68       | 8     | unsigned int | |
| -------  | -------- | ----- | ------------ | End of some                                 |
| Unknown  | 76       | 4     | unsigned int | |
| -------  | -------- | ----- | ------------ | End of some                                 |
| Unknown  | 80       | 2     | unsigned int | |
| -------  | -------- | ----- | ------------ | End of some                                 |
| Unknown  | 82       | 4     | unsigned int | |
| -------  | -------- | ----- | ------------ | End of some                                 |
| Unknown  | 96       | 16    | unsigned int | |
| -------  | -------- | ----- | ------------ | End of some                                 |
| Unknown  | 112      | 4     | unsigned int | |
| -------  | -------- | ----- | ------------ | End of some                                 |
| Breakpts | 116      | 4     | unsigned int | Number of breakpoints set |
| -------  | -------- | ----- | ------------ | End of some                                 |
| Unknown  | 120      | 16    | unsigned int | |
| -------  | -------- | ----- | ------------ | End of some                                 |
| Unknown  | 136      | 1     | unsigned int | |
| -------  | -------- | ----- | ------------ | End of some                                 |
| Unknown  | 137      | 3     | unsigned int | |
| -------  | -------- | ----- | ------------ | End of some                                 |
| Unknown  | 140      | 4     | unsigned int | |
| -------  | -------- | ----- | ------------ | End of some                                 |
| Unknown  | 144      | 16    | unsigned int | |

**Note:** The save record size varies depending on LabVIEW version.
The known sizes are: 68, 76, 80, 82, 96, 112, 116, 120, 136, 137, 140, 144, and 160 bytes.

#### LVSR Basic Flags

| Bit Mask | Description                                                                       |
|----------|-----------------------------------------------------------------------------------|
| 00002000 | VI is locked (possibly with password, see [BDPW](#bdpw---block-diagram-password)) |


#### LVSR Flags

| Bit Mask | Description                        |
|----------|------------------------------------|
| 00000004 | Saved for previous                 |
| 00000400 | Separate compiled code from source |
| 20000000 | Automatic Error Handling           |

#### LVSR Code Flags

| Bit Mask | Description                        |
|----------|------------------------------------|
| 20000000 | Breakpoint(s) Set                  |


### MNGI

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVCC, LVIN

### MUID

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

### NUID

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVIN

**Note:** This resources is missing when **Separate compiled code from source** is turned on

### OBSG

- **extensions** .ctl, .vit, .vi, .ctt
- **file types** LVCC, LVIN

### OMId

- **extensions** .vi, .vit
- **file types** LVIN

### PICC

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVCC, LVIN

### PLAT

- **extensions** .vi, .lsb
- **file types** LVIN, LVSB

### PRIM

- **extensions** .vi
- **file types** LVIN

### PRT

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVCC, LVIN

### PsEL

- **extensions** .vi
- **file types** LVIN

### RSID

- **extensions** .ctl, .vi, .vit
- **file types** LVCC, LVIN

### RTMP

- **extensions** .vi, .vit
- **file types** LVIN

### RTSG

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

### SBSP

- **extensions** .vi
- **file types** LVIN

### SCSR

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVIN

**Note:** This resources is missing when **Separate compiled code from source** is turned on

### STR

- **extensions** .vim, .llb, .vi, .ctl, .vit
- **file types** LVCC, LVAR, LVIN

### STRG

- **extensions** .vim, .llb, .vi, .ctl, .vit, .gbl
- **file types** LVCC, LVAR, LVIN

### SUID

- **extensions** .ctl, .vim, .vi, .vit
- **file types** LVIN

**Note:** This resources is missing when **Separate compiled code from source** is turned on

### TITL

- **extensions** .ctl, .llb, .vi, .vit
- **file types** LVCC, LVAR, LVIN

### TM80

- **extensions** .vim, .vi, .ctl, .ctt, .vit
- **file types** LVCC, LVIN

**Note:** This resources is missing when **Separate compiled code from source** is turned on

### TRec

- **extensions** .ctl, .vi, .vit
- **file types** LVCC, LVIN

### VAST

- **extensions** .vim, .vi
- **file types** LVIN

### VCTP

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

### VICD

- **extensions** .vim, .vi, .ctl, .ctt, .vit
- **file types** LVCC, LVIN

**Note:** This resources is missing when **Separate compiled code from source** is turned on

### VIMS

- **extensions** .vi, .vit
- **file types** LVIN

### VINS

- **extensions** .vim, .vi, .vit
- **file types** LVIN

### VITS

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

### VPDP

- **extensions** .vim, .vi, .ctl, .ctt, .vit
- **file types** LVCC, LVIN

### WEMF

- **extensions** .ctl, .vi, .vit
- **file types** LVCC, LVIN

### XFlg

- **extensions** .vi
- **file types** LVIN

### icl4

- **extensions** .vim, .llb, .vi, .ctl, .vit, .mnu
- **file types** LVRS, LMNU, LVAR, LVIN, LVCC

### icl8

- **extensions** .vim, .llb, .vi, .ctl, .ctt, .vit, .mnu
- **file types** LVRS, LMNU, LVAR, LVIN, LVCC

### vers - LabVIEW Editor Version

- **extensions** .vim, .glb, .vi, .ctl, .ctt, .vit, .gbl
- **file types** LVCC, LVIN

| Field    | Offset   | Size  | Type         | Description                                 |
|----------|---------:|------:|--------------|---------------------------------------------|
| Version  | 0        | 4     | unsigned int | LabVIEW [Version](data_types.md#version)    |
| Language | 4        | 2     | unsigned int | [Language](#version-language)               |
| Text     | 6        | L + 1 |[Byte prefixed string](data_types.md#byte-prefixed-string)  |
| Name     | 6 + L +1 | L + 1 |[Byte prefixed string](data_types.md#byte-prefixed-string)  |


**Note:**
When **Separate compiled code from source** is turned on, only `vers#4` is available.
Otherwise, `vers#7`, `vers#8`, `vers#9`, `vers#10` exist.


#### Version Language

| Language | Value |
|----------|------:|
| English  |   0   |
| French   |   1   |
| German   |   3   |
| Japanese |  14   |
| Korean   |  23   |
| Chinese  |  33   |

**Note** The language codes seem to come from the old Macintosh [Script.h](https://github.com/phracker/MacOSX-SDKs/blob/master/MacOSX10.6.sdk/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/CarbonCore.framework/Versions/A/Headers/Script.h#L121) header file.
No other languages other than the ones above have been found to be used.

## Non-VI types

### ADir

- **extensions** .llb
- **file types** LVAR

### CPRF

- **extensions** .llb
- **file types** LVAR

### FLAG

- **extensions** .mnu, .llb
- **file types** LVRS, LMNU, LVAR

### LPTH

- **extensions** .mnu, .llb
- **file types** LVRS, LMNU, LVAR

### LVzp

- **extensions** .rtexe
- **file types** LVAR

### PALM

- **extensions** .llb
- **file types** LVAR

### PATH

- **extensions** .mnu
- **file types** LVRS, LMNU

### PLM2

- **extensions** .mnu, .llb
- **file types** LVRS, LMNU, LVAR

### TMPL

- **extensions** .llb
- **file types** LVAR

### UCRF

- **extensions** .llb
- **file types** LVAR


## LabWindows/CVI

### DLG3

- **extensions** .uir
- **file types** iUWl

### cALs

- **extensions** .uir
- **file types** x00000000

### cANv

- **extensions** .uir
- **file types** iUWl

### cARR

- **extensions** .uir
- **file types** x00000000

### cDVl

- **extensions** .uir
- **file types** iUWl

### cLSt

- **extensions** .uir
- **file types** iUWl

### cTRl

- **extensions** .uir
- **file types** iUWl

### cUS2

- **extensions** .uir
- **file types** iUWl

### dBNd

- **extensions** .uir
- **file types** iUWl

### dGRF

- **extensions** .uir
- **file types** iUWl

### gRAf

- **extensions** .uir
- **file types** iUWl

### iLSt

- **extensions** .uir
- **file types** iUWl

### lCHk

- **extensions** .uir
- **file types** iUWl

### lISt

- **extensions** .uir
- **file types** x00000000

### mBAr

- **extensions** .uir
- **file types** iUWl

### mBR2

- **extensions** .uir
- **file types** iUWl

### mBRf

- **extensions** .uir
- **file types** iUWl

### mENu

- **extensions** .uir
- **file types** iUWl

### mITm

- **extensions** .uir
- **file types** x00000000

### mLSt

- **extensions** .uir
- **file types** iUWl

### pANl

- **extensions** .uir
- **file types** iUWl

### pBUt

- **extensions** .uir
- **file types** iUWl

### pVAl

- **extensions** .uir
- **file types** iUWl

### pXT2

- **extensions** .uir
- **file types** iUWl

### pXTr

- **extensions** .uir
- **file types** iUWl

### sPLt

- **extensions** .uir
- **file types** iUWl

### sTRn

- **extensions** .uir
- **file types** iUWl

### tAB2

- **extensions** .uir
- **file types** x00000000

### tABl

- **extensions** .uir
- **file types** iUWl

### tABp

- **extensions** .uir
- **file types** iUWl

### tABs

- **extensions** .uir
- **file types** iUWl

### tEXt

- **extensions** .uir
- **file types** iUWl

### tIMr

- **extensions** .uir
- **file types** iUWl

### uIRe

- **extensions** .uir
- **file types** iUWl

### uIRf

- **extensions** .uir
- **file types** iUWl

### uIRr

- **extensions** .uir
- **file types** iUWl
