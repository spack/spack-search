---
name: "r"
layout: package
next_package: r-fs
previous_package: quantum-espresso
languages: ['c']
---
## 3.3.1
12 / 4124 files match, 3 filtered matches.

 - [src/unix/hpdlfcn.c](#srcunixhpdlfcnc)
 - [src/unix/dynload.c](#srcunixdynloadc)
 - [src/unix/hpdlfcn.h](#srcunixhpdlfcnh)

### src/unix/hpdlfcn.c

```c

{% raw %}
127 | void *dlopen(const char *fname, int mode)
{% endraw %}

```
### src/unix/dynload.c

```c

{% raw %}
24 |    We include this table, even when we have dlopen and friends.
91 |     handle = (void *) dlopen(path,openFlag);
126 |     Computes the flag to be passed as the second argument to dlopen(),
165 | 				   resulting dlopen(). */
{% endraw %}

```
### src/unix/hpdlfcn.h

```c

{% raw %}
0 | void *dlopen(const char *, int);
{% endraw %}

```