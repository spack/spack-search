---
name: "gnutls"
layout: package
next_package: go
previous_package: gnupg
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.6.7.1
8 / 4928 files match, 6 filtered matches.

 - [lib/tpm.c](#libtpmc)
 - [lib/fips.c](#libfipsc)
 - [tests/pkcs11/pkcs11-privkey-safenet-always-auth.c](#testspkcs11pkcs11-privkey-safenet-always-authc)
 - [tests/pkcs11/pkcs11-privkey-always-auth.c](#testspkcs11pkcs11-privkey-always-authc)
 - [tests/pkcs11/pkcs11-import-url-privkey.c](#testspkcs11pkcs11-import-url-privkeyc)
 - [fuzz/gnutls_set_trust_file_fuzzer.c](#fuzzgnutls_set_trust_file_fuzzerc)

### lib/tpm.c

```c

{% raw %}
110 | static void *tpm_dl = NULL;
111 | 
112 | #define _DLSYM(dl, sym) \
113 | 	p##sym = dlsym(dl, #sym); \
114 | 	if (p##sym == NULL) { \
115 | 		dlclose(dl); \
{% endraw %}

```
### lib/fips.c

```c

{% raw %}
153 | 	if (dl == NULL)
154 | 		return gnutls_assert_val(GNUTLS_E_FILE_ERROR);
155 | 
156 | 	sym = dlsym(dl, symbol);
157 | 	if (sym == NULL) {
158 | 		ret = gnutls_assert_val(GNUTLS_E_FILE_ERROR);
{% endraw %}

```
### tests/pkcs11/pkcs11-privkey-safenet-always-auth.c

```c

{% raw %}
97 | 			exit(1);
98 | 		}
99 | 
100 | 		pflags = dlsym(dl, "pkcs11_mock_flags");
101 | 		if (pflags == NULL) {
102 | 			fail("could find pkcs11_mock_flags\n");
{% endraw %}

```
### tests/pkcs11/pkcs11-privkey-always-auth.c

```c

{% raw %}
98 | 			exit(1);
99 | 		}
100 | 
101 | 		pflags = dlsym(dl, "pkcs11_mock_flags");
102 | 		if (pflags == NULL) {
103 | 			fail("could find pkcs11_mock_flags\n");
{% endraw %}

```
### tests/pkcs11/pkcs11-import-url-privkey.c

```c

{% raw %}
103 | 			exit(1);
104 | 		}
105 | 
106 | 		pflags = dlsym(dl, "pkcs11_mock_flags");
107 | 		if (pflags == NULL) {
108 | 			fail("could find pkcs11_mock_flags\n");
{% endraw %}

```
### fuzz/gnutls_set_trust_file_fuzzer.c

```c

{% raw %}
32 | FILE *fopen(const char *pathname, const char *mode)
33 | {
34 | 	FILE *(*libc_fopen)(const char *, const char *) =
35 | 		(FILE *(*)(const char *, const char *)) dlsym (RTLD_NEXT, "fopen");
36 | 
37 | 	if (!strcmp(pathname, "ca_or_crl"))
{% endraw %}

```