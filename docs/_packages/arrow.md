---
name: "arrow"
layout: package
next_package: aspect
previous_package: arrayfire
languages: ['cpp']
---
## 0.9.0
1 / 1133 files match, 1 filtered matches.

 - [cpp/src/arrow/io/hdfs-internal.cc](#cppsrcarrowiohdfs-internalcc)

### cpp/src/arrow/io/hdfs-internal.cc

```cpp

{% raw %}
63 | static arrow::Status try_dlopen(std::vector<fs::path> potential_paths, const char* name,
198 | static arrow::Status try_dlopen(std::vector<fs::path> potential_paths, const char* name,
204 |     out_handle = dlopen(i.native().c_str(), RTLD_NOW | RTLD_LOCAL);
229 | static arrow::Status try_dlopen(std::vector<fs::path> potential_paths, const char* name,
535 |     RETURN_NOT_OK(try_dlopen(libjvm_potential_paths, "libjvm", libjvm_handle));
538 |     RETURN_NOT_OK(try_dlopen(libhdfs_potential_paths, "libhdfs", shim->handle));
560 |     RETURN_NOT_OK(try_dlopen(libhdfs3_potential_paths, "libhdfs3", shim->handle));
{% endraw %}

```