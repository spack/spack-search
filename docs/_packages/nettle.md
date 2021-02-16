---
name: "nettle"
layout: package
next_package: magics
previous_package: lcms
languages: ['c']
---
## 3.4.1
5 / 637 files match

 - [fat-setup.h](#fat-setuph)
 - [testsuite/dlopen-test.c](#testsuitedlopen-testc)

### fat-setup.h

```c

{% raw %}
83 |    platform-specific feature. To trigger problems, simply try dlopen
{% endraw %}

```
### testsuite/dlopen-test.c

```c

{% raw %}
11 |   void *handle = dlopen ("../libnettle.so", RTLD_NOW);
15 |       fprintf (stderr, "dlopen failed: %s\n", dlerror());
{% endraw %}

```