---
name: "bcftools"
layout: package
next_package: bear
previous_package: bazel
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.9
2 / 1127 files match, 2 filtered matches.

 - [vcfplugin.c](#vcfpluginc)
 - [htslib-1.9/plugin.c](#htslib-19pluginc)

### vcfplugin.c

```c

{% raw %}
264 |     }
265 | 
266 |     dlerror();
267 |     plugin->init = (dl_init_f) dlsym(plugin->handle, "init");
268 |     char *ret = dlerror();
269 |     if ( ret )
271 |     else
272 |         if ( args->verbose > 1 ) fprintf(stderr,"\tinit     .. ok\n");
273 | 
274 |     plugin->run = (dl_run_f) dlsym(plugin->handle, "run");
275 |     ret = dlerror();
276 |     if ( ret )
285 |         return -1;
286 |     }
287 | 
288 |     plugin->version = (dl_version_f) dlsym(plugin->handle, "version");
289 |     ret = dlerror();
290 |     if ( ret )
294 |         return -1;
295 |     }
296 | 
297 |     plugin->about = (dl_about_f) dlsym(plugin->handle, "about");
298 |     ret = dlerror();
299 |     if ( ret )
302 |         return -1;
303 |     }
304 | 
305 |     plugin->usage = (dl_about_f) dlsym(plugin->handle, "usage");
306 |     ret = dlerror();
307 |     if ( ret )
309 | 
310 |     if ( plugin->run ) return 0;
311 | 
312 |     plugin->process = (dl_process_f) dlsym(plugin->handle, "process");
313 |     ret = dlerror();
314 |     if ( ret )
317 |         return -1;
318 |     }
319 | 
320 |     plugin->destroy = (dl_destroy_f) dlsym(plugin->handle, "destroy");
321 |     ret = dlerror();
322 |     if ( ret )
{% endraw %}

```
### htslib-1.9/plugin.c

```c

{% raw %}
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
137 |     if (lib == NULL) goto error;
138 | 
139 |     void *sym = dlsym(lib, symbol);
140 |     if (sym == NULL) {
141 |         // Reopen the plugin with RTLD_GLOBAL and check for uniquified symbol
151 |         const char *basename = slash? slash+1 : filename;
152 |         kputsn(basename, strcspn(basename, ".-+"), &symbolg);
153 | 
154 |         sym = dlsym(lib, symbolg.s);
155 |         free(symbolg.s);
156 |         if (sym == NULL) goto error;
169 | 
170 | void *plugin_sym(void *plugin, const char *name, const char **errmsg)
171 | {
172 |     void *sym = dlsym(plugin, name);
173 |     if (sym == NULL) *errmsg = dlerror();
174 |     return sym;
{% endraw %}

```