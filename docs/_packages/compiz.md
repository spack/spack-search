---
name: "compiz"
layout: package
next_package: conduit
previous_package: collectd
languages: ['c']
---
## 0.7.8
4 / 222 files match, 2 filtered matches.

 - [src/screen.c](#srcscreenc)
 - [src/plugin.c](#srcpluginc)

### src/screen.c

```c

{% raw %}
939 |     if (!funcPtr)
940 |     {
941 | 	if (!dlhand)
942 | 	    dlhand = dlopen (NULL, RTLD_LAZY);
943 | 
944 | 	if (dlhand)
{% endraw %}

```
### src/plugin.c

```c

{% raw %}
156 |     else
157 | 	sprintf (file, "lib%s.so", name);
158 | 
159 |     dlhand = dlopen (file, RTLD_LAZY);
160 |     if (dlhand)
161 |     {
{% endraw %}

```