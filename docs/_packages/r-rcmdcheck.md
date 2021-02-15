---
name: "r-rcmdcheck"
layout: package
next_package: yorick
previous_package: lumpy-sv
languages: []
---
## 1.3.3
2 / 69 files match

 - [tests/testthat/parse-install-fail.txt](#teststestthatparse-install-failtxt)
 - [tests/testthat/RSQLServer-install/00install.out](#teststestthatrsqlserver-install00installout)

### tests/testthat/parse-install-fail.txt

```

{% raw %}
16 |   dlopen(/Users/hadley/Documents/dplyr/dbplyr/revdep/library/RSQLServer/rJava/libs/rJava.so, 6): Library not loaded: @rpath/libjvm.dylib
{% endraw %}

```
### tests/testthat/RSQLServer-install/00install.out

```

{% raw %}
8 |   dlopen(/Users/hadley/Documents/dplyr/dbplyr/revdep/library/RSQLServer/rJava/libs/rJava.so, 6): Library not loaded: @rpath/libjvm.dylib
{% endraw %}

```