---
name: "libgssglue"
layout: package
next_package: libhbaapi
previous_package: libgpuarray
languages: ['c']
---
## 0.3
3 / 60 files match, 1 filtered matches.

 - [src/g_initialize.c](#srcg_initializec)

### src/g_initialize.c

```c

{% raw %}
228 | 	    *endp = '\0';
229 | 	}
230 | 
231 | 	if ((dl = dlopen(buffer, RTLD_NOW)) == NULL) {
232 | 		/* for debugging only */
233 | 		fprintf(stderr,"can't open %s: %s\n",buffer, dlerror());
305 | 		*endp = '\0';
306 | 	}
307 | 
308 | 	if ((dl = dlopen(buffer, RTLD_NOW | RTLD_LOCAL)) == NULL) {
309 | 	    /* for debugging only */
310 | 	    fprintf(stderr,"can't open %s: %s\n",buffer, dlerror());
{% endraw %}

```