---
name: "sst-core"
layout: package
next_package: sst-macro
previous_package: sqlite
languages: ['cpp']
---
## develop
3 / 525 files match, 1 filtered matches.

 - [src/sst/core/elemLoader.cc](#srcsstcoreelemloadercc)

### src/sst/core/elemLoader.cc

```cpp

{% raw %}
160 |     // This is a little weird, but always try the last path - if we
161 |     // didn't succeed in the stat, we'll get a file not found error
162 |     // from dlopen, which is a useful error message for the user.
163 |     handle = dlopen(fullpath.c_str(), RTLD_NOW|RTLD_GLOBAL);
164 |     if (nullptr == handle) {
165 |         std::vector<char> err_str(1e6); //make darn sure we fit the str
175 | {
176 |     std::string libname = "lib" + elemlib;
177 |     lt_dlhandle lt_handle;
178 |     lt_handle = lt_dlopenadvise(libname.c_str(), loaderData->advise_handle);
179 |     if (nullptr == lt_handle) {
180 |       // The preopen module runs last and if the
{% endraw %}

```