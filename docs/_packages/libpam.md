---
name: "libpam"
layout: package
next_package: cpu-features
previous_package: isl
languages: ['cpp']
---
## 1.07
3 / 32 files match

 - [configure.ac](#configureac)
 - [src/google-authenticator.c](#srcgoogle-authenticatorc)
 - [tests/pam_google_authenticator_unittest.c](#testspam_google_authenticator_unittestc)

### configure.ac

```

{% raw %}
75 | AC_SEARCH_LIBS([dlopen], [dl])
{% endraw %}

```
### src/google-authenticator.c

```cpp

{% raw %}
206 |   void *qrencode = dlopen("libqrencode.so.2", RTLD_NOW | RTLD_LOCAL);
208 |     qrencode = dlopen("libqrencode.so.3", RTLD_NOW | RTLD_LOCAL);
211 |     qrencode = dlopen("libqrencode.so.4", RTLD_NOW | RTLD_LOCAL);
214 |     qrencode = dlopen("libqrencode.3.dylib", RTLD_NOW | RTLD_LOCAL);
217 |     qrencode = dlopen("libqrencode.4.dylib", RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### tests/pam_google_authenticator_unittest.c

```cpp

{% raw %}
216 |   pam_module = dlopen("./.libs/libpam_google_authenticator_testing.so",
219 |     fprintf(stderr, "dlopen(): %s\n", dlerror());
{% endraw %}

```