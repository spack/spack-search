---
name: "linux-pam"
layout: package
next_package: hpctoolkit
previous_package: nfs-utils
languages: ['c']
---
## 1.3.1
14 / 945 files match, 4 filtered matches.

 - [libpam/pam_dynamic.c](#libpampam_dynamicc)
 - [libpam/pam_handlers.c](#libpampam_handlersc)
 - [libpam/pam_private.h](#libpampam_privateh)
 - [tests/tst-dlopen.c](#teststst-dlopenc)

### libpam/pam_dynamic.c

```c

{% raw %}
47 | void *_pam_dlopen(const char *mod_path)
64 | 	return dlopen(mod_path, RTLD_NOW);
{% endraw %}

```
### libpam/pam_handlers.c

```c

{% raw %}
701 | 	D(("_pam_load_module: _pam_dlopen(%s)", mod_path));
702 | 	mod->dl_handle = _pam_dlopen(mod_path);
703 | 	D(("_pam_load_module: _pam_dlopen'ed"));
704 | 	D(("_pam_load_module: dlopen'ed"));
719 | 		    mod->dl_handle = _pam_dlopen(mod_full_isa_path);
725 | 	    D(("_pam_load_module: _pam_dlopen(%s) failed", mod_path));
727 | 		pam_syslog(pamh, LOG_ERR, "unable to dlopen(%s): %s", mod_path,
{% endraw %}

```
### libpam/pam_private.h

```c

{% raw %}
243 | void *_pam_dlopen (const char *mod_path);
{% endraw %}

```
### tests/tst-dlopen.c

```c

{% raw %}
26 |     if (dlopen(argv[i], RTLD_NOW)) {
27 |       fprintf(stdout, "dlopen() of \"%s\" succeeded.\n",
31 |       if ((stat(buf, &st) == 0) && dlopen(buf, RTLD_NOW)) {
32 |         fprintf(stdout, "dlopen() of \"./%s\" "
35 |         fprintf(stdout, "dlopen() of \"%s\" failed: "
{% endraw %}

```