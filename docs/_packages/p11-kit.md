---
name: "p11-kit"
layout: package
next_package: grpc
previous_package: flac
languages: ['cpp']
---
## 0.23.20
9 / 446 files match

 - [configure.ac](#configureac)
 - [meson.build](#mesonbuild)
 - [common/meson.build](#commonmesonbuild)
 - [common/compat.h](#commoncompath)
 - [p11-kit/modules.c](#p11-kitmodulesc)
 - [p11-kit/meson.build](#p11-kitmesonbuild)
 - [trust/meson.build](#trustmesonbuild)
 - [trust/frob-multi-init.c](#trustfrob-multi-initc)
 - [doc/manual/meson.build](#docmanualmesonbuild)

### configure.ac

```

{% raw %}
36 | LT_INIT([dlopen disable-static])
96 | 	AC_SEARCH_LIBS([dlopen], [dl dld], [], [
97 | 		AC_MSG_ERROR([could not find dlopen])
{% endraw %}

```
### meson.build

```

{% raw %}
83 | dlopen_deps = []
102 |   if not cc.has_function('dlopen')
104 |     if cc.has_function('dlopen', dependencies: libdl)
105 |       dlopen_deps += libdl
107 |       error('could not find dlopen')
{% endraw %}

```
### common/meson.build

```

{% raw %}
81 |                  dependencies: dlopen_deps,
94 |              dependencies: dlopen_deps,
{% endraw %}

```
### common/compat.h

```cpp

{% raw %}
236 | 	(dlopen ((f), RTLD_LOCAL | RTLD_NOW))
{% endraw %}

```
### p11-kit/modules.c

```cpp

{% raw %}
349 | dlopen_and_get_function_list (Module *mod,
428 | 	rv = dlopen_and_get_function_list (mod, path, &funcs);
2356 |  * on modules that have been loaded (with dlopen() for example) but not yet
{% endraw %}

```
### p11-kit/meson.build

```

{% raw %}
64 |                             dependencies: libffi_deps + dlopen_deps,
130 |                                      dependencies: [libp11_library_dep] + libffi_deps + dlopen_deps)
140 |            dependencies: [libp11_tool_dep] + libffi_deps + dlopen_deps,
147 |            dependencies: [libp11_tool_dep] + libffi_deps + dlopen_deps,
155 |            dependencies: [libp11_tool_dep] + libffi_deps + dlopen_deps,
163 |            dependencies: [libp11_tool_dep] + libsystemd_deps + libffi_deps + dlopen_deps,
175 |            dependencies: [libp11_tool_dep] + libsystemd_deps + libffi_deps + dlopen_deps,
237 |                  dependencies: [libp11_test_dep] + libffi_deps + dlopen_deps,
251 |                  dependencies: [libp11_test_dep] + libffi_deps + dlopen_deps,
{% endraw %}

```
### trust/meson.build

```

{% raw %}
95 |                           libp11_tool_dep] + libffi_deps + dlopen_deps + libtasn1_deps,
137 |                                 libp11_test_dep] + dlopen_deps,
159 |                                 libp11_test_dep] + libffi_deps + dlopen_deps,
{% endraw %}

```
### trust/frob-multi-init.c

```cpp

{% raw %}
26 | 	dl = dlopen (TRUST_SO, RTLD_LOCAL | RTLD_NOW);
{% endraw %}

```
### doc/manual/meson.build

```

{% raw %}
64 |               dependencies: libffi_deps + dlopen_deps,
{% endraw %}

```