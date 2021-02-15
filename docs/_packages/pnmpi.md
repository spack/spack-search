---
name: "pnmpi"
layout: package
next_package: rocm-opencl
previous_package: lua
languages: ['cpp']
---
## 1.7
2 / 294 files match

 - [README.md](#readmemd)
 - [src/pnmpi/core.c](#srcpnmpicorec)

### README.md

```

{% raw %}
340 |   1. Build the tool as a shared module (a dlopen-able shared library).
{% endraw %}

```
### src/pnmpi/core.c

```cpp

{% raw %}
162 |           *handle = dlopen(location, RTLD_LAZY);
601 |                       DBGPRINT2("dlopen successful");
{% endraw %}

```