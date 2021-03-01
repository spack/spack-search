---
name: "nettle"
layout: package
next_package: neuron
previous_package: netdata
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.4.1
1 / 637 files match, 1 filtered matches.

 - [testsuite/dlopen-test.c](#testsuitedlopen-testc)

### testsuite/dlopen-test.c

```c

{% raw %}
16 |       FAIL ();
17 |     }
18 | 
19 |   get_version = (int(*)(void)) dlsym (handle, "nettle_version_minor");
20 |   if (!get_version)
21 |     {
22 |       fprintf (stderr, "dlsym failed: %s\n", dlerror());
23 |       FAIL ();
24 |     }
{% endraw %}

```