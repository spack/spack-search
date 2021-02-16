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
163 |     handle = dlopen(fullpath.c_str(), RTLD_NOW|RTLD_GLOBAL);
178 |     lt_handle = lt_dlopenadvise(libname.c_str(), loaderData->advise_handle);
{% endraw %}

```