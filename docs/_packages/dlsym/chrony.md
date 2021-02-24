---
name: "chrony"
layout: package
next_package: bazel
previous_package: jags
library_name: dlsym
matches: ['dlsym']
languages: ['c']
---
## 3.3
1 / 143 files match, 1 filtered matches.

 - [sys_macosx.c](#sys_macosxc)

### sys_macosx.c

```c

{% raw %}
482 | SYS_MacOSX_Initialise(void)
483 | {
484 | #ifdef HAVE_MACOS_SYS_TIMEX
485 |   have_ntp_adjtime = (dlsym(RTLD_NEXT, "ntp_adjtime") != NULL);
486 |   if (have_ntp_adjtime) {
487 |     have_bad_adjtime = !test_adjtime();
{% endraw %}

```