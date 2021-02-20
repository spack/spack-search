---
name: "bison"
layout: package
next_package: blast-legacy
previous_package: binutils
languages: ['c']
---
## 3.7.4
2 / 1140 files match, 1 filtered matches.

 - [lib/thread-optim.h](#libthread-optimh)

### lib/thread-optim.h

```c

{% raw %}
41 | 
42 |    The code between the gl_multithreaded () invocation and any use of the
43 |    variable 'mt' must not create threads or invoke functions that may
44 |    indirectly create threads (e.g. 'dlopen' may, indirectly through C++
45 |    initializers of global variables in the shared library being opened,
46 |    create threads).
{% endraw %}

```