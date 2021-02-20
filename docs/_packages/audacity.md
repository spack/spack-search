---
name: "audacity"
layout: package
next_package: autogen
previous_package: aspell
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
63 |    `connect_port()' function below) before it is asked to run.
64 | 
65 |    Plugins will reside in shared object files suitable for dynamic
66 |    linking by dlopen() and family. The file will provide a number of
67 |    `plugin types' that can be used to instantiate actual plugins
68 |    (sometimes known as `plugin instances') that can be connected
{% endraw %}

```
### win/LADSPA_plugins-win/ladspa.h

```c

{% raw %}
59 |    `connect_port()' function below) before it is asked to run.
60 | 
61 |    Plugins will reside in shared object files suitable for dynamic
62 |    linking by dlopen() and family. The file will provide a number of
63 |    `plugin types' that can be used to instantiate actual plugins
64 |    (sometimes known as `plugin instances') that can be connected
{% endraw %}

```
### lib-src/lv2/suil/src/suil_internal.h

```c

{% raw %}
126 | 	         SUIL_MODULE_PREFIX, module_name, SUIL_MODULE_EXT);
127 | 
128 | 	dlerror();
129 | 	void* lib = dlopen(path, RTLD_NOW);
130 | 	if (!lib) {
131 | 		SUIL_ERRORF("Failed to open module %s (%s)\n", path, dlerror());
{% endraw %}

```
### lib-src/lv2/suil/src/instance.c

```c

{% raw %}
198 | {
199 | 	// Open UI library
200 | 	dlerror();
201 | 	void* lib = dlopen(ui_binary_path, RTLD_NOW);
202 | 	if (!lib) {
203 | 		SUIL_ERRORF("Unable to open UI library %s (%s)\n",
{% endraw %}

```
### lib-src/lv2/lilv/src/lib.c

```c

{% raw %}
46 | 	}
47 | 
48 | 	dlerror();
49 | 	void* lib = dlopen(lib_path, RTLD_NOW);
50 | 	if (!lib) {
51 | 		LILV_ERRORF("Failed to open library %s (%s)\n", lib_path, dlerror());
{% endraw %}

```
### lib-src/lv2/lilv/src/world.c

```c

{% raw %}
542 | 
543 | 		// Open library
544 | 		dlerror();
545 | 		void* lib = dlopen(lib_path, RTLD_LAZY);
546 | 		if (!lib) {
547 | 			LILV_ERRORF("Failed to open dynmanifest library `%s' (%s)\n",
{% endraw %}

```
### lib-src/portaudio-v19/src/common/pa_dynload.c

```c

{% raw %}
62 | #if defined(WIN32)
63 |     lib = LoadLibrary(name);
64 | #else
65 |     lib = dlopen(name, RTLD_LAZY);
66 | #endif
67 | 
{% endraw %}

```
### lib-src/portaudio-v19/src/hostapi/alsa/pa_linux_alsa.c

```c

{% raw %}
355 |     PA_DEBUG(( "%s: loading ALSA library file - %s\n", __FUNCTION__, g_AlsaLibName ));
356 | 
357 |     dlerror();
358 |     g_AlsaLib = dlopen(g_AlsaLibName, (RTLD_NOW|RTLD_GLOBAL) );
359 |     if (g_AlsaLib == NULL)
360 |     {
361 |         PA_DEBUG(( "%s: failed dlopen() ALSA library file - %s, error: %s\n", __FUNCTION__, g_AlsaLibName, dlerror() ));
362 |         return 0;
363 |     }
{% endraw %}

```