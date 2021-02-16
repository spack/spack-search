---
name: "audacity"
layout: package
next_package: bash
previous_package: aspect
languages: ['c']
---
## 2.4.0
74 / 8278 files match, 8 filtered matches.

 - [src/effects/ladspa/ladspa.h](#srceffectsladspaladspah)
 - [win/LADSPA_plugins-win/ladspa.h](#winladspa_plugins-winladspah)
 - [lib-src/lv2/suil/src/suil_internal.h](#lib-srclv2suilsrcsuil_internalh)
 - [lib-src/lv2/suil/src/instance.c](#lib-srclv2suilsrcinstancec)
 - [lib-src/lv2/lilv/src/lib.c](#lib-srclv2lilvsrclibc)
 - [lib-src/lv2/lilv/src/world.c](#lib-srclv2lilvsrcworldc)
 - [lib-src/portaudio-v19/src/common/pa_dynload.c](#lib-srcportaudio-v19srccommonpa_dynloadc)
 - [lib-src/portaudio-v19/src/hostapi/alsa/pa_linux_alsa.c](#lib-srcportaudio-v19srchostapialsapa_linux_alsac)

### src/effects/ladspa/ladspa.h

```c

{% raw %}
66 |    linking by dlopen() and family. The file will provide a number of
{% endraw %}

```
### win/LADSPA_plugins-win/ladspa.h

```c

{% raw %}
62 |    linking by dlopen() and family. The file will provide a number of
{% endraw %}

```
### lib-src/lv2/suil/src/suil_internal.h

```c

{% raw %}
129 | 	void* lib = dlopen(path, RTLD_NOW);
{% endraw %}

```
### lib-src/lv2/suil/src/instance.c

```c

{% raw %}
201 | 	void* lib = dlopen(ui_binary_path, RTLD_NOW);
{% endraw %}

```
### lib-src/lv2/lilv/src/lib.c

```c

{% raw %}
49 | 	void* lib = dlopen(lib_path, RTLD_NOW);
{% endraw %}

```
### lib-src/lv2/lilv/src/world.c

```c

{% raw %}
545 | 		void* lib = dlopen(lib_path, RTLD_LAZY);
{% endraw %}

```
### lib-src/portaudio-v19/src/common/pa_dynload.c

```c

{% raw %}
65 |     lib = dlopen(name, RTLD_LAZY);
{% endraw %}

```
### lib-src/portaudio-v19/src/hostapi/alsa/pa_linux_alsa.c

```c

{% raw %}
358 |     g_AlsaLib = dlopen(g_AlsaLibName, (RTLD_NOW|RTLD_GLOBAL) );
361 |         PA_DEBUG(( "%s: failed dlopen() ALSA library file - %s, error: %s\n", __FUNCTION__, g_AlsaLibName, dlerror() ));
{% endraw %}

```