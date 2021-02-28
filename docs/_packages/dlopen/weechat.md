---
name: "weechat"
layout: package
next_package: libyogrt
previous_package: grpc
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.9
4 / 761 files match, 2 filtered matches.

 - [src/plugins/weechat-plugin.h](#srcpluginsweechat-pluginh)
 - [src/plugins/plugin.c](#srcpluginspluginc)

### src/plugins/weechat-plugin.h

```c

{% raw %}
250 | {
251 |     /* plugin variables */
252 |     char *filename;                    /* name of plugin on disk            */
253 |     void *handle;                      /* handle of plugin (given by dlopen)*/
254 |     char *name;                        /* short name                        */
255 |     char *description;                 /* description                       */
{% endraw %}

```
### src/plugins/plugin.c

```c

{% raw %}
411 |     if (plugin_autoload_array && !plugin_check_autoload (filename))
412 |         return NULL;
413 | 
414 |     handle = dlopen (filename, RTLD_GLOBAL | RTLD_NOW);
415 |     if (!handle)
416 |     {
{% endraw %}

```