---
name: "bmi"
layout: package
next_package: iproute2
previous_package: binutils
library_name: dlsym
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
435 | 	dlerror();
436 | 
437 | 	active_method_table[i] = (struct bmi_method_ops *)
438 |             dlsym(meth_mod, "method_interface");
439 | 	mod_error = dlerror();
440 | 	if (mod_error)
{% endraw %}

```
### src/io/bmi/bmi_ib/vapi.c

```c

{% raw %}
814 |     call_result_t (*_dev_mosal_init_lib)(t_lib_descriptor **pp_t_lib);
815 |     const char *errmsg;
816 | 
817 |     _dev_mosal_init_lib = dlsym(dlh, "_dev_mosal_init_lib");
818 |     errmsg = dlerror();
819 |     if (errmsg == NULL) {
838 |      * any way to "trick" the library as above, but there's no need for
839 |      * the hack now that they export a "finalize" function to undo the init.
840 |      */
841 |     mosal_ioctl_open = dlsym(dlh, "mosal_ioctl_open");
842 |     if (dlerror())
843 | 	error("%s: mosal_ioctl_open not found in libmosal", __func__);
844 |     mosal_ioctl_close = dlsym(dlh, "mosal_ioctl_close");
845 |     if (dlerror())
846 | 	error("%s: mosal_ioctl_close not found in libmosal", __func__);
{% endraw %}

```