---
name: "gnutls"
layout: package
next_package: procps
previous_package: fipscheck
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.6.7.1
12 / 4928 files match, 5 filtered matches.

 - [lib/tpm.c](#libtpmc)
 - [lib/fips.c](#libfipsc)
 - [tests/pkcs11/pkcs11-privkey-safenet-always-auth.c](#testspkcs11pkcs11-privkey-safenet-always-authc)
 - [tests/pkcs11/pkcs11-privkey-always-auth.c](#testspkcs11pkcs11-privkey-always-authc)
 - [tests/pkcs11/pkcs11-import-url-privkey.c](#testspkcs11pkcs11-import-url-privkeyc)

### lib/tpm.c

```c

{% raw %}
120 | static int check_init(void)
121 | {
122 | 	if (tpm_dl == NULL) {
123 | 		tpm_dl = dlopen(TROUSERS_LIB, RTLD_LAZY);
124 | 		if (tpm_dl == NULL) {
125 | 			_gnutls_debug_log("couldn't open %s\n", TROUSERS_LIB);
{% endraw %}

```
### lib/fips.c

```c

{% raw %}
149 | int ret;
150 | void *dl, *sym;
151 | 
152 | 	dl = dlopen(lib, RTLD_LAZY);
153 | 	if (dl == NULL)
154 | 		return gnutls_assert_val(GNUTLS_E_FILE_ERROR);
{% endraw %}

```
### tests/pkcs11/pkcs11-privkey-safenet-always-auth.c

```c

{% raw %}
91 | 		void *dl;
92 | 		unsigned int *pflags;
93 | 
94 | 		dl = dlopen(lib, RTLD_NOW);
95 | 		if (dl == NULL) {
96 | 			fail("could not dlopen %s\n", lib);
97 | 			exit(1);
98 | 		}
{% endraw %}

```
### tests/pkcs11/pkcs11-privkey-always-auth.c

```c

{% raw %}
92 | 		void *dl;
93 | 		unsigned int *pflags;
94 | 
95 | 		dl = dlopen(lib, RTLD_NOW);
96 | 		if (dl == NULL) {
97 | 			fail("could not dlopen %s\n", lib);
98 | 			exit(1);
99 | 		}
{% endraw %}

```
### tests/pkcs11/pkcs11-import-url-privkey.c

```c

{% raw %}
97 | 		void *dl;
98 | 		unsigned int *pflags;
99 | 
100 | 		dl = dlopen(lib, RTLD_NOW);
101 | 		if (dl == NULL) {
102 | 			fail("could not dlopen %s\n", lib);
103 | 			exit(1);
104 | 		}
{% endraw %}

```