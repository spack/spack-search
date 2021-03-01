---
name: "bmi"
layout: package
next_package: boost
previous_package: bird
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## develop
2 / 232 files match, 2 filtered matches.

 - [src/io/bmi/bmi.c](#srciobmibmic)
 - [src/io/bmi/bmi_ib/vapi.c](#srciobmibmi_ibvapic)

### src/io/bmi/bmi.c

```c

{% raw %}
425 |     /* iterate through each method in the list and load its module */
426 |     for (i = 0; i < active_method_count; i++)
427 |     {
428 | 	meth_mod = dlopen(modules[i], RTLD_NOW);
429 | 	if (!meth_mod)
430 | 	{
{% endraw %}

```
### src/io/bmi/bmi_ib/vapi.c

```c

{% raw %}
795 |     int (*mosal_ioctl_open)(void);
796 |     int (*mosal_ioctl_close)(void);
797 | 
798 |     dlh = dlopen("libmosal.so", RTLD_LAZY);
799 |     if (!dlh)
800 | 	error("%s: cannot open libmosal shared library", __func__);
{% endraw %}

```