---
name: "gromacs"
layout: package
next_package: None
previous_package: tar
languages: ['c']
---
## 5.1.2
9 / 4523 files match, 4 filtered matches.

 - [src/external/vmd_molfile/vmddlopen.c](#srcexternalvmd_molfilevmddlopenc)
 - [src/external/vmd_molfile/vmddlopen.h](#srcexternalvmd_molfilevmddlopenh)
 - [src/gromacs/fileio/vmdio.c](#srcgromacsfileiovmdioc)
 - [cmake/TestVMD.c](#cmaketestvmdc)

### src/external/vmd_molfile/vmddlopen.c

```c

{% raw %}
81 | void *vmddlopen( const char *path) {
109 | void *vmddlopen( const char *path) {
159 | void *vmddlopen(const char *fname) {
167 |   sprintf(szBuf, "vmddlopen failed: GetLastError returned %lu\n", dw);
185 | void *vmddlopen(const char *fname) {
186 |   return dlopen(fname, RTLD_NOW);
{% endraw %}

```
### src/external/vmd_molfile/vmddlopen.h

```c

{% raw %}
87 | void *vmddlopen(const char *fname);
{% endraw %}

```
### src/gromacs/fileio/vmdio.c

```c

{% raw %}
138 |     handle = vmddlopen(fullpath);
363 |             printf("Compiled with dlopen?\n");
{% endraw %}

```
### cmake/TestVMD.c

```c

{% raw %}
18 |     handle = vmddlopen(argv[1]);
{% endraw %}

```