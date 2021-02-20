---
name: "kripke"
layout: package
next_package: kubernetes
previous_package: krb5
languages: ['c']
---
## 1.2.3
4 / 4301 files match, 1 filtered matches.

 - [tpl/chai/src/tpl/umpire/src/umpire/tpl/conduit/src/thirdparty_builtin/civetweb-0a95342/src/civetweb.c](#tplchaisrctplumpiresrcumpiretplconduitsrcthirdparty_builtincivetweb-0a95342srccivetwebc)

### tpl/chai/src/tpl/umpire/src/umpire/tpl/conduit/src/thirdparty_builtin/civetweb-0a95342/src/civetweb.c

```c

{% raw %}
3845 | 
3846 | 
3847 | static HANDLE
3848 | dlopen(const char *dll_name, int flags)
3849 | {
3850 | 	wchar_t wbuf[PATH_MAX];
11826 | 	void *dll_handle;
11827 | 	struct ssl_func *fp;
11828 | 
11829 | 	if ((dll_handle = dlopen(dll_name, RTLD_LAZY)) == NULL) {
11830 | 		mg_cry(fc(ctx), "%s: cannot load %s", __func__, dll_name);
11831 | 		return NULL;
{% endraw %}

```