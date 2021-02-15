---
name: "ncl"
layout: package
next_package: grass
previous_package: glpk
languages: ['cpp']
---
## 6.5.0
3 / 8693 files match

 - [ni/src/ncl/ncl.y](#nisrcnclncly)
 - [ni/src/ncl/NclDriver.c](#nisrcnclncldriverc)
 - [ni/src/ncl/NclApi.c](#nisrcnclnclapic)

### ni/src/ncl/ncl.y

```

{% raw %}
272 | 								$2->u.package->so_handle = dlopen(_NGResolvePath($3),RTLD_NOW);
342 | 								$3->u.package->so_handle = dlopen(_NGResolvePath($4),RTLD_NOW);
506 | 								$2->u.package->so_handle = dlopen(_NGResolvePath($3),RTLD_NOW);
576 | 								$3->u.package->so_handle = dlopen(_NGResolvePath($4),RTLD_NOW);
{% endraw %}

```
### ni/src/ncl/NclDriver.c

```cpp

{% raw %}
323 |                     so_handle = dlopen(buffer, RTLD_NOW);
{% endraw %}

```
### ni/src/ncl/NclApi.c

```cpp

{% raw %}
221 | 					so_handle = dlopen(buffer,RTLD_NOW);
{% endraw %}

```