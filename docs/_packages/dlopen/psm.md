---
name: "psm"
layout: package
next_package: pulseaudio
previous_package: procps
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2017-04-28
1 / 165 files match, 1 filtered matches.

 - [ptl_ips/ips_opp_path_rec.c](#ptl_ipsips_opp_path_recc)

### ptl_ips/ips_opp_path_rec.c

```c

{% raw %}
374 |   struct ipath_base_info *base_info = &proto->ep->context.base_info;
375 |   char hcaName[32];
376 | 
377 |   proto->opp_lib = dlopen(DF_OPP_LIBRARY, RTLD_NOW);
378 |   if (!proto->opp_lib) {
379 |     char *err = dlerror();
{% endraw %}

```