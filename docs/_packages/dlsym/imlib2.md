---
name: "imlib2"
layout: package
next_package: None
previous_package: None
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.5.1
4 / 157 files match, 2 filtered matches.

 - [src/lib/image.c](#srclibimagec)
 - [src/lib/dynamic_filters.c](#srclibdynamic_filtersc)

### src/lib/image.c

```c

{% raw %}
576 |         free(l);
577 |         return NULL;
578 |      }
579 |    l->load = dlsym(l->handle, "load");
580 |    l->save = dlsym(l->handle, "save");
581 |    l_formats = dlsym(l->handle, "formats");
582 | 
583 |    /* each loader must provide formats() and at least load() or save() */
{% endraw %}

```
### src/lib/dynamic_filters.c

```c

{% raw %}
44 |         free(ptr);
45 |         return NULL;
46 |      }
47 |    ptr->init_filter = dlsym(ptr->handle, "init");
48 |    ptr->deinit_filter = dlsym(ptr->handle, "deinit");
49 |    ptr->exec_filter = dlsym(ptr->handle, "exec");
50 |    if (!ptr->init_filter || !ptr->deinit_filter || !ptr->exec_filter)
51 |      {
{% endraw %}

```