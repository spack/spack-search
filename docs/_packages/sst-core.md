---
name: "sst-core"
layout: package
next_package: ccfits
previous_package: bedtools2
languages: ['cpp']
---
## develop
3 / 525 files match

 - [configure.ac](#configureac)
 - [src/sst/core/elemLoader.cc](#srcsstcoreelemloadercc)
 - [src/sst/core/eli/elementinfo.h](#srcsstcoreelielementinfoh)

### configure.ac

```

{% raw %}
34 | LT_INIT([shared disable-static dlopen])
{% endraw %}

```
### src/sst/core/elemLoader.cc

```cpp

{% raw %}
162 |     // from dlopen, which is a useful error message for the user.
163 |     handle = dlopen(fullpath.c_str(), RTLD_NOW|RTLD_GLOBAL);
178 |     lt_handle = lt_dlopenadvise(libname.c_str(), loaderData->advise_handle);
193 |     //on how weak symbol resolution works in dlopen
{% endraw %}

```
### src/sst/core/eli/elementinfo.h

```cpp

{% raw %}
167 |         //dlopen might thrash this later - add a loader to put it back in case
{% endraw %}

```