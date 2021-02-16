---
name: "libyogrt"
layout: package
next_package: ltrace
previous_package: mindthegap
languages: ['c']
---
## 1.20-2
4 / 60 files match, 1 filtered matches.

 - [src/yogrt.c](#srcyogrtc)

### src/yogrt.c

```c

{% raw %}
270 | 	if ((backend_handle = dlopen(path, flags)) == NULL) {
271 | 		error("dlopen failed: %s\n", dlerror());
{% endraw %}

```