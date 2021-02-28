---
name: "sqlite"
layout: package
next_package: apex
previous_package: alsa-lib
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.27.1
3 / 29 files match, 1 filtered matches.

 - [sqlite3.c](#sqlite3c)

### sqlite3.c

```c

{% raw %}
38801 |   */
38802 |   void (*(*x)(void*,const char*))(void);
38803 |   UNUSED_PARAMETER(NotUsed);
38804 |   x = (void(*(*)(void*,const char*))(void))dlsym;
38805 |   return (*x)(p, zSym);
38806 | }
{% endraw %}

```