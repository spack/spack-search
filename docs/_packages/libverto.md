---
name: "libverto"
layout: package
next_package: amgx
previous_package: libgd
languages: ['cpp']
---
## 0.3.1
2 / 45 files match

 - [configure.ac](#configureac)
 - [src/module.c](#srcmodulec)

### configure.ac

```

{% raw %}
31 | AC_CHECK_LIB([dl],[dlopen])
{% endraw %}

```
### src/module.c

```cpp

{% raw %}
105 |     mod = dlopen(NULL, RTLD_LAZY | RTLD_LOCAL);
181 |     intdll = dlopen(filename, RTLD_LAZY | RTLD_LOCAL);
204 |     intdll = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```