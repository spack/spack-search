---
name: "ruby"
layout: package
next_package: samtools
previous_package: rsyslog
languages: ['c']
---
## 2.7.1
25 / 9819 files match, 4 filtered matches.

 - [addr2line.c](#addr2linec)
 - [mjit_worker.c](#mjit_workerc)
 - [dln.c](#dlnc)
 - [ext/fiddle/handle.c](#extfiddlehandlec)

### addr2line.c

```c

{% raw %}
1733 |             void *handle = dlopen(NULL, RTLD_NOW|RTLD_LOCAL);
{% endraw %}

```
### mjit_worker.c

```c

{% raw %}
876 |         void *handle = dlopen(so_file, RTLD_NOW);
923 |     handle = dlopen(so_file, RTLD_NOW);
{% endraw %}

```
### dln.c

```c

{% raw %}
1340 | 	if ((handle = (void*)dlopen(file, RTLD_LAZY|RTLD_GLOBAL)) == NULL) {
{% endraw %}

```
### ext/fiddle/handle.c

```c

{% raw %}
168 | 	ptr = dlopen("coredll.dll", cflag);
176 | 	ptr = dlopen(clib, cflag);
{% endraw %}

```