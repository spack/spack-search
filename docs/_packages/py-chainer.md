---
name: "py-chainer"
layout: package
next_package: verrou
previous_package: libxslt
languages: ['cpp', 'c']
---
## 7.2.0
5 / 1793 files match

 - [chainerx_cc/chainerx/context.cc](#chainerx_ccchainerxcontextcc)
 - [chainerx_cc/chainerx/context.h](#chainerx_ccchainerxcontexth)
 - [chainerx_cc/chainerx/platform.cc](#chainerx_ccchainerxplatformcc)
 - [chainerx_cc/chainerx/platform/windows.cc](#chainerx_ccchainerxplatformwindowscc)

### chainerx_cc/chainerx/context.cc

```cpp

{% raw %}
48 |     for (void* handle : dlopen_handles_) {
93 |             dlopen_handles_.push_back(handle);
{% endraw %}

```
### chainerx_cc/chainerx/context.h

```c

{% raw %}
162 |     std::vector<void*> dlopen_handles_;
{% endraw %}

```
### chainerx_cc/chainerx/platform.cc

```cpp

{% raw %}
47 |     if (void* handle = ::dlopen(filename.c_str(), RTLD_NOW | RTLD_LOCAL)) {
{% endraw %}

```
### chainerx_cc/chainerx/platform/windows.cc

```cpp

{% raw %}
28 |     throw ChainerxError{"dlopen not implemented for Windows."};
{% endraw %}

```