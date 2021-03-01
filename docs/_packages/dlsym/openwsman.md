---
name: "openwsman"
layout: package
next_package: papi
previous_package: openssl
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.6.10
7 / 490 files match, 6 filtered matches.

 - [src/lib/wsman-server-api.c](#srclibwsman-server-apic)
 - [src/lib/wsman-server.c](#srclibwsman-serverc)
 - [src/lib/wsman-plugins.c](#srclibwsman-pluginsc)
 - [src/server/wsmand-listener.c](#srcserverwsmand-listenerc)
 - [src/server/shttpd/shttpd.c](#srcservershttpdshttpdc)
 - [src/authenticators/pam/pam_auth.c](#srcauthenticatorspampam_authc)

### src/lib/wsman-server-api.c

```c

{% raw %}
83 | 	node = list_first(listener->plugins);
84 | 	while (node) {
85 | 		WsManPlugin *p = (WsManPlugin *) node->list_data;
86 | 		p->set_config = dlsym(p->p_handle, "set_config");
87 | 		if (listener->config && p->set_config) {
88 | 			p->set_config(p->p_handle, listener->config);
{% endraw %}

```
### src/lib/wsman-server.c

```c

{% raw %}
107 |                 }
108 | 		ifcinfo = p->ifc;
109 | 	        ifcinfo->extraData = p->data;
110 | 		p->set_config = dlsym(p->p_handle, "set_config");
111 | 
112 | 		if (listener->config && p->set_config) {
{% endraw %}

```
### src/lib/wsman-plugins.c

```c

{% raw %}
107 |     WsManPluginError PluginError = PLUGIN_ERROR_OK ;
108 |     self->p_name = u_strdup(p_name) ;
109 |     if (NULL != (self->p_handle = dlopen(p_name, RTLD_LAZY))) {
110 |         self->init = dlsym(self->p_handle, "init");
111 |         self->get_endpoints = dlsym(self->p_handle, "get_endpoints");
112 |         if ( ! self->get_endpoints
113 |                 && ! self->init)
{% endraw %}

```
### src/server/wsmand-listener.c

```c

{% raw %}
513 | 		res = 1;
514 | 		goto DONE;
515 | 	}
516 | 	basic_callback = dlsym(hnd, "authorize");
517 | 	if (basic_callback == NULL) {
518 | 		fprintf(stderr, "Could not resolve authorize() in %s\n",
521 | 		goto DONE;
522 | 	}
523 | 
524 | 	init = dlsym(hnd, "initialize");
525 | 	if (init != NULL) {
526 | 		res = init(arg);
{% endraw %}

```
### src/server/shttpd/shttpd.c

```c

{% raw %}
1495 | 	}
1496 | 
1497 | 	for (fp = ssl_sw; fp->name != NULL; fp++)
1498 | 		if ((fp->ptr.v_void = dlsym(lib, fp->name)) == NULL) {
1499 | 			_shttpd_elog(E_LOG, NULL,"set_ssl: cannot find %s", fp->name);
1500 | 			return (FALSE);
{% endraw %}

```
### src/authenticators/pam/pam_auth.c

```c

{% raw %}
63 | 
64 | 
65 | #define debug_dlsym(sym) \
66 | 	debug("Could not dlsym %s", sym)
67 | 
68 | #ifdef STANDALONE
121 | 		debug("Could not dlopen %s", LIBPAM);
122 | 		return 1;
123 | 	}
124 | 	PAM_start = dlsym(hnd, "pam_start");
125 | 	if (PAM_start == NULL) {
126 | 		debug_dlsym("pam_start");
127 | 		dlclose(hnd);
128 | 		return 1;
129 | 	}
130 | 	PAM_authenticate = dlsym(hnd, "pam_authenticate");
131 | 	if (PAM_authenticate == NULL) {
132 | 		debug_dlsym("pam_authenticate");
133 | 		dlclose(hnd);
134 | 		return 1;
135 | 	}
136 | 	PAM_acct_mgmt = dlsym(hnd, "pam_acct_mgmt");
137 | 	if (PAM_acct_mgmt == NULL) {
138 | 		debug_dlsym("pam_acct_mgmt");
139 | 		dlclose(hnd);
140 | 		return 1;
141 | 	}
142 | 	PAM_end = dlsym(hnd, "pam_end");
143 | 	if (PAM_end == NULL) {
144 | 		debug_dlsym("pam_end");
145 | 		dlclose(hnd);
146 | 		return 1;
147 | 	}
148 | 	PAM_strerror = dlsym(hnd, "pam_strerror");
149 | 	if (PAM_strerror == NULL) {
150 | 		debug_dlsym("pam_strerror");
151 | 		dlclose(hnd);
152 | 		return 1;
{% endraw %}

```