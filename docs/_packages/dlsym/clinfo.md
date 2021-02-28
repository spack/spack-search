---
name: "clinfo"
layout: package
next_package: lftp
previous_package: spot
library_name: dlsym
matches: ['dlsym']
languages: ['c']
---
## 2.2.18.04.06
1 / 21 files match, 1 filtered matches.

 - [src/clinfo.c](#srcclinfoc)

### src/clinfo.c

```c

{% raw %}
3045 | 		struct icd_loader_test check = icd_loader_tests[i];
3046 | 		if (check.symbol == NULL)
3047 | 			break;
3048 | 		if (dlsym(DL_MODULE, check.symbol) == NULL)
3049 | 			break;
3050 | 		icdl.detected_version = check.version;
{% endraw %}

```