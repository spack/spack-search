---
name: "haproxy"
layout: package
next_package: raja
previous_package: libffi
languages: ['c']
---
## 2.1.0
1 / 593 files match

 - [src/i386-linux-vsys.c](#srci386-linux-vsysc)

### src/i386-linux-vsys.c

```c

{% raw %}
188 | 	void *handle = dlopen("linux-gate.so.1", RTLD_NOW);
{% endraw %}

```