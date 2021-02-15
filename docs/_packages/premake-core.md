---
name: "premake-core"
layout: package
next_package: openpbs
previous_package: cairo
languages: ['cpp']
---
## 5.0.0-alpha13
2 / 1665 files match

 - [contrib/mbedtls/README.md](#contribmbedtlsreadmemd)
 - [contrib/lua/src/loadlib.c](#contribluasrcloadlibc)

### contrib/mbedtls/README.md

```

{% raw %}
27 | The Make and CMake build systems create three libraries: libmbedcrypto, libmbedx509, and libmbedtls. Note that libmbedtls depends on libmbedx509 and libmbedcrypto, and libmbedx509 depends on libmbedcrypto. As a result, some linkers will expect flags to be in a specific order, for example the GNU linker wants `-lmbedtls -lmbedx509 -lmbedcrypto`. Also, when loading shared libraries using dlopen(), you'll need to load libmbedcrypto first, then libmbedx509, before you can load libmbedtls.
{% endraw %}

```
### contrib/lua/src/loadlib.c

```cpp

{% raw %}
96 | #if defined(LUA_USE_DLOPEN)	/* { */
126 |   void *lib = dlopen(path, RTLD_NOW | (seeglb ? RTLD_GLOBAL : RTLD_LOCAL));
{% endraw %}

```