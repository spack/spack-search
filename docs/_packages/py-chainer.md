---
name: "py-chainer"
layout: package
next_package: verrou
previous_package: libxslt
languages: ['cpp']
---
## 7.2.0
5 / 1793 files match

 - [chainerx_cc/chainerx/context.cc](#chainerx_ccchainerxcontextcc)
 - [chainerx_cc/chainerx/context.h](#chainerx_ccchainerxcontexth)
 - [chainerx_cc/chainerx/platform.cc](#chainerx_ccchainerxplatformcc)
 - [chainerx_cc/chainerx/CMakeLists.txt](#chainerx_ccchainerxcmakeliststxt)
 - [chainerx_cc/chainerx/platform/windows.cc](#chainerx_ccchainerxplatformwindowscc)

### chainerx_cc/chainerx/context.cc

```cpp

{% raw %}
48 |     for (void* handle : dlopen_handles_) {
87 |             handle = DlOpen(so_file_path);
93 |             dlopen_handles_.push_back(handle);
{% endraw %}

```
### chainerx_cc/chainerx/context.h

```cpp

{% raw %}
162 |     std::vector<void*> dlopen_handles_;
{% endraw %}

```
### chainerx_cc/chainerx/platform.cc

```cpp

{% raw %}
26 | void* DlOpen(const std::string& filename) { return windows::DlOpen(filename); }
46 | void* DlOpen(const std::string& filename) {
47 |     if (void* handle = ::dlopen(filename.c_str(), RTLD_NOW | RTLD_LOCAL)) {
{% endraw %}

```
### chainerx_cc/chainerx/CMakeLists.txt

```

{% raw %}
131 | # dlopen / dlclose
{% endraw %}

```
### chainerx_cc/chainerx/platform/windows.cc

```cpp

{% raw %}
26 | void* DlOpen(const std::string& filename) {
27 |     // TODO(hvy): Implement dlopen for Windows.
28 |     throw ChainerxError{"dlopen not implemented for Windows."};
{% endraw %}

```