---
name: "libcanberra"
layout: package
next_package: libepoxy
previous_package: lftp
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.30
3 / 98 files match, 1 filtered matches.

 - [src/dso.c](#srcdsoc)

### src/dso.c

```c

{% raw %}
146 |         return CA_SUCCESS;
147 | }
148 | 
149 | static void* real_dlsym(lt_module m, const char *name, const char *symbol) {
150 |         char sn[256];
151 |         char *s;
169 |                 *s = '_';
170 |         }
171 | 
172 |         if ((r = lt_dlsym(m, sn)))
173 |                 return r;
174 | 
175 |         return lt_dlsym(m, symbol);
176 | }
177 | 
{% endraw %}

```