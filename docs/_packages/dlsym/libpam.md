---
name: "libpam"
layout: package
next_package: tcl
previous_package: bash
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.07
2 / 32 files match, 2 filtered matches.

 - [src/google-authenticator.c](#srcgoogle-authenticatorc)
 - [tests/pam_google_authenticator_unittest.c](#testspam_google_authenticator_unittestc)

### src/google-authenticator.c

```c

{% raw %}
226 |   } QRcode;
227 |   QRcode *(*QRcode_encodeString8bit)(const char *, int, int) =
228 |       (QRcode *(*)(const char *, int, int))
229 |       dlsym(qrencode, "QRcode_encodeString8bit");
230 |   void (*QRcode_free)(QRcode *qrcode) =
231 |       (void (*)(QRcode *))dlsym(qrencode, "QRcode_free");
232 |   if (!QRcode_encodeString8bit || !QRcode_free) {
233 |     dlclose(qrencode);
{% endraw %}

```
### tests/pam_google_authenticator_unittest.c

```c

{% raw %}
131 | // Return the last line of the error message.
132 | static const char *get_error_msg(void) {
133 |   const char *(*get_error_msg)(void) =
134 |     (const char *(*)(void))dlsym(pam_module, "get_error_msg");
135 |   const char* msg = get_error_msg ? get_error_msg() : "";
136 |   const char* p = strrchr(msg, '\n');
224 |   // Look up public symbols
225 |   int (*pam_sm_authenticate)(pam_handle_t *, int, int, const char **) =
226 |       (int (*)(pam_handle_t *, int, int, const char **))
227 |       dlsym(pam_module, "pam_sm_authenticate");
228 |   assert(pam_sm_authenticate != NULL);
229 | 
230 |   // Look up private test-only API
231 |   void (*set_time)(time_t t) =
232 |       (void (*)(time_t))dlsym(pam_module, "set_time");
233 |   assert(set_time);
234 |   int (*compute_code)(uint8_t *, int, unsigned long) =
235 |       (int (*)(uint8_t*, int, unsigned long))dlsym(pam_module, "compute_code");
236 |   assert(compute_code);
237 | 
{% endraw %}

```