---
name: "openssl"
layout: package
next_package: qemu
previous_package: libeatmydata
languages: ['cpp']
---
## 1.1.1i
5 / 3040 files match

 - [crypto/rand/rand_vms.c](#cryptorandrand_vmsc)
 - [crypto/dso/dso_dlfcn.c](#cryptodsodso_dlfcnc)
 - [crypto/dso/dso_local.h](#cryptodsodso_localh)
 - [test/shlibloadtest.c](#testshlibloadtestc)
 - [doc/man3/OPENSSL_init_crypto.pod](#docman3openssl_init_cryptopod)

### crypto/rand/rand_vms.c

```cpp

{% raw %}
524 |         get_entropy_address = dlsym(dlopen(PUBLIC_VECTORS, 0), GET_ENTROPY);
{% endraw %}

```
### crypto/dso/dso_dlfcn.c

```cpp

{% raw %}
69 |  * Prior to using the dlopen() function, we should decide on the flag we
78 | #   define DLOPEN_FLAG DL_LAZY
81 | #    define DLOPEN_FLAG RTLD_NOW
83 | #    define DLOPEN_FLAG 0
87 | #  define DLOPEN_FLAG RTLD_NOW  /* Hope this works everywhere else */
92 |  * (void*) returned from dlopen().
100 |     int flags = DLOPEN_FLAG;
115 |     ptr = dlopen(filename, flags);
122 |      * Some dlopen() implementations (e.g. solaris) do no preserve errno, even
385 |                      * sys/ldr.h, loadquery() and dlopen()/RTLD_MEMBER.
446 |     void *ret = NULL, *handle = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### crypto/dso/dso_local.h

```cpp

{% raw %}
21 |      * Standard dlopen uses a (void *). Win32 uses a HANDLE. VMS doesn't use
{% endraw %}

```
### test/shlibloadtest.c

```cpp

{% raw %}
58 |     *lib = dlopen(filename, dl_flags);
{% endraw %}

```
### doc/man3/OPENSSL_init_crypto.pod

```

{% raw %}
242 | On Linux/Unix where OpenSSL has been loaded via dlopen() and the application is
246 | each thread prior to the dlclose() call, or alternatively the original dlopen()
{% endraw %}

```