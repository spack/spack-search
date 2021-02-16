---
name: "libfuse"
layout: package
next_package: paraview
previous_package: expat
languages: ['c']
---
## 3.9.2
1 / 93 files match

 - [lib/fuse.c](#libfusec)

### lib/fuse.c

```c

{% raw %}
268 | 	so->handle = dlopen(tmp, RTLD_NOW);
270 | 		fuse_log(FUSE_LOG_ERR, "fuse: dlopen(%s) failed: %s\n",
{% endraw %}

```