---
name: "systemtap"
layout: package
next_package: kokkos-nvcc-wrapper
previous_package: py-soundfile
languages: ['cpp']
---
## 4.2
7 / 4791 files match

 - [aclocal.m4](#aclocalm4)
 - [stapdyn/dynutil.cxx](#stapdyndynutilcxx)
 - [stapdyn/dynutil.h](#stapdyndynutilh)
 - [stapdyn/mutator.h](#stapdynmutatorh)
 - [stapdyn/mutator.cxx](#stapdynmutatorcxx)
 - [m4/lib-link.m4](#m4lib-linkm4)
 - [testsuite/systemtap.examples/general/also_ran.stp](#testsuitesystemtapexamplesgeneralalso_ranstp)

### aclocal.m4

```

{% raw %}
2468 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### stapdyn/dynutil.cxx

```

{% raw %}
134 |   // on ld.so, when the mutator is injecting the dlopen for libdyninstAPI_RT.so.
182 | // Get an untyped symbol from a dlopened module.
{% endraw %}

```
### stapdyn/dynutil.h

```cpp

{% raw %}
28 | // Get an untyped symbol from a dlopened module.
32 | // Set a typed pointer by looking it up in a dlopened module.
{% endraw %}

```
### stapdyn/mutator.h

```cpp

{% raw %}
33 |     void* module; // the locally dlopened probe module
{% endraw %}

```
### stapdyn/mutator.cxx

```

{% raw %}
150 |   // NB: dlopen does a library-path search if the filename doesn't have any
199 |   module = dlopen(module_name.c_str(), RTLD_NOW);
202 |       staperror() << "dlopen " << dlerror() << endl;
697 |   staplog(1) << "dlopen \"" << object->name()
{% endraw %}

```
### m4/lib-link.m4

```

{% raw %}
518 |               dnl age, revision, installed, dlopen, dlpreopen, libdir.
{% endraw %}

```
### testsuite/systemtap.examples/general/also_ran.stp

```

{% raw %}
21 | # count shared libraries opened via dlopen operations
{% endraw %}

```