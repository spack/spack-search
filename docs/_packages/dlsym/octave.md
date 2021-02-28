---
name: "octave"
layout: package
next_package: grads
previous_package: brltty
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp', 'c']
---
## 4.0.0
12 / 6223 files match, 2 filtered matches.

 - [liboctave/util/oct-shlib.cc](#liboctaveutiloct-shlibcc)
 - [liboctave/cruft/misc/blaswrap.c](#liboctavecruftmiscblaswrapc)

### liboctave/util/oct-shlib.cc

```cpp

{% raw %}
43 | #else
44 | extern void *dlopen (const char *, int);
45 | extern const char *dlerror (void);
46 | extern void *dlsym (void *, const char *);
47 | extern int dlclose (void *);
48 | #endif
228 |       if (mangler)
229 |         sym_name = mangler (name);
230 | 
231 |       function = dlsym (library, sym_name.c_str ());
232 |     }
233 |   else
{% endraw %}

```
### liboctave/cruft/misc/blaswrap.c

```c

{% raw %}
276 | 
277 |   int i;
278 |   for (i = 0; i < f2c_LAPACK_COUNT; i++)
279 |     if (0 == (f2c_lapack_func[i] = dlsym (apple_vecLib, f2c_lapack_name(i))))
280 |       abort ();
281 |   for (i = 0; i < f2c_BLAS_COUNT; i++)
282 |     if (0 == (f2c_blas_func[i] = dlsym (apple_vecLib, f2c_blas_name(i))))
283 |       abort ();
284 | }
{% endraw %}

```