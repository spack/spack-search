---
name: "fenics"
layout: package
next_package: ecflow
previous_package: kibana
languages: ['python']
---
## 1.6.0
3 / 2235 files match

 - [test/memory/dolfin_valgrind.supp](#testmemorydolfin_valgrindsupp)
 - [site-packages/dolfin/__init__.py](#site-packagesdolfin__init__py)
 - [site-packages/dolfin/importhandler/__init__.py](#site-packagesdolfinimporthandler__init__py)

### test/memory/dolfin_valgrind.supp

```

{% raw %}
110 |    fun:dlopen
219 |    fun:dlopen
221 |    fun:tryall_dlopen
222 |    fun:tryall_dlopen_module
223 |    fun:try_dlopen
224 |    fun:lt_dlopenadvise
435 |    fun:dlopen
437 |    fun:tryall_dlopen
438 |    fun:tryall_dlopen_module
557 |    fun:dlopen
574 |    fun:dlopen
639 |    fun:dlopen
643 |    fun:lt_dlopenadvise
644 |    fun:lt_dlopenext
657 |    fun:dlopen
675 |    fun:dlopen
826 |    fun:dlopen
946 |    fun:dlopen
1073 |    fun:dlopen
1093 |    fun:dlopen
1123 |    fun:dlopen
1191 |    fun:dlopen
1209 |    fun:dlopen
1317 |    fun:dlopen
1351 |    fun:dlopen
1599 |    fun:__libc_dlopen_mode
1613 |    fun:dlopen
1785 |    fun:dlopen
1789 |    fun:lt_dlopenadvise
1790 |    fun:lt_dlopenext
{% endraw %}

```
### site-packages/dolfin/__init__.py

```python

{% raw %}
21 | sys.setdlopenflags(dolfin.importhandler.stored_dlopen_flags)
{% endraw %}

```
### site-packages/dolfin/importhandler/__init__.py

```python

{% raw %}
18 | stored_dlopen_flags = sys.getdlopenflags()
32 |     sys.setdlopenflags(RTLD_NOW | RTLD_GLOBAL)
{% endraw %}

```