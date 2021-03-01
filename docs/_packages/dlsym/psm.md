---
name: "psm"
layout: package
next_package: pulseaudio
previous_package: poppler
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2017-04-28
1 / 165 files match, 1 filtered matches.

 - [ptl_ips/ips_opp_path_rec.c](#ptl_ipsips_opp_path_recc)

### ptl_ips/ips_opp_path_rec.c

```c

{% raw %}
383 |   }
384 |   
385 |   /* Resolve symbols that we require within opp library */
386 |   proto->opp_fn.op_path_find_hca = dlsym(proto->opp_lib, "op_path_find_hca");
387 |   proto->opp_fn.op_path_open = dlsym(proto->opp_lib, "op_path_open");
388 |   proto->opp_fn.op_path_close = dlsym(proto->opp_lib, "op_path_close");
389 |   proto->opp_fn. op_path_get_path_by_rec = dlsym(proto->opp_lib, "op_path_get_path_by_rec");
390 |   
391 |   /* If we can't resovle any symbol then fail to load opp module */  
{% endraw %}

```