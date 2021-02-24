---
name: "eztrace"
layout: package
next_package: ipcalc
previous_package: bind9
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.1-10
38 / 1095 files match, 4 filtered matches.

 - [src/core/eztrace.h](#srccoreeztraceh)
 - [src/modules/pthread/pthread.c](#srcmodulespthreadpthreadc)
 - [src/modules/memory/memory.c](#srcmodulesmemorymemoryc)
 - [test/pptrace/perf/tests/libpreload.c](#testpptraceperftestslibpreloadc)

### src/core/eztrace.h

```c

{% raw %}
165 |   do {								\
166 |     if(var) break;						\
167 |     void *__handle = RTLD_NEXT;					\
168 |     var = (typeof(var)) (uintptr_t) dlsym(__handle, func);	\
169 |   } while(0)
170 | 
213 | /* check wether dlsym returned successfully */
214 | #define DYNAMIC_INTERCEPTION(func, varName, var)	\
215 |   do {							\
216 |     var = (void**) dlsym(NULL, varName);		\
217 |     if(NULL == var) {					\
218 |       TREAT_ERROR();					\
{% endraw %}

```
### src/modules/pthread/pthread.c

```c

{% raw %}
61 |    there's only one thread. Thus, we do not to call mutex_lock for
62 |    real.
63 |    If you try to call mutex_lock in that case, you'll get a SIGSEVG
64 |    since dlsym was not called yet for mutex_lock
65 |    */
66 |   if (__pthread_initialized) {
{% endraw %}

```
### src/modules/memory/memory.c

```c

{% raw %}
154 |      * If dlsym calls malloc, memory will be allocated 'by hand'
155 |      */
156 |     malloc_protect_on = 1;
157 |     libmalloc = dlsym(RTLD_NEXT, "malloc");
158 |     char* error;
159 |     if ((error = dlerror()) != NULL) {
202 |   FUNCTION_ENTRY;
203 | 
204 |   if (!librealloc) {
205 |     librealloc = dlsym(RTLD_NEXT, "realloc");
206 |     char* error;
207 |     if ((error = dlerror()) != NULL) {
286 | void free(void* ptr) {
287 | 
288 |   if (!libfree) {
289 |     libfree = dlsym(RTLD_NEXT, "free");
290 |     char* error;
291 |     if ((error = dlerror()) != NULL) {
{% endraw %}

```
### test/pptrace/perf/tests/libpreload.c

```c

{% raw %}
34 | void __hijack_init(void) {
35 |   void* handle = dlopen("libalacon.so", RTLD_NOW);
36 |   if (handle) {
37 |     orig_foo = dlsym(handle, "foo");
38 |     orig_bar = dlsym(handle, "bar");
39 |   }
40 | }
{% endraw %}

```