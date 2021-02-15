---
name: "stacks"
layout: package
next_package: libxpresent
previous_package: slang
languages: ['cpp']
---
## 1.46
2 / 250 files match

 - [htslib/plugin.c](#htslibpluginc)
 - [htslib/hfile_internal.h](#htslibhfile_internalh)

### htslib/plugin.c

```cpp

{% raw %}
139 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### htslib/hfile_internal.h

```cpp

{% raw %}
104 |     /* On entry, the plugin's handle as returned by dlopen() etc.  */
{% endraw %}

```