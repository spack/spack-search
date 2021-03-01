---
name: "wget"
layout: package
next_package: whizard
previous_package: weechat
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.20.3
5 / 1055 files match, 4 filtered matches.

 - [fuzz/wget_ftpls_fuzzer.c](#fuzzwget_ftpls_fuzzerc)
 - [fuzz/wget_css_fuzzer.c](#fuzzwget_css_fuzzerc)
 - [fuzz/wget_netrc_fuzzer.c](#fuzzwget_netrc_fuzzerc)
 - [fuzz/wget_options_fuzzer.c](#fuzzwget_options_fuzzerc)

### fuzz/wget_ftpls_fuzzer.c

```c

{% raw %}
75 | 	if (do_jump) {
76 | 		longjmp(jmpbuf, 1);
77 | 	} else {
78 | 		void (*libc_exit)(int) = (void(*)(int)) dlsym (RTLD_NEXT, "exit");
79 | 		libc_exit(status);
80 | 	}
{% endraw %}

```
### fuzz/wget_css_fuzzer.c

```c

{% raw %}
83 | 	if (do_jump) {
84 | 		longjmp(jmpbuf, 1);
85 | 	} else {
86 | 		void (*libc_exit)(int) = (void(*)(int)) dlsym (RTLD_NEXT, "exit");
87 | 		libc_exit(status);
88 | 	}
{% endraw %}

```
### fuzz/wget_netrc_fuzzer.c

```c

{% raw %}
74 | 	if (do_jump) {
75 | 		longjmp(jmpbuf, 1);
76 | 	} else {
77 | 		void (*libc_exit)(int) = (void(*)(int)) dlsym (RTLD_NEXT, "exit");
78 | 		libc_exit(status);
79 | 	}
{% endraw %}

```
### fuzz/wget_options_fuzzer.c

```c

{% raw %}
76 | 	if (do_jump) {
77 | 		longjmp(jmpbuf, 1);
78 | 	} else {
79 | 		void (*libc_exit)(int) = (void(*)(int)) dlsym (RTLD_NEXT, "exit");
80 | 		libc_exit(status);
81 | 	}
{% endraw %}

```