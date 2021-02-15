---
name: "xorg-cf-files"
layout: package
next_package: libusb
previous_package: speex
languages: []
---
## 1.0.6
4 / 126 files match

 - [lnxLib.rules](#lnxlibrules)
 - [xf86site.def](#xf86sitedef)
 - [sun.cf](#suncf)
 - [xorgsite.def](#xorgsitedef)

### lnxLib.rules

```

{% raw %}
46 |  * object which needs libc.so via dlopen (), I think it should fail.
47 |  * It is a very bad idea. The moral story is DON'T USE dlopen () IN
{% endraw %}

```
### xf86site.def

```

{% raw %}
439 |  * Build dlopen() style modules instead of the standard loader modules.
{% endraw %}

```
### sun.cf

```

{% raw %}
509 | #  define DlLibrary	-lc  /* dlopen() is in libc in Solaris 10 */
512 | # define HasDlopen	YES
{% endraw %}

```
### xorgsite.def

```

{% raw %}
449 |  * This release defaults to building dlopen() style modules instead of the
{% endraw %}

```