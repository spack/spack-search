---
name: "vampirtrace"
layout: package
next_package: varnish-cache
previous_package: valgrind
languages: ['c']
---
## 5.14.4
10 / 650 files match, 4 filtered matches.

 - [vtlib/vt_mallocwrap.c](#vtlibvt_mallocwrapc)
 - [vtlib/vt_libwrap.c](#vtlibvt_libwrapc)
 - [vtlib/vt_iowrap.c](#vtlibvt_iowrapc)
 - [vtlib/vt_plugin_cntr.c](#vtlibvt_plugin_cntrc)

### vtlib/vt_mallocwrap.c

```c

{% raw %}
89 |   "LIBC-MALLOC", /* func_group */
90 | 
91 |   /* Do not search the actual function pointers in an external LIBC, because
92 |      dlopen calls malloc which would result in an infinite recursion when
93 |      determining the actual function pointer of malloc. Using RTLD_NEXT
94 |      instead. */
{% endraw %}

```
### vtlib/vt_libwrap.c

```c

{% raw %}
156 | #endif /* VT_MT || VT_HYB || VT_JAVA */
157 | 
158 |     (void)dlerror();
159 |     libc_handle = dlopen(SHLIBC_PATHNAME,
160 |                          RTLD_LAZY | RTLD_LOCAL
161 | #ifdef _AIX
170 | #ifdef VT_IOWRAP
171 |       /* do not use vt_error_msg() here to prevent possible recursive calls to
172 |          this function */
173 |       printf("VampirTrace: FATAL: dlopen(\""SHLIBC_PATHNAME"\") failed: %s\n",
174 |              dlerror());
175 |       exit(EXIT_FAILURE);
176 | #else /* VT_IOWRAP */
177 |       vt_error_msg("dlopen(\""SHLIBC_PATHNAME"\") failed: %s\n", dlerror());
178 | #endif /* VT_IOWRAP */
179 |     }
259 |       for( i = 0; i < (*lw)->attr->shlibs_num; i++ )
260 |       {
261 |         (void)dlerror();
262 |         (*lw)->handlev[i] = dlopen((*lw)->attr->shlibs[i],
263 |                                    RTLD_LAZY | RTLD_LOCAL
264 | #ifdef _AIX
269 |         {
270 |           error = 1;
271 |           snprintf(error_msg, sizeof(error_msg) - 1,
272 |                    "dlopen(\"%s\") failed: %s",
273 |                    (*lw)->attr->shlibs[i], dlerror());
274 |           break;
{% endraw %}

```
### vtlib/vt_iowrap.c

```c

{% raw %}
117 | 
118 |     if( iolib_pathname != NULL ) {
119 |       (void)dlerror();
120 |       iolib_handle = dlopen( iolib_pathname,
121 |                              RTLD_LAZY | RTLD_LOCAL
122 | #ifdef _AIX
124 | #endif /* _AIX */
125 |                            );
126 |       if( !iolib_handle ) {
127 |         printf("VampirTrace: FATAL: dlopen(\"%s\") error: %s\n", iolib_pathname, dlerror());
128 |         exit(EXIT_FAILURE);
129 |       }
{% endraw %}

```
### vtlib/vt_plugin_cntr.c

```c

{% raw %}
210 |     sprintf(buffer, "lib%s.so", current_plugin);
211 | 
212 |     /* now dlopen it */
213 |     handle = dlopen(buffer, RTLD_NOW);
214 | 
215 |     /* if it is not valid */
{% endraw %}

```