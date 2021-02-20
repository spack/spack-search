---
name: "apr"
layout: package
next_package: arrayfire
previous_package: apex
languages: ['c']
---
## 1.7.0
8 / 467 files match, 4 filtered matches.

 - [include/arch/aix/apr_arch_dso.h](#includearchaixapr_arch_dsoh)
 - [dso/unix/dso.c](#dsounixdsoc)
 - [dso/aix/dso.c](#dsoaixdsoc)
 - [dso/netware/dso.c](#dsonetwaredsoc)

### include/arch/aix/apr_arch_dso.h

```c

{% raw %}
24 | 
25 | #if APR_HAS_DSO
26 | 
27 | void *dlopen(const char *path, int mode);
28 | void *dlsym(void *handle, const char *symbol);
29 | const char *dlerror(void);
{% endraw %}

```
### dso/unix/dso.c

```c

{% raw %}
119 | #if defined(OSF1) || defined(SEQUENT) || defined(SNI) ||\
120 |     (defined(__FreeBSD_version) && (__FreeBSD_version >= 220000)) ||\
121 |     defined(__DragonFly__)
122 |     void *os_handle = dlopen((char *)path, RTLD_NOW | RTLD_GLOBAL);
123 | 
124 | #else
135 |         flags |= RTLD_MEMBER;
136 |     }
137 | #endif
138 |     os_handle = dlopen(path, flags);
139 | #endif    
140 | #endif /* DSO_USE_x */
{% endraw %}

```
### dso/aix/dso.c

```c

{% raw %}
127 | APR_DECLARE(apr_status_t) apr_dso_load(apr_dso_handle_t **res_handle, 
128 |                                        const char *path, apr_pool_t *ctx)
129 | {
130 |     void *os_handle = dlopen((char *)path, RTLD_NOW | RTLD_GLOBAL);
131 | 
132 |     *res_handle = apr_pcalloc(ctx, sizeof(*res_handle));
238 | static void terminate(void);
239 | static void *findMain(void);
240 | 
241 | void *dlopen(const char *path, int mode)
242 | {
243 |     register ModulePtr mp;
282 | 	free(mp->name);
283 | 	free(mp);
284 | 	errvalid++;
285 | 	strcpy(errbuf, "dlopen: ");
286 | 	strcat(errbuf, path);
287 | 	strcat(errbuf, ": ");
{% endraw %}

```
### dso/netware/dso.c

```c

{% raw %}
77 |         return rv;
78 |     }
79 | 
80 |     os_handle = dlopen(fullpath, RTLD_NOW | RTLD_LOCAL);
81 | 
82 |     *res_handle = apr_pcalloc(pool, sizeof(**res_handle));
{% endraw %}

```