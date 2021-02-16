---
name: "openwsman"
layout: package
next_package: libidl
previous_package: libgssglue
languages: ['c']
---
## 2.6.10
7 / 490 files match

 - [src/lib/wsman-plugins.c](#srclibwsman-pluginsc)
 - [src/server/wsmand-listener.c](#srcserverwsmand-listenerc)
 - [src/server/shttpd/shttpd.c](#srcservershttpdshttpdc)
 - [src/authenticators/pam/pam_auth.c](#srcauthenticatorspampam_authc)

### src/lib/wsman-plugins.c

```c

{% raw %}
109 |     if (NULL != (self->p_handle = dlopen(p_name, RTLD_LAZY))) {
{% endraw %}

```
### src/server/wsmand-listener.c

```c

{% raw %}
510 | 	hnd = dlopen(name, RTLD_LAZY | RTLD_GLOBAL);
512 | 		fprintf(stderr, "Could not dlopen %s\n", name);
{% endraw %}

```
### src/server/shttpd/shttpd.c

```c

{% raw %}
1492 | 	if ((lib = dlopen(SSL_LIB, RTLD_LAZY)) == NULL) {
{% endraw %}

```
### src/authenticators/pam/pam_auth.c

```c

{% raw %}
119 | 	hnd = dlopen(LIBPAM, RTLD_LAZY | RTLD_GLOBAL);
121 | 		debug("Could not dlopen %s", LIBPAM);
{% endraw %}

```