---
name: "xedit"
layout: package
next_package: xhmm
previous_package: xdm
languages: ['c']
---
## 1.2.2
1 / 114 files match, 1 filtered matches.

 - [lisp/require.c](#lisprequirec)

### lisp/require.c

```c

{% raw %}
118 | 
119 | 	if (lisp__data.module == NULL) {
120 | 	    /* export our own symbols */
121 | 	    if (dlopen(NULL, RTLD_LAZY | RTLD_GLOBAL) == NULL)
122 | 		LispDestroy("%s: ", STRFUN(builtin), dlerror());
123 | 	}
124 | 
125 | 	lisp_module = (LispModule*)LispMalloc(sizeof(LispModule));
126 | 	if ((lisp_module->handle =
127 | 	     dlopen(filename, RTLD_LAZY | RTLD_GLOBAL)) == NULL)
128 | 	    LispDestroy("%s: dlopen: %s", STRFUN(builtin), dlerror());
129 | 	snprintf(data, sizeof(data), "%sLispModuleData", THESTR(module));
130 | 	if ((lisp_module->data =
{% endraw %}

```