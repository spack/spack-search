---
name: "grads"
layout: package
next_package: flac
previous_package: lzo
languages: ['c']
---
## 2.2.1
8 / 515 files match

 - [src/gafunc.c](#srcgafuncc)
 - [src/gxsubs.c](#srcgxsubsc)
 - [src/gradspy.c](#srcgradspyc)

### src/gafunc.c

```c

{% raw %}
7214 |     handle = dlopen(upb->fname,RTLD_LAZY);
7216 |       snprintf (pout,1255,"Error: dlopen failed to get a handle on %s \n",upb->fname);
{% endraw %}

```
### src/gxsubs.c

```c

{% raw %}
150 |   phandle = dlopen (pname, RTLD_LAZY);
152 |     printf("GX Package Error: dlopen failed to get a handle on gxprint plug-in named \"%s\" \n",gxpopt); 
190 |   dhandle = dlopen (dname, RTLD_LAZY);
192 |     printf("GX Package Error: dlopen failed to get a a handle on gxdisplay plug-in named \"%s\" \n",gxdopt); 
{% endraw %}

```
### src/gradspy.c

```c

{% raw %}
245 |   handle = dlopen ("libgradspy.so",    RTLD_LAZY | RTLD_GLOBAL );  /* for linux */
{% endraw %}

```