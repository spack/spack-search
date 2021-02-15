---
name: "nbdkit"
layout: package
next_package: cups
previous_package: embree
languages: ['cpp']
---
## 1.23.7
8 / 763 files match

 - [server/internal.h](#serverinternalh)
 - [server/main.c](#servermainc)
 - [plugins/vddk/reexec.c](#pluginsvddkreexecc)
 - [plugins/vddk/README.VDDK](#pluginsvddkreadmevddk)
 - [plugins/vddk/vddk.c](#pluginsvddkvddkc)
 - [plugins/cc/cc.c](#pluginsccccc)
 - [valgrind/glibc.suppressions](#valgrindglibcsuppressions)
 - [docs/nbdkit-plugin.pod](#docsnbdkit-pluginpod)

### server/internal.h

```cpp

{% raw %}
72 | /* XXX This causes dlopen in the server to leak during fuzzing.
372 |   /* The dlopen handle for the backend. */
{% endraw %}

```
### server/main.c

```cpp

{% raw %}
808 |   dl = dlopen (filename, RTLD_NOW|RTLD_GLOBAL);
819 |   /* Initialize the plugin.  See dlopen(3) to understand C weirdness. */
861 |   dl = dlopen (filename, RTLD_NOW|RTLD_GLOBAL);
868 |   /* Initialize the filter.  See dlopen(3) to understand C weirdness. */
{% endraw %}

```
### plugins/vddk/reexec.c

```cpp

{% raw %}
230 |  * as the value of "reexeced_".  dlopen uses the value of
{% endraw %}

```
### plugins/vddk/README.VDDK

```

{% raw %}
15 | uses dlopen to load the library from a directory determined by the
{% endraw %}

```
### plugins/vddk/vddk.c

```cpp

{% raw %}
76 | static void *dl;                           /* dlopen handle */
313 |     /* Set the full path so that dlopen will preferentially load the
321 |     dl = dlopen (path, RTLD_NOW);
423 |  * already checked in .get_ready that the library is dlopenable.
{% endraw %}

```
### plugins/cc/cc.c

```cpp

{% raw %}
234 |   dl = dlopen (tmpfile, RTLD_NOW);
{% endraw %}

```
### valgrind/glibc.suppressions

```

{% raw %}
40 | # Suppress leaks from dlopen.  When running under valgrind we
42 | # print symbols.  So it's expected that dlopen will leak.
{% endraw %}

```
### docs/nbdkit-plugin.pod

```

{% raw %}
1742 | be resolved by the server binary when nbdkit dlopens the plugin.
{% endraw %}

```