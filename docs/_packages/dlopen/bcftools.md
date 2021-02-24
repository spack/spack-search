---
name: "bcftools"
layout: package
next_package: openssl
previous_package: guile
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.9
5 / 1127 files match, 2 filtered matches.

 - [vcfplugin.c](#vcfpluginc)
 - [htslib-1.9/plugin.c](#htslib-19pluginc)

### vcfplugin.c

```c

{% raw %}
200 |     add_plugin_paths(args, path ? path : "");
201 | }
202 | 
203 | static void *dlopen_plugin(args_t *args, const char *fname)
204 | {
205 |     init_plugin_paths(args);
212 |         for (i=0; i<args->nplugin_paths; i++)
213 |         {
214 | 	    tmp = msprintf("%s/%s%s", args->plugin_paths[i], fname, PLUGIN_EXT);
215 |             handle = dlopen(tmp, RTLD_NOW); // valgrind complains about unfreed memory, not our problem though
216 |             if ( args->verbose > 1 )
217 |             {
218 |                 if ( !handle ) fprintf(stderr,"%s:\n\tdlopen   .. %s\n", tmp,dlerror());
219 |                 else fprintf(stderr,"%s:\n\tdlopen   .. ok\n", tmp);
220 |             }
221 |             free(tmp);
223 |         }
224 |     }
225 | 
226 |     handle = dlopen(fname, RTLD_NOW);
227 |     if ( args->verbose > 1 )
228 |     {
229 |         if ( !handle ) fprintf(stderr,"%s:\n\tdlopen   .. %s\n", fname,dlerror());
230 |         else fprintf(stderr,"%s:\n\tdlopen   .. ok\n", fname);
231 |     }
232 | 
252 | {
253 |     plugin->name = strdup(fname);
254 | 
255 |     plugin->handle = dlopen_plugin(args, fname);
256 |     if ( !plugin->handle )
257 |     {
{% endraw %}

```
### htslib-1.9/plugin.c

```c

{% raw %}
133 | 
134 | void *load_plugin(void **pluginp, const char *filename, const char *symbol)
135 | {
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
137 |     if (lib == NULL) goto error;
138 | 
139 |     void *sym = dlsym(lib, symbol);
140 |     if (sym == NULL) {
141 |         // Reopen the plugin with RTLD_GLOBAL and check for uniquified symbol
142 |         void *libg = dlopen(filename, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL);
143 |         if (libg == NULL) goto error;
144 |         dlclose(lib);
{% endraw %}

```