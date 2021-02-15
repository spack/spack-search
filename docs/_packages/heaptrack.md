---
name: "heaptrack"
layout: package
next_package: lftp
previous_package: json-glib
languages: ['yaml', 'cmake', 'cpp', 'bash']
---
## 1.1.0
9 / 147 files match

 - [.travis.yml](#travisyml)
 - [src/track/libheaptrack.cpp](#srctracklibheaptrackcpp)
 - [src/track/heaptrack_preload.cpp](#srctrackheaptrack_preloadcpp)
 - [src/track/heaptrack.sh.cmake](#srctrackheaptrackshcmake)
 - [src/track/heaptrack_inject.cpp](#srctrackheaptrack_injectcpp)
 - [tests/auto/tst_inject.cpp](#testsautotst_injectcpp)
 - [3rdparty/libbacktrace/dwarf.c](#3rdpartylibbacktracedwarfc)
 - [3rdparty/libbacktrace/CMakeLists.txt](#3rdpartylibbacktracecmakeliststxt)
 - [tools/build_appimage.sh](#toolsbuild_appimagesh)

### .travis.yml

```yaml

{% raw %}
50 |   - # Ensure we prefer the bundled libs also when calling dlopen, cf.: https://github.com/KDAB/hotspot/issues/89
{% endraw %}

```
### src/track/libheaptrack.cpp

```

{% raw %}
456 |         debugLog<VerboseOutput>("dlopen_notify_callback: %s %zx", fileName, info->dlpi_addr);
624 |          * Calls to dlopen/dlclose mark the cache as dirty.
{% endraw %}

```
### src/track/heaptrack_preload.cpp

```

{% raw %}
93 | HOOK(dlopen);
141 |                        hooks::dlopen.init();
289 | void* dlopen(const char* filename, int flag) noexcept
291 |     if (!hooks::dlopen) {
295 |     void* ret = hooks::dlopen(filename, flag);
{% endraw %}

```
### src/track/heaptrack.sh.cmake

```cmake

{% raw %}
228 |             --eval-command="call (void) __libc_dlopen_mode(\"$LIBHEAPTRACK_INJECT\", 0x80000000 | 0x002)" \
235 |             --eval-command="call (void) __libc_dlopen_mode(\"$LIBHEAPTRACK_INJECT\", 0x80000000 | 0x002)" \
{% endraw %}

```
### src/track/heaptrack_inject.cpp

```

{% raw %}
129 | struct dlopen
131 |     static constexpr auto name = "dlopen";
132 |     static constexpr auto original = &::dlopen;
211 |         || hook<posix_memalign>(symname, addr, restore) || hook<dlopen>(symname, addr, restore)
{% endraw %}

```
### tests/auto/tst_inject.cpp

```

{% raw %}
86 | TEST_CASE ("inject via dlopen", "[inject]") {
90 |             auto* handle = dlopen(HEAPTRACK_LIB_INJECT_SO, RTLD_NOW);
92 |                 std::cerr << "DLOPEN FAILED: " << dlerror() << std::endl;
100 | __attribute__((weak)) void* __libc_dlopen_mode(const char* filename, int flag);
105 |     REQUIRE(__libc_dlopen_mode);
106 |     runInjectTest([]() { return __libc_dlopen_mode(HEAPTRACK_LIB_INJECT_SO, 0x80000000 | 0x002); },
{% endraw %}

```
### 3rdparty/libbacktrace/dwarf.c

```cpp

{% raw %}
2904 |   /* FIXME: See if any libraries have been dlopen'ed.  */
{% endraw %}

```
### 3rdparty/libbacktrace/CMakeLists.txt

```

{% raw %}
80 |       # Fix startup crash in dlopen_notify_callback (called indirectly from our dlopen() function) when tracing glxspheres on my AMD dev box (x86 release only)
{% endraw %}

```
### tools/build_appimage.sh

```bash

{% raw %}
53 | # Ensure we prefer the bundled libs also when calling dlopen, cf.: https://github.com/KDAB/hotspot/issues/89
{% endraw %}

```