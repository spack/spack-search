---
name: "rr"
layout: package
next_package: rsync
previous_package: rose
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp', 'c']
---
## 4.5.0
3 / 939 files match, 3 filtered matches.

 - [src/ThreadDb.cc](#srcthreaddbcc)
 - [src/preload/preload.c](#srcpreloadpreloadc)
 - [src/test/exit_with_syscallbuf_signal.c](#srctestexit_with_syscallbuf_signalc)

### src/ThreadDb.cc

```cpp

{% raw %}
222 | 
223 | #define FIND_FUNCTION(Name)                                                    \
224 |   do {                                                                         \
225 |     Name##_fn = (decltype(Name)*)(dlsym(thread_db_library, #Name));            \
226 |     if (!Name##_fn) {                                                          \
227 |       LOG(debug) << "load_library failed to find " << #Name;                   \
{% endraw %}

```
### src/preload/preload.c

```c

{% raw %}
629 |       (uintptr_t)_syscall_hook_trampoline_89_c1_31_d2 }
630 |   };
631 | 
632 |   real_pthread_create = dlsym(RTLD_NEXT, "pthread_create");
633 | #else
634 | #error Unknown architecture
736 |    * indirect call.
737 |    */
738 |   if (!real_pthread_mutex_timedlock) {
739 |     real_pthread_mutex_timedlock = dlsym(RTLD_NEXT, "pthread_mutex_timedlock");
740 |   }
741 |   return real_pthread_mutex_timedlock(mutex, abstime);
2662 | 
2663 | static void random_device_init_helper(void* this) {
2664 |   void** file_ptr = (void**)this;
2665 |   void* f_ptr = dlsym(RTLD_DEFAULT, "fopen");
2666 |   fopen_ptr fopen = (fopen_ptr)f_ptr;
2667 |   *file_ptr = fopen("/dev/urandom", "rb");
{% endraw %}

```
### src/test/exit_with_syscallbuf_signal.c

```c

{% raw %}
17 | int main(void) {
18 |   pthread_t thread;
19 | 
20 |   very_slow_exit_syscall = dlsym(RTLD_DEFAULT, "very_slow_exit_syscall");
21 |   if (!very_slow_exit_syscall) {
22 |     atomic_puts("syscallbuf not loaded");
{% endraw %}

```