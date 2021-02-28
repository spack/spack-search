---
name: "arrow"
layout: package
next_package: fio
previous_package: multiverso
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 0.9.0
1 / 1133 files match, 1 filtered matches.

 - [cpp/src/arrow/io/hdfs-internal.cc](#cppsrcarrowiohdfs-internalcc)

### cpp/src/arrow/io/hdfs-internal.cc

```cpp

{% raw %}
60 | static std::vector<fs::path> get_potential_libjvm_paths();
61 | static std::vector<fs::path> get_potential_libhdfs_paths();
62 | static std::vector<fs::path> get_potential_libhdfs3_paths();
63 | static arrow::Status try_dlopen(std::vector<fs::path> potential_paths, const char* name,
64 | #ifndef _WIN32
65 |                                 void*& out_handle);
195 | }
196 | 
197 | #ifndef _WIN32
198 | static arrow::Status try_dlopen(std::vector<fs::path> potential_paths, const char* name,
199 |                                 void*& out_handle) {
200 |   std::vector<std::string> error_messages;
201 | 
202 |   for (auto& i : potential_paths) {
203 |     i.make_preferred();
204 |     out_handle = dlopen(i.native().c_str(), RTLD_NOW | RTLD_LOCAL);
205 | 
206 |     if (out_handle != NULL) {
226 | }
227 | 
228 | #else
229 | static arrow::Status try_dlopen(std::vector<fs::path> potential_paths, const char* name,
230 |                                 HINSTANCE& out_handle) {
231 |   std::vector<std::string> error_messages;
532 |     shim->Initialize();
533 | 
534 |     std::vector<fs::path> libjvm_potential_paths = get_potential_libjvm_paths();
535 |     RETURN_NOT_OK(try_dlopen(libjvm_potential_paths, "libjvm", libjvm_handle));
536 | 
537 |     std::vector<fs::path> libhdfs_potential_paths = get_potential_libhdfs_paths();
538 |     RETURN_NOT_OK(try_dlopen(libhdfs_potential_paths, "libhdfs", shim->handle));
539 |   } else if (shim->handle == nullptr) {
540 |     return Status::IOError("Prior attempt to load libhdfs failed");
557 |     shim->Initialize();
558 | 
559 |     std::vector<fs::path> libhdfs3_potential_paths = get_potential_libhdfs3_paths();
560 |     RETURN_NOT_OK(try_dlopen(libhdfs3_potential_paths, "libhdfs3", shim->handle));
561 |   } else if (shim->handle == nullptr) {
562 |     return Status::IOError("Prior attempt to load libhdfs3 failed");
{% endraw %}

```