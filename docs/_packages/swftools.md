---
name: "swftools"
layout: package
next_package: swipl
previous_package: stinger
languages: ['cpp']
---
## 0.9.2
2 / 480 files match, 1 filtered matches.

 - [lib/pdf/xpdf/GlobalParams.cc](#libpdfxpdfglobalparamscc)

### lib/pdf/xpdf/GlobalParams.cc

```cpp

{% raw %}
508 | #else
509 |   //~ need to deal with other extensions here
510 |   path->append(".so");
511 |   if (!(dlA = dlopen(path->getCString(), RTLD_NOW))) {
512 |     error(-1, "Failed to load plugin '%s': %s",
513 | 	  path->getCString(), dlerror());
{% endraw %}

```