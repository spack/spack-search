---
name: "glib"
layout: package
next_package: global
previous_package: glfw
languages: ['c']
---
## 2.56.2
14 / 2643 files match, 2 filtered matches.

 - [gmodule/gmodule-ar.c](#gmodulegmodule-arc)
 - [gmodule/gmodule-dl.c](#gmodulegmodule-dlc)

### gmodule/gmodule-ar.c

```c

{% raw %}
116 |   else
117 |     full_name = g_strdup (file_name);
118 |   
119 |   handle = dlopen (full_name, 
120 | 		   (bind_local ? RTLD_LOCAL : RTLD_GLOBAL) | RTLD_MEMBER | (bind_lazy ? RTLD_LAZY : RTLD_NOW));
121 | 
132 | {
133 |   gpointer handle;
134 | 
135 |   handle = dlopen (NULL, RTLD_GLOBAL | RTLD_LAZY);
136 |   if (!handle)
137 |     g_module_set_error (fetch_dlerror (TRUE));
{% endraw %}

```
### gmodule/gmodule-dl.c

```c

{% raw %}
94 | {
95 |   gpointer handle;
96 |   
97 |   handle = dlopen (file_name,
98 | 		   (bind_local ? 0 : RTLD_GLOBAL) | (bind_lazy ? RTLD_LAZY : RTLD_NOW));
99 |   if (!handle)
121 | #if defined(__BIONIC__)
122 |   handle = RTLD_DEFAULT;
123 | #else
124 |   handle = dlopen (NULL, RTLD_GLOBAL | RTLD_LAZY);
125 | #endif
126 |   if (!handle)
{% endraw %}

```