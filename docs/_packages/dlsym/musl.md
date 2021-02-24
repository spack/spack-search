---
name: "musl"
layout: package
next_package: pmix
previous_package: rr
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.1.20
19 / 2392 files match, 4 filtered matches.

 - [src/ldso/dlsym.c](#srcldsodlsymc)
 - [src/ldso/__dlsym.c](#srcldso__dlsymc)
 - [include/dlfcn.h](#includedlfcnh)
 - [ldso/dynlink.c](#ldsodynlinkc)

### src/ldso/dlsym.c

```c

{% raw %}
1 | 
2 | void *__dlsym(void *restrict, const char *restrict, void *restrict);
3 | 
4 | void *dlsym(void *restrict p, const char *restrict s)
5 | {
6 | 	return __dlsym(p, s, 0);
7 | }
8 | 
{% endraw %}

```
### src/ldso/__dlsym.c

```c

{% raw %}
3 | __attribute__((__visibility__("hidden")))
4 | void __dl_seterr(const char *, ...);
5 | 
6 | static void *stub_dlsym(void *restrict p, const char *restrict s, void *restrict ra)
7 | {
8 | 	__dl_seterr("Symbol not found: %s", s);
9 | 	return 0;
10 | }
11 | 
12 | weak_alias(stub_dlsym, __dlsym);
13 | 
{% endraw %}

```
### include/dlfcn.h

```c

{% raw %}
21 | int    dlclose(void *);
22 | char  *dlerror(void);
23 | void  *dlopen(const char *, int);
24 | void  *dlsym(void *__restrict, const char *__restrict);
25 | 
26 | #if defined(_GNU_SOURCE) || defined(_BSD_SOURCE)
{% endraw %}

```
### ldso/dynlink.c

```c

{% raw %}
1903 | 
1904 | void *__tls_get_addr(tls_mod_off_t *);
1905 | 
1906 | static void *do_dlsym(struct dso *p, const char *s, void *ra)
1907 | {
1908 | 	size_t i;
2027 | }
2028 | 
2029 | __attribute__((__visibility__("hidden")))
2030 | void *__dlsym(void *restrict p, const char *restrict s, void *restrict ra)
2031 | {
2032 | 	void *res;
2033 | 	pthread_rwlock_rdlock(&lock);
2034 | 	res = do_dlsym(p, s, ra);
2035 | 	pthread_rwlock_unlock(&lock);
2036 | 	return res;
{% endraw %}

```