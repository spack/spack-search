---
name: "boost"
layout: package
next_package: None
previous_package: None
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.49.0
6 / 38128 files match, 2 filtered matches.

 - [tools/build/v2/engine/boehm_gc/pthread_support.c](#toolsbuildv2engineboehm_gcpthread_supportc)
 - [tools/build/v2/engine/boehm_gc/dyn_load.c](#toolsbuildv2engineboehm_gcdyn_loadc)

### tools/build/v2/engine/boehm_gc/pthread_support.c

```c

{% raw %}
195 |       if (NULL == dl_handle) ABORT("Couldn't open libpthread\n");
196 | #   endif
197 |     GC_real_pthread_create = (GC_pthread_create_t)
198 | 	    			dlsym(dl_handle, "pthread_create");
199 |     GC_real_pthread_sigmask = (GC_pthread_sigmask_t)
200 | 	    			dlsym(dl_handle, "pthread_sigmask");
201 |     GC_real_pthread_join = (GC_pthread_join_t)
202 | 	    			dlsym(dl_handle, "pthread_join");
203 |     GC_real_pthread_detach = (GC_pthread_detach_t)
204 | 	    			dlsym(dl_handle, "pthread_detach");
205 |     GC_syms_initialized = TRUE;
206 |   }
{% endraw %}

```
### tools/build/v2/engine/boehm_gc/dyn_load.c

```c

{% raw %}
136 | 	/* at program startup.						*/
137 | 	if( dynStructureAddr == 0 ) {
138 | 	  void* startupSyms = dlopen(0, RTLD_LAZY);
139 | 	  dynStructureAddr = (ElfW(Dyn)*)dlsym(startupSyms, "_DYNAMIC");
140 | 		}
141 | #   else
{% endraw %}

```