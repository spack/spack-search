---
name: "stat"
layout: package
next_package: fakechroot
previous_package: julia
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c', 'python']
---
## 4.0.2
7 / 275 files match, 4 filtered matches.

 - [src/dysect/DysectAPI/DysectAPI.C](#srcdysectdysectapidysectapic)
 - [examples/scripts/script_test.py](#examplesscriptsscript_testpy)
 - [scripts/STATview.py](#scriptsstatviewpy)
 - [scripts/STATGUI.py](#scriptsstatguipy)

### src/dysect/DysectAPI/DysectAPI.C

```c

{% raw %}
20 | using namespace DysectAPI;
21 | 
22 | DysectErrorCode SessionLibrary::loadLibrary(const char *path) {
23 |   libraryHandle = dlopen(path, RTLD_LAZY);
24 | 
25 |   if (!libraryHandle) {
{% endraw %}

```
### examples/scripts/script_test.py

```python

{% raw %}
1 | # invoke with ${prefix}/bin/stat-script
2 | 
3 | import sys, DLFCN
4 | sys.setdlopenflags(DLFCN.RTLD_NOW | DLFCN.RTLD_GLOBAL)
5 | import os, time, subprocess
6 | import traceback
{% endraw %}

```
### scripts/STATview.py

```python

{% raw %}
36 | from collections import defaultdict
37 | import copy
38 | 
39 | dlopenflags_set = False
40 | try:
41 |     import DLFCN
42 |     sys.setdlopenflags(DLFCN.RTLD_NOW | DLFCN.RTLD_GLOBAL)
43 |     dlopenflags_set = True
44 | except:
45 |     pass
46 | if dlopenflags_set == False:
47 |     sys.setdlopenflags(os.RTLD_NOW | os.RTLD_GLOBAL)
48 | 
49 | (MODEL_INDEX_HIDE, MODEL_INDEX_NAME, MODEL_INDEX_CASESENSITIVE, MODEL_INDEX_REGEX, MODEL_INDEX_EDITABLE, MODEL_INDEX_NOTEDITABLE, MODEL_INDEX_CALLBACK, MODEL_INDEX_ICON, MODEL_INDEX_BUTTONNAME) = range(9)
{% endraw %}

```
### scripts/STATGUI.py

```python

{% raw %}
38 | 
39 | import sys
40 | import os
41 | dlopenflags_set = False
42 | try:
43 |     import DLFCN
44 |     sys.setdlopenflags(DLFCN.RTLD_NOW | DLFCN.RTLD_GLOBAL)
45 |     dlopenflags_set = True
46 | except:
47 |     pass
48 | if dlopenflags_set == False:
49 |     sys.setdlopenflags(os.RTLD_NOW | os.RTLD_GLOBAL)
50 | 
51 | from STAT import STAT_FrontEnd, intArray, STAT_LOG_NONE, STAT_LOG_FE, STAT_LOG_BE, STAT_LOG_CP, STAT_LOG_MRN, STAT_LOG_SW, STAT_LOG_SWERR, STAT_OK, STAT_APPLICATION_EXITED, STAT_VERBOSE_ERROR, STAT_VERBOSE_FULL, STAT_VERBOSE_STDOUT, STAT_TOPOLOGY_AUTO, STAT_TOPOLOGY_DEPTH, STAT_TOPOLOGY_FANOUT, STAT_TOPOLOGY_USER, STAT_PENDING_ACK, STAT_LAUNCH, STAT_ATTACH, STAT_SERIAL_ATTACH, STAT_GDB_ATTACH, STAT_SERIAL_GDB_ATTACH, STAT_SAMPLE_FUNCTION_ONLY, STAT_SAMPLE_LINE, STAT_SAMPLE_PC, STAT_SAMPLE_COUNT_REP, STAT_SAMPLE_THREADS, STAT_SAMPLE_CLEAR_ON_SAMPLE, STAT_SAMPLE_PYTHON, STAT_SAMPLE_MODULE_OFFSET, STAT_CP_NONE, STAT_CP_SHAREAPPNODES, STAT_CP_EXCLUSIVE
{% endraw %}

```