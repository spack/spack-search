---
name: "esmf"
layout: package
next_package: extrae
previous_package: erlang
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['python', 'c']
---
## 8.0.1
7 / 3654 files match, 6 filtered matches.

 - [src/Infrastructure/Trace/preload/preload_io.C](#srcinfrastructuretracepreloadpreload_ioc)
 - [src/Infrastructure/Trace/preload/preload_mpi.C](#srcinfrastructuretracepreloadpreload_mpic)
 - [src/Infrastructure/Trace/preload/gen_wrappers_mpi.py](#srcinfrastructuretracepreloadgen_wrappers_mpipy)
 - [src/Infrastructure/Trace/src/ESMCI_Trace.C](#srcinfrastructuretracesrcesmci_tracec)
 - [src/Superstructure/Component/src/ESMCI_MethodTable.C](#srcsuperstructurecomponentsrcesmci_methodtablec)
 - [src/Superstructure/Component/src/ESMCI_FTable.C](#srcsuperstructurecomponentsrcesmci_ftablec)

### src/Infrastructure/Trace/preload/preload_io.C

```c

{% raw %}
38 |   static ssize_t (*__real_ptr_write)(int fildes, const void *buf, size_t nbyte) = NULL;  
39 |   ssize_t __real_write(int fd, const void *buf, size_t nbytes) {   
40 |     if (__real_ptr_write == NULL) {
41 |       __real_ptr_write = (ssize_t (*)(int, const void *, size_t)) dlsym(RTLD_NEXT, "write");
42 |     }
43 |     return __real_ptr_write(fd, buf, nbytes);
51 |   static ssize_t (*__real_ptr_writev)(int fd, const struct iovec *iov, int iovcnt) = NULL;
52 |   ssize_t __real_writev(int fd, const struct iovec *iov, int iovcnt) {
53 |     if (__real_ptr_writev == NULL) {
54 |       __real_ptr_writev = (ssize_t (*)(int, const struct iovec *, int)) dlsym(RTLD_NEXT, "writev");
55 |     }
56 |     return __real_ptr_writev(fd, iov, iovcnt);
64 |   static ssize_t (*__real_ptr_pwrite)(int fd, const void *buf, size_t nbytes, off_t offset) = NULL;
65 |   ssize_t __real_pwrite(int fd, const void *buf, size_t nbytes, off_t offset) {
66 |     if (__real_ptr_pwrite == NULL) {
67 |       __real_ptr_pwrite = (ssize_t (*)(int, const void *, size_t, off_t)) dlsym(RTLD_NEXT, "pwrite");
68 |     }
69 |     return __real_ptr_pwrite(fd, buf, nbytes, offset);
77 |   static ssize_t (*__real_ptr_read)(int fd, void *buf, size_t nbytes) = NULL;
78 |   ssize_t __real_read(int fd, void *buf, size_t nbytes) {
79 |     if (__real_ptr_read == NULL) {
80 |       __real_ptr_read = (ssize_t (*)(int, void *, size_t)) dlsym(RTLD_NEXT, "read");
81 |     }
82 |     return __real_ptr_read(fd, buf, nbytes);
91 |   static int (*__real_ptr_open)(const char *path, int oflag, ...) = NULL;
92 |   int __real_open(const char *path, int oflag, ...) {
93 |     if (__real_ptr_open == NULL) {
94 |       __real_ptr_open = (int (*) (const char *, int, ...)) dlsym(RTLD_NEXT, "open");
95 |     }
96 |     
{% endraw %}

```
### src/Infrastructure/Trace/preload/preload_mpi.C

```c

{% raw %}
44 | 
45 |     int __real_MPI_Allgather(ESMF_MPI_CONST void *sendbuf, int  sendcount, MPI_Datatype sendtype, void *recvbuf, int recvcount, MPI_Datatype recvtype, MPI_Comm comm) {
46 |       if (__real_ptr_MPI_Allgather == NULL) {
47 |         __real_ptr_MPI_Allgather = (int (*)(ESMF_MPI_CONST void *sendbuf, int  sendcount, MPI_Datatype sendtype, void *recvbuf, int recvcount, MPI_Datatype recvtype, MPI_Comm comm)) dlsym(RTLD_NEXT, "MPI_Allgather");
48 |       }
49 |       return __real_ptr_MPI_Allgather(sendbuf, sendcount, sendtype, recvbuf, recvcount, recvtype, comm);
58 | 
59 |     int __real_MPI_Allgatherv(ESMF_MPI_CONST void *sendbuf, int sendcount, MPI_Datatype sendtype, void *recvbuf, ESMF_MPI_CONST int recvcounts[], ESMF_MPI_CONST int displs[], MPI_Datatype recvtype, MPI_Comm comm) {
60 |       if (__real_ptr_MPI_Allgatherv == NULL) {
61 |         __real_ptr_MPI_Allgatherv = (int (*)(ESMF_MPI_CONST void *sendbuf, int sendcount, MPI_Datatype sendtype, void *recvbuf, ESMF_MPI_CONST int recvcounts[], ESMF_MPI_CONST int displs[], MPI_Datatype recvtype, MPI_Comm comm)) dlsym(RTLD_NEXT, "MPI_Allgatherv");
62 |       }
63 |       return __real_ptr_MPI_Allgatherv(sendbuf, sendcount, sendtype, recvbuf, recvcounts, displs, recvtype, comm);
72 | 
73 |     int __real_MPI_Allreduce(ESMF_MPI_CONST void *sendbuf, void *recvbuf, int count, MPI_Datatype datatype, MPI_Op op, MPI_Comm comm) {
74 |       if (__real_ptr_MPI_Allreduce == NULL) {
75 |         __real_ptr_MPI_Allreduce = (int (*)(ESMF_MPI_CONST void *sendbuf, void *recvbuf, int count, MPI_Datatype datatype, MPI_Op op, MPI_Comm comm)) dlsym(RTLD_NEXT, "MPI_Allreduce");
76 |       }
77 |       return __real_ptr_MPI_Allreduce(sendbuf, recvbuf, count, datatype, op, comm);
86 | 
87 |     int __real_MPI_Alltoall(ESMF_MPI_CONST void *sendbuf, int sendcount, MPI_Datatype sendtype, void *recvbuf, int recvcount, MPI_Datatype recvtype, MPI_Comm comm) {
88 |       if (__real_ptr_MPI_Alltoall == NULL) {
89 |         __real_ptr_MPI_Alltoall = (int (*)(ESMF_MPI_CONST void *sendbuf, int sendcount, MPI_Datatype sendtype, void *recvbuf, int recvcount, MPI_Datatype recvtype, MPI_Comm comm)) dlsym(RTLD_NEXT, "MPI_Alltoall");
90 |       }
91 |       return __real_ptr_MPI_Alltoall(sendbuf, sendcount, sendtype, recvbuf, recvcount, recvtype, comm);
100 | 
101 |     int __real_MPI_Alltoallv(ESMF_MPI_CONST void *sendbuf, ESMF_MPI_CONST int sendcounts[], ESMF_MPI_CONST int sdispls[], MPI_Datatype sendtype, void *recvbuf, ESMF_MPI_CONST int recvcounts[], ESMF_MPI_CONST int rdispls[], MPI_Datatype recvtype, MPI_Comm comm) {
102 |       if (__real_ptr_MPI_Alltoallv == NULL) {
103 |         __real_ptr_MPI_Alltoallv = (int (*)(ESMF_MPI_CONST void *sendbuf, ESMF_MPI_CONST int sendcounts[], ESMF_MPI_CONST int sdispls[], MPI_Datatype sendtype, void *recvbuf, ESMF_MPI_CONST int recvcounts[], ESMF_MPI_CONST int rdispls[], MPI_Datatype recvtype, MPI_Comm comm)) dlsym(RTLD_NEXT, "MPI_Alltoallv");
104 |       }
105 |       return __real_ptr_MPI_Alltoallv(sendbuf, sendcounts, sdispls, sendtype, recvbuf, recvcounts, rdispls, recvtype, comm);
114 | 
115 |     int __real_MPI_Alltoallw(ESMF_MPI_CONST void *sendbuf, ESMF_MPI_CONST int sendcounts[], ESMF_MPI_CONST int sdispls[], ESMF_MPI_CONST MPI_Datatype sendtypes[], void *recvbuf, ESMF_MPI_CONST int recvcounts[], ESMF_MPI_CONST int rdispls[], ESMF_MPI_CONST MPI_Datatype recvtypes[], MPI_Comm comm) {
116 |       if (__real_ptr_MPI_Alltoallw == NULL) {
117 |         __real_ptr_MPI_Alltoallw = (int (*)(ESMF_MPI_CONST void *sendbuf, ESMF_MPI_CONST int sendcounts[], ESMF_MPI_CONST int sdispls[], ESMF_MPI_CONST MPI_Datatype sendtypes[], void *recvbuf, ESMF_MPI_CONST int recvcounts[], ESMF_MPI_CONST int rdispls[], ESMF_MPI_CONST MPI_Datatype recvtypes[], MPI_Comm comm)) dlsym(RTLD_NEXT, "MPI_Alltoallw");
118 |       }
119 |       return __real_ptr_MPI_Alltoallw(sendbuf, sendcounts, sdispls, sendtypes, recvbuf, recvcounts, rdispls, recvtypes, comm);
128 | 
129 |     int __real_MPI_Barrier(MPI_Comm comm) {
130 |       if (__real_ptr_MPI_Barrier == NULL) {
131 |         __real_ptr_MPI_Barrier = (int (*)(MPI_Comm comm)) dlsym(RTLD_NEXT, "MPI_Barrier");
132 |       }
133 |       return __real_ptr_MPI_Barrier(comm);
142 | 
143 |     int __real_MPI_Bcast(void *buffer, int count, MPI_Datatype datatype, int root, MPI_Comm comm) {
144 |       if (__real_ptr_MPI_Bcast == NULL) {
145 |         __real_ptr_MPI_Bcast = (int (*)(void *buffer, int count, MPI_Datatype datatype, int root, MPI_Comm comm)) dlsym(RTLD_NEXT, "MPI_Bcast");
146 |       }
147 |       return __real_ptr_MPI_Bcast(buffer, count, datatype, root, comm);
156 | 
157 |     int __real_MPI_Gather(ESMF_MPI_CONST void *sendbuf, int sendcount, MPI_Datatype sendtype, void *recvbuf, int recvcount, MPI_Datatype recvtype, int root, MPI_Comm comm) {
158 |       if (__real_ptr_MPI_Gather == NULL) {
159 |         __real_ptr_MPI_Gather = (int (*)(ESMF_MPI_CONST void *sendbuf, int sendcount, MPI_Datatype sendtype, void *recvbuf, int recvcount, MPI_Datatype recvtype, int root, MPI_Comm comm)) dlsym(RTLD_NEXT, "MPI_Gather");
160 |       }
161 |       return __real_ptr_MPI_Gather(sendbuf, sendcount, sendtype, recvbuf, recvcount, recvtype, root, comm);
170 | 
171 |     int __real_MPI_Gatherv(ESMF_MPI_CONST void *sendbuf, int sendcount, MPI_Datatype sendtype, void *recvbuf, ESMF_MPI_CONST int recvcounts[], ESMF_MPI_CONST int displs[], MPI_Datatype recvtype, int root, MPI_Comm comm) {
172 |       if (__real_ptr_MPI_Gatherv == NULL) {
173 |         __real_ptr_MPI_Gatherv = (int (*)(ESMF_MPI_CONST void *sendbuf, int sendcount, MPI_Datatype sendtype, void *recvbuf, ESMF_MPI_CONST int recvcounts[], ESMF_MPI_CONST int displs[], MPI_Datatype recvtype, int root, MPI_Comm comm)) dlsym(RTLD_NEXT, "MPI_Gatherv");
174 |       }
175 |       return __real_ptr_MPI_Gatherv(sendbuf, sendcount, sendtype, recvbuf, recvcounts, displs, recvtype, root, comm);
184 | 
185 |     int __real_MPI_Recv(void *buf, int count, MPI_Datatype datatype, int source, int tag, MPI_Comm comm, MPI_Status *status) {
186 |       if (__real_ptr_MPI_Recv == NULL) {
187 |         __real_ptr_MPI_Recv = (int (*)(void *buf, int count, MPI_Datatype datatype, int source, int tag, MPI_Comm comm, MPI_Status *status)) dlsym(RTLD_NEXT, "MPI_Recv");
188 |       }
189 |       return __real_ptr_MPI_Recv(buf, count, datatype, source, tag, comm, status);
198 | 
199 |     int __real_MPI_Reduce(ESMF_MPI_CONST void *sendbuf, void *recvbuf, int count, MPI_Datatype datatype, MPI_Op op, int root, MPI_Comm comm) {
200 |       if (__real_ptr_MPI_Reduce == NULL) {
201 |         __real_ptr_MPI_Reduce = (int (*)(ESMF_MPI_CONST void *sendbuf, void *recvbuf, int count, MPI_Datatype datatype, MPI_Op op, int root, MPI_Comm comm)) dlsym(RTLD_NEXT, "MPI_Reduce");
202 |       }
203 |       return __real_ptr_MPI_Reduce(sendbuf, recvbuf, count, datatype, op, root, comm);
212 | 
213 |     int __real_MPI_Scatter(ESMF_MPI_CONST void *sendbuf, int sendcount, MPI_Datatype sendtype, void *recvbuf, int recvcount, MPI_Datatype recvtype, int root, MPI_Comm comm) {
214 |       if (__real_ptr_MPI_Scatter == NULL) {
215 |         __real_ptr_MPI_Scatter = (int (*)(ESMF_MPI_CONST void *sendbuf, int sendcount, MPI_Datatype sendtype, void *recvbuf, int recvcount, MPI_Datatype recvtype, int root, MPI_Comm comm)) dlsym(RTLD_NEXT, "MPI_Scatter");
216 |       }
217 |       return __real_ptr_MPI_Scatter(sendbuf, sendcount, sendtype, recvbuf, recvcount, recvtype, root, comm);
226 | 
227 |     int __real_MPI_Send(ESMF_MPI_CONST void *buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm) {
228 |       if (__real_ptr_MPI_Send == NULL) {
229 |         __real_ptr_MPI_Send = (int (*)(ESMF_MPI_CONST void *buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm)) dlsym(RTLD_NEXT, "MPI_Send");
230 |       }
231 |       return __real_ptr_MPI_Send(buf, count, datatype, dest, tag, comm);
240 | 
241 |     int __real_MPI_Sendrecv(ESMF_MPI_CONST void *sendbuf, int sendcount, MPI_Datatype sendtype, int dest, int sendtag, void *recvbuf, int recvcount, MPI_Datatype recvtype, int source, int recvtag, MPI_Comm comm, MPI_Status *status) {
242 |       if (__real_ptr_MPI_Sendrecv == NULL) {
243 |         __real_ptr_MPI_Sendrecv = (int (*)(ESMF_MPI_CONST void *sendbuf, int sendcount, MPI_Datatype sendtype, int dest, int sendtag, void *recvbuf, int recvcount, MPI_Datatype recvtype, int source, int recvtag, MPI_Comm comm, MPI_Status *status)) dlsym(RTLD_NEXT, "MPI_Sendrecv");
244 |       }
245 |       return __real_ptr_MPI_Sendrecv(sendbuf, sendcount, sendtype, dest, sendtag, recvbuf, recvcount, recvtype, source, recvtag, comm, status);
254 | 
255 |     int __real_MPI_Wait(MPI_Request *request, MPI_Status *status) {
256 |       if (__real_ptr_MPI_Wait == NULL) {
257 |         __real_ptr_MPI_Wait = (int (*)(MPI_Request *request, MPI_Status *status)) dlsym(RTLD_NEXT, "MPI_Wait");
258 |       }
259 |       return __real_ptr_MPI_Wait(request, status);
268 | 
269 |     int __real_MPI_Waitall(int count, MPI_Request array_of_requests[], MPI_Status *array_of_statuses) {
270 |       if (__real_ptr_MPI_Waitall == NULL) {
271 |         __real_ptr_MPI_Waitall = (int (*)(int count, MPI_Request array_of_requests[], MPI_Status *array_of_statuses)) dlsym(RTLD_NEXT, "MPI_Waitall");
272 |       }
273 |       return __real_ptr_MPI_Waitall(count, array_of_requests, array_of_statuses);
282 | 
283 |     int __real_MPI_Waitany(int count, MPI_Request array_of_requests[], int *index, MPI_Status *status) {
284 |       if (__real_ptr_MPI_Waitany == NULL) {
285 |         __real_ptr_MPI_Waitany = (int (*)(int count, MPI_Request array_of_requests[], int *index, MPI_Status *status)) dlsym(RTLD_NEXT, "MPI_Waitany");
286 |       }
287 |       return __real_ptr_MPI_Waitany(count, array_of_requests, index, status);
296 | 
297 |     int __real_MPI_Waitsome(int incount, MPI_Request array_of_requests[], int *outcount, int array_of_indices[], MPI_Status array_of_statuses[]) {
298 |       if (__real_ptr_MPI_Waitsome == NULL) {
299 |         __real_ptr_MPI_Waitsome = (int (*)(int incount, MPI_Request array_of_requests[], int *outcount, int array_of_indices[], MPI_Status array_of_statuses[])) dlsym(RTLD_NEXT, "MPI_Waitsome");
300 |       }
301 |       return __real_ptr_MPI_Waitsome(incount, array_of_requests, outcount, array_of_indices, array_of_statuses);
316 | 
317 |     void FTN_X(__real_mpi_allgather)(MPI_Fint *sendbuf, MPI_Fint *sendcount, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcount, MPI_Fint *recvtype, MPI_Fint *comm, MPI_Fint *ierr) {
318 |       if (FTN_X(__real_ptr_mpi_allgather) == NULL) {
319 |         FTN_X(__real_ptr_mpi_allgather) = (void (*)(MPI_Fint *sendbuf, MPI_Fint *sendcount, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcount, MPI_Fint *recvtype, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_allgather)));
320 |       }
321 |       FTN_X(__real_ptr_mpi_allgather)(sendbuf, sendcount, sendtype, recvbuf, recvcount, recvtype, comm, ierr);
330 | 
331 |     void FTN_X(__real_mpi_allgatherv)(MPI_Fint *sendbuf, MPI_Fint *sendcount, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcount, MPI_Fint *displs, MPI_Fint *recvtype, MPI_Fint *comm, MPI_Fint *ierr) {
332 |       if (FTN_X(__real_ptr_mpi_allgatherv) == NULL) {
333 |         FTN_X(__real_ptr_mpi_allgatherv) = (void (*)(MPI_Fint *sendbuf, MPI_Fint *sendcount, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcount, MPI_Fint *displs, MPI_Fint *recvtype, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_allgatherv)));
334 |       }
335 |       FTN_X(__real_ptr_mpi_allgatherv)(sendbuf, sendcount, sendtype, recvbuf, recvcount, displs, recvtype, comm, ierr);
344 | 
345 |     void FTN_X(__real_mpi_allreduce)(MPI_Fint *sendbuf, MPI_Fint *recvbuf, MPI_Fint *count, MPI_Fint *datatype, MPI_Fint *op, MPI_Fint *comm, MPI_Fint *ierr) {
346 |       if (FTN_X(__real_ptr_mpi_allreduce) == NULL) {
347 |         FTN_X(__real_ptr_mpi_allreduce) = (void (*)(MPI_Fint *sendbuf, MPI_Fint *recvbuf, MPI_Fint *count, MPI_Fint *datatype, MPI_Fint *op, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_allreduce)));
348 |       }
349 |       FTN_X(__real_ptr_mpi_allreduce)(sendbuf, recvbuf, count, datatype, op, comm, ierr);
358 | 
359 |     void FTN_X(__real_mpi_alltoall)(MPI_Fint *sendbuf, MPI_Fint *sendcount, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcount, MPI_Fint *recvtype, MPI_Fint *comm, MPI_Fint *ierr) {
360 |       if (FTN_X(__real_ptr_mpi_alltoall) == NULL) {
361 |         FTN_X(__real_ptr_mpi_alltoall) = (void (*)(MPI_Fint *sendbuf, MPI_Fint *sendcount, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcount, MPI_Fint *recvtype, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_alltoall)));
362 |       }
363 |       FTN_X(__real_ptr_mpi_alltoall)(sendbuf, sendcount, sendtype, recvbuf, recvcount, recvtype, comm, ierr);
372 | 
373 |     void FTN_X(__real_mpi_alltoallv)(MPI_Fint *sendbuf, MPI_Fint *sendcounts, MPI_Fint *sdispls, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcounts, MPI_Fint *rdispls, MPI_Fint *recvtype, MPI_Fint *comm, MPI_Fint *ierr) {
374 |       if (FTN_X(__real_ptr_mpi_alltoallv) == NULL) {
375 |         FTN_X(__real_ptr_mpi_alltoallv) = (void (*)(MPI_Fint *sendbuf, MPI_Fint *sendcounts, MPI_Fint *sdispls, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcounts, MPI_Fint *rdispls, MPI_Fint *recvtype, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_alltoallv)));
376 |       }
377 |       FTN_X(__real_ptr_mpi_alltoallv)(sendbuf, sendcounts, sdispls, sendtype, recvbuf, recvcounts, rdispls, recvtype, comm, ierr);
386 | 
387 |     void FTN_X(__real_mpi_alltoallw)(MPI_Fint *sendbuf, MPI_Fint *sendcounts, MPI_Fint *sdispls, MPI_Fint *sendtypes, MPI_Fint *recvbuf, MPI_Fint *recvcounts, MPI_Fint *rdispls, MPI_Fint *recvtypes, MPI_Fint *comm, MPI_Fint *ierr) {
388 |       if (FTN_X(__real_ptr_mpi_alltoallw) == NULL) {
389 |         FTN_X(__real_ptr_mpi_alltoallw) = (void (*)(MPI_Fint *sendbuf, MPI_Fint *sendcounts, MPI_Fint *sdispls, MPI_Fint *sendtypes, MPI_Fint *recvbuf, MPI_Fint *recvcounts, MPI_Fint *rdispls, MPI_Fint *recvtypes, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_alltoallw)));
390 |       }
391 |       FTN_X(__real_ptr_mpi_alltoallw)(sendbuf, sendcounts, sdispls, sendtypes, recvbuf, recvcounts, rdispls, recvtypes, comm, ierr);
400 | 
401 |     void FTN_X(__real_mpi_barrier)(MPI_Fint *comm, MPI_Fint *ierr) {
402 |       if (FTN_X(__real_ptr_mpi_barrier) == NULL) {
403 |         FTN_X(__real_ptr_mpi_barrier) = (void (*)(MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_barrier)));
404 |       }
405 |       FTN_X(__real_ptr_mpi_barrier)(comm, ierr);
414 | 
415 |     void FTN_X(__real_mpi_bcast)(MPI_Fint *buffer, MPI_Fint *count, MPI_Fint *datatype, MPI_Fint *root, MPI_Fint *comm, MPI_Fint *ierr) {
416 |       if (FTN_X(__real_ptr_mpi_bcast) == NULL) {
417 |         FTN_X(__real_ptr_mpi_bcast) = (void (*)(MPI_Fint *buffer, MPI_Fint *count, MPI_Fint *datatype, MPI_Fint *root, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_bcast)));
418 |       }
419 |       FTN_X(__real_ptr_mpi_bcast)(buffer, count, datatype, root, comm, ierr);
428 | 
429 |     void FTN_X(__real_mpi_exscan)(MPI_Fint *sendbuf, MPI_Fint *recvbuf, MPI_Fint *count, MPI_Fint *datatype, MPI_Fint *op, MPI_Fint *comm, MPI_Fint *ierr) {
430 |       if (FTN_X(__real_ptr_mpi_exscan) == NULL) {
431 |         FTN_X(__real_ptr_mpi_exscan) = (void (*)(MPI_Fint *sendbuf, MPI_Fint *recvbuf, MPI_Fint *count, MPI_Fint *datatype, MPI_Fint *op, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_exscan)));
432 |       }
433 |       FTN_X(__real_ptr_mpi_exscan)(sendbuf, recvbuf, count, datatype, op, comm, ierr);
442 | 
443 |     void FTN_X(__real_mpi_gather)(MPI_Fint *sendbuf, MPI_Fint *sendcount, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcount, MPI_Fint *recvtype, MPI_Fint *root, MPI_Fint *comm, MPI_Fint *ierr) {
444 |       if (FTN_X(__real_ptr_mpi_gather) == NULL) {
445 |         FTN_X(__real_ptr_mpi_gather) = (void (*)(MPI_Fint *sendbuf, MPI_Fint *sendcount, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcount, MPI_Fint *recvtype, MPI_Fint *root, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_gather)));
446 |       }
447 |       FTN_X(__real_ptr_mpi_gather)(sendbuf, sendcount, sendtype, recvbuf, recvcount, recvtype, root, comm, ierr);
456 | 
457 |     void FTN_X(__real_mpi_gatherv)(MPI_Fint *sendbuf, MPI_Fint *sendcount, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcounts, MPI_Fint *displs, MPI_Fint *recvtype, MPI_Fint *root, MPI_Fint *comm, MPI_Fint *ierr) {
458 |       if (FTN_X(__real_ptr_mpi_gatherv) == NULL) {
459 |         FTN_X(__real_ptr_mpi_gatherv) = (void (*)(MPI_Fint *sendbuf, MPI_Fint *sendcount, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcounts, MPI_Fint *displs, MPI_Fint *recvtype, MPI_Fint *root, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_gatherv)));
460 |       }
461 |       FTN_X(__real_ptr_mpi_gatherv)(sendbuf, sendcount, sendtype, recvbuf, recvcounts, displs, recvtype, root, comm, ierr);
470 | 
471 |     void FTN_X(__real_mpi_recv)(MPI_Fint *buf, MPI_Fint *count, MPI_Fint *datatype, MPI_Fint *source, MPI_Fint *tag, MPI_Fint *comm, MPI_Fint *status, MPI_Fint *ierr) {
472 |       if (FTN_X(__real_ptr_mpi_recv) == NULL) {
473 |         FTN_X(__real_ptr_mpi_recv) = (void (*)(MPI_Fint *buf, MPI_Fint *count, MPI_Fint *datatype, MPI_Fint *source, MPI_Fint *tag, MPI_Fint *comm, MPI_Fint *status, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_recv)));
474 |       }
475 |       FTN_X(__real_ptr_mpi_recv)(buf, count, datatype, source, tag, comm, status, ierr);
484 | 
485 |     void FTN_X(__real_mpi_reduce)(MPI_Fint *sendbuf, MPI_Fint *recvbuf, MPI_Fint *count, MPI_Fint *datatype, MPI_Fint *op, MPI_Fint *root, MPI_Fint *comm, MPI_Fint *ierr) {
486 |       if (FTN_X(__real_ptr_mpi_reduce) == NULL) {
487 |         FTN_X(__real_ptr_mpi_reduce) = (void (*)(MPI_Fint *sendbuf, MPI_Fint *recvbuf, MPI_Fint *count, MPI_Fint *datatype, MPI_Fint *op, MPI_Fint *root, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_reduce)));
488 |       }
489 |       FTN_X(__real_ptr_mpi_reduce)(sendbuf, recvbuf, count, datatype, op, root, comm, ierr);
498 | 
499 |     void FTN_X(__real_mpi_reduce_scatter)(MPI_Fint *sendbuf, MPI_Fint *recvbuf, MPI_Fint *recvcounts, MPI_Fint *datatype, MPI_Fint *op, MPI_Fint *comm, MPI_Fint *ierr) {
500 |       if (FTN_X(__real_ptr_mpi_reduce_scatter) == NULL) {
501 |         FTN_X(__real_ptr_mpi_reduce_scatter) = (void (*)(MPI_Fint *sendbuf, MPI_Fint *recvbuf, MPI_Fint *recvcounts, MPI_Fint *datatype, MPI_Fint *op, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_reduce_scatter)));
502 |       }
503 |       FTN_X(__real_ptr_mpi_reduce_scatter)(sendbuf, recvbuf, recvcounts, datatype, op, comm, ierr);
512 | 
513 |     void FTN_X(__real_mpi_scatter)(MPI_Fint *sendbuf, MPI_Fint *sendcount, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcount, MPI_Fint *recvtype, MPI_Fint *root, MPI_Fint *comm, MPI_Fint *ierr) {
514 |       if (FTN_X(__real_ptr_mpi_scatter) == NULL) {
515 |         FTN_X(__real_ptr_mpi_scatter) = (void (*)(MPI_Fint *sendbuf, MPI_Fint *sendcount, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcount, MPI_Fint *recvtype, MPI_Fint *root, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_scatter)));
516 |       }
517 |       FTN_X(__real_ptr_mpi_scatter)(sendbuf, sendcount, sendtype, recvbuf, recvcount, recvtype, root, comm, ierr);
526 | 
527 |     void FTN_X(__real_mpi_scatterv)(MPI_Fint *sendbuf, MPI_Fint *sendcounts, MPI_Fint *displs, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcount, MPI_Fint *recvtype, MPI_Fint *root, MPI_Fint *comm, MPI_Fint *ierr) {
528 |       if (FTN_X(__real_ptr_mpi_scatterv) == NULL) {
529 |         FTN_X(__real_ptr_mpi_scatterv) = (void (*)(MPI_Fint *sendbuf, MPI_Fint *sendcounts, MPI_Fint *displs, MPI_Fint *sendtype, MPI_Fint *recvbuf, MPI_Fint *recvcount, MPI_Fint *recvtype, MPI_Fint *root, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_scatterv)));
530 |       }
531 |       FTN_X(__real_ptr_mpi_scatterv)(sendbuf, sendcounts, displs, sendtype, recvbuf, recvcount, recvtype, root, comm, ierr);
540 | 
541 |     void FTN_X(__real_mpi_scan)(MPI_Fint *sendbuf, MPI_Fint *recvbuf, MPI_Fint *count, MPI_Fint *datatype, MPI_Fint *op, MPI_Fint *comm, MPI_Fint *ierr) {
542 |       if (FTN_X(__real_ptr_mpi_scan) == NULL) {
543 |         FTN_X(__real_ptr_mpi_scan) = (void (*)(MPI_Fint *sendbuf, MPI_Fint *recvbuf, MPI_Fint *count, MPI_Fint *datatype, MPI_Fint *op, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_scan)));
544 |       }
545 |       FTN_X(__real_ptr_mpi_scan)(sendbuf, recvbuf, count, datatype, op, comm, ierr);
554 | 
555 |     void FTN_X(__real_mpi_send)(MPI_Fint *buf, MPI_Fint *count, MPI_Fint *datatype, MPI_Fint *dest, MPI_Fint *tag, MPI_Fint *comm, MPI_Fint *ierr) {
556 |       if (FTN_X(__real_ptr_mpi_send) == NULL) {
557 |         FTN_X(__real_ptr_mpi_send) = (void (*)(MPI_Fint *buf, MPI_Fint *count, MPI_Fint *datatype, MPI_Fint *dest, MPI_Fint *tag, MPI_Fint *comm, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_send)));
558 |       }
559 |       FTN_X(__real_ptr_mpi_send)(buf, count, datatype, dest, tag, comm, ierr);
568 | 
569 |     void FTN_X(__real_mpi_wait)(MPI_Fint *request, MPI_Fint *status, MPI_Fint *ierr) {
570 |       if (FTN_X(__real_ptr_mpi_wait) == NULL) {
571 |         FTN_X(__real_ptr_mpi_wait) = (void (*)(MPI_Fint *request, MPI_Fint *status, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_wait)));
572 |       }
573 |       FTN_X(__real_ptr_mpi_wait)(request, status, ierr);
582 | 
583 |     void FTN_X(__real_mpi_waitall)(MPI_Fint *count, MPI_Fint *reqs, MPI_Fint *stats, MPI_Fint *ierr) {
584 |       if (FTN_X(__real_ptr_mpi_waitall) == NULL) {
585 |         FTN_X(__real_ptr_mpi_waitall) = (void (*)(MPI_Fint *count, MPI_Fint *reqs, MPI_Fint *stats, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_waitall)));
586 |       }
587 |       FTN_X(__real_ptr_mpi_waitall)(count, reqs, stats, ierr);
596 | 
597 |     void FTN_X(__real_mpi_waitany)(MPI_Fint *count, MPI_Fint *reqs, MPI_Fint *index, MPI_Fint *status, MPI_Fint *ierr) {
598 |       if (FTN_X(__real_ptr_mpi_waitany) == NULL) {
599 |         FTN_X(__real_ptr_mpi_waitany) = (void (*)(MPI_Fint *count, MPI_Fint *reqs, MPI_Fint *index, MPI_Fint *status, MPI_Fint *ierr)) dlsym(RTLD_NEXT, xstr(FTN_X(mpi_waitany)));
600 |       }
601 |       FTN_X(__real_ptr_mpi_waitany)(count, reqs, index, status, ierr);
{% endraw %}

```
### src/Infrastructure/Trace/preload/gen_wrappers_mpi.py

```python

{% raw %}
176 | 
177 |     {{f.ret}} __real_{{f.name}}({{f.params}}) {
178 |       if (__real_ptr_{{f.name}} == NULL) {
179 |         __real_ptr_{{f.name}} = ({{f.ret}} (*)({{f.params}})) dlsym(RTLD_NEXT, "{{f.name}}");
180 |       }
181 |       return __real_ptr_{{f.name}}({{f.args}});
196 | 
197 |     void FTN_X(__real_{{f.name}})({{f.params}}) {
198 |       if (FTN_X(__real_ptr_{{f.name}}) == NULL) {
199 |         FTN_X(__real_ptr_{{f.name}}) = (void (*)({{f.params}})) dlsym(RTLD_NEXT, xstr(FTN_X({{f.name}})));
200 |       }
201 |       FTN_X(__real_ptr_{{f.name}})({{f.args}});
{% endraw %}

```
### src/Infrastructure/Trace/src/ESMCI_Trace.C

```c

{% raw %}
406 |       ESMC_LogDefault.Write("ESMF Tracing/Profiling could not open shared library containing instrumentation.", ESMC_LOGMSG_WARN);
407 |     }
408 |     else {
409 |       notify_wrappers = (int (*)(int)) dlsym(preload_lib, "c_esmftrace_notify_wrappers");
410 |       if (notify_wrappers != NULL) {
411 |         wrappersPresent = notify_wrappers(1);
{% endraw %}

```
### src/Superstructure/Component/src/ESMCI_MethodTable.C

```c

{% raw %}
314 |         "shared object not found", ESMC_CONTEXT, &rc);
315 |       return rc;
316 |     }
317 |     pointer = (void *)dlsym(lib, name.c_str());
318 |     if (pointer == NULL){
319 |       ESMC_LogDefault.MsgFoundError(ESMC_RC_ARG_BAD, 
{% endraw %}

```
### src/Superstructure/Component/src/ESMCI_FTable.C

```c

{% raw %}
253 |     }
254 |     string routine(routineArg, rlen);
255 |     routine.resize(routine.find_last_not_of(" ")+1);
256 |     void (*func)() = (void (*)())dlsym(lib, routine.c_str());
257 |     if ((void *)func == NULL){
258 |       ESMC_LogDefault.MsgFoundError(ESMC_RC_ARG_BAD,
306 |     }
307 |     string routine(routineArg, rlen);
308 |     routine.resize(routine.find_last_not_of(" ")+1);
309 |     void (*func)() = (void (*)())dlsym(lib, routine.c_str());
310 |     if ((void *)func != NULL){
311 |       // Routine was found
1909 |                 "- shared object not found", ESMC_CONTEXT, &rc);
1910 |               return rc;
1911 |             }
1912 |             void *pointer = (void *)dlsym(lib, value[0].c_str());
1913 |             if (pointer == NULL){
1914 |               ESMC_LogDefault.MsgFoundError(ESMC_RC_ARG_BAD,
1978 |             envVar = VM::getenv("ESMF_RUNTIME_COMPLIANCEICREGISTER");
1979 |             void *pointer;
1980 |             if (envVar != NULL)
1981 |               pointer = (void *)dlsym(lib, envVar);
1982 |             else
1983 |               pointer = (void *)dlsym(lib,
1984 |                 QUOTEMACRO(FTN(esmf_complianceicregister)) );
1985 |             if (pointer == NULL){
{% endraw %}

```