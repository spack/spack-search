---
name: "libpam"
layout: package
next_package: libquo
previous_package: libmonitor
languages: ['c']
---
## 1.07
3 / 32 files match, 2 filtered matches.

 - [src/google-authenticator.c](#srcgoogle-authenticatorc)
 - [tests/pam_google_authenticator_unittest.c](#testspam_google_authenticator_unittestc)

### src/google-authenticator.c

```c

{% raw %}
206 |   void *qrencode = dlopen("libqrencode.so.2", RTLD_NOW | RTLD_LOCAL);
208 |     qrencode = dlopen("libqrencode.so.3", RTLD_NOW | RTLD_LOCAL);
211 |     qrencode = dlopen("libqrencode.so.4", RTLD_NOW | RTLD_LOCAL);
214 |     qrencode = dlopen("libqrencode.3.dylib", RTLD_NOW | RTLD_LOCAL);
217 |     qrencode = dlopen("libqrencode.4.dylib", RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### tests/pam_google_authenticator_unittest.c

```c

{% raw %}
216 |   pam_module = dlopen("./.libs/libpam_google_authenticator_testing.so",
219 |     fprintf(stderr, "dlopen(): %s\n", dlerror());
{% endraw %}

```