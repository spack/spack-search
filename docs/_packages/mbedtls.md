---
name: "mbedtls"
layout: package
next_package: gmap-gsnap
previous_package: openpbs
languages: []
---
## 2.16.9
1 / 992 files match

 - [README.md](#readmemd)

### README.md

```

{% raw %}
23 | The Make and CMake build systems create three libraries: libmbedcrypto, libmbedx509, and libmbedtls. Note that libmbedtls depends on libmbedx509 and libmbedcrypto, and libmbedx509 depends on libmbedcrypto. As a result, some linkers will expect flags to be in a specific order, for example the GNU linker wants `-lmbedtls -lmbedx509 -lmbedcrypto`. Also, when loading shared libraries using dlopen(), you'll need to load libmbedcrypto first, then libmbedx509, before you can load libmbedtls.
{% endraw %}

```