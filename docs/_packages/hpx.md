---
name: "hpx"
layout: package
next_package: libnsl
previous_package: curl
languages: []
---
## master
3 / 4279 files match

 - [libs/core/plugin/CMakeLists.txt](#libscoreplugincmakeliststxt)
 - [libs/core/plugin/include/hpx/plugin/dll.hpp](#libscorepluginincludehpxplugindllhpp)
 - [libs/core/plugin/include/hpx/plugin/detail/dll_dlopen.hpp](#libscorepluginincludehpxplugindetaildll_dlopenhpp)

### libs/core/plugin/CMakeLists.txt

```

{% raw %}
21 |     hpx/plugin/detail/dll_dlopen.hpp
{% endraw %}

```
### libs/core/plugin/include/hpx/plugin/dll.hpp

```

{% raw %}
11 | #if !defined(HPX_HAS_DLOPEN)
12 | #define HPX_HAS_DLOPEN 1
18 | #elif defined(HPX_HAS_DLOPEN)
19 | #include <hpx/plugin/detail/dll_dlopen.hpp>
{% endraw %}

```
### libs/core/plugin/include/hpx/plugin/detail/dll_dlopen.hpp

```

{% raw %}
32 | #if !defined(HPX_HAS_DLOPEN)
54 |     reinterpret_cast<HMODULE>(dlopen(x, RTLD_GLOBAL | RTLD_LAZY))
349 |                         HMODULE probe_handle = ::dlopen(image_name, RTLD_NOW);
{% endraw %}

```