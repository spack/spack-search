---
name: "scalpel"
layout: package
next_package: scorep
previous_package: sblim-sfcc
languages: ['c']
---
## 0.5.4
1 / 1005 files match, 1 filtered matches.

 - [bcftools-1.1/vcfplugin.c](#bcftools-11vcfpluginc)

### bcftools-1.1/vcfplugin.c

```c

{% raw %}
164 |         args->nplugin_paths = 0;
165 | }
166 | 
167 | static void *dlopen_plugin(args_t *args, const char *fname)
168 | {
169 |     init_plugin_paths(args);
176 |         for (i=0; i<args->nplugin_paths; i++)
177 |         {
178 |             tmp = msprintf("%s/%s.so", args->plugin_paths[i],fname);
179 |             handle = dlopen(tmp, RTLD_NOW); // valgrind complains about unfreed memory, not our problem though
180 |             if ( args->verbose )
181 |             {
187 |         }
188 |     }
189 | 
190 |     handle = dlopen(fname, RTLD_NOW);
191 |     if ( args->verbose )
192 |     {
221 | {
222 |     plugin->name = strdup(fname);
223 | 
224 |     plugin->handle = dlopen_plugin(args, fname);
225 |     if ( !plugin->handle )
226 |     {
{% endraw %}

```