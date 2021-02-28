---
name: "ace"
layout: package
next_package: imlib2
previous_package: libxsmm
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c', 'pl']
---
## 6.5.12
20 / 8830 files match, 2 filtered matches.

 - [bin/fuzz.pl](#binfuzzpl)
 - [ace/OS_NS_dlfcn.h](#aceos_ns_dlfcnh)

### bin/fuzz.pl

```pl

{% raw %}
624 | 
625 |     $OS_NS_dirent_symbols = "closedir|opendir|readdir|readdir_r|rewinddir|scandir|alphasort|seekdir|telldir|opendir_emulation|scandir_emulation|closedir_emulation|readdir_emulation";
626 | 
627 |     $OS_NS_dlfcn_symbols = "dlclose|dlerror|dlopen|dlsym";
628 | 
629 |     $OS_NS_errno_symbols = "last_error|set_errno_to_last_error|set_errno_to_wsa_last_error";
{% endraw %}

```
### ace/OS_NS_dlfcn.h

```c

{% raw %}
42 |   ACE_TCHAR *dlerror (void);
43 | 
44 |   ACE_NAMESPACE_INLINE_FUNCTION
45 |   ACE_SHLIB_HANDLE dlopen (const ACE_TCHAR *filename,
46 |                            int mode = ACE_DEFAULT_SHLIB_MODE);
47 | 
{% endraw %}

```