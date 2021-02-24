---
name: "krb5"
layout: package
next_package: file
previous_package: rhash
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.16.2
9 / 4638 files match, 5 filtered matches.

 - [src/include/k5-thread.h](#srcincludek5-threadh)
 - [src/tests/shlib/t_loader.c](#srctestsshlibt_loaderc)
 - [src/plugins/preauth/pkinit/pkinit_crypto_openssl.c](#srcpluginspreauthpkinitpkinit_crypto_opensslc)
 - [src/util/exitsleep.c](#srcutilexitsleepc)
 - [src/util/support/plugins.c](#srcutilsupportpluginsc)

### src/include/k5-thread.h

```c

{% raw %}
242 |    threads.
243 | 
244 |    If we find a platform with non-functional stubs and no weak
245 |    references, we may have to resort to some hack like dlsym on the
246 |    symbol tables of the current process.  */
247 | 
{% endraw %}

```
### src/tests/shlib/t_loader.c

```c

{% raw %}
115 |         printf("from line %d: get_sym(%s)...%*s", line, symname,
116 |                HORIZ-strlen(symname), "");
117 | 
118 |     s = dlsym(libhandle, symname);
119 |     if (s == 0) {
120 |         fprintf(stderr, "symbol %s not found\n", symname);
{% endraw %}

```
### src/plugins/preauth/pkinit/pkinit_crypto_openssl.c

```c

{% raw %}
3677 |         pkiDebug("not found\n");
3678 |         return NULL;
3679 |     }
3680 |     getflist = (CK_RV (*)(CK_FUNCTION_LIST_PTR_PTR)) dlsym(handle, "C_GetFunctionList");
3681 |     if (getflist == NULL || (*getflist)(p11p) != CKR_OK) {
3682 |         dlclose(handle);
{% endraw %}

```
### src/util/exitsleep.c

```c

{% raw %}
42 | 
43 |     tv.tv_sec = 0;
44 |     tv.tv_usec = 100000;
45 |     realexit = (void (*)(int))dlsym(RTLD_NEXT, "exit");
46 |     select(0, 0, 0, 0, &tv);
47 |     realexit(status);
{% endraw %}

```
### src/util/support/plugins.c

```c

{% raw %}
337 |     if (!err && !sym && (h->dlhandle != NULL)) {
338 |         /* XXX Do we need to add a leading "_" to the symbol name on any
339 |            modern platforms?  */
340 |         sym = dlsym (h->dlhandle, csymname);
341 |         if (sym == NULL) {
342 |             const char *e = dlerror (); /* XXX copy and save away */
343 |             if (e == NULL)
344 |                 e = "unknown failure";
345 |             Tprintf ("dlsym(%s): %s\n", csymname, e);
346 |             err = ENOENT; /* XXX */
347 |             k5_set_error(ep, err, "%s", e);
{% endraw %}

```