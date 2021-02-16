---
name: "pulseaudio"
layout: package
next_package: kahip
previous_package: cbtf-lanl
languages: ['c']
---
## 13.0
60 / 892 files match

 - [src/daemon/ltdl-bind-now.c](#srcdaemonltdl-bind-nowc)
 - [src/pulsecore/module.c](#srcpulsecoremodulec)
 - [src/pulsecore/modinfo.c](#srcpulsecoremodinfoc)
 - [src/modules/ladspa.h](#srcmodulesladspah)
 - [src/modules/module-ladspa-sink.c](#srcmodulesmodule-ladspa-sinkc)

### src/daemon/ltdl-bind-now.c

```c

{% raw %}
73 |     if (!(m = dlopen(fname, PA_BIND_NOW))) {
114 |     const lt_dlvtable *dlopen_loader;
124 |     if (!(dlopen_loader = lt_dlloader_find((char*) "lt_dlopen"))) {
125 |         pa_log_warn(_("Failed to find original lt_dlopen loader."));
134 |     memcpy(bindnow_loader, dlopen_loader, sizeof(*bindnow_loader));
{% endraw %}

```
### src/pulsecore/module.c

```c

{% raw %}
137 |     if (!(m->dl = lt_dlopenext(name))) {
{% endraw %}

```
### src/pulsecore/modinfo.c

```c

{% raw %}
76 |     if (!(dl = lt_dlopenext(name))) {
{% endraw %}

```
### src/modules/ladspa.h

```c

{% raw %}
65 |    linking by dlopen() and family. The file will provide a number of
{% endraw %}

```
### src/modules/module-ladspa-sink.c

```c

{% raw %}
1080 |     m->dl = lt_dlopenext(plugin);
{% endraw %}

```