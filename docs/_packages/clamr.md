---
name: "clamr"
layout: package
next_package: clfft
previous_package: clamav
languages: ['c']
---
## master
1 / 1046 files match, 1 filtered matches.

 - [l7/l7_init.c](#l7l7_initc)

### l7/l7_init.c

```c

{% raw %}
119 | 
120 | #ifdef HAVE_LTTRACE
121 |    if (lttrace_on){
122 |       void *handle = dlopen("lttrace.so",RTLD_LAZY);
123 |       if (! handle) {
124 |          printf("DEBUG -- open failed\n");
{% endraw %}

```