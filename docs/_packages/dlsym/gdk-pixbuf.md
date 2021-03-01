---
name: "gdk-pixbuf"
layout: package
next_package: None
previous_package: None
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.38.2
1 / 685 files match, 1 filtered matches.

 - [gdk-pixbuf/pixops/pixops.c](#gdk-pixbufpixopspixopsc)

### gdk-pixbuf/pixops/pixops.c

```c

{% raw %}
214 |            * For x86 processors use of libumem conflicts with
215 |            * mediaLib, so avoid using it.
216 |            */
217 |           if (dlsym (RTLD_PROBE,   "umem_alloc") != NULL)
218 |             {
219 |               use_medialib = FALSE;
{% endraw %}

```