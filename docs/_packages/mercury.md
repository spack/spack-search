---
name: "mercury"
layout: package
next_package: unuran
previous_package: turbine
languages: []
---
## 2.0.0
3 / 569 files match

 - [Testing/driver/kwsys/DynamicLoader.cxx](#testingdriverkwsysdynamicloadercxx)
 - [Testing/driver/kwsys/DynamicLoader.hxx.in](#testingdriverkwsysdynamicloaderhxxin)
 - [Testing/driver/kwsys/testDynamicLoader.cxx](#testingdriverkwsystestdynamicloadercxx)

### Testing/driver/kwsys/DynamicLoader.cxx

```

{% raw %}
22 | //   later) which use dlopen
400 | // later) which use dlopen
408 |   return dlopen(libname.c_str(), RTLD_LAZY);
{% endraw %}

```
### Testing/driver/kwsys/DynamicLoader.hxx.in

```

{% raw %}
32 |  * \warning dlopen on *nix system works the following way:
{% endraw %}

```
### Testing/driver/kwsys/testDynamicLoader.cxx

```

{% raw %}
89 | // dlopen() on Syllable before 11/22/2007 doesn't return 0 on error
99 |   // This one is actually fun to test, since dlopen is by default
101 |   res += TestDynamicLoader("foobar.lib", "dlopen", 0, 1, 0);
102 |   res += TestDynamicLoader("libdl.so", "dlopen", 1, 1, 1);
{% endraw %}

```