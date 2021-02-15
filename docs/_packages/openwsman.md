---
name: "openwsman"
layout: package
next_package: libidl
previous_package: libgssglue
languages: ['cpp']
---
## 2.6.10
7 / 490 files match

 - [src/lib/wsman-plugins.c](#srclibwsman-pluginsc)
 - [src/lib/wsman-soap.c](#srclibwsman-soapc)
 - [src/server/wsmand-listener.c](#srcserverwsmand-listenerc)
 - [src/server/shttpd/compat_win32.h](#srcservershttpdcompat_win32h)
 - [src/server/shttpd/shttpd.c](#srcservershttpdshttpdc)
 - [src/plugins/swig/src/target_ruby.c](#srcpluginsswigsrctarget_rubyc)
 - [src/authenticators/pam/pam_auth.c](#srcauthenticatorspampam_authc)

### src/lib/wsman-plugins.c

```cpp

{% raw %}
109 |     if (NULL != (self->p_handle = dlopen(p_name, RTLD_LAZY))) {
{% endraw %}

```
### src/lib/wsman-soap.c

```cpp

{% raw %}
987 |  * However, if they are dlopened from somewhere other than 
{% endraw %}

```
### src/server/wsmand-listener.c

```cpp

{% raw %}
510 | 	hnd = dlopen(name, RTLD_LAZY | RTLD_GLOBAL);
512 | 		fprintf(stderr, "Could not dlopen %s\n", name);
{% endraw %}

```
### src/server/shttpd/compat_win32.h

```cpp

{% raw %}
51 | #define	dlopen(x,y)		LoadLibraryW(x)
{% endraw %}

```
### src/server/shttpd/shttpd.c

```cpp

{% raw %}
1492 | 	if ((lib = dlopen(SSL_LIB, RTLD_LAZY)) == NULL) {
{% endraw %}

```
### src/plugins/swig/src/target_ruby.c

```cpp

{% raw %}
160 |  * self: handle (from dlopen)
{% endraw %}

```
### src/authenticators/pam/pam_auth.c

```cpp

{% raw %}
119 | 	hnd = dlopen(LIBPAM, RTLD_LAZY | RTLD_GLOBAL);
121 | 		debug("Could not dlopen %s", LIBPAM);
{% endraw %}

```