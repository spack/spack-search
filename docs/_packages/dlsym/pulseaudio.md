---
name: "pulseaudio"
layout: package
next_package: ipcalc
previous_package: papi
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 13.0
7 / 892 files match, 5 filtered matches.

 - [src/utils/padsp.c](#srcutilspadspc)
 - [src/daemon/dumpmodules.c](#srcdaemondumpmodulesc)
 - [src/daemon/main.c](#srcdaemonmainc)
 - [src/daemon/ltdl-bind-now.c](#srcdaemonltdl-bind-nowc)
 - [src/pulsecore/ltdl-helper.c](#srcpulsecoreltdl-helperc)

### src/utils/padsp.c

```c

{% raw %}
138 | /* dlsym() violates ISO C, so confide the breakage into this function to
139 |  * avoid warnings. */
140 | typedef void (*fnptr)(void);
141 | static inline fnptr dlsym_fn(void *handle, const char *symbol) {
142 |     return (fnptr) (long) dlsym(handle, symbol);
143 | }
144 | 
146 | do { \
147 |     pthread_mutex_lock(&func_mutex); \
148 |     if (!_ioctl)  \
149 |         _ioctl = (int (*)(int, int, void*)) dlsym_fn(RTLD_NEXT, "ioctl"); \
150 |     pthread_mutex_unlock(&func_mutex); \
151 | } while(0)
154 | do { \
155 |     pthread_mutex_lock(&func_mutex); \
156 |     if (!_open) \
157 |         _open = (int (*)(const char *, int, mode_t)) dlsym_fn(RTLD_NEXT, "open"); \
158 |     pthread_mutex_unlock(&func_mutex); \
159 | } while(0)
162 | do { \
163 |     pthread_mutex_lock(&func_mutex); \
164 |     if (!___open_2) \
165 |         ___open_2 = (int (*)(const char *, int)) dlsym_fn(RTLD_NEXT, "__open_2"); \
166 |     pthread_mutex_unlock(&func_mutex); \
167 | } while(0)
170 | do { \
171 |     pthread_mutex_lock(&func_mutex); \
172 |     if (!_open64) \
173 |         _open64 = (int (*)(const char *, int, mode_t)) dlsym_fn(RTLD_NEXT, "open64"); \
174 |     pthread_mutex_unlock(&func_mutex); \
175 | } while(0)
178 | do { \
179 |     pthread_mutex_lock(&func_mutex); \
180 |     if (!___open64_2) \
181 |         ___open64_2 = (int (*)(const char *, int)) dlsym_fn(RTLD_NEXT, "__open64_2"); \
182 |     pthread_mutex_unlock(&func_mutex); \
183 | } while(0)
186 | do { \
187 |     pthread_mutex_lock(&func_mutex); \
188 |     if (!_close) \
189 |         _close = (int (*)(int)) dlsym_fn(RTLD_NEXT, "close"); \
190 |     pthread_mutex_unlock(&func_mutex); \
191 | } while(0)
194 | do { \
195 |     pthread_mutex_lock(&func_mutex); \
196 |     if (!_access) \
197 |         _access = (int (*)(const char*, int)) dlsym_fn(RTLD_NEXT, "access"); \
198 |     pthread_mutex_unlock(&func_mutex); \
199 | } while(0)
202 | do { \
203 |     pthread_mutex_lock(&func_mutex); \
204 |     if (!_stat) \
205 |         _stat = (int (*)(const char *, struct stat *)) dlsym_fn(RTLD_NEXT, "stat"); \
206 |     pthread_mutex_unlock(&func_mutex); \
207 | } while(0)
210 | do { \
211 |     pthread_mutex_lock(&func_mutex); \
212 |     if (!_stat64) \
213 |         _stat64 = (int (*)(const char *, struct stat64 *)) dlsym_fn(RTLD_NEXT, "stat64"); \
214 |     pthread_mutex_unlock(&func_mutex); \
215 | } while(0)
218 | do { \
219 |     pthread_mutex_lock(&func_mutex); \
220 |     if (!___xstat) \
221 |         ___xstat = (int (*)(int, const char *, struct stat *)) dlsym_fn(RTLD_NEXT, "__xstat"); \
222 |     pthread_mutex_unlock(&func_mutex); \
223 | } while(0)
226 | do { \
227 |     pthread_mutex_lock(&func_mutex); \
228 |     if (!___xstat64) \
229 |         ___xstat64 = (int (*)(int, const char *, struct stat64 *)) dlsym_fn(RTLD_NEXT, "__xstat64"); \
230 |     pthread_mutex_unlock(&func_mutex); \
231 | } while(0)
234 | do { \
235 |     pthread_mutex_lock(&func_mutex); \
236 |     if (!_fopen) \
237 |         _fopen = (FILE* (*)(const char *, const char*)) dlsym_fn(RTLD_NEXT, "fopen"); \
238 |     pthread_mutex_unlock(&func_mutex); \
239 | } while(0)
242 | do { \
243 |     pthread_mutex_lock(&func_mutex); \
244 |     if (!_fopen64) \
245 |         _fopen64 = (FILE* (*)(const char *, const char*)) dlsym_fn(RTLD_NEXT, "fopen64"); \
246 |     pthread_mutex_unlock(&func_mutex); \
247 | } while(0)
250 | do { \
251 |     pthread_mutex_lock(&func_mutex); \
252 |     if (!_fclose) \
253 |         _fclose = (int (*)(FILE *)) dlsym_fn(RTLD_NEXT, "fclose"); \
254 |     pthread_mutex_unlock(&func_mutex); \
255 | } while(0)
316 | 
317 |     pthread_mutex_lock(&func_mutex);
318 |     if (!sym_resolved) {
319 |         sym = (int*) dlsym(RTLD_DEFAULT, "__padsp_disabled__");
320 |         sym_resolved = 1;
321 |     }
{% endraw %}

```
### src/daemon/dumpmodules.c

```c

{% raw %}
87 | }
88 | 
89 | static int is_preloaded(const char *name) {
90 |     const lt_dlsymlist *l;
91 | 
92 |     for (l = lt_preloaded_symbols; l->name; l++) {
130 |         for (i = 0; i < argc; i++)
131 |             show_info(argv[i], NULL, long_info);
132 |     } else {
133 |         const lt_dlsymlist *l;
134 | 
135 |         for (l = lt_preloaded_symbols; l->name; l++) {
{% endraw %}

```
### src/daemon/main.c

```c

{% raw %}
100 | #ifdef DISABLE_LIBTOOL_PRELOAD
101 | /* FIXME: work around a libtool bug by making sure we have 2 elements. Bug has
102 |  * been reported: https://debbugs.gnu.org/cgi/bugreport.cgi?bug=29576 */
103 | const lt_dlsymlist lt_preloaded_symbols[] = {
104 |     { "@PROGRAM@", NULL },
105 |     { NULL, NULL }
{% endraw %}

```
### src/daemon/ltdl-bind-now.c

```c

{% raw %}
97 |     pa_assert(m);
98 |     pa_assert(symbol);
99 | 
100 |     if (!(ptr = dlsym(m, symbol))) {
101 |         lt_dlseterror(LT_ERROR_SYMBOL_NOT_FOUND);
102 |         return NULL;
{% endraw %}

```
### src/pulsecore/ltdl-helper.c

```c

{% raw %}
38 |     pa_assert(handle);
39 |     pa_assert(symbol);
40 | 
41 |     f = (pa_void_func_t) lt_dlsym(handle, symbol);
42 | 
43 |     if (f)
55 |         if (!isalnum((unsigned char)*c))
56 |             *c = '_';
57 | 
58 |     f = (pa_void_func_t) lt_dlsym(handle, sn);
59 |     pa_xfree(sn);
60 | 
{% endraw %}

```