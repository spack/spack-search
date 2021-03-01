---
name: "gpgme"
layout: package
next_package: grads
previous_package: gotcha
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.12.0
3 / 630 files match, 1 filtered matches.

 - [src/w32-util.c](#srcw32-utilc)

### src/w32-util.c

```c

{% raw %}
114 | }
115 | 
116 | static GPG_ERR_INLINE void *
117 | dlsym (void * hd, const char * sym)
118 | {
119 |   if (hd && sym)
212 |       handle = dlopen ("user32.dll", RTLD_LAZY);
213 |       if (handle)
214 |         {
215 |           func = dlsym (handle, "AllowSetForegroundWindow");
216 |           if (!func)
217 |             {
{% endraw %}

```