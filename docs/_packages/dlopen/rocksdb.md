---
name: "rocksdb"
layout: package
next_package: root
previous_package: rocfft
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 6.7.3
2 / 1539 files match, 1 filtered matches.

 - [env/env_posix.cc](#envenv_posixcc)

### env/env_posix.cc

```cpp

{% raw %}
165 |     Status status;
166 |     assert(result != nullptr);
167 |     if (name.empty()) {
168 |       void* hndl = dlopen(NULL, RTLD_NOW);
169 |       if (hndl != nullptr) {
170 |         result->reset(new PosixDynamicLibrary(name, hndl));
182 |       }
183 | #endif
184 |       if (path.empty()) {
185 |         void* hndl = dlopen(library_name.c_str(), RTLD_NOW);
186 |         if (hndl != nullptr) {
187 |           result->reset(new PosixDynamicLibrary(library_name, hndl));
193 |         while (getline(ss, local_path, kPathSeparator)) {
194 |           if (!path.empty()) {
195 |             std::string full_name = local_path + "/" + library_name;
196 |             void* hndl = dlopen(full_name.c_str(), RTLD_NOW);
197 |             if (hndl != nullptr) {
198 |               result->reset(new PosixDynamicLibrary(full_name, hndl));
{% endraw %}

```