---
name: "gpgme"
layout: package
next_package: cronie
previous_package: veclibfort
languages: ['c']
---
## 1.12.0
5 / 630 files match, 2 filtered matches.

 - [src/w32-util.c](#srcw32-utilc)
 - [src/w32-io.c](#srcw32-ioc)

### src/w32-util.c

```c

{% raw %}
108 | dlopen (const char * name, int flag)
212 |       handle = dlopen ("user32.dll", RTLD_LAZY);
{% endraw %}

```
### src/w32-io.c

```c

{% raw %}
550 |      dlopen that syscall.  */
{% endraw %}

```