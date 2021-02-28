---
name: "grads"
layout: package
next_package: ruby
previous_package: octave
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.2.1
8 / 515 files match, 3 filtered matches.

 - [src/gafunc.c](#srcgafuncc)
 - [src/gxsubs.c](#srcgxsubsc)
 - [src/gradspy.c](#srcgradspyc)

### src/gafunc.c

```c

{% raw %}
7211 | 
7212 |   /* load the shared object file and get the function pointer */
7213 |   if (upb->pfunc == NULL) {
7214 |     handle = dlopen(upb->fname,RTLD_LAZY);
7215 |     if (handle==NULL) {
7216 |       snprintf (pout,1255,"Error: dlopen failed to get a handle on %s \n",upb->fname);
7217 |       gaprnt (0,pout);
7218 |       return (1);
{% endraw %}

```
### src/gxsubs.c

```c

{% raw %}
147 |     return(1);
148 |   }
149 |   dlerror();
150 |   phandle = dlopen (pname, RTLD_LAZY);
151 |   if (!phandle) {
152 |     printf("GX Package Error: dlopen failed to get a handle on gxprint plug-in named \"%s\" \n",gxpopt); 
153 |     if ((err=dlerror())!=NULL) printf("   %s\n",err); 
154 |     return(1);
187 |     return(1);
188 |   }
189 |   dlerror();
190 |   dhandle = dlopen (dname, RTLD_LAZY);
191 |   if (!dhandle) {
192 |     printf("GX Package Error: dlopen failed to get a a handle on gxdisplay plug-in named \"%s\" \n",gxdopt); 
193 |     if ((err=dlerror())!=NULL) printf("   %s\n",err); 
194 |     return(2);
{% endraw %}

```
### src/gradspy.c

```c

{% raw %}
242 | 
243 |   Py_InitModule3("gradspy", gradspy_funcs,"GrADS extension modlues for Python");
244 | 
245 |   handle = dlopen ("libgradspy.so",    RTLD_LAZY | RTLD_GLOBAL );  /* for linux */
246 | /*   handle = dlopen ("libgradspy.dylib", RTLD_LAZY | RTLD_GLOBAL );  /\* for mac   *\/ */
247 |   if (!handle) {
{% endraw %}

```