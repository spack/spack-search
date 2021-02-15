---
name: "jchronoss"
layout: package
next_package: php
previous_package: xclock
languages: ['cpp']
---
## 1.2
2 / 386 files match

 - [deps/libwebsockets/lib/libuv.c](#depslibwebsocketsliblibuvc)
 - [deps/libwebsockets/lib/lws-plat-unix.c](#depslibwebsocketsliblws-plat-unixc)

### deps/libwebsockets/lib/libuv.c

```cpp

{% raw %}
495 | 			if (uv_dlopen(path, &lib)) {
{% endraw %}

```
### deps/libwebsockets/lib/lws-plat-unix.c

```cpp

{% raw %}
341 | 			l = dlopen(path, RTLD_NOW);
{% endraw %}

```