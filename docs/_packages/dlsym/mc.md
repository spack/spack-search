---
name: "mc"
layout: package
next_package: memkind
previous_package: mariadb
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 4.8.23
3 / 1128 files match, 1 filtered matches.

 - [lib/tty/key.c](#libttykeyc)

### lib/tty/key.c

```c

{% raw %}
923 |             ph_handle = dlopen ("/usr/lib/libph.so", RTLD_NOW);
924 |             if (ph_handle != NULL)
925 |             {
926 |                 ph_attach = (ph_dv_f) dlsym (ph_handle, "PhAttach");
927 |                 ph_input_group = (ph_ov_f) dlsym (ph_handle, "PhInputGroup");
928 |                 ph_query_cursor = (ph_pqc_f) dlsym (ph_handle, "PhQueryCursor");
929 |                 if ((ph_attach != NULL) && (ph_input_group != NULL) && (ph_query_cursor != NULL)
930 |                     && (*ph_attach) (0, 0) != NULL)
{% endraw %}

```