---
name: "ghostscript"
layout: package
next_package: glew
previous_package: geopm
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 9.27
15 / 4764 files match, 4 filtered matches.

 - [base/gp_unix.c](#basegp_unixc)
 - [base/memento.c](#basemementoc)
 - [jbig2dec/memento.c](#jbig2decmementoc)
 - [contrib/opvp/gdevopvp.c](#contribopvpgdevopvpc)

### base/gp_unix.c

```c

{% raw %}
75 |   while ((dirent = readdir(dir)) != 0) {
76 |     strncpy(pbuff, dirent->d_name, sizeof(buff) - (pbuff - buff) - 1);
77 |     if ((handle = dlopen(buff, RTLD_NOW)) != 0) {
78 |       if ((gs_shared_init = dlsym(handle, "gs_shared_init")) != 0) {
79 |         (*gs_shared_init)();
80 |       } else {
{% endraw %}

```
### base/memento.c

```c

{% raw %}
564 |     if (libbt == NULL)
565 |         goto fail;
566 | 
567 |     backtrace_create_state = dlsym(libbt, "backtrace_create_state");
568 |     backtrace_syminfo      = dlsym(libbt, "backtrace_syminfo");
569 |     backtrace_pcinfo       = dlsym(libbt, "backtrace_pcinfo");
570 | 
571 |     if (backtrace_create_state == NULL ||
{% endraw %}

```
### jbig2dec/memento.c

```c

{% raw %}
564 |     if (libbt == NULL)
565 |         goto fail;
566 | 
567 |     backtrace_create_state = dlsym(libbt, "backtrace_create_state");
568 |     backtrace_syminfo      = dlsym(libbt, "backtrace_syminfo");
569 |     backtrace_pcinfo       = dlsym(libbt, "backtrace_pcinfo");
570 | 
571 |     if (backtrace_create_state == NULL ||
{% endraw %}

```
### contrib/opvp/gdevopvp.c

```c

{% raw %}
1778 |         i = 0;
1779 |         while (list[i]) {
1780 |             if ((h = dlopen(list[i],RTLD_NOW))) {
1781 |                 OpenPrinter = dlsym(h,"opvpOpenPrinter");
1782 |                 ErrorNo = dlsym(h,"opvpErrorNo");
1783 |                 if (OpenPrinter && ErrorNo) {
1784 |                     handle = h;
1787 |                 OpenPrinter = NULL;
1788 |                 ErrorNo = NULL;
1789 |                 /* try version 0.2 driver */
1790 |                 OpenPrinter_0_2 = dlsym(h,"OpenPrinter");
1791 |                 ErrorNo = dlsym(h,"errorno");
1792 |                 if (OpenPrinter_0_2 && ErrorNo) {
1793 |                     handle = h;
{% endraw %}

```