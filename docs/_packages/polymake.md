---
name: "polymake"
layout: package
next_package: icu4c
previous_package: fakexrandr
languages: ['cpp']
---
## 3.5
1 / 3513 files match, 1 filtered matches.

 - [lib/callable/src/perl/Main.cc](#libcallablesrcperlmaincc)

### lib/callable/src/perl/Main.cc

```cpp

{% raw %}
168 |       polyhandle = dlopen(dli_polymake.dli_fname, RTLD_LAZY | RTLD_NOLOAD | RTLD_GLOBAL );
171 |       std::cerr << "*** WARNING: Failed to (re-)dlopen libpolymake with RTLD_GLOBAL: " 
178 |       perlhandle = dlopen(dli_perl.dli_fname, RTLD_LAZY | RTLD_NOLOAD | RTLD_GLOBAL );
181 |       std::cerr << "*** WARNING: Failed to (re-)dlopen libperl with RTLD_GLOBAL: " 
{% endraw %}

```