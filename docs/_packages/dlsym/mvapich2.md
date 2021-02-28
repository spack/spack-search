---
name: "mvapich2"
layout: package
next_package: global
previous_package: tk
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.2
29 / 8321 files match, 8 filtered matches.

 - [src/pm/hydra/tools/topo/hwloc/hwloc/src/components.c](#srcpmhydratoolstopohwlochwlocsrccomponentsc)
 - [src/pm/hydra/tools/topo/hwloc/hwloc/include/hwloc/plugins.h](#srcpmhydratoolstopohwlochwlocincludehwlocpluginsh)
 - [src/mpid/ch3/channels/common/src/scr/scr_interpose.c](#srcmpidch3channelscommonsrcscrscr_interposec)
 - [src/mpid/ch3/channels/common/src/memory/mem_hooks.c](#srcmpidch3channelscommonsrcmemorymem_hooksc)
 - [src/pmi/pmi2/poe/poe2pmi.c](#srcpmipmi2poepoe2pmic)
 - [test/mpid/dluse.c](#testmpiddlusec)
 - [contrib/hwloc/src/components.c](#contribhwlocsrccomponentsc)
 - [contrib/hwloc/include/hwloc/plugins.h](#contribhwlocincludehwlocpluginsh)

### src/pm/hydra/tools/topo/hwloc/hwloc/src/components.c

```c

{% raw %}
91 |   }
92 |   componentsymbolname = malloc(strlen(basename)+10+1);
93 |   sprintf(componentsymbolname, "%s_component", basename);
94 |   component = lt_dlsym(handle, componentsymbolname);
95 |   if (!component) {
96 |     if (hwloc_plugins_verbose)
{% endraw %}

```
### src/pm/hydra/tools/topo/hwloc/hwloc/include/hwloc/plugins.h

```c

{% raw %}
328 |   if (!handle)
329 |     /* cannot check, assume things will work */
330 |     return 0;
331 |   sym = lt_dlsym(handle, symbol);
332 |   lt_dlclose(handle);
333 |   if (!sym) {
{% endraw %}

```
### src/mpid/ch3/channels/common/src/scr/scr_interpose.c

```c

{% raw %}
589 | ==============================================================================
590 | */
591 | 
592 | static void* mydlsym(const char *name)
593 | {
594 |   void *p = dlsym(RTLD_NEXT, name);
595 |   if (!p) {
596 |     fprintf(stderr,"dlsym(RTLD_NEXT, %s) failed: %s\n", name, dlerror());
597 |     exit(1);
598 |   }
606 | 
607 |   /* interpose MPI functions */
608 |   if (scri_real_mpi_init == NULL) {
609 |     scri_real_mpi_init = (int (*)(int *, char ***)) mydlsym("MPI_Init");
610 |   }
611 |   if (scri_real_mpi_fini == NULL) {
612 |     scri_real_mpi_fini = (int (*)()) mydlsym("MPI_Finalize");
613 |   }
614 | 
615 |   /* interpose open/close functions */
616 |   if (scri_real_open == NULL) {
617 |     scri_real_open  = (int (*)(const char *, int, ...)) mydlsym("open");
618 |   }
619 |   /*
620 |   scri_real_open  = (int (*)(const char *, int, mode_t)) mydlsym("open");
621 |   */
622 |   if (scri_real_close == NULL) {
623 |     scri_real_close = (int (*)(int fd)) mydlsym("close");
624 |   }
625 | 
626 |   /* interpose fopen/fclose functions */
627 |   if (scri_real_fopen == NULL) {
628 |     scri_real_fopen  = (FILE* (*)(const char *, const char *)) mydlsym("fopen");
629 |   }
630 |   if (scri_real_fclose == NULL) {
631 |     scri_real_fclose = (int (*)(FILE*)) mydlsym("fclose");
632 |   }
633 | 
634 |   /* interpose mkdir */
635 |   if (scri_real_mkdir == NULL) {
636 |     scri_real_mkdir = (int (*)(const char*, mode_t)) mydlsym("mkdir");
637 |   }
638 | 
639 |   /* interpose read/write functions */
640 | /*
641 |   real_read  = (ssize_t (*)(int fd, void *buf, size_t count))       mydlsym("read");
642 |   real_write = (ssize_t (*)(int fd, const void *buf, size_t count)) mydlsym("write");
643 | */
644 | 
{% endraw %}

```
### src/mpid/ch3/channels/common/src/memory/mem_hooks.c

```c

{% raw %}
50 | 
51 | static void set_real_munmap_ptr()
52 | {
53 |     munmap_t munmap_ptr = (munmap_t) dlsym(RTLD_NEXT, "munmap");
54 |     char* dlerror_str = dlerror();
55 |     if(NULL != dlerror_str) {
77 | 
78 |     if (NULL != handle) {
79 |         /* Shared libraries are in use, otherwise simply proceed. */
80 |         munmap_t mvapich_munmap_ptr = (munmap_t) dlsym(handle, "munmap");
81 |         char* dlerror_str = dlerror();
82 |         if(NULL != dlerror_str) {
{% endraw %}

```
### src/pmi/pmi2/poe/poe2pmi.c

```c

{% raw %}
100 |         TRACE_ERR("failed to open %s error=%s\n", poelibname, dlerror());
101 |     }
102 | 
103 |     pmi2_init = (int (*)())dlsym(poeptr, "PMI2_Init");
104 |     if (pmi2_init == NULL) {
105 |         TRACE_ERR("failed to dlsym PMI2_Init\n");
106 |     }
107 | 
118 | 
119 |     int (*pmi2_finalize)(void);
120 | 
121 |     pmi2_finalize = (int (*)())dlsym(poeptr, "PMI2_Finalize");
122 |     if (pmi2_finalize == NULL) {
123 |         TRACE_ERR("failed to dlsym PMI2_Finalize\n");
124 |     }
125 | 
140 | {
141 |     int (*pmi2_abort)(int, const char*);
142 | 
143 |     pmi2_abort = (int (*)())dlsym(poeptr, "PMI2_Abort");
144 |     if (pmi2_abort == NULL) {
145 |         TRACE_ERR("failed to dlsym pmi2_abort\n");
146 |     }
147 | 
169 | 
170 |     int (*pmi2_job_spawn)(int , const char * [], int [], const char ** [],const int [],const int [],const struct MPID_Info *[],int ,const struct MPID_Info *[],char jobId[],int ,int []);
171 | 
172 |     pmi2_job_spawn = (int (*)())dlsym(poeptr, "PMI2_Job_Spawn");
173 |     if (pmi2_job_spawn == NULL) {
174 |         TRACE_ERR("failed to dlsym pmi2_job_spawn\n");
175 |     }
176 | 
192 | 
193 |     int (*pmi2_job_getid)(char*, int);
194 | 
195 |     pmi2_job_getid = (int (*)())dlsym(poeptr, "PMI2_Job_GetId");
196 |     if (pmi2_job_getid == NULL) {
197 |         TRACE_ERR("failed to dlsym pmi2_job_getid\n");
198 |     }
199 | 
209 | 
210 |     int (*pmi2_kvs_put)(const char*, const char*);
211 | 
212 |     pmi2_kvs_put = (int (*)())dlsym(poeptr, "PMI2_KVS_Put");
213 |     if (pmi2_kvs_put == NULL) {
214 |         TRACE_ERR("failed to dlsym pmi2_kvs_put\n");
215 |     }
216 | 
225 | 
226 |     int (*pmi2_kvs_fence)(void);
227 | 
228 |     pmi2_kvs_fence = (int (*)())dlsym(poeptr, "PMI2_KVS_Fence");
229 |     if (pmi2_kvs_fence == NULL) {
230 |         TRACE_ERR("failed to dlsym pmi2_kvs_fence\n");
231 |     }
232 | 
246 | 
247 |     int (*pmi2_kvs_get)(const char*, int, const char *, char *, int, int*);
248 | 
249 |     pmi2_kvs_get = (int (*)())dlsym(poeptr, "PMI2_KVS_Get");
250 |     if (pmi2_kvs_get == NULL) {
251 |         TRACE_ERR("failed to dlsym pmi2_kvs_get\n");
252 |     }
253 | 
266 | 
267 |     int (*pmi2_info_getjobattr)(const char*, char *, int, int*);
268 | 
269 |     pmi2_info_getjobattr = (int (*)())dlsym(poeptr, "PMI2_Info_GetJobAttr");
270 |     if (pmi2_info_getjobattr == NULL) {
271 |         TRACE_ERR("failed to dlsym pmi2_info_getjobattr\n");
272 |     }
273 | 
{% endraw %}

```
### test/mpid/dluse.c

```c

{% raw %}
24 | 	exit(1);
25 |     }
26 | 
27 |     init = (int (*)(void))dlsym( handle, "init" );
28 |     counter = (int *)dlsym( handle, "counter" );
29 |     finalize = (int (*)(int))dlsym( handle, "finalize" );
30 |     if (!init || !counter || !finalize) {
31 | 	errs++;
{% endraw %}

```
### contrib/hwloc/src/components.c

```c

{% raw %}
97 |   }
98 |   componentsymbolname = malloc(strlen(basename)+10+1);
99 |   sprintf(componentsymbolname, "%s_component", basename);
100 |   component = lt_dlsym(handle, componentsymbolname);
101 |   if (!component) {
102 |     if (hwloc_plugins_verbose)
{% endraw %}

```
### contrib/hwloc/include/hwloc/plugins.h

```c

{% raw %}
371 |   if (!handle)
372 |     /* cannot check, assume things will work */
373 |     return 0;
374 |   sym = lt_dlsym(handle, symbol);
375 |   lt_dlclose(handle);
376 |   if (!sym) {
{% endraw %}

```