---
name: "gromacs"
layout: package
next_package: guacamole-server
previous_package: gridlab-d
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
78 | #include <errno.h>
79 | #include <string.h>
80 | 
81 | void *vmddlopen( const char *path) {
82 |     void *ret;
83 |     ret = shl_load( path, BIND_IMMEDIATE | BIND_FIRST | BIND_VERBOSE, 0);
106 |  */
107 | #include <mach-o/dyld.h>
108 | 
109 | void *vmddlopen( const char *path) {
110 |   NSObjectFileImage image;
111 |   NSObjectFileImageReturnCode retval;
156 | 
157 | #include <windows.h>
158 | 
159 | void *vmddlopen(const char *fname) {
160 |   return (void *)LoadLibrary(fname);
161 | }
164 |   static CHAR szBuf[80]; 
165 |   DWORD dw = GetLastError(); 
166 |  
167 |   sprintf(szBuf, "vmddlopen failed: GetLastError returned %lu\n", dw);
168 |   return szBuf;
169 | }
182 | /* All remaining platforms (not Windows, HP-UX, or MacOS X <= 10.3) */
183 | #include <dlfcn.h>
184 | 
185 | void *vmddlopen(const char *fname) {
186 |   return dlopen(fname, RTLD_NOW);
187 | }
188 | const char *vmddlerror(void) {
{% endraw %}

```
### src/external/vmd_molfile/vmddlopen.h

```c

{% raw %}
84 | /* Try to open the specified library.  All symbols must be resolved or the 
85 |  * load will fail (RTLD_NOW).  
86 |  */
87 | void *vmddlopen(const char *fname);
88 | 
89 | /* Try to load the specified symbol using the given handle.  Returns NULL if 
{% endraw %}

```
### src/gromacs/fileio/vmdio.c

```c

{% raw %}
135 | {
136 |     /* Open the dll; try to execute the init function. */
137 |     void *handle, *ifunc, *registerfunc;
138 |     handle = vmddlopen(fullpath);
139 |     if (!handle)
140 |     {
360 |         err = vmddlerror();
361 |         if (!err)
362 |         {
363 |             printf("Compiled with dlopen?\n");
364 |         }
365 |         else
{% endraw %}

```
### cmake/TestVMD.c

```c

{% raw %}
15 |     void *handle, *ifunc, *registerfunc;
16 |     molfile_plugin_t* api;
17 |     if (argc!=2) return -1;
18 |     handle = vmddlopen(argv[1]);
19 |     if (!handle)
20 |     {
{% endraw %}

```