---
name: "poppler"
layout: package
next_package: portcullis
previous_package: polymake
languages: ['cpp']
---
## 0.61.1
1 / 818 files match, 1 filtered matches.

 - [poppler/GlobalParams.cc](#popplerglobalparamscc)

### poppler/GlobalParams.cc

```cpp

{% raw %}
447 | #else
448 |   //~ need to deal with other extensions here
449 |   path->append(".so");
450 |   if (!(dlA = dlopen(path->getCString(), RTLD_NOW))) {
451 |     error(errIO, -1, "Failed to load plugin '{0:t}': {1:s}",
452 | 	  path, dlerror());
{% endraw %}

```