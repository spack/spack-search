---
name: "coin3d"
layout: package
next_package: collectd
previous_package: code-server
languages: ['c']
---
## 2.0.0
5 / 1787 files match, 1 filtered matches.

 - [src/glue/dl.c](#srcgluedlc)

### src/glue/dl.c

```c

{% raw %}
169 |   /* FIXME: support HP-UX shn_load()? (dlopen() is missing on older
170 |      HP-UX versions.)
171 | 
172 |      Some versions of HP-UX has dlopen() (from version 11 and
173 |      onwards?). Although according to a discussion on the libtool
174 |      mailinglist it has been buggy in an official release, needing a
175 |      patch to function properly. This is of course a good reason to
176 |      try to use shn_load() *first*, then dlopen() on HP-UX.
177 | 
178 |      Note also that it looks like dlopen() might reside in a library
179 |      "svld" instead of "dl".
180 | 
182 | 
183 | #ifdef HAVE_DL_LIB
184 | 
185 |   h->nativehnd = dlopen(filename, RTLD_LAZY);
186 |   /*
187 |     If dlopen() fails for any reason than not being able to find the
188 |     dynamic link-library given by "filename" on disk, we should really
189 |     detect it and report an error, whether we're running in debug mode
201 |   if (cc_dl_debugging() && (h->nativehnd == NULL)) {
202 |     const char * e = dlerror();
203 |     if (e) {
204 |       cc_debugerror_post("cc_dl_open", "dlopen(\"%s\") failed with: '%s'", filename, e);
205 |     }
206 |   }
209 | 
210 |   /* FIXME: if filename==NULL, could we use Module32First() and
211 |      Module32Next() to cycle through the loaded modules, to "fake"
212 |      what happens on dlopen(NULL) on UNIX-systems?
213 | 
214 |      That would still not work on NT4, which is missing the Tool Help
{% endraw %}

```