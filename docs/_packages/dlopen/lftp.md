---
name: "lftp"
layout: package
next_package: libblastrampoline
previous_package: legion
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 4.8.1
9 / 797 files match, 1 filtered matches.

 - [src/module.cc](#srcmodulecc)

### src/module.cc

```cpp

{% raw %}
172 | 	 access_so(fullpath);
173 |       }
174 |    }
175 |    map=dlopen(fullpath,DLOPEN_FLAGS);  // LAZY?
176 |    if(map==0)
177 |       return 0;
{% endraw %}

```