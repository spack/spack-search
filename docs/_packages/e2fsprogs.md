---
name: "e2fsprogs"
layout: package
next_package: efivar
previous_package: dyninst
languages: ['c']
---
## 1.45.5
8 / 1500 files match, 2 filtered matches.

 - [lib/ss/get_readline.c](#libssget_readlinec)
 - [lib/support/plausible.c](#libsupportplausiblec)

### lib/ss/get_readline.c

```c

{% raw %}
66 | 			*next++ = 0;
67 | 		if (*cp == 0)
68 | 			continue;
69 | 		if ((handle = dlopen(cp, RTLD_NOW))) {
70 | 			/* printf("Using %s for readline library\n", cp); */
71 | 			break;
{% endraw %}

```
### lib/support/plausible.c

```c

{% raw %}
61 | static int magic_library_available(void)
62 | {
63 | 	if (!magic_handle) {
64 | 		magic_handle = dlopen("libmagic.so.1", RTLD_NOW);
65 | 		if (!magic_handle)
66 | 			return 0;
{% endraw %}

```