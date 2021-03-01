---
name: "pulseaudio"
layout: package
next_package: pythia8
previous_package: psm
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 13.0
60 / 892 files match, 5 filtered matches.

 - [src/daemon/ltdl-bind-now.c](#srcdaemonltdl-bind-nowc)
 - [src/pulsecore/module.c](#srcpulsecoremodulec)
 - [src/pulsecore/modinfo.c](#srcpulsecoremodinfoc)
 - [src/modules/ladspa.h](#srcmodulesladspah)
 - [src/modules/module-ladspa-sink.c](#srcmodulesmodule-ladspa-sinkc)

### src/daemon/ltdl-bind-now.c

```c

{% raw %}
70 | 
71 |     pa_assert(fname);
72 | 
73 |     if (!(m = dlopen(fname, PA_BIND_NOW))) {
74 |         pa_log(_("Failed to open module %s: %s"), fname, dlerror());
75 |         lt_dlseterror(LT_ERROR_CANNOT_OPEN);
111 | void pa_ltdl_init(void) {
112 | 
113 | #ifdef PA_BIND_NOW
114 |     const lt_dlvtable *dlopen_loader;
115 | #endif
116 | 
121 |     if (bindnow_loader)
122 |         return;
123 | 
124 |     if (!(dlopen_loader = lt_dlloader_find((char*) "lt_dlopen"))) {
125 |         pa_log_warn(_("Failed to find original lt_dlopen loader."));
126 |         return;
127 |     }
131 |         return;
132 |     }
133 | 
134 |     memcpy(bindnow_loader, dlopen_loader, sizeof(*bindnow_loader));
135 |     bindnow_loader->name = "bind-now-loader";
136 |     bindnow_loader->module_open = bind_now_open;
{% endraw %}

```
### src/pulsecore/module.c

```c

{% raw %}
134 |     m->hooks = pa_dynarray_new((pa_free_cb_t) pa_hook_slot_free);
135 |     m->index = PA_IDXSET_INVALID;
136 | 
137 |     if (!(m->dl = lt_dlopenext(name))) {
138 |         /* We used to print the error that is returned by lt_dlerror(), but
139 |          * lt_dlerror() is useless. It returns pretty much always "file not
{% endraw %}

```
### src/pulsecore/modinfo.c

```c

{% raw %}
73 | 
74 |     pa_assert(name);
75 | 
76 |     if (!(dl = lt_dlopenext(name))) {
77 |         pa_log("Failed to open module \"%s\": %s", name, lt_dlerror());
78 |         return NULL;
{% endraw %}

```
### src/modules/ladspa.h

```c

{% raw %}
62 |    `connect_port()' function below) before it is asked to run.
63 | 
64 |    Plugins will reside in shared object files suitable for dynamic
65 |    linking by dlopen() and family. The file will provide a number of
66 |    `plugin types' that can be used to instantiate actual plugins
67 |    (sometimes known as `plugin instances') that can be connected
{% endraw %}

```
### src/modules/module-ladspa-sink.c

```c

{% raw %}
1077 |     /* FIXME: This is not exactly thread safe */
1078 |     t = pa_xstrdup(lt_dlgetsearchpath());
1079 |     lt_dlsetsearchpath(e);
1080 |     m->dl = lt_dlopenext(plugin);
1081 |     lt_dlsetsearchpath(t);
1082 |     pa_xfree(t);
{% endraw %}

```