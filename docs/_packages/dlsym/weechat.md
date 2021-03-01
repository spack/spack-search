---
name: "weechat"
layout: package
next_package: wget
previous_package: vtk
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.9
1 / 761 files match, 1 filtered matches.

 - [src/plugins/plugin.c](#srcpluginspluginc)

### src/plugins/plugin.c

```c

{% raw %}
338 |         return 1;
339 | 
340 |     /* look for plugin init function */
341 |     init_func = dlsym (plugin->handle, "weechat_plugin_init");
342 |     if (!init_func)
343 |         return 0;
427 |     }
428 | 
429 |     /* look for plugin name */
430 |     name = dlsym (handle, "weechat_plugin_name");
431 |     if (!name)
432 |     {
441 |     }
442 | 
443 |     /* look for API version */
444 |     api_version = dlsym (handle, "weechat_plugin_api_version");
445 |     if (!api_version)
446 |     {
489 |     }
490 | 
491 |     /* look for plugin description */
492 |     description = dlsym (handle, "weechat_plugin_description");
493 |     if (!description)
494 |     {
503 |     }
504 | 
505 |     /* look for plugin author */
506 |     author = dlsym (handle, "weechat_plugin_author");
507 |     if (!author)
508 |     {
517 |     }
518 | 
519 |     /* look for plugin version */
520 |     version = dlsym (handle, "weechat_plugin_version");
521 |     if (!version)
522 |     {
531 |     }
532 | 
533 |     /* look for plugin license */
534 |     license = dlsym (handle, "weechat_plugin_license");
535 |     if (!license)
536 |     {
545 |     }
546 | 
547 |     /* look for plugin charset (optional, default is UTF-8) */
548 |     charset = dlsym (handle, "weechat_plugin_charset");
549 | 
550 |     /* look for plugin init function */
551 |     init_func = dlsym (handle, "weechat_plugin_init");
552 |     if (!init_func)
553 |     {
566 |      * appropriate order: the important plugins that don't depend on other
567 |      * plugins are initialized first
568 |      */
569 |     priority = dlsym (handle, "weechat_plugin_priority");
570 | 
571 |     /* create new plugin */
1221 | 
1222 |     if (plugin->initialized)
1223 |     {
1224 |         end_func = dlsym (plugin->handle, "weechat_plugin_end");
1225 |         if (end_func)
1226 |             (void) (end_func) (plugin);
{% endraw %}

```