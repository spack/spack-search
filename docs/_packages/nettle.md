---
name: "nettle"
layout: package
next_package: neuron
previous_package: netperf
languages: ['c']
---
## 3.4.1
5 / 637 files match, 2 filtered matches.

 - [fat-setup.h](#fat-setuph)
 - [testsuite/dlopen-test.c](#testsuitedlopen-testc)

### fat-setup.h

```c

{% raw %}
80 |    one can call any libc functions from the ifunc resolver. On x86 and
81 |    x86_64, the corresponding IRELATIVE relocs are supposed to be
82 |    processed last, but that doesn't seem to happen, and its a
83 |    platform-specific feature. To trigger problems, simply try dlopen
84 |    ("libnettle.so", RTLD_NOW), which crashes in an uninitialized plt
85 |    entry. */
{% endraw %}

```
### testsuite/dlopen-test.c

```c

{% raw %}
8 | main (int argc UNUSED, char **argv UNUSED)
9 | {
10 | #if HAVE_LIBDL
11 |   void *handle = dlopen ("../libnettle.so", RTLD_NOW);
12 |   int (*get_version)(void);
13 |   if (!handle)
14 |     {
15 |       fprintf (stderr, "dlopen failed: %s\n", dlerror());
16 |       FAIL ();
17 |     }
{% endraw %}

```