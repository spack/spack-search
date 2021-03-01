---
name: "legion"
layout: package
next_package: None
previous_package: None
library_name: dlmopen
matches: ['dlsym', 'dlopen', 'dlmopen']
languages: ['cpp']
---
## master
1 / 2136 files match, 1 filtered matches.

 - [runtime/realm/python/python_module.cc](#runtimerealmpythonpython_modulecc)

### runtime/realm/python/python_module.cc

```cpp

{% raw %}
133 |     const char *dlmproxy_filename = getenv("DLMPROXY_LIBPTHREAD");
134 |     if(!dlmproxy_filename)
135 |       dlmproxy_filename = "dlmproxy_libpthread.so.0";
136 |     dlmproxy_handle = dlmopen(LM_ID_NEWLM,
137 | 			      dlmproxy_filename,
138 | 			      RTLD_DEEPBIND | RTLD_GLOBAL | RTLD_LAZY);
139 |     if(!dlmproxy_handle) {
140 |       const char *error = dlerror();
141 |       log_py.fatal() << "HELP!  Use of dlmopen for python requires dlmproxy for pthreads!  Failed to\n"
142 | 		     << "  load: " << dlmproxy_filename << "\n"
143 | 		     << "  error: " << error;
157 |     int ret = dlinfo(dlmproxy_handle, RTLD_DI_LMID, &lmid);
158 |     assert(ret == 0);
159 | 
160 |     handle = dlmopen(lmid, python_lib, RTLD_DEEPBIND | RTLD_GLOBAL | RTLD_NOW);
161 | #else
162 |     // life is so much easier if we use dlopen (but we only get one copy then)
{% endraw %}

```