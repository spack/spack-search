---
name: "gnutls"
layout: package
next_package: hip-rocclr
previous_package: libxscrnsaver
languages: ['c']
---
## 3.6.7.1
12 / 4928 files match

 - [lib/tpm.c](#libtpmc)
 - [lib/fips.c](#libfipsc)
 - [tests/pkcs11/pkcs11-privkey-safenet-always-auth.c](#testspkcs11pkcs11-privkey-safenet-always-authc)
 - [tests/pkcs11/pkcs11-privkey-always-auth.c](#testspkcs11pkcs11-privkey-always-authc)
 - [tests/pkcs11/pkcs11-import-url-privkey.c](#testspkcs11pkcs11-import-url-privkeyc)

### lib/tpm.c

```c

{% raw %}
123 | 		tpm_dl = dlopen(TROUSERS_LIB, RTLD_LAZY);
{% endraw %}

```
### lib/fips.c

```c

{% raw %}
152 | 	dl = dlopen(lib, RTLD_LAZY);
{% endraw %}

```
### tests/pkcs11/pkcs11-privkey-safenet-always-auth.c

```c

{% raw %}
94 | 		dl = dlopen(lib, RTLD_NOW);
96 | 			fail("could not dlopen %s\n", lib);
{% endraw %}

```
### tests/pkcs11/pkcs11-privkey-always-auth.c

```c

{% raw %}
95 | 		dl = dlopen(lib, RTLD_NOW);
97 | 			fail("could not dlopen %s\n", lib);
{% endraw %}

```
### tests/pkcs11/pkcs11-import-url-privkey.c

```c

{% raw %}
100 | 		dl = dlopen(lib, RTLD_NOW);
102 | 			fail("could not dlopen %s\n", lib);
{% endraw %}

```