---
name: "bedtools2"
layout: package
next_package: sst-core
previous_package: jags
languages: ['c']
---
## 2.29.2
3 / 1042 files match, 1 filtered matches.

 - [src/utils/htslib/plugin.c](#srcutilshtslibpluginc)

### src/utils/htslib/plugin.c

```c

{% raw %}
136 |     void *lib = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
142 |         void *libg = dlopen(filename, RTLD_NOLOAD | RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```