---
name: "krb5"
layout: package
next_package: lammps
previous_package: kmod
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.16.2
7 / 4638 files match, 4 filtered matches.

 - [src/lib/gssapi/mechglue/g_initialize.c](#srclibgssapimechglueg_initializec)
 - [src/tests/shlib/t_loader.c](#srctestsshlibt_loaderc)
 - [src/plugins/preauth/pkinit/pkinit_crypto_openssl.c](#srcpluginspreauthpkinitpkinit_crypto_opensslc)
 - [src/util/support/plugins.c](#srcutilsupportpluginsc)

### src/lib/gssapi/mechglue/g_initialize.c

```c

{% raw %}
916 | 	if (krb5int_open_plugin(minfo->uLibName, &dl, &errinfo) != 0 ||
917 | 	    errinfo.code != 0) {
918 | #if 0
919 | 		(void) syslog(LOG_INFO, "libgss dlopen(%s): %s\n",
920 | 				aMech->uLibName, dlerror());
921 | #endif
1161 | 	if (krb5int_open_plugin(aMech->uLibName, &dl, &errinfo) != 0 ||
1162 | 	    errinfo.code != 0) {
1163 | #if 0
1164 | 		(void) syslog(LOG_INFO, "libgss dlopen(%s): %s\n",
1165 | 				aMech->uLibName, dlerror());
1166 | #endif
{% endraw %}

```
### src/tests/shlib/t_loader.c

```c

{% raw %}
92 | #ifndef RTLD_MEMBER
93 | #define RTLD_MEMBER 0
94 | #endif
95 |     p = dlopen(namebuf, (lazy ? RTLD_LAZY : RTLD_NOW) | RTLD_MEMBER);
96 |     if (p == 0) {
97 |         fprintf(stderr, "dlopen of %s failed: %s\n", namebuf, dlerror());
98 |         exit(1);
99 |     }
{% endraw %}

```
### src/plugins/preauth/pkinit/pkinit_crypto_openssl.c

```c

{% raw %}
3672 |     CK_RV (*getflist)(CK_FUNCTION_LIST_PTR_PTR);
3673 | 
3674 |     pkiDebug("loading module \"%s\"... ", modname);
3675 |     handle = dlopen(modname, RTLD_NOW);
3676 |     if (handle == NULL) {
3677 |         pkiDebug("not found\n");
{% endraw %}

```
### src/util/support/plugins.c

```c

{% raw %}
266 | #endif /* USE_CFBUNDLE */
267 | 
268 |         if (!err) {
269 |             handle = dlopen(filepath, PLUGIN_DLOPEN_FLAGS);
270 |             if (handle == NULL) {
271 |                 const char *e = dlerror();
272 |                 if (e == NULL)
273 |                     e = _("unknown failure");
274 |                 Tprintf ("dlopen(%s): %s\n", filepath, e);
275 |                 err = ENOENT; /* XXX */
276 |                 k5_set_error(ep, err, _("unable to load plugin [%s]: %s"),
{% endraw %}

```