---
name: "scalpel"
layout: package
next_package: swipl
previous_package: netcdf-cxx4
languages: ['c']
---
## 0.5.4
1 / 1005 files match, 1 filtered matches.

 - [bcftools-1.1/vcfplugin.c](#bcftools-11vcfpluginc)

### bcftools-1.1/vcfplugin.c

```c

{% raw %}
167 | static void *dlopen_plugin(args_t *args, const char *fname)
179 |             handle = dlopen(tmp, RTLD_NOW); // valgrind complains about unfreed memory, not our problem though
190 |     handle = dlopen(fname, RTLD_NOW);
224 |     plugin->handle = dlopen_plugin(args, fname);
{% endraw %}

```