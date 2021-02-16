---
name: "krb5"
layout: package
next_package: py-mypy
previous_package: geopm
languages: ['c']
---
## 1.16.2
7 / 4638 files match

 - [src/lib/gssapi/mechglue/g_initialize.c](#srclibgssapimechglueg_initializec)
 - [src/tests/shlib/t_loader.c](#srctestsshlibt_loaderc)
 - [src/plugins/preauth/pkinit/pkinit_crypto_openssl.c](#srcpluginspreauthpkinitpkinit_crypto_opensslc)
 - [src/util/support/plugins.c](#srcutilsupportpluginsc)

### src/lib/gssapi/mechglue/g_initialize.c

```c

{% raw %}
919 | 		(void) syslog(LOG_INFO, "libgss dlopen(%s): %s\n",
1164 | 		(void) syslog(LOG_INFO, "libgss dlopen(%s): %s\n",
{% endraw %}

```
### src/tests/shlib/t_loader.c

```c

{% raw %}
95 |     p = dlopen(namebuf, (lazy ? RTLD_LAZY : RTLD_NOW) | RTLD_MEMBER);
97 |         fprintf(stderr, "dlopen of %s failed: %s\n", namebuf, dlerror());
{% endraw %}

```
### src/plugins/preauth/pkinit/pkinit_crypto_openssl.c

```c

{% raw %}
3675 |     handle = dlopen(modname, RTLD_NOW);
{% endraw %}

```
### src/util/support/plugins.c

```c

{% raw %}
269 |             handle = dlopen(filepath, PLUGIN_DLOPEN_FLAGS);
274 |                 Tprintf ("dlopen(%s): %s\n", filepath, e);
{% endraw %}

```