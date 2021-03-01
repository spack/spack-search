---
name: "poppler"
layout: package
next_package: psm
previous_package: pocl
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 0.61.1
1 / 818 files match, 1 filtered matches.

 - [poppler/GlobalParams.cc](#popplerglobalparamscc)

### poppler/GlobalParams.cc

```cpp

{% raw %}
452 | 	  path, dlerror());
453 |     goto err1;
454 |   }
455 |   if (!(vt = (XpdfPluginVecTable *)dlsym(dlA, "xpdfPluginVecTable"))) {
456 |     error(errIO, -1, "Failed to find xpdfPluginVecTable in plugin '{0:t}'",
457 | 	  path);
473 |     goto err2;
474 |   }
475 | #else
476 |   if (!(xpdfInitPlugin = (XpdfBool (*)(void))dlsym(dlA, "xpdfInitPlugin"))) {
477 |     error(errIO, -1, "Failed to find xpdfInitPlugin in plugin '{0:t}'",
478 | 	  path);
525 |   }
526 |   FreeLibrary(lib);
527 | #else
528 |   if ((xpdfFreePlugin = (void (*)(void))dlsym(dl, "xpdfFreePlugin"))) {
529 |     (*xpdfFreePlugin)();
530 |   }
{% endraw %}

```