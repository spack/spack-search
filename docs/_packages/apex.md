---
name: "apex"
layout: package
next_package: json-c
previous_package: petsc
languages: ['cpp']
---
## 0.1
1 / 266 files match

 - [src/wrappers/pthread_wrapper.c](#srcwrapperspthread_wrapperc)

### src/wrappers/pthread_wrapper.c

```cpp

{% raw %}
46 |     void * syms = dlopen(NULL, RTLD_NOW);
{% endraw %}

```