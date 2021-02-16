---
name: "zsh"
layout: package
next_package: raft
previous_package: jq
languages: ['c']
---
## 5.4.2
4 / 446 files match

 - [Src/module.c](#srcmodulec)

### Src/module.c

```c

{% raw %}
1591 | 	if (*buf) /* dlopen(NULL) returns a handle to the main binary */
1592 | 	    ret = dlopen(buf, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```