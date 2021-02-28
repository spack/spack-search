---
name: "tau"
layout: package
next_package: cdo
previous_package: glusterfs
library_name: dlmopen
matches: ['dlsym', 'dlopen', 'dlmopen']
languages: ['c']
---
## master
2 / 3176 files match, 1 filtered matches.

 - [src/wrappers/taupreload/dl_auditor.c](#srcwrapperstaupreloaddl_auditorc)

### src/wrappers/taupreload/dl_auditor.c

```c

{% raw %}
35 |   static Tau_bfd_register_objopen_counter_t Tau_bfd_register_objopen_counter = NULL;
36 |   void * tau_so;
37 | 
38 |   tau_so = dlmopen(LM_ID_BASE, "libTAU.so", RTLD_NOW);
39 | 
40 |   if (tau_so) {
{% endraw %}

```