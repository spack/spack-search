---
name: "openssh"
layout: package
next_package: py-pyopenssl
previous_package: py-shapely
languages: ['cpp']
---
## 7.9p1
2 / 674 files match

 - [configure.ac](#configureac)
 - [ssh-pkcs11.c](#ssh-pkcs11c)

### configure.ac

```

{% raw %}
1864 | 	# PKCS#11 support requires dlopen() and co
1865 | 	AC_SEARCH_LIBS([dlopen], [dl],
3223 | 			AC_CHECK_LIB([dl], [dlopen], , )
3235 | 			if test $ac_cv_lib_dl_dlopen = yes; then
{% endraw %}

```
### ssh-pkcs11.c

```cpp

{% raw %}
610 | 	if ((handle = dlopen(provider_id, RTLD_NOW)) == NULL) {
611 | 		error("dlopen %s failed: %s", provider_id, dlerror());
{% endraw %}

```