---
name: "flux-core"
layout: package
next_package: foam-extend
previous_package: flexiblas
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
218 |         errno = ENOENT;
219 |         goto error;
220 |     }
221 |     if (!(dso = dlopen (path, RTLD_LAZY | RTLD_LOCAL | FLUX_DEEPBIND))) {
222 |         errno = EINVAL;
223 |         goto error;
224 |     }
225 |     if (!(connector_init = dlsym (dso, "connector_init"))) {
226 |         errno = EINVAL;
227 |         goto error_dlopen;
228 |     }
229 |     *dsop = dso;
230 |     free (path);
231 |     return connector_init;
232 | error_dlopen:
233 |     ERRNO_SAFE_WRAP (dlclose, dso);
234 | error:
{% endraw %}

```
### src/common/libflux/module.c

```c

{% raw %}
40 |         errno = EINVAL;
41 |         return NULL;
42 |     }
43 |     if (!(dso = dlopen (path, RTLD_LAZY | RTLD_LOCAL | FLUX_DEEPBIND))) {
44 |         if (cb)
45 |             cb (dlerror (), arg);
{% endraw %}

```
### src/common/libflux/plugin.c

```c

{% raw %}
198 |     if (access (path, R_OK) < 0)
199 |         return plugin_seterror (p, errno, "%s: %s", path, strerror (errno));
200 |     dlerror ();
201 |     if (!(p->dso = dlopen (path, RTLD_LAZY|RTLD_LOCAL|FLUX_DEEPBIND)))
202 |         return plugin_seterror (p, errno, "dlopen: %s", dlerror ());
203 | 
204 |     free (p->path);
{% endraw %}

```
### src/common/libflux/test/plugin.c

```c

{% raw %}
389 |         "flux_plugin_strerror returns expected result");
390 |     ok (flux_plugin_load_dso (p, "/tmp") < 0,
391 |         "flux_plugin_load_dso on directory fails");
392 |     like (flux_plugin_strerror (p), "^dlopen: .*Is a directory",
393 |         "flux_plugin_strerror returns expected result");
394 | 
{% endraw %}

```
### src/modules/pymod/py_mod.c

```c

{% raw %}
152 |     }
153 | 
154 |     flux_log(h, LOG_INFO, "loading python module named: %s", module_name);
155 |     if (!dlopen (PYTHON_LIBRARY, RTLD_LAZY|RTLD_GLOBAL))
156 |         flux_log_error (h, "Unable to dlopen libpython");
157 | 
158 |     PyObject *module = PyImport_ImportModule("flux.core.trampoline");
{% endraw %}

```
### src/broker/pmiutil.c

```c

{% raw %}
58 | /* Notes:
59 |  * - Use RTLD_GLOBAL due to issue #432
60 |  */
61 | static struct pmi_dso *broker_pmi_dlopen (const char *pmi_library, int debug)
62 | {
63 |     struct pmi_dso *dso;
72 |         goto error;
73 |     FOREACH_ZLIST (libs, name) {
74 |         dlerror ();
75 |         if (!(dso->dso = dlopen (name, RTLD_NOW | RTLD_GLOBAL))) {
76 |             if (debug) {
77 |                 char *errstr = dlerror ();
78 |                 if (errstr)
79 |                     log_msg ("%s", errstr);
80 |                 else
81 |                     log_msg ("dlopen %s failed", name);
82 |             }
83 |         }
89 |         }
90 |         else {
91 |             if (debug)
92 |                 log_msg ("dlopen %s", name);
93 |         }
94 |     }
255 |      * Fortunately it emulates singleton in that case, in lieu of failing.
256 |      */
257 |     if (!pmi->cli)
258 |         pmi->dso = broker_pmi_dlopen (getenv ("PMI_LIBRARY"), pmi->debug);
259 |     /* If neither pmi->cli nor pmi->dso is set, singleton is assumed later.
260 |      */
261 |     if (pmi->debug)
262 |         log_msg ("using %s", pmi->cli ? "PMI-1 wire protocol"
263 |                            : pmi->dso ? "dlopen" : "singleton");
264 |     return pmi;
265 | }
{% endraw %}

```
### src/broker/module.c

```c

{% raw %}
63 |     uuid_t uuid;            /* uuid for unique request sender identity */
64 |     char uuid_str[UUID_STR_LEN];
65 |     pthread_t t;            /* module thread */
66 |     mod_main_f *main;       /* dlopened mod_main() */
67 |     char *name;
68 |     void *dso;              /* reference on dlopened module */
69 |     int size;               /* size of .so file for lsmod */
70 |     char *digest;           /* digest of .so file for lsmod */
543 |     int rc;
544 | 
545 |     dlerror ();
546 |     if (!(dso = dlopen (path, RTLD_NOW | RTLD_LOCAL | FLUX_DEEPBIND))) {
547 |         log_msg ("%s", dlerror ());
548 |         errno = ENOENT;
{% endraw %}

```
### t/module/parent.c

```c

{% raw %}
74 |         return NULL;
75 |     }
76 |     m->size = sb.st_size;
77 |     m->dso = dlopen (path, RTLD_NOW | RTLD_LOCAL);
78 |     if (!m->dso || !(m->main = dlsym (m->dso, "mod_main"))) {
79 |         module_destroy (m);
{% endraw %}

```