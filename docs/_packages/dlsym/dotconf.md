---
name: "dotconf"
layout: package
next_package: dpdk
previous_package: dmtcp
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.3
2 / 42 files match, 2 filtered matches.

 - [examples/duplicates/duplicate.c](#examplesduplicatesduplicatec)
 - [examples/modules/module.c](#examplesmodulesmodulec)

### examples/duplicates/duplicate.c

```c

{% raw %}
234 | 		return "Out of handle space. Not loading module\n";
235 | 	}
236 | 	// get the options
237 | 	module_options = dlsym(shared_object, "options");
238 | 	error = dlerror();
239 | 	if (error) {
{% endraw %}

```
### examples/modules/module.c

```c

{% raw %}
109 | 		if (!handles[i])
110 | 			printf("Error opening library: %s\n", dlerror());
111 | 		dotconf_register_options(cmd->configfile,
112 | 					 dlsym(handles[i], "new_options"));
113 | 	}
114 | 	printf("Module %s successfully loaded\n", cmd->data.str);
{% endraw %}

```