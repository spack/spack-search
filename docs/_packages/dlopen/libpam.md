---
name: "libpam"
layout: package
next_package: libpng
previous_package: libnl
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.07
3 / 32 files match, 2 filtered matches.

 - [src/google-authenticator.c](#srcgoogle-authenticatorc)
 - [tests/pam_google_authenticator_unittest.c](#testspam_google_authenticator_unittestc)

### src/google-authenticator.c

```c

{% raw %}
203 | 
204 | // Display QR code visually. If not possible, return 0.
205 | static int displayQRCode(const char* url) {
206 |   void *qrencode = dlopen("libqrencode.so.2", RTLD_NOW | RTLD_LOCAL);
207 |   if (!qrencode) {
208 |     qrencode = dlopen("libqrencode.so.3", RTLD_NOW | RTLD_LOCAL);
209 |   }
210 |   if (!qrencode) {
211 |     qrencode = dlopen("libqrencode.so.4", RTLD_NOW | RTLD_LOCAL);
212 |   }
213 |   if (!qrencode) {
214 |     qrencode = dlopen("libqrencode.3.dylib", RTLD_NOW | RTLD_LOCAL);
215 |   }
216 |   if (!qrencode) {
217 |     qrencode = dlopen("libqrencode.4.dylib", RTLD_NOW | RTLD_LOCAL);
218 |   }
219 |   if (!qrencode) {
{% endraw %}

```
### tests/pam_google_authenticator_unittest.c

```c

{% raw %}
213 | 
214 |   // Load the PAM module
215 |   puts("Loading PAM module");
216 |   pam_module = dlopen("./.libs/libpam_google_authenticator_testing.so",
217 |                       RTLD_NOW | RTLD_GLOBAL);
218 |   if (pam_module == NULL) {
219 |     fprintf(stderr, "dlopen(): %s\n", dlerror());
220 |     exit(1);
221 |   }
{% endraw %}

```