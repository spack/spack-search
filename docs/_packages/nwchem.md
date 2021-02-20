---
name: "nwchem"
layout: package
next_package: ocaml
previous_package: nvhpc
languages: ['c']
---
## 6.8.1
26 / 20838 files match, 1 filtered matches.

 - [src/tools/ga-5.6.5/comex/src-ofi/ofi.h](#srctoolsga-565comexsrc-ofiofih)

### src/tools/ga-5.6.5/comex/src-ofi/ofi.h

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