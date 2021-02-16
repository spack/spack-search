---
name: "flux-core"
layout: package
next_package: rocm-debug-agent
previous_package: flit
languages: ['c']
---
## 0.15.0
18 / 1484 files match, 8 filtered matches.

 - [src/common/libflux/handle.c](#srccommonlibfluxhandlec)
 - [src/common/libflux/module.c](#srccommonlibfluxmodulec)
 - [src/common/libflux/plugin.c](#srccommonlibfluxpluginc)
 - [src/common/libflux/test/plugin.c](#srccommonlibfluxtestpluginc)
 - [src/modules/pymod/py_mod.c](#srcmodulespymodpy_modc)
 - [src/broker/pmiutil.c](#srcbrokerpmiutilc)
 - [src/broker/module.c](#srcbrokermodulec)
 - [t/module/parent.c](#tmoduleparentc)

### src/common/libflux/handle.c

```c

{% raw %}
221 |     if (!(dso = dlopen (path, RTLD_LAZY | RTLD_LOCAL | FLUX_DEEPBIND))) {
227 |         goto error_dlopen;
232 | error_dlopen:
{% endraw %}

```
### src/common/libflux/module.c

```c

{% raw %}
43 |     if (!(dso = dlopen (path, RTLD_LAZY | RTLD_LOCAL | FLUX_DEEPBIND))) {
{% endraw %}

```
### src/common/libflux/plugin.c

```c

{% raw %}
201 |     if (!(p->dso = dlopen (path, RTLD_LAZY|RTLD_LOCAL|FLUX_DEEPBIND)))
202 |         return plugin_seterror (p, errno, "dlopen: %s", dlerror ());
{% endraw %}

```
### src/common/libflux/test/plugin.c

```c

{% raw %}
392 |     like (flux_plugin_strerror (p), "^dlopen: .*Is a directory",
{% endraw %}

```
### src/modules/pymod/py_mod.c

```c

{% raw %}
155 |     if (!dlopen (PYTHON_LIBRARY, RTLD_LAZY|RTLD_GLOBAL))
156 |         flux_log_error (h, "Unable to dlopen libpython");
{% endraw %}

```
### src/broker/pmiutil.c

```c

{% raw %}
61 | static struct pmi_dso *broker_pmi_dlopen (const char *pmi_library, int debug)
75 |         if (!(dso->dso = dlopen (name, RTLD_NOW | RTLD_GLOBAL))) {
81 |                     log_msg ("dlopen %s failed", name);
92 |                 log_msg ("dlopen %s", name);
258 |         pmi->dso = broker_pmi_dlopen (getenv ("PMI_LIBRARY"), pmi->debug);
263 |                            : pmi->dso ? "dlopen" : "singleton");
{% endraw %}

```
### src/broker/module.c

```c

{% raw %}
66 |     mod_main_f *main;       /* dlopened mod_main() */
68 |     void *dso;              /* reference on dlopened module */
546 |     if (!(dso = dlopen (path, RTLD_NOW | RTLD_LOCAL | FLUX_DEEPBIND))) {
{% endraw %}

```
### t/module/parent.c

```c

{% raw %}
77 |     m->dso = dlopen (path, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```