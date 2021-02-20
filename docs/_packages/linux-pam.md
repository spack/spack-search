---
name: "linux-pam"
layout: package
next_package: lksctp-tools
previous_package: linux-headers
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
44 | #define SHLIB_SYM_PREFIX "_"
45 | #endif
46 | 
47 | void *_pam_dlopen(const char *mod_path)
48 | {
49 | #ifdef PAM_SHL
61 | 
62 | 	return ret;
63 | #else
64 | 	return dlopen(mod_path, RTLD_NOW);
65 | #endif
66 | }
{% endraw %}

```
### libpam/pam_handlers.c

```c

{% raw %}
698 | 	/* Be pessimistic... */
699 | 	success = PAM_ABORT;
700 | 
701 | 	D(("_pam_load_module: _pam_dlopen(%s)", mod_path));
702 | 	mod->dl_handle = _pam_dlopen(mod_path);
703 | 	D(("_pam_load_module: _pam_dlopen'ed"));
704 | 	D(("_pam_load_module: dlopen'ed"));
705 | 	if (mod->dl_handle == NULL) {
706 | 	    if (strstr(mod_path, "$ISA")) {
716 | 		        memmove(isa + strlen(_PAM_ISA), isa + 4, strlen(isa + 4) + 1);
717 | 		        memmove(isa, _PAM_ISA, strlen(_PAM_ISA));
718 | 		    }
719 | 		    mod->dl_handle = _pam_dlopen(mod_full_isa_path);
720 | 		    _pam_drop(mod_full_isa_path);
721 | 		}
722 | 	    }
723 | 	}
724 | 	if (mod->dl_handle == NULL) {
725 | 	    D(("_pam_load_module: _pam_dlopen(%s) failed", mod_path));
726 | 	    if (handler_type != PAM_HT_SILENT_MODULE)
727 | 		pam_syslog(pamh, LOG_ERR, "unable to dlopen(%s): %s", mod_path,
728 | 		    _pam_dlerror());
729 | 	    /* Don't abort yet; static code may be able to find function.
{% endraw %}

```
### libpam/pam_private.h

```c

{% raw %}
240 | typedef void (*voidfunc(void))(void);
241 | typedef int (*servicefn)(pam_handle_t *, int, int, char **);
242 | 
243 | void *_pam_dlopen (const char *mod_path);
244 | servicefn _pam_dlsym (void *handle, const char *symbol);
245 | void _pam_dlclose (void *handle);
{% endraw %}

```
### tests/tst-dlopen.c

```c

{% raw %}
23 |   char buf[PATH_MAX];
24 | 
25 |   for (i = 1; i < argc; i++) {
26 |     if (dlopen(argv[i], RTLD_NOW)) {
27 |       fprintf(stdout, "dlopen() of \"%s\" succeeded.\n",
28 |               argv[i]);
29 |     } else {
30 |       snprintf(buf, sizeof(buf), "./%s", argv[i]);
31 |       if ((stat(buf, &st) == 0) && dlopen(buf, RTLD_NOW)) {
32 |         fprintf(stdout, "dlopen() of \"./%s\" "
33 |                 "succeeded.\n", argv[i]);
34 |       } else {
35 |         fprintf(stdout, "dlopen() of \"%s\" failed: "
36 |                 "%s\n", argv[i], dlerror());
37 |         return 1;
{% endraw %}

```