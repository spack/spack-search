---
name: "libnl"
layout: package
next_package: libpam
previous_package: libmicrohttpd
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.3.0
4 / 448 files match, 1 filtered matches.

 - [src/lib/utils.c](#srclibutilsc)

### src/lib/utils.c

```c

{% raw %}
224 | 	snprintf(path, sizeof(path), "%s/%s/%s.so",
225 | 		 PKGLIBDIR, prefix, name);
226 | 
227 | 	if (!(handle = dlopen(path, RTLD_NOW)))
228 | 		nl_cli_fatal(ENOENT, "Unable to load module \"%s\": %s\n",
229 | 			path, dlerror());
{% endraw %}

```