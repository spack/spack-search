---
name: "ghostscript"
layout: package
next_package: kmod
previous_package: cntk
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 9.27
19 / 4764 files match, 4 filtered matches.

 - [base/gp_unix.c](#basegp_unixc)
 - [base/memento.c](#basemementoc)
 - [jbig2dec/memento.c](#jbig2decmementoc)
 - [contrib/opvp/gdevopvp.c](#contribopvpgdevopvpc)

### base/gp_unix.c

```c

{% raw %}
74 | 
75 |   while ((dirent = readdir(dir)) != 0) {
76 |     strncpy(pbuff, dirent->d_name, sizeof(buff) - (pbuff - buff) - 1);
77 |     if ((handle = dlopen(buff, RTLD_NOW)) != 0) {
78 |       if ((gs_shared_init = dlsym(handle, "gs_shared_init")) != 0) {
79 |         (*gs_shared_init)();
{% endraw %}

```
### base/memento.c

```c

{% raw %}
552 | 
553 | static int init_libbt(void)
554 | {
555 |     libbt = dlopen("libbacktrace.so", RTLD_LAZY);
556 |     if (libbt == NULL)
557 |         libbt = dlopen("/opt/lib/libbacktrace.so", RTLD_LAZY);
558 |     if (libbt == NULL)
559 |         libbt = dlopen("/lib/libbacktrace.so", RTLD_LAZY);
560 |     if (libbt == NULL)
561 |         libbt = dlopen("/usr/lib/libbacktrace.so", RTLD_LAZY);
562 |     if (libbt == NULL)
563 |         libbt = dlopen("/usr/local/lib/libbacktrace.so", RTLD_LAZY);
564 |     if (libbt == NULL)
565 |         goto fail;
{% endraw %}

```
### jbig2dec/memento.c

```c

{% raw %}
552 | 
553 | static int init_libbt(void)
554 | {
555 |     libbt = dlopen("libbacktrace.so", RTLD_LAZY);
556 |     if (libbt == NULL)
557 |         libbt = dlopen("/opt/lib/libbacktrace.so", RTLD_LAZY);
558 |     if (libbt == NULL)
559 |         libbt = dlopen("/lib/libbacktrace.so", RTLD_LAZY);
560 |     if (libbt == NULL)
561 |         libbt = dlopen("/usr/lib/libbacktrace.so", RTLD_LAZY);
562 |     if (libbt == NULL)
563 |         libbt = dlopen("/usr/local/lib/libbacktrace.so", RTLD_LAZY);
564 |     if (libbt == NULL)
565 |         goto fail;
{% endraw %}

```
### contrib/opvp/gdevopvp.c

```c

{% raw %}
1777 |     if (list) {
1778 |         i = 0;
1779 |         while (list[i]) {
1780 |             if ((h = dlopen(list[i],RTLD_NOW))) {
1781 |                 OpenPrinter = dlsym(h,"opvpOpenPrinter");
1782 |                 ErrorNo = dlsym(h,"opvpErrorNo");
{% endraw %}

```