---
name: "apex"
layout: package
next_package: json-c
previous_package: petsc
languages: ['c']
---
## 0.1
1 / 266 files match, 1 filtered matches.

 - [src/wrappers/pthread_wrapper.c](#srcwrapperspthread_wrapperc)

### src/wrappers/pthread_wrapper.c

```c

{% raw %}
46 |     void * syms = dlopen(NULL, RTLD_NOW);
{% endraw %}

```