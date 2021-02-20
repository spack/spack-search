---
name: "hepmc3"
layout: package
next_package: hip-rocclr
previous_package: hdf5
languages: ['cpp']
---
## 3.2.2
3 / 373 files match, 2 filtered matches.

 - [src/WriterPlugin.cc](#srcwriterplugincc)
 - [src/ReaderPlugin.cc](#srcreaderplugincc)

### src/WriterPlugin.cc

```cpp

{% raw %}
39 | 
40 | #if defined(__linux__) || defined(__darwin__)
41 |     dll_handle=nullptr;
42 |     dll_handle = dlopen(libname.c_str(), RTLD_LAZY | RTLD_GLOBAL);
43 |     if (!dll_handle) { printf("Error  while loading library %s: %s\n",libname.c_str(),dlerror()); m_writer=nullptr; return;  }
44 |     Writer* (*newWriter)(std::ostream & stream,std::shared_ptr<GenRunInfo>);
63 | 
64 | #if defined(__linux__) || defined(__darwin__)
65 |     dll_handle=nullptr;
66 |     dll_handle = dlopen(libname.c_str(), RTLD_LAZY | RTLD_GLOBAL);
67 |     if (!dll_handle) { printf("Error  while loading library %s: %s\n",libname.c_str(),dlerror()); m_writer=nullptr; return;  }
68 |     Writer* (*newWriter)(const std::string&,std::shared_ptr<GenRunInfo>);
{% endraw %}

```
### src/ReaderPlugin.cc

```cpp

{% raw %}
38 | 
39 | #if defined(__linux__) || defined(__darwin__)
40 |     dll_handle=nullptr;
41 |     dll_handle = dlopen(libname.c_str(), RTLD_LAZY | RTLD_GLOBAL);
42 |     if (!dll_handle) { printf("Error  while loading library %s: %s\n",libname.c_str(),dlerror()); m_reader=nullptr; return;  }
43 |     Reader* (*newReader)(std::istream & stream);
62 | 
63 | #if defined(__linux__) || defined(__darwin__)
64 |     dll_handle=nullptr;
65 |     dll_handle = dlopen(libname.c_str(), RTLD_LAZY | RTLD_GLOBAL);
66 |     if (!dll_handle) { printf("Error  while loading library %s: %s\n",libname.c_str(),dlerror()); m_reader=nullptr; return;  }
67 |     Reader* (*newReader)(const std::string&);
{% endraw %}

```