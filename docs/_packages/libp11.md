---
name: "libp11"
layout: package
next_package: sfcgal
previous_package: harfbuzz
languages: ['cpp']
---
## 0.4.10
2 / 85 files match

 - [configure.ac](#configureac)
 - [src/libpkcs11.c](#srclibpkcs11c)

### configure.ac

```

{% raw %}
188 | 		[dlopen],
191 | 		[AC_MSG_ERROR([dlopen required])]
{% endraw %}

```
### src/libpkcs11.c

```cpp

{% raw %}
66 | 	mod->handle = dlopen(mspec, RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```