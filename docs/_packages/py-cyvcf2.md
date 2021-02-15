---
name: "py-cyvcf2"
layout: package
next_package: mono
previous_package: vim
languages: ['cpp']
---
## 0.11.7
2 / 145 files match

 - [htslib/plugin.c](#htslibpluginc)
 - [htslib/hfile_internal.h](#htslibhfile_internalh)

### htslib/plugin.c

```cpp

{% raw %}
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
142 |         void *libg = dlopen(filename, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### htslib/hfile_internal.h

```cpp

{% raw %}
145 |     /* On entry, the plugin's handle as returned by dlopen() etc.  */
{% endraw %}

```