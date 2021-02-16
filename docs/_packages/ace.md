---
name: "ace"
layout: package
next_package: activeharmony
previous_package: abseil-cpp
languages: ['pl', 'c']
---
## 6.5.12
20 / 8830 files match, 2 filtered matches.

 - [bin/fuzz.pl](#binfuzzpl)
 - [ace/OS_NS_dlfcn.h](#aceos_ns_dlfcnh)

### bin/fuzz.pl

```pl

{% raw %}
627 |     $OS_NS_dlfcn_symbols = "dlclose|dlerror|dlopen|dlsym";
{% endraw %}

```
### ace/OS_NS_dlfcn.h

```c

{% raw %}
45 |   ACE_SHLIB_HANDLE dlopen (const ACE_TCHAR *filename,
{% endraw %}

```