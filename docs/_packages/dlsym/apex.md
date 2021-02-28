---
name: "apex"
layout: package
next_package: jags
previous_package: sqlite
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.1
1 / 266 files match, 1 filtered matches.

 - [src/wrappers/pthread_wrapper.c](#srcwrapperspthread_wrapperc)

### src/wrappers/pthread_wrapper.c

```c

{% raw %}
33 |   RESET_DLERROR();
34 | 
35 |   // Attempt to get the function handle
36 |   handle = dlsym(RTLD_NEXT, name);
37 | 
38 |   // Detect errors
47 |     CHECK_DLERROR();
48 |     do {
49 |       RESET_DLERROR();
50 |       handle = dlsym(syms, name);
51 |       CHECK_DLERROR();
52 |     } while (handle == caller);
{% endraw %}

```