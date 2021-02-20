---
name: "globalarrays"
layout: package
next_package: glpk
previous_package: global
languages: ['c']
---
## 5.6.4
25 / 1410 files match, 1 filtered matches.

 - [comex/src-ofi/ofi.h](#comexsrc-ofiofih)

### comex/src-ofi/ofi.h

```c

{% raw %}
94 | 
95 | static inline int load_ofi(fi_loadable_methods_t* table)
96 | {
97 |     ld_table.handle = dlopen(env_data.library_path, RTLD_NOW);
98 |     if (!ld_table.handle)
99 |     {
{% endraw %}

```