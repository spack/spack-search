---
name: "openwsman"
layout: package
next_package: p11-kit
previous_package: openssl
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.6.10
7 / 490 files match, 4 filtered matches.

 - [src/lib/wsman-plugins.c](#srclibwsman-pluginsc)
 - [src/server/wsmand-listener.c](#srcserverwsmand-listenerc)
 - [src/server/shttpd/shttpd.c](#srcservershttpdshttpdc)
 - [src/authenticators/pam/pam_auth.c](#srcauthenticatorspampam_authc)

### src/lib/wsman-plugins.c

```c

{% raw %}
106 | {
107 |     WsManPluginError PluginError = PLUGIN_ERROR_OK ;
108 |     self->p_name = u_strdup(p_name) ;
109 |     if (NULL != (self->p_handle = dlopen(p_name, RTLD_LAZY))) {
110 |         self->init = dlsym(self->p_handle, "init");
111 |         self->get_endpoints = dlsym(self->p_handle, "get_endpoints");
{% endraw %}

```
### src/server/wsmand-listener.c

```c

{% raw %}
507 | 		should_return = 1;
508 | 	}
509 | 
510 | 	hnd = dlopen(name, RTLD_LAZY | RTLD_GLOBAL);
511 | 	if (hnd == NULL) {
512 | 		fprintf(stderr, "Could not dlopen %s\n", name);
513 | 		res = 1;
514 | 		goto DONE;
{% endraw %}

```
### src/server/shttpd/shttpd.c

```c

{% raw %}
1489 | 	EC_KEY*		key;
1490 | 
1491 | 	/* Load SSL library dynamically */
1492 | 	if ((lib = dlopen(SSL_LIB, RTLD_LAZY)) == NULL) {
1493 | 		_shttpd_elog(E_LOG, NULL, "set_ssl: cannot load %s", SSL_LIB);
1494 | 		return (FALSE);
{% endraw %}

```
### src/authenticators/pam/pam_auth.c

```c

{% raw %}
116 | {
117 | 	void *hnd;
118 | 
119 | 	hnd = dlopen(LIBPAM, RTLD_LAZY | RTLD_GLOBAL);
120 | 	if (hnd == NULL) {
121 | 		debug("Could not dlopen %s", LIBPAM);
122 | 		return 1;
123 | 	}
{% endraw %}

```