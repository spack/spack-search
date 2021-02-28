---
name: "gpgme"
layout: package
next_package: memkind
previous_package: sst-macro
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.12.0
5 / 630 files match, 2 filtered matches.

 - [src/w32-util.c](#srcw32-utilc)
 - [src/w32-io.c](#srcw32-ioc)

### src/w32-util.c

```c

{% raw %}
105 | #define RTLD_LAZY 0
106 | 
107 | static GPG_ERR_INLINE void *
108 | dlopen (const char * name, int flag)
109 | {
110 |   void * hd = LoadLibrary (name);
209 |     {
210 |       /* Available since W2000; thus we dynload it.  */
211 |       initialized = 1;
212 |       handle = dlopen ("user32.dll", RTLD_LAZY);
213 |       if (handle)
214 |         {
{% endraw %}

```
### src/w32-io.c

```c

{% raw %}
547 |      out of the recv.  A shutdown does this nicely.  For handles
548 |      (i.e. pipes) it would also be nice to cancel the operation, but
549 |      such a feature is only available since Vista.  Thus we need to
550 |      dlopen that syscall.  */
551 |   if (ctx->file_hd != INVALID_HANDLE_VALUE)
552 |     {
{% endraw %}

```