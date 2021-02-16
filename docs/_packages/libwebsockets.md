---
name: "libwebsockets"
layout: package
next_package: libx11
previous_package: libvips
languages: ['c']
---
## 2.0.3
2 / 149 files match, 2 filtered matches.

 - [lib/libuv.c](#liblibuvc)
 - [lib/lws-plat-unix.c](#liblws-plat-unixc)

### lib/libuv.c

```c

{% raw %}
487 | 			if (uv_dlopen(path, &lib)) {
{% endraw %}

```
### lib/lws-plat-unix.c

```c

{% raw %}
335 | 			l = dlopen(path, RTLD_NOW);
{% endraw %}

```