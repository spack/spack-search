---
name: "extrae"
layout: package
next_package: lvm2
previous_package: nix
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.4.1
17 / 975 files match, 13 filtered matches.

 - [src/loader/extrae-loader.c](#srcloaderextrae-loaderc)
 - [src/tracer/wrappers/pthread/pthread_wrapper.c](#srctracerwrapperspthreadpthread_wrapperc)
 - [src/tracer/wrappers/MPI/mpi_wrapper.c](#srctracerwrappersmpimpi_wrapperc)
 - [src/tracer/wrappers/OPENCL/opencl_wrapper.c](#srctracerwrappersopenclopencl_wrapperc)
 - [src/tracer/wrappers/IO/io_wrapper.c](#srctracerwrappersioio_wrapperc)
 - [src/tracer/wrappers/CUDA/cuda_wrapper.c](#srctracerwrapperscudacuda_wrapperc)
 - [src/tracer/wrappers/openshmem/openshmem_wrappers.c](#srctracerwrappersopenshmemopenshmem_wrappersc)
 - [src/tracer/wrappers/OMP/omp_wrapper.c](#srctracerwrappersompomp_wrapperc)
 - [src/tracer/wrappers/OMP/ibm-xlsmp-1.6.c](#srctracerwrappersompibm-xlsmp-16c)
 - [src/tracer/wrappers/OMP/intel-kmpc-11.c](#srctracerwrappersompintel-kmpc-11c)
 - [src/tracer/wrappers/OMP/gnu-libgomp-4.9.c](#srctracerwrappersompgnu-libgomp-49c)
 - [src/tracer/wrappers/OMP/gnu-libgomp-4.2.c](#srctracerwrappersompgnu-libgomp-42c)
 - [src/tracer/wrappers/MALLOC/malloc_wrapper.c](#srctracerwrappersmallocmalloc_wrapperc)

### src/loader/extrae-loader.c

```c

{% raw %}
83 |   char *error = NULL;
84 | 
85 |   fprintf(stderr, "extrae-loader: Looking for '%s'... ", symbol);
86 |   symbol_ptr = dlsym(handle, symbol); 
87 |   if ((error = dlerror()) != NULL)
88 |   {
{% endraw %}

```
### src/tracer/wrappers/pthread/pthread_wrapper.c

```c

{% raw %}
92 | 	/* Obtain @ for pthread_create */
93 | 	pthread_create_real =
94 | 		(int(*)(pthread_t*,const pthread_attr_t*,void *(*) (void *),void*))
95 | 		dlsym (RTLD_NEXT, "pthread_create");
96 | 	if (pthread_create_real == NULL && rank == 0)
97 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_create in DSOs!!\n");
98 | 
99 | 	/* Obtain @ for pthread_join */
100 | 	pthread_join_real =
101 | 		(int(*)(pthread_t,void**)) dlsym (RTLD_NEXT, "pthread_join");
102 | 	if (pthread_join_real == NULL && rank == 0)
103 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_join in DSOs!!\n");
105 | #if defined(HAVE_PTHREAD_BARRIER_WAIT)
106 |   	/* Obtain @ for pthread_barrier_wait */
107 | 	pthread_barrier_wait_real =
108 | 		(int(*)(pthread_barrier_t *)) dlsym (RTLD_NEXT, "pthread_barrier_wait");
109 | 	if (pthread_barrier_wait_real == NULL && rank == 0)
110 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_barrier_wait in DSOs!!\n");
111 | #endif
112 | 
113 | 	/* Obtain @ for pthread_detach */
114 | 	pthread_detach_real = (int(*)(pthread_t)) dlsym (RTLD_NEXT, "pthread_detach");
115 | 	if (pthread_detach_real == NULL && rank == 0)
116 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_detach in DSOs!!\n");
117 | 
118 | 	/* Obtain @ for pthread_exit */
119 | 	pthread_exit_real = (void(*)(void*)) dlsym (RTLD_NEXT, "pthread_exit");
120 | 	if (pthread_exit_real == NULL && rank == 0)
121 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_exit in DSOs!!\n");
122 | 
123 | 	/* Obtain @ for pthread_mutex_lock */
124 | 	pthread_mutex_lock_real = (int(*)(pthread_mutex_t*)) dlsym (RTLD_NEXT, "pthread_mutex_lock");
125 | 	if (pthread_mutex_lock_real == NULL && rank == 0)
126 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_lock in DSOs!!\n");
127 | 	
128 | 	/* Obtain @ for pthread_mutex_unlock */
129 | 	pthread_mutex_unlock_real = (int(*)(pthread_mutex_t*)) dlsym (RTLD_NEXT, "pthread_mutex_unlock");
130 | 	if (pthread_mutex_unlock_real == NULL && rank == 0)
131 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_unlock in DSOs!!\n");
132 | 	
133 | 	/* Obtain @ for pthread_mutex_trylock */
134 | 	pthread_mutex_trylock_real = (int(*)(pthread_mutex_t*)) dlsym (RTLD_NEXT, "pthread_mutex_trylock");
135 | 	if (pthread_mutex_trylock_real == NULL && rank == 0)
136 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_trylock in DSOs!!\n");
137 | 
138 | 	/* Obtain @ for pthread_mutex_timedlock */
139 | 	pthread_mutex_timedlock_real = (int(*)(pthread_mutex_t*,const struct timespec*)) dlsym (RTLD_NEXT, "pthread_mutex_timedlock");
140 | 	if (pthread_mutex_timedlock_real == NULL && rank == 0)
141 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_mutex_timedlock in DSOs!!\n");
142 | 
143 | #if 0
144 | 	/* Obtain @ for pthread_cond_signal */
145 | 	pthread_cond_signal_real = (int(*)(pthread_cond_t*)) dlsym (RTLD_NEXT, "pthread_cond_signal");
146 | 	if (pthread_cond_signal_real == NULL && rank == 0)
147 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_cond_signal in DSOs!!\n");
148 | 	
149 | 	/* Obtain @ for pthread_cond_broadcast */
150 | 	pthread_cond_broadcast_real = (int(*)(pthread_cond_t*)) dlsym (RTLD_NEXT, "pthread_cond_broadcast");
151 | 	if (pthread_cond_broadcast_real == NULL && rank == 0)
152 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_cond_broadcast in DSOs!!\n");
153 | 	
154 | 	/* Obtain @ for pthread_cond_wait */
155 | 	pthread_cond_wait_real = (int(*)(pthread_cond_t*,pthread_mutex_t*)) dlsym (RTLD_NEXT, "pthread_cond_wait");
156 | 	if (pthread_cond_wait_real == NULL && rank == 0)
157 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_cond_wait in DSOs!!\n");
158 | 	
159 | 	/* Obtain @ for pthread_cond_timedwait */
160 | 	pthread_cond_timedwait_real = (int(*)(pthread_cond_t*,pthread_mutex_t*,const struct timespec*)) dlsym (RTLD_NEXT, "pthread_cond_timedwait");
161 | 	if (pthread_cond_timedwait_real == NULL && rank == 0)
162 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_cond_timedwait in DSOs!!\n");
163 | #endif
164 | 	
165 | 	/* Obtain @ for pthread_rwlock_rdlock */
166 | 	pthread_rwlock_rdlock_real = (int(*)(pthread_rwlock_t*)) dlsym (RTLD_NEXT, "pthread_rwlock_rdlock");
167 | 	if (pthread_rwlock_rdlock_real == NULL && rank == 0)
168 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_rwlock_rdlock in DSOs!!\n");
169 | 	
170 | 	/* Obtain @ for pthread_rwlock_tryrdlock */
171 | 	pthread_rwlock_tryrdlock_real = (int(*)(pthread_rwlock_t*)) dlsym (RTLD_NEXT, "pthread_rwlock_tryrdlock");
172 | 	if (pthread_rwlock_tryrdlock_real == NULL && rank == 0)
173 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_rwlock_tryrdlock in DSOs!!\n");
174 | 	
175 | 	/* Obtain @ for pthread_rwlock_timedrdlock */
176 | 	pthread_rwlock_timedrdlock_real = (int(*)(pthread_rwlock_t *, const struct timespec *)) dlsym (RTLD_NEXT, "pthread_rwlock_timedrdlock");
177 | 	if (pthread_rwlock_timedrdlock_real == NULL && rank == 0)
178 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_rwlock_timedrdlock in DSOs!!\n");
179 | 	
180 | 	/* Obtain @ for pthread_rwlock_rwlock */
181 | 	pthread_rwlock_wrlock_real = (int(*)(pthread_rwlock_t*)) dlsym (RTLD_NEXT, "pthread_rwlock_wrlock");
182 | 	if (pthread_rwlock_wrlock_real == NULL && rank == 0)
183 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_rwlock_wrlock in DSOs!!\n");
184 | 	
185 | 	/* Obtain @ for pthread_rwlock_tryrwlock */
186 | 	pthread_rwlock_trywrlock_real = (int(*)(pthread_rwlock_t*)) dlsym (RTLD_NEXT, "pthread_rwlock_trywrlock");
187 | 	if (pthread_rwlock_trywrlock_real == NULL && rank == 0)
188 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_rwlock_trywrlock in DSOs!!\n");
189 | 	
190 | 	/* Obtain @ for pthread_rwlock_timedrwlock */
191 | 	pthread_rwlock_timedwrlock_real = (int(*)(pthread_rwlock_t *, const struct timespec *)) dlsym (RTLD_NEXT, "pthread_rwlock_timedwrlock");
192 | 	if (pthread_rwlock_timedwrlock_real == NULL && rank == 0)
193 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_rwlock_timedwrlock in DSOs!!\n");
194 | 
195 | 	/* Obtain @ for pthread_rwlock_unlock */
196 | 	pthread_rwlock_unlock_real = (int(*)(pthread_rwlock_t*)) dlsym (RTLD_NEXT, "pthread_rwlock_unlock");
197 | 	if (pthread_rwlock_unlock_real == NULL && rank == 0)
198 | 		fprintf (stderr, PACKAGE_NAME": Unable to find pthread_rwlock_unlock in DSOs!!\n");
{% endraw %}

```
### src/tracer/wrappers/MPI/mpi_wrapper.c

```c

{% raw %}
985 | 
986 | #ifdef WITH_PMPI_HOOK
987 |         int (*real_mpi_init)(MPI_Fint *ierror) = NULL;
988 |         real_mpi_init = dlsym(RTLD_NEXT, STRINGIFY(CtoF77 (mpi_init)));
989 | 
990 |         if (real_mpi_init != NULL) {
1103 | 
1104 | #ifdef WITH_PMPI_HOOK
1105 |         int (*real_mpi_init_thread)(MPI_Fint *required, MPI_Fint *provided, MPI_Fint *ierror) = NULL;
1106 |         real_mpi_init_thread = dlsym(RTLD_NEXT, STRINGIFY(CtoF77 (mpi_init_thread)));
1107 | 
1108 |         if (real_mpi_init_thread != NULL) {
1252 | 
1253 | #ifdef WITH_PMPI_HOOK
1254 | 		int (*real_mpi_finalize)(MPI_Fint *ierror) = NULL;
1255 | 		real_mpi_finalize = dlsym(RTLD_NEXT, STRINGIFY(CtoF77 (mpi_finalize)));
1256 | 		if (real_mpi_finalize != NULL) {
1257 | 			CtoF77 (real_mpi_finalize) (ierror);
1974 | 
1975 | #ifdef WITH_PMPI_HOOK
1976 | 	int (*real_mpi_init)(int *argc, char ***argv) = NULL;
1977 | 	real_mpi_init = dlsym(RTLD_NEXT, "MPI_Init");
1978 | 	if (real_mpi_init != NULL) {
1979 | 		val = real_mpi_init (argc, argv);
2090 | 
2091 | #ifdef WITH_PMPI_HOOK
2092 | 	int (*real_mpi_init_thread)(int *argc, char ***argv, int required, int *provided) = NULL;
2093 | 	real_mpi_init_thread = dlsym(RTLD_NEXT, "MPI_Init_thread");
2094 | 	if (real_mpi_init_thread != NULL) {
2095 | 		val = real_mpi_init_thread (argc, argv, required, provided);
2237 | 
2238 | #ifdef WITH_PMPI_HOOK
2239 | 		int (*real_mpi_finalize)() = NULL;
2240 | 		real_mpi_finalize = dlsym(RTLD_NEXT, "MPI_Finalize");
2241 | 		if (real_mpi_finalize != NULL) {
2242 | 			ierror = real_mpi_finalize();
{% endraw %}

```
### src/tracer/wrappers/OPENCL/opencl_wrapper.c

```c

{% raw %}
118 | #endif
119 | 
120 | 	real_clCreateBuffer = (cl_mem(*)(cl_context, cl_mem_flags, size_t, void*, cl_int *))
121 | 		dlsym (lib, "clCreateBuffer");
122 | 
123 | 	real_clCreateCommandQueue = (cl_command_queue(*)(cl_context, cl_device_id, cl_command_queue_properties, cl_int*))
124 | 		dlsym (lib, "clCreateCommandQueue");
125 | 
126 | 	real_clCreateContext = (cl_context(*)(const cl_context_properties *, cl_uint, const cl_device_id *, void *, void *, cl_int *))
127 | 		dlsym (lib, "clCreateContext");
128 | 
129 | 	real_clCreateContextFromType = (cl_context(*)(const cl_context_properties *, cl_device_type, void *, void *, cl_int *))
130 | 		dlsym (lib, "clCreateContextFromType");
131 | 
132 | 	real_clCreateKernel = (cl_kernel(*)(cl_program, const char *, cl_int *))
133 | 		dlsym (lib, "clCreateKernel");
134 | 
135 | 	real_clCreateKernelsInProgram = (cl_int(*)(cl_program, cl_uint, cl_kernel *, cl_uint *))
136 | 		dlsym (lib, "clCreateKernelsInProgram");
137 | 
138 | 	real_clSetKernelArg = (cl_int(*)(cl_kernel, cl_uint, size_t, const void *))
139 | 		dlsym (lib, "clSetKernelArg");
140 | 
141 | 	real_clCreateProgramWithSource = (cl_program(*)(cl_context, cl_uint, const char **, const size_t *, cl_int *))
142 | 		dlsym (lib, "clCreateProgramWithSource");
143 | 
144 | 	real_clCreateProgramWithBinary = (cl_program(*)(cl_context, cl_uint, const cl_device_id *, const size_t *, const unsigned char **, cl_int *, cl_int *))
145 | 		dlsym (lib, "clCreateProgramWithBinary");
146 | 
147 | 	real_clCreateProgramWithBuiltInKernels = (cl_program(*)(cl_context, cl_uint, const cl_device_id *, const char *, cl_int *))
148 | 		dlsym (lib, "clCreateProgramWithBuiltInKernels");
149 | 
150 | 	real_clCreateSubBuffer = (cl_mem(*)(cl_mem, cl_mem_flags, cl_buffer_create_type, const void *, cl_int *))
151 | 		dlsym (lib, "clCreateSubBuffer");
152 | 
153 | 	real_clEnqueueFillBuffer = (cl_int(*)(cl_command_queue, cl_mem, const void *, size_t, size_t, size_t, cl_uint, const cl_event *, cl_event *))
154 | 		dlsym (lib, "clEnqueueFillBuffer");
155 | 
156 | 	real_clEnqueueCopyBuffer = (cl_int(*)(cl_command_queue, cl_mem, cl_mem, size_t, size_t, size_t, cl_uint, const cl_event *, cl_event *))
157 | 		dlsym (lib, "clEnqueueCopyBuffer");
158 | 
159 | 	real_clEnqueueCopyBufferRect = (cl_int(*)(cl_command_queue, cl_mem, cl_mem, const size_t *, const size_t *, const size_t *, size_t, size_t, size_t, size_t, cl_uint, const cl_event *, cl_event *))
160 | 		dlsym (lib, "clEnqueueCopyBufferRect");
161 | 
162 | 	real_clEnqueueNDRangeKernel = (cl_int(*)(cl_command_queue, cl_kernel, cl_uint, const size_t *, const size_t *, const size_t *, cl_uint, const cl_event *, cl_event *))
163 | 		dlsym (lib, "clEnqueueNDRangeKernel");
164 | 
165 | 	real_clEnqueueTask = (cl_int(*)(cl_command_queue, cl_kernel, cl_uint, const cl_event *, cl_event *))
166 | 		dlsym (lib, "clEnqueueTask");
167 | 
168 | 	real_clEnqueueNativeKernel = (cl_int(*)(cl_command_queue, void *, void *, size_t, cl_uint, const cl_mem *, const void **, cl_uint, const cl_event *, cl_event *))
169 | 		dlsym (lib, "clEnqueueNativeKernel");
170 | 
171 | 	real_clEnqueueReadBuffer = (cl_int(*)(cl_command_queue, cl_mem, cl_bool, size_t, size_t, void *, cl_uint, const cl_event *, cl_event *))
172 | 		dlsym (lib, "clEnqueueReadBuffer");
173 | 
174 | 	real_clEnqueueReadBufferRect = (cl_int(*)(cl_command_queue, cl_mem, cl_bool, const size_t *, const size_t *, const size_t *, size_t, size_t, size_t, size_t, void *, cl_uint, const cl_event *, cl_event *))
175 | 		dlsym (lib, "clEnqueueReadBufferRect");
176 | 
177 | 	real_clEnqueueWriteBuffer = (cl_int(*)(cl_command_queue, cl_mem, cl_bool, size_t, size_t, const void *, cl_uint, const cl_event *, cl_event *))
178 | 		dlsym (lib, "clEnqueueWriteBuffer");
179 | 
180 | 	real_clEnqueueWriteBufferRect = (cl_int(*)(cl_command_queue, cl_mem, cl_bool, const size_t *, const size_t *, const size_t *, size_t, size_t, size_t, size_t, const void *, cl_uint, const cl_event *, cl_event *))
181 | 		dlsym (lib, "clEnqueueWriteBufferRect");
182 | 
183 | 	real_clBuildProgram = (cl_int(*)(cl_program, cl_uint, const cl_device_id *, const char *, void *, void *))
184 | 		dlsym (lib, "clBuildProgram");
185 | 
186 | 	real_clCompileProgram = (cl_int(*)(cl_program, cl_uint, const cl_device_id *, const char *, cl_uint, const cl_program *, const char **, void *, void *))
187 | 		dlsym (lib, "clCompileProgram");
188 | 
189 | 	real_clLinkProgram = (cl_program(*)(cl_context, cl_uint, const cl_device_id *, const char *, cl_uint, const cl_program *, void *, void *, cl_int *))
190 | 		dlsym (lib, "clLinkProgram");
191 | 
192 | 	real_clFinish = (cl_int(*)(cl_command_queue))
193 | 		dlsym (lib, "clFinish");
194 | 
195 | 	real_clFlush = (cl_int(*)(cl_command_queue))
196 | 		dlsym (lib, "clFlush");
197 | 
198 | 	real_clWaitForEvents = (cl_int(*)(cl_uint, const cl_event *el))
199 | 		dlsym (lib, "clWaitForEvents");
200 | 
201 | #ifdef CL_VERSION_1_2
202 | 	real_clEnqueueMarkerWithWaitList = (cl_int(*)(cl_command_queue, cl_uint, const cl_event *, cl_event *))
203 | 		dlsym (lib, "clEnqueueMarkerWithWaitList");
204 | 
205 | 	real_clEnqueueBarrierWithWaitList = (cl_int(*)(cl_command_queue, cl_uint, const cl_event *, cl_event *))
206 | 		dlsym (lib, "clEnqueueBarrierWithWaitList");
207 | #endif
208 | 
209 | 	real_clEnqueueMarker = (cl_int(*)(cl_command_queue, cl_event *))
210 | 		dlsym (lib, "clEnqueueMarker");
211 | 
212 | 	real_clEnqueueBarrier = (cl_int(*)(cl_command_queue))
213 | 		dlsym (lib, "clEnqueueBarrier");
214 | 
215 | 	real_clEnqueueMapBuffer = (void* (*)(cl_command_queue, cl_mem, cl_bool, cl_map_flags, size_t, size_t, cl_uint, const cl_event *, cl_event *, cl_int *))
216 | 		dlsym (lib, "clEnqueueMapBuffer");
217 | 
218 | 	real_clEnqueueUnmapMemObject = (cl_int (*)(cl_command_queue, cl_mem, void *, cl_uint, const cl_event *, cl_event *))
219 | 		dlsym (lib, "clEnqueueUnmapMemObject");
220 | 
221 | #ifdef CL_VERSION_1_2
222 | 	real_clEnqueueMigrateMemObjects = (cl_int (*)(cl_command_queue, cl_uint, const cl_mem *, cl_mem_migration_flags, cl_uint, const cl_event *, cl_event *))
223 | 		dlsym (lib, "clEnqueueMigrateMemObjects");
224 | #endif
225 | 
226 | 	real_clRetainCommandQueue = (cl_int(*)(cl_command_queue))
227 | 	  dlsym (lib, "clRetainCommandQueue");
228 | 
229 | 	real_clReleaseCommandQueue = (cl_int(*)(cl_command_queue))
230 | 	  dlsym (lib, "clReleaseCommandQueue");
231 | 
232 | 	real_clRetainContext = (cl_int(*)(cl_context))
233 | 	  dlsym (lib, "clRetainContext");
234 | 
235 | 	real_clReleaseContext = (cl_int(*)(cl_context))
236 | 	  dlsym (lib, "clReleaseContext");
237 | 
238 | 	real_clRetainDevice = (cl_int(*)(cl_device_id))
239 | 	  dlsym (lib, "clRetainDevice");
240 | 
241 | 	real_clReleaseDevice = (cl_int(*)(cl_device_id))
242 | 	  dlsym (lib, "clReleaseDevice");
243 | 
244 | 	real_clRetainEvent = (cl_int(*)(cl_event))
245 | 	  dlsym (lib, "clRetainEvent");
246 | 
247 | 	real_clReleaseEvent = (cl_int(*)(cl_event))
248 | 	  dlsym (lib, "clReleaseEvent");
249 | 
250 | 	real_clRetainKernel = (cl_int(*)(cl_kernel))
251 | 	  dlsym (lib, "clRetainKernel");
252 | 
253 | 	real_clReleaseKernel = (cl_int(*)(cl_kernel))
254 | 	  dlsym (lib, "clReleaseKernel");
255 | 
256 | 	real_clRetainMemObject = (cl_int(*)(cl_mem))
257 | 	  dlsym (lib, "clRetainMemObject");
258 | 
259 | 	real_clReleaseMemObject = (cl_int(*)(cl_mem))
260 | 	  dlsym (lib, "clReleaseMemObject");
261 | 
262 | 	real_clRetainProgram = (cl_int(*)(cl_program))
263 | 	  dlsym (lib, "clRetainProgram");
264 | 
265 | 	real_clReleaseProgram = (cl_int(*)(cl_program))
266 | 	  dlsym (lib, "clReleaseProgram");
267 | #else
268 | 	fprintf (stderr, PACKAGE_NAME": Warning! OpenCL instrumentation requires linking with shared library!\n");
{% endraw %}

```
### src/tracer/wrappers/IO/io_wrapper.c

```c

{% raw %}
122 |    * after the current library. Not finding any of the symbols doesn't throw an error 
123 |    * unless the application tries to use it later. 
124 |    */
125 |   real_open      = (int(*)(const char *, int, ...)) dlsym(RTLD_NEXT, "open");
126 |   real_open64    = (int(*)(const char *, int, ...)) dlsym(RTLD_NEXT, "open64");
127 |   real_fopen     = (FILE *(*)(const char *, const char *)) dlsym(RTLD_NEXT, "fopen");
128 |   real_fopen64   = (FILE *(*)(const char *, const char *)) dlsym(RTLD_NEXT, "fopen64");
129 | 
130 |   real_read      = (ssize_t(*)(int, void*, size_t)) dlsym (RTLD_NEXT, "read");
131 |   real_write     = (ssize_t(*)(int, const void*, size_t)) dlsym (RTLD_NEXT, "write");
132 | 
133 |   real_fread     = (size_t(*)(void *, size_t, size_t, FILE *)) dlsym (RTLD_NEXT, "fread");
134 |   real_fwrite    = (size_t(*)(const void *, size_t, size_t, FILE *)) dlsym (RTLD_NEXT, "fwrite");
135 | 
136 |   real_pread     = (ssize_t(*)(int fd, void *buf, size_t count, off_t offset)) dlsym (RTLD_NEXT, "pread");
137 |   real_pwrite    = (ssize_t(*)(int fd, const void *buf, size_t count, off_t offset)) dlsym (RTLD_NEXT, "pwrite");
138 | 
139 |   real_readv     = (ssize_t(*)(int, const struct iovec *, int)) dlsym (RTLD_NEXT, "readv");
140 |   real_writev    = (ssize_t(*)(int, const struct iovec *, int)) dlsym (RTLD_NEXT, "writev");
141 |   real_preadv    = (ssize_t(*)(int, const struct iovec *, int, off_t)) dlsym (RTLD_NEXT, "preadv");
142 |   real_preadv64  = (ssize_t(*)(int, const struct iovec *, int, __off64_t)) dlsym (RTLD_NEXT, "preadv64");
143 |   real_pwritev   = (ssize_t(*)(int, const struct iovec *, int, off_t)) dlsym (RTLD_NEXT, "pwritev");
144 |   real_pwritev64 = (ssize_t(*)(int, const struct iovec *, int, __off64_t)) dlsym (RTLD_NEXT, "pwritev64");
145 | 
146 | #  if defined(DEBUG)
{% endraw %}

```
### src/tracer/wrappers/CUDA/cuda_wrapper.c

```c

{% raw %}
64 | 	UNREFERENCED_PARAMETER(rank);
65 | 
66 | #if defined(PIC)
67 | 	real_cudaLaunch = (cudaError_t(*)(const char*)) dlsym (RTLD_NEXT, "cudaLaunch");
68 | 
69 | 	real_cudaConfigureCall = (cudaError_t(*)(dim3, dim3, size_t, cudaStream_t)) dlsym (RTLD_NEXT, "cudaConfigureCall");
70 | 
71 | 	real_cudaThreadSynchronize = (cudaError_t(*)(void)) dlsym (RTLD_NEXT, "cudaThreadSynchronize");
72 | 
73 | 	real_cudaDeviceSynchronize = (cudaError_t(*)(void)) dlsym (RTLD_NEXT, "cudaDeviceSynchronize");
74 | 
75 | 	real_cudaStreamSynchronize = (cudaError_t(*)(cudaStream_t)) dlsym (RTLD_NEXT, "cudaStreamSynchronize");
76 | 
77 | 	real_cudaMemcpy = (cudaError_t(*)(void*,const void*,size_t,enum cudaMemcpyKind)) dlsym (RTLD_NEXT, "cudaMemcpy");
78 | 
79 | 	real_cudaMemcpyAsync = (cudaError_t(*)(void*,const void*,size_t,enum cudaMemcpyKind,cudaStream_t)) dlsym (RTLD_NEXT, "cudaMemcpyAsync");
80 | 
81 | 	real_cudaStreamCreate = (cudaError_t(*)(cudaStream_t*)) dlsym (RTLD_NEXT, "cudaStreamCreate");
82 | 
83 | 	real_cudaDeviceReset = (cudaError_t(*)(void)) dlsym (RTLD_NEXT, "cudaDeviceReset");
84 | 
85 | 	real_cudaThreadExit = (cudaError_t(*)(void)) dlsym (RTLD_NEXT, "cudaThreadExit");
86 | #else
87 | 	fprintf (stderr, PACKAGE_NAME": Warning! CUDA instrumentation requires linking with shared library!\n");
{% endraw %}

```
### src/tracer/wrappers/openshmem/openshmem_wrappers.c

```c

{% raw %}
591 |   /* Obtain @ for start_pes */
592 |   start_pes_real = 
593 |     (void (*)(int))
594 |     dlsym( lib, "start_pes" );
595 |   if (start_pes_real == NULL && rank == 0)
596 |     fprintf(stderr, PACKAGE_NAME": Unable to find start_pes in DSOs!!\n");
598 |   /* Obtain @ for shmem_my_pe */
599 |   shmem_my_pe_real = 
600 |     (int (*)(void))
601 |     dlsym( lib, "shmem_my_pe" );
602 |   if (shmem_my_pe_real == NULL && rank == 0)
603 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_my_pe in DSOs!!\n");
605 |   /* Obtain @ for _my_pe */
606 |   _my_pe_real = 
607 |     (int (*)(void))
608 |     dlsym( lib, "_my_pe" );
609 |   if (_my_pe_real == NULL && rank == 0)
610 |     fprintf(stderr, PACKAGE_NAME": Unable to find _my_pe in DSOs!!\n");
612 |   /* Obtain @ for shmem_n_pes */
613 |   shmem_n_pes_real = 
614 |     (int (*)(void))
615 |     dlsym( lib, "shmem_n_pes" );
616 |   if (shmem_n_pes_real == NULL && rank == 0)
617 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_n_pes in DSOs!!\n");
619 |   /* Obtain @ for _num_pes */
620 |   _num_pes_real = 
621 |     (int (*)(void))
622 |     dlsym( lib, "_num_pes" );
623 |   if (_num_pes_real == NULL && rank == 0)
624 |     fprintf(stderr, PACKAGE_NAME": Unable to find _num_pes in DSOs!!\n");
626 |   /* Obtain @ for shmem_pe_accessible */
627 |   shmem_pe_accessible_real = 
628 |     (int (*)(int))
629 |     dlsym( lib, "shmem_pe_accessible" );
630 |   if (shmem_pe_accessible_real == NULL && rank == 0)
631 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_pe_accessible in DSOs!!\n");
633 |   /* Obtain @ for shmem_addr_accessible */
634 |   shmem_addr_accessible_real = 
635 |     (int (*)(void *, int))
636 |     dlsym( lib, "shmem_addr_accessible" );
637 |   if (shmem_addr_accessible_real == NULL && rank == 0)
638 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_addr_accessible in DSOs!!\n");
640 |   /* Obtain @ for shmem_ptr */
641 |   shmem_ptr_real = 
642 |     (void * (*)(void *, int))
643 |     dlsym( lib, "shmem_ptr" );
644 |   if (shmem_ptr_real == NULL && rank == 0)
645 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_ptr in DSOs!!\n");
647 |   /* Obtain @ for shmalloc */
648 |   shmalloc_real = 
649 |     (void * (*)(size_t))
650 |     dlsym( lib, "shmalloc" );
651 |   if (shmalloc_real == NULL && rank == 0)
652 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmalloc in DSOs!!\n");
654 |   /* Obtain @ for shfree */
655 |   shfree_real = 
656 |     (void (*)(void *))
657 |     dlsym( lib, "shfree" );
658 |   if (shfree_real == NULL && rank == 0)
659 |     fprintf(stderr, PACKAGE_NAME": Unable to find shfree in DSOs!!\n");
661 |   /* Obtain @ for shrealloc */
662 |   shrealloc_real = 
663 |     (void * (*)(void *, size_t))
664 |     dlsym( lib, "shrealloc" );
665 |   if (shrealloc_real == NULL && rank == 0)
666 |     fprintf(stderr, PACKAGE_NAME": Unable to find shrealloc in DSOs!!\n");
668 |   /* Obtain @ for shmemalign */
669 |   shmemalign_real = 
670 |     (void * (*)(size_t, size_t))
671 |     dlsym( lib, "shmemalign" );
672 |   if (shmemalign_real == NULL && rank == 0)
673 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmemalign in DSOs!!\n");
675 |   /* Obtain @ for shmem_double_put */
676 |   shmem_double_put_real = 
677 |     (void (*)(double *, const double *, size_t, int))
678 |     dlsym( lib, "shmem_double_put" );
679 |   if (shmem_double_put_real == NULL && rank == 0)
680 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_double_put in DSOs!!\n");
682 |   /* Obtain @ for shmem_float_put */
683 |   shmem_float_put_real = 
684 |     (void (*)(float *, const float *, size_t, int))
685 |     dlsym( lib, "shmem_float_put" );
686 |   if (shmem_float_put_real == NULL && rank == 0)
687 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_float_put in DSOs!!\n");
689 |   /* Obtain @ for shmem_int_put */
690 |   shmem_int_put_real = 
691 |     (void (*)(int *, const int *, size_t, int))
692 |     dlsym( lib, "shmem_int_put" );
693 |   if (shmem_int_put_real == NULL && rank == 0)
694 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_put in DSOs!!\n");
696 |   /* Obtain @ for shmem_long_put */
697 |   shmem_long_put_real = 
698 |     (void (*)(long *, const long *, size_t, int))
699 |     dlsym( lib, "shmem_long_put" );
700 |   if (shmem_long_put_real == NULL && rank == 0)
701 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_put in DSOs!!\n");
703 |   /* Obtain @ for shmem_longdouble_put */
704 |   shmem_longdouble_put_real = 
705 |     (void (*)(long double *, const long double *, size_t, int))
706 |     dlsym( lib, "shmem_longdouble_put" );
707 |   if (shmem_longdouble_put_real == NULL && rank == 0)
708 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longdouble_put in DSOs!!\n");
710 |   /* Obtain @ for shmem_longlong_put */
711 |   shmem_longlong_put_real = 
712 |     (void (*)(long long *, const long long *, size_t, int))
713 |     dlsym( lib, "shmem_longlong_put" );
714 |   if (shmem_longlong_put_real == NULL && rank == 0)
715 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_put in DSOs!!\n");
717 |   /* Obtain @ for shmem_put32 */
718 |   shmem_put32_real = 
719 |     (void (*)(void *, const void *, size_t, int))
720 |     dlsym( lib, "shmem_put32" );
721 |   if (shmem_put32_real == NULL && rank == 0)
722 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_put32 in DSOs!!\n");
724 |   /* Obtain @ for shmem_put64 */
725 |   shmem_put64_real = 
726 |     (void (*)(void *, const void *, size_t, int))
727 |     dlsym( lib, "shmem_put64" );
728 |   if (shmem_put64_real == NULL && rank == 0)
729 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_put64 in DSOs!!\n");
731 |   /* Obtain @ for shmem_put128 */
732 |   shmem_put128_real = 
733 |     (void (*)(void *, const void *, size_t, int))
734 |     dlsym( lib, "shmem_put128" );
735 |   if (shmem_put128_real == NULL && rank == 0)
736 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_put128 in DSOs!!\n");
738 |   /* Obtain @ for shmem_putmem */
739 |   shmem_putmem_real = 
740 |     (void (*)(void *, const void *, size_t, int))
741 |     dlsym( lib, "shmem_putmem" );
742 |   if (shmem_putmem_real == NULL && rank == 0)
743 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_putmem in DSOs!!\n");
745 |   /* Obtain @ for shmem_short_put */
746 |   shmem_short_put_real = 
747 |     (void (*)(short*, const short*, size_t, int))
748 |     dlsym( lib, "shmem_short_put" );
749 |   if (shmem_short_put_real == NULL && rank == 0)
750 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_short_put in DSOs!!\n");
752 |   /* Obtain @ for shmem_char_p */
753 |   shmem_char_p_real = 
754 |     (void (*)(char *, char, int))
755 |     dlsym( lib, "shmem_char_p" );
756 |   if (shmem_char_p_real == NULL && rank == 0)
757 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_char_p in DSOs!!\n");
759 |   /* Obtain @ for shmem_short_p */
760 |   shmem_short_p_real = 
761 |     (void (*)(short *, short, int))
762 |     dlsym( lib, "shmem_short_p" );
763 |   if (shmem_short_p_real == NULL && rank == 0)
764 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_short_p in DSOs!!\n");
766 |   /* Obtain @ for shmem_int_p */
767 |   shmem_int_p_real = 
768 |     (void (*)(int *, int, int))
769 |     dlsym( lib, "shmem_int_p" );
770 |   if (shmem_int_p_real == NULL && rank == 0)
771 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_p in DSOs!!\n");
773 |   /* Obtain @ for shmem_long_p */
774 |   shmem_long_p_real = 
775 |     (void (*)(long *, long, int))
776 |     dlsym( lib, "shmem_long_p" );
777 |   if (shmem_long_p_real == NULL && rank == 0)
778 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_p in DSOs!!\n");
780 |   /* Obtain @ for shmem_longlong_p */
781 |   shmem_longlong_p_real = 
782 |     (void (*)(long long *, long long, int))
783 |     dlsym( lib, "shmem_longlong_p" );
784 |   if (shmem_longlong_p_real == NULL && rank == 0)
785 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_p in DSOs!!\n");
787 |   /* Obtain @ for shmem_float_p */
788 |   shmem_float_p_real = 
789 |     (void (*)(float *, float, int))
790 |     dlsym( lib, "shmem_float_p" );
791 |   if (shmem_float_p_real == NULL && rank == 0)
792 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_float_p in DSOs!!\n");
794 |   /* Obtain @ for shmem_double_p */
795 |   shmem_double_p_real = 
796 |     (void (*)(double *, double, int))
797 |     dlsym( lib, "shmem_double_p" );
798 |   if (shmem_double_p_real == NULL && rank == 0)
799 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_double_p in DSOs!!\n");
801 |   /* Obtain @ for shmem_longdouble_p */
802 |   shmem_longdouble_p_real = 
803 |     (void (*)(long double *, long double, int))
804 |     dlsym( lib, "shmem_longdouble_p" );
805 |   if (shmem_longdouble_p_real == NULL && rank == 0)
806 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longdouble_p in DSOs!!\n");
808 |   /* Obtain @ for shmem_double_iput */
809 |   shmem_double_iput_real = 
810 |     (void (*)(double *, const double *, ptrdiff_t, ptrdiff_t, size_t, int))
811 |     dlsym( lib, "shmem_double_iput" );
812 |   if (shmem_double_iput_real == NULL && rank == 0)
813 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_double_iput in DSOs!!\n");
815 |   /* Obtain @ for shmem_float_iput */
816 |   shmem_float_iput_real = 
817 |     (void (*)(float *, const float *, ptrdiff_t, ptrdiff_t, size_t, int))
818 |     dlsym( lib, "shmem_float_iput" );
819 |   if (shmem_float_iput_real == NULL && rank == 0)
820 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_float_iput in DSOs!!\n");
822 |   /* Obtain @ for shmem_int_iput */
823 |   shmem_int_iput_real = 
824 |     (void (*)(int *, const int *, ptrdiff_t, ptrdiff_t, size_t, int))
825 |     dlsym( lib, "shmem_int_iput" );
826 |   if (shmem_int_iput_real == NULL && rank == 0)
827 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_iput in DSOs!!\n");
829 |   /* Obtain @ for shmem_iput32 */
830 |   shmem_iput32_real = 
831 |     (void (*)(void *, const void *, ptrdiff_t, ptrdiff_t, size_t, int))
832 |     dlsym( lib, "shmem_iput32" );
833 |   if (shmem_iput32_real == NULL && rank == 0)
834 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_iput32 in DSOs!!\n");
836 |   /* Obtain @ for shmem_iput64 */
837 |   shmem_iput64_real = 
838 |     (void (*)(void *, const void *, ptrdiff_t, ptrdiff_t, size_t, int))
839 |     dlsym( lib, "shmem_iput64" );
840 |   if (shmem_iput64_real == NULL && rank == 0)
841 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_iput64 in DSOs!!\n");
843 |   /* Obtain @ for shmem_iput128 */
844 |   shmem_iput128_real = 
845 |     (void (*)(void *, const void *, ptrdiff_t, ptrdiff_t, size_t, int))
846 |     dlsym( lib, "shmem_iput128" );
847 |   if (shmem_iput128_real == NULL && rank == 0)
848 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_iput128 in DSOs!!\n");
850 |   /* Obtain @ for shmem_long_iput */
851 |   shmem_long_iput_real = 
852 |     (void (*)(long *, const long *, ptrdiff_t, ptrdiff_t, size_t, int))
853 |     dlsym( lib, "shmem_long_iput" );
854 |   if (shmem_long_iput_real == NULL && rank == 0)
855 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_iput in DSOs!!\n");
857 |   /* Obtain @ for shmem_longdouble_iput */
858 |   shmem_longdouble_iput_real = 
859 |     (void (*)(long double *, const long double *, ptrdiff_t, ptrdiff_t, size_t, int))
860 |     dlsym( lib, "shmem_longdouble_iput" );
861 |   if (shmem_longdouble_iput_real == NULL && rank == 0)
862 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longdouble_iput in DSOs!!\n");
864 |   /* Obtain @ for shmem_longlong_iput */
865 |   shmem_longlong_iput_real = 
866 |     (void (*)(long long *, const long long *, ptrdiff_t, ptrdiff_t, size_t, int))
867 |     dlsym( lib, "shmem_longlong_iput" );
868 |   if (shmem_longlong_iput_real == NULL && rank == 0)
869 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_iput in DSOs!!\n");
871 |   /* Obtain @ for shmem_short_iput */
872 |   shmem_short_iput_real = 
873 |     (void (*)(short *, const short *, ptrdiff_t, ptrdiff_t, size_t, int))
874 |     dlsym( lib, "shmem_short_iput" );
875 |   if (shmem_short_iput_real == NULL && rank == 0)
876 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_short_iput in DSOs!!\n");
878 |   /* Obtain @ for shmem_double_get */
879 |   shmem_double_get_real = 
880 |     (void (*)(double *, const double *, size_t, int))
881 |     dlsym( lib, "shmem_double_get" );
882 |   if (shmem_double_get_real == NULL && rank == 0)
883 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_double_get in DSOs!!\n");
885 |   /* Obtain @ for shmem_float_get */
886 |   shmem_float_get_real = 
887 |     (void (*)(float *, const float *, size_t, int))
888 |     dlsym( lib, "shmem_float_get" );
889 |   if (shmem_float_get_real == NULL && rank == 0)
890 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_float_get in DSOs!!\n");
892 |   /* Obtain @ for shmem_get32 */
893 |   shmem_get32_real = 
894 |     (void (*)(void *, const void *, size_t, int))
895 |     dlsym( lib, "shmem_get32" );
896 |   if (shmem_get32_real == NULL && rank == 0)
897 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_get32 in DSOs!!\n");
899 |   /* Obtain @ for shmem_get64 */
900 |   shmem_get64_real = 
901 |     (void (*)(void *, const void *, size_t, int))
902 |     dlsym( lib, "shmem_get64" );
903 |   if (shmem_get64_real == NULL && rank == 0)
904 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_get64 in DSOs!!\n");
906 |   /* Obtain @ for shmem_get128 */
907 |   shmem_get128_real = 
908 |     (void (*)(void *, const void *, size_t, int))
909 |     dlsym( lib, "shmem_get128" );
910 |   if (shmem_get128_real == NULL && rank == 0)
911 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_get128 in DSOs!!\n");
913 |   /* Obtain @ for shmem_getmem */
914 |   shmem_getmem_real = 
915 |     (void (*)(void *, const void *, size_t, int))
916 |     dlsym( lib, "shmem_getmem" );
917 |   if (shmem_getmem_real == NULL && rank == 0)
918 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_getmem in DSOs!!\n");
920 |   /* Obtain @ for shmem_int_get */
921 |   shmem_int_get_real = 
922 |     (void (*)(int *, const int *, size_t, int))
923 |     dlsym( lib, "shmem_int_get" );
924 |   if (shmem_int_get_real == NULL && rank == 0)
925 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_get in DSOs!!\n");
927 |   /* Obtain @ for shmem_long_get */
928 |   shmem_long_get_real = 
929 |     (void (*)(long *, const long *, size_t, int))
930 |     dlsym( lib, "shmem_long_get" );
931 |   if (shmem_long_get_real == NULL && rank == 0)
932 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_get in DSOs!!\n");
934 |   /* Obtain @ for shmem_longdouble_get */
935 |   shmem_longdouble_get_real = 
936 |     (void (*)(long double *, const long double *, size_t, int))
937 |     dlsym( lib, "shmem_longdouble_get" );
938 |   if (shmem_longdouble_get_real == NULL && rank == 0)
939 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longdouble_get in DSOs!!\n");
941 |   /* Obtain @ for shmem_longlong_get */
942 |   shmem_longlong_get_real = 
943 |     (void (*)(long long *, const long long *, size_t, int))
944 |     dlsym( lib, "shmem_longlong_get" );
945 |   if (shmem_longlong_get_real == NULL && rank == 0)
946 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_get in DSOs!!\n");
948 |   /* Obtain @ for shmem_short_get */
949 |   shmem_short_get_real = 
950 |     (void (*)(short *, const short *, size_t, int))
951 |     dlsym( lib, "shmem_short_get" );
952 |   if (shmem_short_get_real == NULL && rank == 0)
953 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_short_get in DSOs!!\n");
955 |   /* Obtain @ for shmem_char_g */
956 |   shmem_char_g_real = 
957 |     (char (*)(char *, int))
958 |     dlsym( lib, "shmem_char_g" );
959 |   if (shmem_char_g_real == NULL && rank == 0)
960 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_char_g in DSOs!!\n");
962 |   /* Obtain @ for shmem_short_g */
963 |   shmem_short_g_real = 
964 |     (short (*)(short *, int))
965 |     dlsym( lib, "shmem_short_g" );
966 |   if (shmem_short_g_real == NULL && rank == 0)
967 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_short_g in DSOs!!\n");
969 |   /* Obtain @ for shmem_int_g */
970 |   shmem_int_g_real = 
971 |     (int (*)(int *, int))
972 |     dlsym( lib, "shmem_int_g" );
973 |   if (shmem_int_g_real == NULL && rank == 0)
974 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_g in DSOs!!\n");
976 |   /* Obtain @ for shmem_long_g */
977 |   shmem_long_g_real = 
978 |     (long (*)(long *, int))
979 |     dlsym( lib, "shmem_long_g" );
980 |   if (shmem_long_g_real == NULL && rank == 0)
981 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_g in DSOs!!\n");
983 |   /* Obtain @ for shmem_longlong_g */
984 |   shmem_longlong_g_real = 
985 |     (long long (*)(long long *, int))
986 |     dlsym( lib, "shmem_longlong_g" );
987 |   if (shmem_longlong_g_real == NULL && rank == 0)
988 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_g in DSOs!!\n");
990 |   /* Obtain @ for shmem_float_g */
991 |   shmem_float_g_real = 
992 |     (float (*)(float *, int))
993 |     dlsym( lib, "shmem_float_g" );
994 |   if (shmem_float_g_real == NULL && rank == 0)
995 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_float_g in DSOs!!\n");
997 |   /* Obtain @ for shmem_double_g */
998 |   shmem_double_g_real = 
999 |     (double (*)(double *, int))
1000 |     dlsym( lib, "shmem_double_g" );
1001 |   if (shmem_double_g_real == NULL && rank == 0)
1002 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_double_g in DSOs!!\n");
1004 |   /* Obtain @ for shmem_longdouble_g */
1005 |   shmem_longdouble_g_real = 
1006 |     (long double (*)(long double *, int))
1007 |     dlsym( lib, "shmem_longdouble_g" );
1008 |   if (shmem_longdouble_g_real == NULL && rank == 0)
1009 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longdouble_g in DSOs!!\n");
1011 |   /* Obtain @ for shmem_double_iget */
1012 |   shmem_double_iget_real = 
1013 |     (void (*)(double *, const double *, ptrdiff_t, ptrdiff_t, size_t, int))
1014 |     dlsym( lib, "shmem_double_iget" );
1015 |   if (shmem_double_iget_real == NULL && rank == 0)
1016 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_double_iget in DSOs!!\n");
1018 |   /* Obtain @ for shmem_float_iget */
1019 |   shmem_float_iget_real = 
1020 |     (void (*)(float *, const float *, ptrdiff_t, ptrdiff_t, size_t, int))
1021 |     dlsym( lib, "shmem_float_iget" );
1022 |   if (shmem_float_iget_real == NULL && rank == 0)
1023 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_float_iget in DSOs!!\n");
1025 |   /* Obtain @ for shmem_iget32 */
1026 |   shmem_iget32_real = 
1027 |     (void (*)(void *, const void *, ptrdiff_t, ptrdiff_t, size_t, int))
1028 |     dlsym( lib, "shmem_iget32" );
1029 |   if (shmem_iget32_real == NULL && rank == 0)
1030 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_iget32 in DSOs!!\n");
1032 |   /* Obtain @ for shmem_iget64 */
1033 |   shmem_iget64_real = 
1034 |     (void (*)(void *, const void *, ptrdiff_t, ptrdiff_t, size_t, int))
1035 |     dlsym( lib, "shmem_iget64" );
1036 |   if (shmem_iget64_real == NULL && rank == 0)
1037 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_iget64 in DSOs!!\n");
1039 |   /* Obtain @ for shmem_iget128 */
1040 |   shmem_iget128_real = 
1041 |     (void (*)(void *, const void *, ptrdiff_t, ptrdiff_t, size_t, int))
1042 |     dlsym( lib, "shmem_iget128" );
1043 |   if (shmem_iget128_real == NULL && rank == 0)
1044 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_iget128 in DSOs!!\n");
1046 |   /* Obtain @ for shmem_int_iget */
1047 |   shmem_int_iget_real = 
1048 |     (void (*)(int *, const int *, ptrdiff_t, ptrdiff_t, size_t, int))
1049 |     dlsym( lib, "shmem_int_iget" );
1050 |   if (shmem_int_iget_real == NULL && rank == 0)
1051 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_iget in DSOs!!\n");
1053 |   /* Obtain @ for shmem_long_iget */
1054 |   shmem_long_iget_real = 
1055 |     (void (*)(long *, const long *, ptrdiff_t, ptrdiff_t, size_t, int))
1056 |     dlsym( lib, "shmem_long_iget" );
1057 |   if (shmem_long_iget_real == NULL && rank == 0)
1058 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_iget in DSOs!!\n");
1060 |   /* Obtain @ for shmem_longdouble_iget */
1061 |   shmem_longdouble_iget_real = 
1062 |     (void (*)(long double *, const long double *, ptrdiff_t, ptrdiff_t, size_t, int))
1063 |     dlsym( lib, "shmem_longdouble_iget" );
1064 |   if (shmem_longdouble_iget_real == NULL && rank == 0)
1065 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longdouble_iget in DSOs!!\n");
1067 |   /* Obtain @ for shmem_longlong_iget */
1068 |   shmem_longlong_iget_real = 
1069 |     (void (*)(long long *, const long long *, ptrdiff_t, ptrdiff_t, size_t, int))
1070 |     dlsym( lib, "shmem_longlong_iget" );
1071 |   if (shmem_longlong_iget_real == NULL && rank == 0)
1072 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_iget in DSOs!!\n");
1074 |   /* Obtain @ for shmem_short_iget */
1075 |   shmem_short_iget_real = 
1076 |     (void (*)(short *, const short *, ptrdiff_t, ptrdiff_t, size_t, int))
1077 |     dlsym( lib, "shmem_short_iget" );
1078 |   if (shmem_short_iget_real == NULL && rank == 0)
1079 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_short_iget in DSOs!!\n");
1081 |   /* Obtain @ for shmem_int_add */
1082 |   shmem_int_add_real = 
1083 |     (void (*)(int *, int, int))
1084 |     dlsym( lib, "shmem_int_add" );
1085 |   if (shmem_int_add_real == NULL && rank == 0)
1086 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_add in DSOs!!\n");
1088 |   /* Obtain @ for shmem_long_add */
1089 |   shmem_long_add_real = 
1090 |     (void (*)(long *, long, int))
1091 |     dlsym( lib, "shmem_long_add" );
1092 |   if (shmem_long_add_real == NULL && rank == 0)
1093 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_add in DSOs!!\n");
1095 |   /* Obtain @ for shmem_longlong_add */
1096 |   shmem_longlong_add_real = 
1097 |     (void (*)(long long *, long long, int))
1098 |     dlsym( lib, "shmem_longlong_add" );
1099 |   if (shmem_longlong_add_real == NULL && rank == 0)
1100 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_add in DSOs!!\n");
1102 |   /* Obtain @ for shmem_int_cswap */
1103 |   shmem_int_cswap_real = 
1104 |     (int (*)(int *, int, int, int))
1105 |     dlsym( lib, "shmem_int_cswap" );
1106 |   if (shmem_int_cswap_real == NULL && rank == 0)
1107 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_cswap in DSOs!!\n");
1109 |   /* Obtain @ for shmem_long_cswap */
1110 |   shmem_long_cswap_real = 
1111 |     (long (*)(long *, long, long, int))
1112 |     dlsym( lib, "shmem_long_cswap" );
1113 |   if (shmem_long_cswap_real == NULL && rank == 0)
1114 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_cswap in DSOs!!\n");
1116 |   /* Obtain @ for shmem_longlong_cswap */
1117 |   shmem_longlong_cswap_real = 
1118 |     (long long (*)(long long *, long long, long long, int))
1119 |     dlsym( lib, "shmem_longlong_cswap" );
1120 |   if (shmem_longlong_cswap_real == NULL && rank == 0)
1121 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_cswap in DSOs!!\n");
1123 |   /* Obtain @ for shmem_double_swap */
1124 |   shmem_double_swap_real = 
1125 |     (double (*)(double *, double, int))
1126 |     dlsym( lib, "shmem_double_swap" );
1127 |   if (shmem_double_swap_real == NULL && rank == 0)
1128 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_double_swap in DSOs!!\n");
1130 |   /* Obtain @ for shmem_float_swap */
1131 |   shmem_float_swap_real = 
1132 |     (float (*)(float *, float, int))
1133 |     dlsym( lib, "shmem_float_swap" );
1134 |   if (shmem_float_swap_real == NULL && rank == 0)
1135 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_float_swap in DSOs!!\n");
1137 |   /* Obtain @ for shmem_int_swap */
1138 |   shmem_int_swap_real = 
1139 |     (int (*)(int *, int, int))
1140 |     dlsym( lib, "shmem_int_swap" );
1141 |   if (shmem_int_swap_real == NULL && rank == 0)
1142 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_swap in DSOs!!\n");
1144 |   /* Obtain @ for shmem_long_swap */
1145 |   shmem_long_swap_real = 
1146 |     (long (*)(long *, long, int))
1147 |     dlsym( lib, "shmem_long_swap" );
1148 |   if (shmem_long_swap_real == NULL && rank == 0)
1149 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_swap in DSOs!!\n");
1151 |   /* Obtain @ for shmem_longlong_swap */
1152 |   shmem_longlong_swap_real = 
1153 |     (long long (*)(long long *, long long, int))
1154 |     dlsym( lib, "shmem_longlong_swap" );
1155 |   if (shmem_longlong_swap_real == NULL && rank == 0)
1156 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_swap in DSOs!!\n");
1158 |   /* Obtain @ for shmem_swap */
1159 |   shmem_swap_real = 
1160 |     (long (*)(long *, long, int))
1161 |     dlsym( lib, "shmem_swap" );
1162 |   if (shmem_swap_real == NULL && rank == 0)
1163 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_swap in DSOs!!\n");
1165 |   /* Obtain @ for shmem_int_finc */
1166 |   shmem_int_finc_real = 
1167 |     (int (*)(int *, int))
1168 |     dlsym( lib, "shmem_int_finc" );
1169 |   if (shmem_int_finc_real == NULL && rank == 0)
1170 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_finc in DSOs!!\n");
1172 |   /* Obtain @ for shmem_long_finc */
1173 |   shmem_long_finc_real = 
1174 |     (long (*)(long *, int))
1175 |     dlsym( lib, "shmem_long_finc" );
1176 |   if (shmem_long_finc_real == NULL && rank == 0)
1177 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_finc in DSOs!!\n");
1179 |   /* Obtain @ for shmem_longlong_finc */
1180 |   shmem_longlong_finc_real = 
1181 |     (long long (*)(long long *, int))
1182 |     dlsym( lib, "shmem_longlong_finc" );
1183 |   if (shmem_longlong_finc_real == NULL && rank == 0)
1184 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_finc in DSOs!!\n");
1186 |   /* Obtain @ for shmem_int_inc */
1187 |   shmem_int_inc_real = 
1188 |     (void (*)(int *, int))
1189 |     dlsym( lib, "shmem_int_inc" );
1190 |   if (shmem_int_inc_real == NULL && rank == 0)
1191 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_inc in DSOs!!\n");
1193 |   /* Obtain @ for shmem_long_inc */
1194 |   shmem_long_inc_real = 
1195 |     (void (*)(long *, int))
1196 |     dlsym( lib, "shmem_long_inc" );
1197 |   if (shmem_long_inc_real == NULL && rank == 0)
1198 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_inc in DSOs!!\n");
1200 |   /* Obtain @ for shmem_longlong_inc */
1201 |   shmem_longlong_inc_real = 
1202 |     (void (*)(long long *, int))
1203 |     dlsym( lib, "shmem_longlong_inc" );
1204 |   if (shmem_longlong_inc_real == NULL && rank == 0)
1205 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_inc in DSOs!!\n");
1207 |   /* Obtain @ for shmem_int_fadd */
1208 |   shmem_int_fadd_real = 
1209 |     (int (*)(int *, int, int))
1210 |     dlsym( lib, "shmem_int_fadd" );
1211 |   if (shmem_int_fadd_real == NULL && rank == 0)
1212 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_fadd in DSOs!!\n");
1214 |   /* Obtain @ for shmem_long_fadd */
1215 |   shmem_long_fadd_real = 
1216 |     (long (*)(long *, long, int))
1217 |     dlsym( lib, "shmem_long_fadd" );
1218 |   if (shmem_long_fadd_real == NULL && rank == 0)
1219 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_fadd in DSOs!!\n");
1221 |   /* Obtain @ for shmem_longlong_fadd */
1222 |   shmem_longlong_fadd_real = 
1223 |     (long long (*)(long long *, long long, int))
1224 |     dlsym( lib, "shmem_longlong_fadd" );
1225 |   if (shmem_longlong_fadd_real == NULL && rank == 0)
1226 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_fadd in DSOs!!\n");
1228 |   /* Obtain @ for shmem_barrier_all */
1229 |   shmem_barrier_all_real = 
1230 |     (void (*)(void))
1231 |     dlsym( lib, "shmem_barrier_all" );
1232 |   if (shmem_barrier_all_real == NULL && rank == 0)
1233 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_barrier_all in DSOs!!\n");
1235 |   /* Obtain @ for shmem_barrier */
1236 |   shmem_barrier_real = 
1237 |     (void (*)(int, int, int, long *))
1238 |     dlsym( lib, "shmem_barrier" );
1239 |   if (shmem_barrier_real == NULL && rank == 0)
1240 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_barrier in DSOs!!\n");
1242 |   /* Obtain @ for shmem_broadcast32 */
1243 |   shmem_broadcast32_real = 
1244 |     (void (*)(void *, const void *, size_t, int, int, int, int, long *))
1245 |     dlsym( lib, "shmem_broadcast32" );
1246 |   if (shmem_broadcast32_real == NULL && rank == 0)
1247 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_broadcast32 in DSOs!!\n");
1249 |   /* Obtain @ for shmem_broadcast64 */
1250 |   shmem_broadcast64_real = 
1251 |     (void (*)(void *, const void *, size_t, int, int, int, int, long *))
1252 |     dlsym( lib, "shmem_broadcast64" );
1253 |   if (shmem_broadcast64_real == NULL && rank == 0)
1254 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_broadcast64 in DSOs!!\n");
1256 |   /* Obtain @ for shmem_collect32 */
1257 |   shmem_collect32_real = 
1258 |     (void (*)(void *, const void *, size_t, int, int, int, long *))
1259 |     dlsym( lib, "shmem_collect32" );
1260 |   if (shmem_collect32_real == NULL && rank == 0)
1261 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_collect32 in DSOs!!\n");
1263 |   /* Obtain @ for shmem_collect64 */
1264 |   shmem_collect64_real = 
1265 |     (void (*)(void *, const void *, size_t, int, int, int, long *))
1266 |     dlsym( lib, "shmem_collect64" );
1267 |   if (shmem_collect64_real == NULL && rank == 0)
1268 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_collect64 in DSOs!!\n");
1270 |   /* Obtain @ for shmem_fcollect32 */
1271 |   shmem_fcollect32_real = 
1272 |     (void (*)(void *, const void *, size_t, int, int, int, long *))
1273 |     dlsym( lib, "shmem_fcollect32" );
1274 |   if (shmem_fcollect32_real == NULL && rank == 0)
1275 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_fcollect32 in DSOs!!\n");
1277 |   /* Obtain @ for shmem_fcollect64 */
1278 |   shmem_fcollect64_real = 
1279 |     (void (*)(void *, const void *, size_t, int, int, int, long *))
1280 |     dlsym( lib, "shmem_fcollect64" );
1281 |   if (shmem_fcollect64_real == NULL && rank == 0)
1282 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_fcollect64 in DSOs!!\n");
1284 |   /* Obtain @ for shmem_int_and_to_all */
1285 |   shmem_int_and_to_all_real = 
1286 |     (void (*)(int *, int *, int, int, int, int, int *, long *))
1287 |     dlsym( lib, "shmem_int_and_to_all" );
1288 |   if (shmem_int_and_to_all_real == NULL && rank == 0)
1289 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_and_to_all in DSOs!!\n");
1291 |   /* Obtain @ for shmem_long_and_to_all */
1292 |   shmem_long_and_to_all_real = 
1293 |     (void (*)(long *, long *, int, int, int, int, long *, long *))
1294 |     dlsym( lib, "shmem_long_and_to_all" );
1295 |   if (shmem_long_and_to_all_real == NULL && rank == 0)
1296 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_and_to_all in DSOs!!\n");
1298 |   /* Obtain @ for shmem_longlong_and_to_all */
1299 |   shmem_longlong_and_to_all_real = 
1300 |     (void (*)(long long *, long long *, int, int, int, int, long long *, long *))
1301 |     dlsym( lib, "shmem_longlong_and_to_all" );
1302 |   if (shmem_longlong_and_to_all_real == NULL && rank == 0)
1303 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_and_to_all in DSOs!!\n");
1305 |   /* Obtain @ for shmem_short_and_to_all */
1306 |   shmem_short_and_to_all_real = 
1307 |     (void (*)(short *, short *, int, int, int, int, short *, long *))
1308 |     dlsym( lib, "shmem_short_and_to_all" );
1309 |   if (shmem_short_and_to_all_real == NULL && rank == 0)
1310 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_short_and_to_all in DSOs!!\n");
1312 |   /* Obtain @ for shmem_double_max_to_all */
1313 |   shmem_double_max_to_all_real = 
1314 |     (void (*)(double *, double *, int, int, int, int, double *, long *))
1315 |     dlsym( lib, "shmem_double_max_to_all" );
1316 |   if (shmem_double_max_to_all_real == NULL && rank == 0)
1317 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_double_max_to_all in DSOs!!\n");
1319 |   /* Obtain @ for shmem_float_max_to_all */
1320 |   shmem_float_max_to_all_real = 
1321 |     (void (*)(float *, float *, int, int, int, int, float *, long *))
1322 |     dlsym( lib, "shmem_float_max_to_all" );
1323 |   if (shmem_float_max_to_all_real == NULL && rank == 0)
1324 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_float_max_to_all in DSOs!!\n");
1326 |   /* Obtain @ for shmem_int_max_to_all */
1327 |   shmem_int_max_to_all_real = 
1328 |     (void (*)(int *, int *, int, int, int, int, int *, long *))
1329 |     dlsym( lib, "shmem_int_max_to_all" );
1330 |   if (shmem_int_max_to_all_real == NULL && rank == 0)
1331 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_max_to_all in DSOs!!\n");
1333 |   /* Obtain @ for shmem_long_max_to_all */
1334 |   shmem_long_max_to_all_real = 
1335 |     (void (*)(long *, long *, int, int, int, int, long *, long *))
1336 |     dlsym( lib, "shmem_long_max_to_all" );
1337 |   if (shmem_long_max_to_all_real == NULL && rank == 0)
1338 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_max_to_all in DSOs!!\n");
1340 |   /* Obtain @ for shmem_longdouble_max_to_all */
1341 |   shmem_longdouble_max_to_all_real = 
1342 |     (void (*)(long double *, long double *, int, int, int, int, long double *, long *))
1343 |     dlsym( lib, "shmem_longdouble_max_to_all" );
1344 |   if (shmem_longdouble_max_to_all_real == NULL && rank == 0)
1345 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longdouble_max_to_all in DSOs!!\n");
1347 |   /* Obtain @ for shmem_longlong_max_to_all */
1348 |   shmem_longlong_max_to_all_real = 
1349 |     (void (*)(long long *, long long *, int, int, int, int, long long *, long *))
1350 |     dlsym( lib, "shmem_longlong_max_to_all" );
1351 |   if (shmem_longlong_max_to_all_real == NULL && rank == 0)
1352 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_max_to_all in DSOs!!\n");
1354 |   /* Obtain @ for shmem_short_max_to_all */
1355 |   shmem_short_max_to_all_real = 
1356 |     (void (*)(short *, short *, int, int, int, int, short *, long *))
1357 |     dlsym( lib, "shmem_short_max_to_all" );
1358 |   if (shmem_short_max_to_all_real == NULL && rank == 0)
1359 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_short_max_to_all in DSOs!!\n");
1361 |   /* Obtain @ for shmem_double_min_to_all */
1362 |   shmem_double_min_to_all_real = 
1363 |     (void (*)(double *, double *, int, int, int, int, double *, long *))
1364 |     dlsym( lib, "shmem_double_min_to_all" );
1365 |   if (shmem_double_min_to_all_real == NULL && rank == 0)
1366 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_double_min_to_all in DSOs!!\n");
1368 |   /* Obtain @ for shmem_int_wait */
1369 |   shmem_int_wait_real = 
1370 |     (void (*)(int *, int))
1371 |     dlsym( lib, "shmem_int_wait" );
1372 |   if (shmem_int_wait_real == NULL && rank == 0)
1373 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_wait in DSOs!!\n");
1375 |   /* Obtain @ for shmem_int_wait_until */
1376 |   shmem_int_wait_until_real = 
1377 |     (void (*)(int *, int, int))
1378 |     dlsym( lib, "shmem_int_wait_until" );
1379 |   if (shmem_int_wait_until_real == NULL && rank == 0)
1380 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_int_wait_until in DSOs!!\n");
1382 |   /* Obtain @ for shmem_long_wait */
1383 |   shmem_long_wait_real = 
1384 |     (void (*)(long *, long))
1385 |     dlsym( lib, "shmem_long_wait" );
1386 |   if (shmem_long_wait_real == NULL && rank == 0)
1387 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_wait in DSOs!!\n");
1389 |   /* Obtain @ for shmem_long_wait_until */
1390 |   shmem_long_wait_until_real = 
1391 |     (void (*)(long *, int, long))
1392 |     dlsym( lib, "shmem_long_wait_until" );
1393 |   if (shmem_long_wait_until_real == NULL && rank == 0)
1394 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_long_wait_until in DSOs!!\n");
1396 |   /* Obtain @ for shmem_longlong_wait */
1397 |   shmem_longlong_wait_real = 
1398 |     (void (*)(long long *, long long))
1399 |     dlsym( lib, "shmem_longlong_wait" );
1400 |   if (shmem_longlong_wait_real == NULL && rank == 0)
1401 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_wait in DSOs!!\n");
1403 |   /* Obtain @ for shmem_longlong_wait_until */
1404 |   shmem_longlong_wait_until_real = 
1405 |     (void (*)(long long *, int, long long))
1406 |     dlsym( lib, "shmem_longlong_wait_until" );
1407 |   if (shmem_longlong_wait_until_real == NULL && rank == 0)
1408 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_longlong_wait_until in DSOs!!\n");
1410 |   /* Obtain @ for shmem_short_wait */
1411 |   shmem_short_wait_real = 
1412 |     (void (*)(short *, short))
1413 |     dlsym( lib, "shmem_short_wait" );
1414 |   if (shmem_short_wait_real == NULL && rank == 0)
1415 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_short_wait in DSOs!!\n");
1417 |   /* Obtain @ for shmem_short_wait_until */
1418 |   shmem_short_wait_until_real = 
1419 |     (void (*)(short *, int, short))
1420 |     dlsym( lib, "shmem_short_wait_until" );
1421 |   if (shmem_short_wait_until_real == NULL && rank == 0)
1422 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_short_wait_until in DSOs!!\n");
1424 |   /* Obtain @ for shmem_wait */
1425 |   shmem_wait_real = 
1426 |     (void (*)(long *, long))
1427 |     dlsym( lib, "shmem_wait" );
1428 |   if (shmem_wait_real == NULL && rank == 0)
1429 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_wait in DSOs!!\n");
1431 |   /* Obtain @ for shmem_wait_until */
1432 |   shmem_wait_until_real = 
1433 |     (void (*)(long *, int, long))
1434 |     dlsym( lib, "shmem_wait_until" );
1435 |   if (shmem_wait_until_real == NULL && rank == 0)
1436 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_wait_until in DSOs!!\n");
1438 |   /* Obtain @ for shmem_fence */
1439 |   shmem_fence_real = 
1440 |     (void (*)(void))
1441 |     dlsym( lib, "shmem_fence" );
1442 |   if (shmem_fence_real == NULL && rank == 0)
1443 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_fence in DSOs!!\n");
1445 |   /* Obtain @ for shmem_quiet */
1446 |   shmem_quiet_real = 
1447 |     (void (*)(void))
1448 |     dlsym( lib, "shmem_quiet" );
1449 |   if (shmem_quiet_real == NULL && rank == 0)
1450 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_quiet in DSOs!!\n");
1452 |   /* Obtain @ for shmem_clear_lock */
1453 |   shmem_clear_lock_real = 
1454 |     (void (*)(long *))
1455 |     dlsym( lib, "shmem_clear_lock" );
1456 |   if (shmem_clear_lock_real == NULL && rank == 0)
1457 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_clear_lock in DSOs!!\n");
1459 |   /* Obtain @ for shmem_set_lock */
1460 |   shmem_set_lock_real = 
1461 |     (void (*)(long *))
1462 |     dlsym( lib, "shmem_set_lock" );
1463 |   if (shmem_set_lock_real == NULL && rank == 0)
1464 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_set_lock in DSOs!!\n");
1466 |   /* Obtain @ for shmem_test_lock */
1467 |   shmem_test_lock_real = 
1468 |     (int (*)(long *))
1469 |     dlsym( lib, "shmem_test_lock" );
1470 |   if (shmem_test_lock_real == NULL && rank == 0)
1471 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_test_lock in DSOs!!\n");
1473 |   /* Obtain @ for shmem_clear_cache_inv */
1474 |   shmem_clear_cache_inv_real = 
1475 |     (void (*)(void))
1476 |     dlsym( lib, "shmem_clear_cache_inv" );
1477 |   if (shmem_clear_cache_inv_real == NULL && rank == 0)
1478 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_clear_cache_inv in DSOs!!\n");
1480 |   /* Obtain @ for shmem_set_cache_inv */
1481 |   shmem_set_cache_inv_real = 
1482 |     (void (*)(void))
1483 |     dlsym( lib, "shmem_set_cache_inv" );
1484 |   if (shmem_set_cache_inv_real == NULL && rank == 0)
1485 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_set_cache_inv in DSOs!!\n");
1487 |   /* Obtain @ for shmem_clear_cache_line_inv */
1488 |   shmem_clear_cache_line_inv_real = 
1489 |     (void (*)(void *))
1490 |     dlsym( lib, "shmem_clear_cache_line_inv" );
1491 |   if (shmem_clear_cache_line_inv_real == NULL && rank == 0)
1492 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_clear_cache_line_inv in DSOs!!\n");
1494 |   /* Obtain @ for shmem_set_cache_line_inv */
1495 |   shmem_set_cache_line_inv_real = 
1496 |     (void (*)(void *))
1497 |     dlsym( lib, "shmem_set_cache_line_inv" );
1498 |   if (shmem_set_cache_line_inv_real == NULL && rank == 0)
1499 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_set_cache_line_inv in DSOs!!\n");
1501 |   /* Obtain @ for shmem_udcflush */
1502 |   shmem_udcflush_real = 
1503 |     (void (*)(void))
1504 |     dlsym( lib, "shmem_udcflush" );
1505 |   if (shmem_udcflush_real == NULL && rank == 0)
1506 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_udcflush in DSOs!!\n");
1508 |   /* Obtain @ for shmem_udcflush_line */
1509 |   shmem_udcflush_line_real = 
1510 |     (void (*)(void *))
1511 |     dlsym( lib, "shmem_udcflush_line" );
1512 |   if (shmem_udcflush_line_real == NULL && rank == 0)
1513 |     fprintf(stderr, PACKAGE_NAME": Unable to find shmem_udcflush_line in DSOs!!\n");
{% endraw %}

```
### src/tracer/wrappers/OMP/omp_wrapper.c

```c

{% raw %}
74 | #if defined(PIC)
75 | 	/* Obtain @ for omp_set_lock */
76 | 	omp_get_thread_num_real =
77 | 		(int(*)(void)) dlsym (RTLD_NEXT, "omp_get_thread_num");
78 | 
79 | 	/* Obtain @ for omp_set_lock */
80 | 	omp_set_lock_real =
81 | 		(void(*)(void*)) dlsym (RTLD_NEXT, "omp_set_lock");
82 | 
83 | 	/* Obtain @ for omp_unset_lock */
84 | 	omp_unset_lock_real =
85 | 		(void(*)(void*)) dlsym (RTLD_NEXT, "omp_unset_lock");
86 | 
87 | 	/* Obtain @ for omp_set_num_threads */
88 | 	omp_set_num_threads_real =
89 | 		(void(*)(int)) dlsym (RTLD_NEXT, "omp_set_num_threads");
90 | #endif /* PIC */
91 | }
{% endraw %}

```
### src/tracer/wrappers/OMP/ibm-xlsmp-1.6.c

```c

{% raw %}
224 | 	/* Obtain @ for _xlsmpParallelDoSetup_TPO */
225 | 	_xlsmpParallelDoSetup_TPO_real =
226 | 		(void(*)(int,void**,long,long,long,long,void**,void**,void**,long,long,void**,long))
227 | 		dlsym (RTLD_NEXT, "_xlsmpParallelDoSetup_TPO");
228 | 	INC_IF_NOT_NULL(_xlsmpParallelDoSetup_TPO_real,count);
229 | 
230 | 	/* Obtain @ for _xlsmpParRegionSetup_TPO */
231 | 	_xlsmpParRegionSetup_TPO_real =
232 | 		(void(*)(int,void*,int,void*,void*,void**,long,long))
233 | 		dlsym (RTLD_NEXT, "_xlsmpParRegionSetup_TPO");
234 | 	INC_IF_NOT_NULL(_xlsmpParRegionSetup_TPO_real,count);
235 | 
236 | 	/* Obtain @ for _xlsmpWSDoSetup_TPO */
237 | 	_xlsmpWSDoSetup_TPO_real =
238 | 		(void(*)(int,void*,long,long,long,long,void*,void*,void**,long))
239 | 		dlsym (RTLD_NEXT, "_xlsmpWSDoSetup_TPO");
240 | 	INC_IF_NOT_NULL(_xlsmpWSDoSetup_TPO_real,count);
241 | 
242 | 	/* Obtain @ for _xlsmpWSSectSetup_TPO */
243 | 	_xlsmpWSSectSetup_TPO_real =
244 | 		(void(*)(int,void*,long,void*,void*,void**,long,long))
245 | 		dlsym (RTLD_NEXT, "_xlsmpWSSectSetup_TPO");
246 | 	INC_IF_NOT_NULL(_xlsmpWSSectSetup_TPO_real,count);
247 | 
248 | 	/* Obtain @ for _xlsmpSingleSetup_TPO */
249 | 	_xlsmpSingleSetup_TPO_real =
250 | 		(void(*)(int,void*,int,void*)) dlsym (RTLD_NEXT, "_xlsmpSingleSetup_TPO");
251 | 	INC_IF_NOT_NULL(_xlsmpSingleSetup_TPO_real,count);
252 | 
253 | 	/* Obtain @ for _xlsmpBarrier_TPO */
254 | 	_xlsmpBarrier_TPO_real =
255 | 		(void(*)(int,int*)) dlsym (RTLD_NEXT, "_xlsmpBarrier_TPO");
256 | 	INC_IF_NOT_NULL(_xlsmpBarrier_TPO_real,count);
257 | 
258 | 	/* Obtain @ for _xlsmpGetDefaultSLock */
259 | 	_xlsmpGetDefaultSLock_real =
260 | 		(void(*)(void*)) dlsym (RTLD_NEXT, "_xlsmpGetDefaultSLock");
261 | 	INC_IF_NOT_NULL(_xlsmpGetDefaultSLock_real,count);
262 | 
263 | 	/* Obtain @ for _xlsmpRelDefaultSLock */
264 | 	_xlsmpRelDefaultSLock_real =
265 | 		(void(*)(void*)) dlsym (RTLD_NEXT, "_xlsmpRelDefaultSLock");
266 | 	INC_IF_NOT_NULL(_xlsmpRelDefaultSLock_real,count);
267 | 
268 | 	/* Obtain @ for _xlsmpGetSLock */
269 | 	_xlsmpGetSLock_real =
270 | 		(void(*)(void*)) dlsym (RTLD_NEXT, "_xlsmpGetSLock");
271 | 	INC_IF_NOT_NULL(_xlsmpGetSLock_real,count);
272 | 
273 | 	/* Obtain @ for _xlsmpRelSLock */
274 | 	_xlsmpRelSLock_real =
275 | 		(void(*)(void*)) dlsym (RTLD_NEXT, "_xlsmpRelSLock");
276 | 	INC_IF_NOT_NULL(_xlsmpRelSLock_real,count);
277 | 
{% endraw %}

```
### src/tracer/wrappers/OMP/intel-kmpc-11.c

```c

{% raw %}
102 | 		/* Obtain @ for __kmpc_fork_call */
103 | 		__kmpc_fork_call_real =
104 | 			(void(*)(void*,int,void*,...))
105 | 			dlsym (RTLD_NEXT, "__kmpc_fork_call");
106 | 		INC_IF_NOT_NULL(__kmpc_fork_call_real,count);
107 | 	}
109 | 	/* Obtain @ for __kmpc_barrier */
110 | 	__kmpc_barrier_real =
111 | 		(void(*)(void*,int))
112 | 		dlsym (RTLD_NEXT, "__kmpc_barrier");
113 | 	INC_IF_NOT_NULL(__kmpc_barrier_real,count);
114 | 
115 | 	/* Obtain @ for __kmpc_critical */
116 | 	__kmpc_critical_real =
117 | 		(void(*)(void*,int,void*))
118 | 		dlsym (RTLD_NEXT, "__kmpc_critical");
119 | 	INC_IF_NOT_NULL(__kmpc_critical_real,count);
120 | 
121 | 	/* Obtain @ for __kmpc_end_critical */
122 | 	__kmpc_end_critical_real =
123 | 		(void(*)(void*,int,void*))
124 | 		dlsym (RTLD_NEXT, "__kmpc_end_critical");
125 | 	INC_IF_NOT_NULL(__kmpc_end_critical_real,count);
126 | 
127 | 	/* Obtain @ for __kmpc_dispatch_next_4 */
128 | 	__kmpc_dispatch_next_4_real =
129 | 		(int(*)(void*,int,int*,int*,int*,int*))
130 | 		dlsym (RTLD_NEXT, "__kmpc_dispatch_next_4");
131 | 	INC_IF_NOT_NULL(__kmpc_dispatch_next_4_real,count);
132 | 
133 | 	/* Obtain @ for __kmpc_dispatch_next_8 */
134 | 	__kmpc_dispatch_next_8_real =
135 | 		(int(*)(void*,int,int*,long long *,long long *, long long *))
136 | 		dlsym (RTLD_NEXT, "__kmpc_dispatch_next_8");
137 | 	INC_IF_NOT_NULL(__kmpc_dispatch_next_8_real,count);
138 | 
139 | 	/* Obtain @ for __kmpc_dispatch_next_8 */
140 | 	__kmpc_single_real =
141 | 		(int(*)(void*,int)) dlsym (RTLD_NEXT, "__kmpc_single");
142 | 	INC_IF_NOT_NULL(__kmpc_single_real,count);
143 | 
144 | 	/* Obtain @ for __kmpc_dispatch_next_8 */
145 | 	__kmpc_end_single_real =
146 | 		(void(*)(void*,int)) dlsym (RTLD_NEXT, "__kmpc_end_single");
147 | 	INC_IF_NOT_NULL(__kmpc_end_single_real,count);
148 | 
149 | 	/* Obtain @ for __kmpc_dispatch_init_4 */
150 | 	__kmpc_dispatch_init_4_real =
151 | 		(void(*)(void*,int,int,int,int,int,int)) dlsym (RTLD_NEXT, "__kmpc_dispatch_init_4");
152 | 	INC_IF_NOT_NULL(__kmpc_dispatch_init_4_real,count);
153 | 
154 | 	/* Obtain @ for __kmpc_dispatch_init_8 */
155 | 	__kmpc_dispatch_init_8_real =
156 | 		(void(*)(void*,int,int,long long,long long,long long,long long)) dlsym (RTLD_NEXT, "__kmpc_dispatch_init_8");
157 | 	INC_IF_NOT_NULL(__kmpc_dispatch_init_8_real,count);
158 | 
159 | 	/* Obtain @ for __kmpc_dispatch_fini_4 */
160 | 	__kmpc_dispatch_fini_4_real =
161 | 		(void(*)(void*,int)) dlsym (RTLD_NEXT, "__kmpc_dispatch_fini_4");
162 | 	INC_IF_NOT_NULL(__kmpc_dispatch_fini_4_real,count);
163 | 
164 | 	/* Obtain @ for __kmpc_dispatch_fini_8 */
165 | 	__kmpc_dispatch_fini_8_real =
166 | 		(void(*)(void*,long long)) dlsym (RTLD_NEXT, "__kmpc_dispatch_fini_8");
167 | 	INC_IF_NOT_NULL(__kmpc_dispatch_fini_8_real,count);
168 | 
169 | 	/* Obtain @ for __kmpc_omp_task_alloc */
170 | 	__kmpc_omp_task_alloc_real =
171 | 		(void*(*)(void*,int,int,size_t,size_t,void*)) dlsym (RTLD_NEXT, "__kmpc_omp_task_alloc");
172 | 	INC_IF_NOT_NULL(__kmpc_omp_task_alloc_real, count);
173 | 
174 | 	/* Obtain @ for __kmpc_omp_task_begin_if0 */
175 | 	__kmpc_omp_task_begin_if0_real =
176 | 		(void(*)(void*,int,void*)) dlsym (RTLD_NEXT, "__kmpc_omp_task_begin_if0");
177 | 	INC_IF_NOT_NULL(__kmpc_omp_task_begin_if0_real, count);
178 | 
179 | 	/* Obtain @ for __kmpc_omp_task_complete_if0 */
180 | 	__kmpc_omp_task_complete_if0_real =
181 | 		(void(*)(void*,int,void*)) dlsym (RTLD_NEXT, "__kmpc_omp_task_complete_if0");
182 | 	INC_IF_NOT_NULL(__kmpc_omp_task_complete_if0_real, count);
183 | 
184 | 	/* Obtain @ for __kmpc_omp_taskwait */
185 | 	__kmpc_omp_taskwait_real = (int(*)(void*,int)) dlsym (RTLD_NEXT, "__kmpc_omp_taskwait");
186 | 	INC_IF_NOT_NULL(__kmpc_omp_taskwait_real, count);
187 | 
188 | 	/* Obtain @ for ompc_set_num_threads */
189 | 	ompc_set_num_threads_real =
190 | 		(void(*)(int)) dlsym (RTLD_NEXT, "ompc_set_num_threads");
191 | 	INC_IF_NOT_NULL(ompc_set_num_threads_real, count);
192 | 
{% endraw %}

```
### src/tracer/wrappers/OMP/gnu-libgomp-4.9.c

```c

{% raw %}
210 | 
211 | 	/* Obtain @ for GOMP_parallel */
212 | 	GOMP_parallel_real =
213 | 		(void(*)(void*,void*,unsigned,unsigned)) dlsym (RTLD_NEXT, "GOMP_parallel");
214 | 	INC_IF_NOT_NULL(GOMP_parallel_start_real,count);
215 | 
216 | 	/* Obtain @ for GOMP_parallel_start */
217 | 	GOMP_parallel_start_real =
218 | 		(void(*)(void*,void*,unsigned)) dlsym (RTLD_NEXT, "GOMP_parallel_start");
219 | 	INC_IF_NOT_NULL(GOMP_parallel_start_real,count);
220 | 
221 | 	/* Obtain @ for GOMP_parallel_end */
222 | 	GOMP_parallel_end_real =
223 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_parallel_end");
224 | 	INC_IF_NOT_NULL(GOMP_parallel_end_real,count);
225 | 
226 | 	/* Obtain @ for GOMP_barrier */
227 | 	GOMP_barrier_real =
228 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_barrier");
229 | 	INC_IF_NOT_NULL(GOMP_barrier_real,count);
230 | 
231 | 	/* Obtain @ for GOMP_atomic_start */
232 | 	GOMP_atomic_start_real =
233 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_atomic_start");
234 | 	INC_IF_NOT_NULL(GOMP_atomic_start_real,count);
235 | 
236 | 	/* Obtain @ for GOMP_atomic_end */
237 | 	GOMP_atomic_end_real =
238 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_atomic_end");
239 | 	INC_IF_NOT_NULL(GOMP_atomic_end_real,count);
240 | 
241 | 	/* Obtain @ for GOMP_critical_enter */
242 | 	GOMP_critical_start_real =
243 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_critical_start");
244 | 	INC_IF_NOT_NULL(GOMP_critical_start_real,count);
245 | 
246 | 	/* Obtain @ for GOMP_critical_end */
247 | 	GOMP_critical_end_real =
248 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_critical_end");
249 | 	INC_IF_NOT_NULL(GOMP_critical_end_real,count);
250 | 
251 | 	/* Obtain @ for GOMP_critical_name_start */
252 | 	GOMP_critical_name_start_real =
253 | 		(void(*)(void**)) dlsym (RTLD_NEXT, "GOMP_critical_name_start");
254 | 	INC_IF_NOT_NULL(GOMP_critical_name_start_real,count);
255 | 
256 | 	/* Obtain @ for GOMP_critical_name_end */
257 | 	GOMP_critical_name_end_real =
258 | 		(void(*)(void**)) dlsym (RTLD_NEXT, "GOMP_critical_name_end");
259 | 	INC_IF_NOT_NULL(GOMP_critical_name_end_real,count);
260 | 
261 | 	/* Obtain @ for GOMP_parallel_loop_static_start */
262 | 	GOMP_parallel_loop_static_start_real =
263 | 		(void(*)(void*,void*,unsigned, long, long, long, long)) dlsym (RTLD_NEXT, "GOMP_parallel_loop_static_start");
264 | 	INC_IF_NOT_NULL(GOMP_parallel_loop_static_start_real,count);
265 | 
266 | 	/* Obtain @ for GOMP_parallel_loop_runtime_start */
267 | 	GOMP_parallel_loop_runtime_start_real =
268 | 		(void(*)(void*,void*,unsigned, long, long, long, long)) dlsym (RTLD_NEXT, "GOMP_parallel_loop_runtime_start");
269 | 	INC_IF_NOT_NULL(GOMP_parallel_loop_runtime_start_real,count);
270 | 
271 | 	/* Obtain @ for GOMP_parallel_loop_guided_start */
272 | 	GOMP_parallel_loop_guided_start_real =
273 | 		(void(*)(void*,void*,unsigned, long, long, long, long)) dlsym (RTLD_NEXT, "GOMP_parallel_loop_guided_start");
274 | 	INC_IF_NOT_NULL(GOMP_parallel_loop_guided_start_real,count);
275 | 
276 | 	/* Obtain @ for GOMP_parallel_loop_dynamic_start */
277 | 	GOMP_parallel_loop_dynamic_start_real =
278 | 		(void(*)(void*,void*,unsigned, long, long, long, long)) dlsym (RTLD_NEXT, "GOMP_parallel_loop_dynamic_start");
279 | 	INC_IF_NOT_NULL(GOMP_parallel_loop_dynamic_start_real,count);
280 | 
281 | 	/* Obtain @ for GOMP_loop_static_next */
282 | 	GOMP_loop_static_next_real =
283 | 		(int(*)(long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_static_next");
284 | 	INC_IF_NOT_NULL(GOMP_loop_static_next_real,count);
285 | 
286 | 	/* Obtain @ for GOMP_loop_runtime_next */
287 | 	GOMP_loop_runtime_next_real =
288 | 		(int(*)(long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_runtime_next");
289 | 	INC_IF_NOT_NULL(GOMP_loop_runtime_next_real,count);
290 | 
291 | 	/* Obtain @ for GOMP_loop_guided_next */
292 | 	GOMP_loop_guided_next_real =
293 | 		(int(*)(long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_guided_next");
294 | 	INC_IF_NOT_NULL(GOMP_loop_guided_next_real,count);
295 | 
296 | 	/* Obtain @ for GOMP_loop_dynamic_next */
297 | 	GOMP_loop_dynamic_next_real =
298 | 		(int(*)(long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_dynamic_next");
299 | 	INC_IF_NOT_NULL(GOMP_loop_dynamic_next_real,count);
300 | 
301 | 	/* Obtain @ for GOMP_loop_static_start */
302 | 	GOMP_loop_static_start_real =
303 | 		(int(*)(long,long,long,long,long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_static_start");
304 | 	INC_IF_NOT_NULL(GOMP_loop_static_start_real,count);
305 | 
306 | 	/* Obtain @ for GOMP_loop_runtime_start */
307 | 	GOMP_loop_runtime_start_real =
308 | 		(int(*)(long,long,long,long,long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_runtime_start");
309 | 	INC_IF_NOT_NULL(GOMP_loop_runtime_start_real,count);
310 | 
311 | 	/* Obtain @ for GOMP_loop_guided_start */
312 | 	GOMP_loop_guided_start_real =
313 | 		(int(*)(long,long,long,long,long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_guided_start");
314 | 	INC_IF_NOT_NULL(GOMP_loop_guided_start_real,count);
315 | 
316 | 	/* Obtain @ for GOMP_loop_dynamic_start */
317 | 	GOMP_loop_dynamic_start_real =
318 | 		(int(*)(long,long,long,long,long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_dynamic_start");
319 | 	INC_IF_NOT_NULL(GOMP_loop_dynamic_start_real,count);
320 | 
321 | 	/* Obtain @ for GOMP_loop_end */
322 | 	GOMP_loop_end_real =
323 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_loop_end");
324 | 	INC_IF_NOT_NULL(GOMP_loop_end_real,count);
325 | 
326 | 	/* Obtain @ for GOMP_loop_end_nowait */
327 | 	GOMP_loop_end_nowait_real =
328 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_loop_end_nowait");
329 | 	INC_IF_NOT_NULL(GOMP_loop_end_nowait_real,count);
330 | 
331 | 	/* Obtain @ for GOMP_sections_end */
332 | 	GOMP_sections_end_real =
333 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_sections_end");
334 | 	INC_IF_NOT_NULL(GOMP_sections_end_real,count);
335 | 
336 | 	/* Obtain @ for GOMP_sections_end_nowait */
337 | 	GOMP_sections_end_nowait_real =
338 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_sections_end_nowait");
339 | 	INC_IF_NOT_NULL(GOMP_sections_end_nowait_real,count);
340 | 
341 | 	/* Obtain @ for GOMP_sections_start */
342 | 	GOMP_sections_start_real =
343 | 		(unsigned(*)(unsigned)) dlsym (RTLD_NEXT, "GOMP_sections_start");
344 | 	INC_IF_NOT_NULL(GOMP_sections_start_real,count);
345 | 
346 | 	/* Obtain @ for GOMP_sections_next */
347 | 	GOMP_sections_next_real =
348 | 		(unsigned(*)(void)) dlsym (RTLD_NEXT, "GOMP_sections_next");
349 | 	INC_IF_NOT_NULL(GOMP_sections_next_real,count);
350 | 
351 | 	/* Obtain @ for GOMP_parallel_sections_start */
352 | 	GOMP_parallel_sections_start_real = 
353 | 		(void(*)(void*,void*,unsigned,unsigned)) dlsym (RTLD_NEXT, "GOMP_parallel_sections_start");
354 | 	INC_IF_NOT_NULL(GOMP_parallel_sections_start_real,count);
355 | 
356 | 	/* Obtain @ for GOMP_task */
357 | 	GOMP_task_real =
358 | 		(void(*)(void*,void*,void*,long,long,int,unsigned,void**)) dlsym (RTLD_NEXT, "GOMP_task");
359 | 	INC_IF_NOT_NULL(GOMP_task_real,count);
360 | 
361 | 	/* Obtain @ for GOMP_taskwait */
362 | 	GOMP_taskwait_real = (void(*)(void)) dlsym (RTLD_NEXT, "GOMP_taskwait");
363 | 	INC_IF_NOT_NULL(GOMP_taskwait_real,count);
364 | 
365 | 	/* Obtain @ for GOMP_taskgroup_start */
366 | 	GOMP_taskgroup_start_real = (void(*)(void)) dlsym (RTLD_NEXT, "GOMP_taskgroup_start");
367 | 	INC_IF_NOT_NULL(GOMP_taskgroup_start_real,count);
368 | 
369 | 	/* Obtain @ for GOMP_taskgroup_end */
370 | 	GOMP_taskgroup_end_real = (void(*)(void)) dlsym (RTLD_NEXT, "GOMP_taskgroup_end");
371 | 	INC_IF_NOT_NULL(GOMP_taskgroup_end_real,count);
372 | 
373 | 	/* Obtain @ for GOMP_loop_ordered_static_start */
374 | 	GOMP_loop_ordered_static_start_real = 
375 | 		(int(*)(long, long, long, long, long *, long *)) dlsym (RTLD_NEXT, "GOMP_loop_ordered_static_start");
376 | 	INC_IF_NOT_NULL(GOMP_loop_ordered_static_start_real, count);
377 | 
378 | 	/* Obtain @ for GOMP_loop_ordered_runtime_start */
379 | 	GOMP_loop_ordered_runtime_start_real = 
380 | 		(int(*)(long, long, long, long, long *, long *)) dlsym (RTLD_NEXT, "GOMP_loop_ordered_runtime_start");
381 | 	INC_IF_NOT_NULL(GOMP_loop_ordered_runtime_start_real, count);
382 | 
383 | 	/* Obtain @ for GOMP_loop_ordered_dynamic_start */
384 | 	GOMP_loop_ordered_dynamic_start_real = 
385 | 		(int(*)(long, long, long, long, long *, long *)) dlsym (RTLD_NEXT, "GOMP_loop_ordered_dynamic_start");
386 | 	INC_IF_NOT_NULL(GOMP_loop_ordered_dynamic_start_real, count);
387 | 
388 | 	/* Obtain @ for GOMP_loop_ordered_guided_start */
389 | 	GOMP_loop_ordered_guided_start_real = 
390 | 		(int(*)(long, long, long, long, long *, long *)) dlsym (RTLD_NEXT, "GOMP_loop_ordered_guided_start");
391 | 	INC_IF_NOT_NULL(GOMP_loop_ordered_guided_start_real, count);
392 | 
393 | #if 0
394 | 	/* Obtain @ for GOMP_ordered_start */
395 | 	GOMP_ordered_start_real = (void(*)(void)) dlsym (RTLD_NEXT, "GOMP_ordered_start");
396 | 	INC_IF_NOT_NULL(GOMP_ordered_start_real,count);
397 | 	
398 | 	/* Obtain @ for GOMP_ordered_end */
399 | 	GOMP_ordered_end_real = (void(*)(void)) dlsym (RTLD_NEXT, "GOMP_ordered_end");
400 | 	INC_IF_NOT_NULL(GOMP_ordered_end_real,count);
401 | #endif
{% endraw %}

```
### src/tracer/wrappers/OMP/gnu-libgomp-4.2.c

```c

{% raw %}
208 | 
209 | 	/* Obtain @ for GOMP_parallel */
210 | 	GOMP_parallel_real =
211 | 		(void(*)(void*,void*,unsigned,unsigned)) dlsym (RTLD_NEXT, "GOMP_parallel");
212 | 	INC_IF_NOT_NULL(GOMP_parallel_start_real,count);
213 | 
214 | 	/* Obtain @ for GOMP_parallel_start */
215 | 	GOMP_parallel_start_real =
216 | 		(void(*)(void*,void*,unsigned)) dlsym (RTLD_NEXT, "GOMP_parallel_start");
217 | 	INC_IF_NOT_NULL(GOMP_parallel_start_real,count);
218 | 
219 | 	/* Obtain @ for GOMP_parallel_end */
220 | 	GOMP_parallel_end_real =
221 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_parallel_end");
222 | 	INC_IF_NOT_NULL(GOMP_parallel_end_real,count);
223 | 
224 | 	/* Obtain @ for GOMP_barrier */
225 | 	GOMP_barrier_real =
226 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_barrier");
227 | 	INC_IF_NOT_NULL(GOMP_barrier_real,count);
228 | 
229 | 	/* Obtain @ for GOMP_atomic_start */
230 | 	GOMP_atomic_start_real =
231 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_atomic_start");
232 | 	INC_IF_NOT_NULL(GOMP_atomic_start_real,count);
233 | 
234 | 	/* Obtain @ for GOMP_atomic_end */
235 | 	GOMP_atomic_end_real =
236 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_atomic_end");
237 | 	INC_IF_NOT_NULL(GOMP_atomic_end_real,count);
238 | 
239 | 	/* Obtain @ for GOMP_critical_enter */
240 | 	GOMP_critical_start_real =
241 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_critical_start");
242 | 	INC_IF_NOT_NULL(GOMP_critical_start_real,count);
243 | 
244 | 	/* Obtain @ for GOMP_critical_end */
245 | 	GOMP_critical_end_real =
246 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_critical_end");
247 | 	INC_IF_NOT_NULL(GOMP_critical_end_real,count);
248 | 
249 | 	/* Obtain @ for GOMP_critical_name_start */
250 | 	GOMP_critical_name_start_real =
251 | 		(void(*)(void**)) dlsym (RTLD_NEXT, "GOMP_critical_name_start");
252 | 	INC_IF_NOT_NULL(GOMP_critical_name_start_real,count);
253 | 
254 | 	/* Obtain @ for GOMP_critical_name_end */
255 | 	GOMP_critical_name_end_real =
256 | 		(void(*)(void**)) dlsym (RTLD_NEXT, "GOMP_critical_name_end");
257 | 	INC_IF_NOT_NULL(GOMP_critical_name_end_real,count);
258 | 
259 | 	/* Obtain @ for GOMP_parallel_loop_static_start */
260 | 	GOMP_parallel_loop_static_start_real =
261 | 		(void(*)(void*,void*,unsigned, long, long, long, long)) dlsym (RTLD_NEXT, "GOMP_parallel_loop_static_start");
262 | 	INC_IF_NOT_NULL(GOMP_parallel_loop_static_start_real,count);
263 | 
264 | 	/* Obtain @ for GOMP_parallel_loop_runtime_start */
265 | 	GOMP_parallel_loop_runtime_start_real =
266 | 		(void(*)(void*,void*,unsigned, long, long, long, long)) dlsym (RTLD_NEXT, "GOMP_parallel_loop_runtime_start");
267 | 	INC_IF_NOT_NULL(GOMP_parallel_loop_runtime_start_real,count);
268 | 
269 | 	/* Obtain @ for GOMP_parallel_loop_guided_start */
270 | 	GOMP_parallel_loop_guided_start_real =
271 | 		(void(*)(void*,void*,unsigned, long, long, long, long)) dlsym (RTLD_NEXT, "GOMP_parallel_loop_guided_start");
272 | 	INC_IF_NOT_NULL(GOMP_parallel_loop_guided_start_real,count);
273 | 
274 | 	/* Obtain @ for GOMP_parallel_loop_dynamic_start */
275 | 	GOMP_parallel_loop_dynamic_start_real =
276 | 		(void(*)(void*,void*,unsigned, long, long, long, long)) dlsym (RTLD_NEXT, "GOMP_parallel_loop_dynamic_start");
277 | 	INC_IF_NOT_NULL(GOMP_parallel_loop_dynamic_start_real,count);
278 | 
279 | 	/* Obtain @ for GOMP_loop_static_next */
280 | 	GOMP_loop_static_next_real =
281 | 		(int(*)(long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_static_next");
282 | 	INC_IF_NOT_NULL(GOMP_loop_static_next_real,count);
283 | 
284 | 	/* Obtain @ for GOMP_loop_runtime_next */
285 | 	GOMP_loop_runtime_next_real =
286 | 		(int(*)(long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_runtime_next");
287 | 	INC_IF_NOT_NULL(GOMP_loop_runtime_next_real,count);
288 | 
289 | 	/* Obtain @ for GOMP_loop_guided_next */
290 | 	GOMP_loop_guided_next_real =
291 | 		(int(*)(long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_guided_next");
292 | 	INC_IF_NOT_NULL(GOMP_loop_guided_next_real,count);
293 | 
294 | 	/* Obtain @ for GOMP_loop_dynamic_next */
295 | 	GOMP_loop_dynamic_next_real =
296 | 		(int(*)(long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_dynamic_next");
297 | 	INC_IF_NOT_NULL(GOMP_loop_dynamic_next_real,count);
298 | 
299 | 	/* Obtain @ for GOMP_loop_static_start */
300 | 	GOMP_loop_static_start_real =
301 | 		(int(*)(long,long,long,long,long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_static_start");
302 | 	INC_IF_NOT_NULL(GOMP_loop_static_start_real,count);
303 | 
304 | 	/* Obtain @ for GOMP_loop_runtime_start */
305 | 	GOMP_loop_runtime_start_real =
306 | 		(int(*)(long,long,long,long,long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_runtime_start");
307 | 	INC_IF_NOT_NULL(GOMP_loop_runtime_start_real,count);
308 | 
309 | 	/* Obtain @ for GOMP_loop_guided_start */
310 | 	GOMP_loop_guided_start_real =
311 | 		(int(*)(long,long,long,long,long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_guided_start");
312 | 	INC_IF_NOT_NULL(GOMP_loop_guided_start_real,count);
313 | 
314 | 	/* Obtain @ for GOMP_loop_dynamic_start */
315 | 	GOMP_loop_dynamic_start_real =
316 | 		(int(*)(long,long,long,long,long*,long*)) dlsym (RTLD_NEXT, "GOMP_loop_dynamic_start");
317 | 	INC_IF_NOT_NULL(GOMP_loop_dynamic_start_real,count);
318 | 
319 | 	/* Obtain @ for GOMP_loop_end */
320 | 	GOMP_loop_end_real =
321 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_loop_end");
322 | 	INC_IF_NOT_NULL(GOMP_loop_end_real,count);
323 | 
324 | 	/* Obtain @ for GOMP_loop_end_nowait */
325 | 	GOMP_loop_end_nowait_real =
326 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_loop_end_nowait");
327 | 	INC_IF_NOT_NULL(GOMP_loop_end_nowait_real,count);
328 | 
329 | 	/* Obtain @ for GOMP_sections_end */
330 | 	GOMP_sections_end_real =
331 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_sections_end");
332 | 	INC_IF_NOT_NULL(GOMP_sections_end_real,count);
333 | 
334 | 	/* Obtain @ for GOMP_sections_end_nowait */
335 | 	GOMP_sections_end_nowait_real =
336 | 		(void(*)(void)) dlsym (RTLD_NEXT, "GOMP_sections_end_nowait");
337 | 	INC_IF_NOT_NULL(GOMP_sections_end_nowait_real,count);
338 | 
339 | 	/* Obtain @ for GOMP_sections_start */
340 | 	GOMP_sections_start_real =
341 | 		(unsigned(*)(unsigned)) dlsym (RTLD_NEXT, "GOMP_sections_start");
342 | 	INC_IF_NOT_NULL(GOMP_sections_start_real,count);
343 | 
344 | 	/* Obtain @ for GOMP_sections_next */
345 | 	GOMP_sections_next_real =
346 | 		(unsigned(*)(void)) dlsym (RTLD_NEXT, "GOMP_sections_next");
347 | 	INC_IF_NOT_NULL(GOMP_sections_next_real,count);
348 | 
349 | 	/* Obtain @ for GOMP_parallel_sections_start */
350 | 	GOMP_parallel_sections_start_real = 
351 | 		(void(*)(void*,void*,unsigned,unsigned)) dlsym (RTLD_NEXT, "GOMP_parallel_sections_start");
352 | 	INC_IF_NOT_NULL(GOMP_parallel_sections_start_real,count);
353 | 
354 | 	/* Obtain @ for GOMP_task */
355 | 	GOMP_task_real =
356 | 		(void(*)(void*,void*,void*,long,long,int,unsigned)) dlsym (RTLD_NEXT, "GOMP_task");
357 | 	INC_IF_NOT_NULL(GOMP_task_real,count);
358 | 
359 | 	/* Obtain @ for GOMP_taskwait */
360 | 	GOMP_taskwait_real = (void(*)(void)) dlsym (RTLD_NEXT, "GOMP_taskwait");
361 | 	INC_IF_NOT_NULL(GOMP_taskwait_real,count);
362 | 
363 | 	/* Obtain @ for GOMP_loop_ordered_static_start */
364 | 	GOMP_loop_ordered_static_start_real = 
365 | 		(int(*)(long, long, long, long, long *, long *)) dlsym (RTLD_NEXT, "GOMP_loop_ordered_static_start");
366 | 	INC_IF_NOT_NULL(GOMP_loop_ordered_static_start_real, count);
367 | 
368 | 	/* Obtain @ for GOMP_loop_ordered_runtime_start */
369 | 	GOMP_loop_ordered_runtime_start_real = 
370 | 		(int(*)(long, long, long, long, long *, long *)) dlsym (RTLD_NEXT, "GOMP_loop_ordered_runtime_start");
371 | 	INC_IF_NOT_NULL(GOMP_loop_ordered_runtime_start_real, count);
372 | 
373 | 	/* Obtain @ for GOMP_loop_ordered_dynamic_start */
374 | 	GOMP_loop_ordered_dynamic_start_real = 
375 | 		(int(*)(long, long, long, long, long *, long *)) dlsym (RTLD_NEXT, "GOMP_loop_ordered_dynamic_start");
376 | 	INC_IF_NOT_NULL(GOMP_loop_ordered_dynamic_start_real, count);
377 | 
378 | 	/* Obtain @ for GOMP_loop_ordered_guided_start */
379 | 	GOMP_loop_ordered_guided_start_real = 
380 | 		(int(*)(long, long, long, long, long *, long *)) dlsym (RTLD_NEXT, "GOMP_loop_ordered_guided_start");
381 | 	INC_IF_NOT_NULL(GOMP_loop_ordered_guided_start_real, count);
382 | 
383 | #if 0
384 | 	/* Obtain @ for GOMP_ordered_start */
385 | 	GOMP_ordered_start_real = (void(*)(void)) dlsym (RTLD_NEXT, "GOMP_ordered_start");
386 | 	INC_IF_NOT_NULL(GOMP_ordered_start_real,count);
387 | 	
388 | 	/* Obtain @ for GOMP_ordered_end */
389 | 	GOMP_ordered_end_real = (void(*)(void)) dlsym (RTLD_NEXT, "GOMP_ordered_end");
390 | 	INC_IF_NOT_NULL(GOMP_ordered_end_real,count);
391 | #endif
{% endraw %}

```
### src/tracer/wrappers/MALLOC/malloc_wrapper.c

```c

{% raw %}
70 | void Extrae_malloctrace_init (void)
71 | {
72 | # if defined(PIC) /* This is only available for .so libraries */
73 | 	real_free = (void(*)(void*)) dlsym (RTLD_NEXT, "free");
74 | 	real_malloc = (void*(*)(size_t)) dlsym (RTLD_NEXT, "malloc");
75 | 	/* real_calloc = (void*(*)(size_t, size_t)) dlsym (RTLD_NEXT, "calloc"); */
76 | 	real_realloc = (void*(*)(void*, size_t)) dlsym (RTLD_NEXT, "realloc");
77 | 	real_posix_memalign = (int(*)(void **, size_t, size_t)) dlsym (RTLD_NEXT, "posix_memalign");
78 | 	
79 | #  if HAVE_MEMKIND
80 | 	real_memkind_malloc = (void*(*)(memkind_t, size_t)) dlsym (RTLD_NEXT, "memkind_malloc");
81 | 	real_memkind_calloc = (void*(*)(memkind_t, size_t, size_t)) dlsym (RTLD_NEXT, "memkind_calloc");
82 | 	real_memkind_realloc = (void*(*)(memkind_t, void *, size_t)) dlsym (RTLD_NEXT, "memkind_realloc");
83 | 	real_memkind_posix_memalign = (int(*)(memkind_t, void **, size_t, size_t)) dlsym (RTLD_NEXT, "memkind_posix_memalign");
84 | 	real_memkind_free = (void(*)(memkind_t, void *)) dlsym (RTLD_NEXT, "memkind_free");
85 | #  endif
86 | # else
{% endraw %}

```