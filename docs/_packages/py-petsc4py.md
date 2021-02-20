---
name: "py-petsc4py"
layout: package
next_package: py-pillow
previous_package: py-osqp
languages: ['c']
---
## develop
1 / 221 files match, 1 filtered matches.

 - [src/include/compat/mpi.h](#srcincludecompatmpih)

### src/include/compat/mpi.h

```c

{% raw %}
50 |   #if defined(__cplusplus) || defined(c_plusplus)
51 |   extern "C" {
52 |   #endif
53 |   extern void *dlopen(const char *, int);
54 |   extern void *dlsym(void *, const char *);
55 |   extern int   dlclose(void *);
73 | #endif
74 | 
75 | /*
76 | static void * my_dlopen(const char *name, int mode) {
77 |   void *handle;
78 |   static int called = 0;
93 |     #endif
94 |     printf("\n");
95 |   }
96 |   handle = dlopen(name, mode);
97 |   printf("dlopen(\"%s\",0x%X) -> %p\n", name, mode, handle);
98 |   printf("dlerror() -> %s\n\n", dlerror());
99 |   return handle;
101 | #define dlopen my_dlopen
102 | */
103 | 
104 | static void OPENMPI_dlopen_libmpi(void)
105 | {
106 |   void *handle = 0;
112 |   #endif
113 |   #if defined(OMPI_MAJOR_VERSION)
114 |   #if OMPI_MAJOR_VERSION == 3
115 |   if (!handle) handle = dlopen("libmpi.40.dylib", mode);
116 |   #elif OMPI_MAJOR_VERSION == 2
117 |   if (!handle) handle = dlopen("libmpi.20.dylib", mode);
118 |   #elif OMPI_MAJOR_VERSION == 1 && OMPI_MINOR_VERSION >= 10
119 |   if (!handle) handle = dlopen("libmpi.12.dylib", mode);
120 |   #elif OMPI_MAJOR_VERSION == 1 && OMPI_MINOR_VERSION >= 6
121 |   if (!handle) handle = dlopen("libmpi.1.dylib", mode);
122 |   #elif OMPI_MAJOR_VERSION == 1
123 |   if (!handle) handle = dlopen("libmpi.0.dylib", mode);
124 |   #endif
125 |   #endif
126 |   if (!handle) handle = dlopen("libmpi.dylib", mode);
127 | #else
128 |   /* GNU/Linux and others */
131 |   #endif
132 |   #if defined(OMPI_MAJOR_VERSION)
133 |   #if OMPI_MAJOR_VERSION >= 10 /* IBM Spectrum MPI */
134 |   if (!handle) handle = dlopen("libmpi_ibm.so.2", mode);
135 |   if (!handle) handle = dlopen("libmpi_ibm.so.1", mode);
136 |   if (!handle) handle = dlopen("libmpi_ibm.so", mode);
137 |   #elif OMPI_MAJOR_VERSION == 3
138 |   if (!handle) handle = dlopen("libmpi.so.40", mode);
139 |   #elif OMPI_MAJOR_VERSION == 2
140 |   if (!handle) handle = dlopen("libmpi.so.20", mode);
141 |   #elif OMPI_MAJOR_VERSION == 1 && OMPI_MINOR_VERSION >= 10
142 |   if (!handle) handle = dlopen("libmpi.so.12", mode);
143 |   #elif OMPI_MAJOR_VERSION == 1 && OMPI_MINOR_VERSION >= 6
144 |   if (!handle) handle = dlopen("libmpi.so.1", mode);
145 |   #elif OMPI_MAJOR_VERSION == 1
146 |   if (!handle) handle = dlopen("libmpi.so.0", mode);
147 |   #endif
148 |   #endif
149 |   if (!handle) handle = dlopen("libmpi.so", mode);
150 | #endif
151 | }
154 |                                               const char file[],
155 |                                               const char help[])
156 | {
157 |   OPENMPI_dlopen_libmpi();
158 |   return PetscInitialize(argc,args,file,help);
159 | }
{% endraw %}

```