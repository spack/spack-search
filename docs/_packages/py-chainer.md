---
name: "py-chainer"
layout: package
next_package: py-cryptography
previous_package: py-cffi
languages: ['cpp', 'c']
---
## 7.2.0
5 / 1793 files match, 4 filtered matches.

 - [chainerx_cc/chainerx/context.cc](#chainerx_ccchainerxcontextcc)
 - [chainerx_cc/chainerx/context.h](#chainerx_ccchainerxcontexth)
 - [chainerx_cc/chainerx/platform.cc](#chainerx_ccchainerxplatformcc)
 - [chainerx_cc/chainerx/platform/windows.cc](#chainerx_ccchainerxplatformwindowscc)

### chainerx_cc/chainerx/context.cc

```cpp

{% raw %}
45 | Context::~Context() {
46 |     // Need to call dtor of all backends before closing shared objects
47 |     backends_.clear();
48 |     for (void* handle : dlopen_handles_) {
49 |         try {
50 |             DlClose(handle);
90 |         }
91 |         {
92 |             std::lock_guard<std::mutex> lock{mutex_};
93 |             dlopen_handles_.push_back(handle);
94 |         }
95 | 
{% endraw %}

```
### chainerx_cc/chainerx/context.h

```c

{% raw %}
159 |     std::string ToBackpropIdString(BackpropOrdinal ordinal) const;
160 | 
161 |     std::unordered_map<std::string, std::unique_ptr<Backend, context_detail::BackendDeleter>> backends_;
162 |     std::vector<void*> dlopen_handles_;
163 |     mutable std::mutex mutex_;
164 | 
{% endraw %}

```
### chainerx_cc/chainerx/platform.cc

```cpp

{% raw %}
44 | }
45 | 
46 | void* DlOpen(const std::string& filename) {
47 |     if (void* handle = ::dlopen(filename.c_str(), RTLD_NOW | RTLD_LOCAL)) {
48 |         return handle;
49 |     }
{% endraw %}

```
### chainerx_cc/chainerx/platform/windows.cc

```cpp

{% raw %}
25 | 
26 | void* DlOpen(const std::string& filename) {
27 |     // TODO(hvy): Implement dlopen for Windows.
28 |     throw ChainerxError{"dlopen not implemented for Windows."};
29 | }
30 | 
{% endraw %}

```