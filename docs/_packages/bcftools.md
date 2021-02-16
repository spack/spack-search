---
name: "bcftools"
layout: package
next_package: libunwind
previous_package: pangolin
languages: ['c']
---
## 1.9
5 / 1127 files match, 2 filtered matches.

 - [vcfplugin.c](#vcfpluginc)
 - [htslib-1.9/plugin.c](#htslib-19pluginc)

### vcfplugin.c

```c

{% raw %}
203 | static void *dlopen_plugin(args_t *args, const char *fname)
215 |             handle = dlopen(tmp, RTLD_NOW); // valgrind complains about unfreed memory, not our problem though
218 |                 if ( !handle ) fprintf(stderr,"%s:\n\tdlopen   .. %s\n", tmp,dlerror());
219 |                 else fprintf(stderr,"%s:\n\tdlopen   .. ok\n", tmp);
226 |     handle = dlopen(fname, RTLD_NOW);
229 |         if ( !handle ) fprintf(stderr,"%s:\n\tdlopen   .. %s\n", fname,dlerror());
230 |         else fprintf(stderr,"%s:\n\tdlopen   .. ok\n", fname);
255 |     plugin->handle = dlopen_plugin(args, fname);
{% endraw %}

```
### htslib-1.9/plugin.c

```c

{% raw %}
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
142 |         void *libg = dlopen(filename, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```