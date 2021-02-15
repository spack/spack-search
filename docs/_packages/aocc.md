---
name: "aocc"
layout: package
next_package: librsb
previous_package: hsa-rocr-dev
languages: ['cpp']
---
## 2.2.0
7 / 2874 files match

 - [lib/clang/10.0.0/lib/linux/libclang_rt.msan-x86_64.a.syms](#libclang1000liblinuxlibclang_rtmsan-x86_64asyms)
 - [lib/clang/10.0.0/lib/linux/libclang_rt.asan-x86_64.a.syms](#libclang1000liblinuxlibclang_rtasan-x86_64asyms)
 - [lib/clang/10.0.0/lib/linux/libclang_rt.tsan-x86_64.a.syms](#libclang1000liblinuxlibclang_rttsan-x86_64asyms)
 - [lib/clang/10.0.0/share/dfsan_abilist.txt](#libclang1000sharedfsan_abilisttxt)
 - [include/llvm/BinaryFormat/DynamicTags.def](#includellvmbinaryformatdynamictagsdef)
 - [include/llvm/Support/DynamicLibrary.h](#includellvmsupportdynamiclibraryh)
 - [include/llvm-c/LinkTimeOptimizer.h](#includellvm-clinktimeoptimizerh)

### lib/clang/10.0.0/lib/linux/libclang_rt.msan-x86_64.a.syms

```

{% raw %}
122 |   __interceptor_dlopen;
1374 |   dlopen;
{% endraw %}

```
### lib/clang/10.0.0/lib/linux/libclang_rt.asan-x86_64.a.syms

```

{% raw %}
87 |   __interceptor_dlopen;
1248 |   dlopen;
{% endraw %}

```
### lib/clang/10.0.0/lib/linux/libclang_rt.tsan-x86_64.a.syms

```

{% raw %}
96 |   __interceptor_dlopen;
1339 |   dlopen;
{% endraw %}

```
### lib/clang/10.0.0/share/dfsan_abilist.txt

```

{% raw %}
153 | fun:dlopen=custom
1096 | fun:__libc_dlopen_mode=uninstrumented
1869 | fun:dlopen=uninstrumented
{% endraw %}

```
### include/llvm/BinaryFormat/DynamicTags.def

```

{% raw %}
195 |                                                 // by rld on dlopen() calls.
{% endraw %}

```
### include/llvm/Support/DynamicLibrary.h

```cpp

{% raw %}
90 |       /// SO_Linker - Search as a call to dlsym(dlopen(NULL)) would when
{% endraw %}

```
### include/llvm-c/LinkTimeOptimizer.h

```cpp

{% raw %}
49 |   /// linker to use dlopen() interface to dynamically load LinkTimeOptimizer.
50 |   /// extern "C" helps, because dlopen() interface uses name to find the symbol.
{% endraw %}

```