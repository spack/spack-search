---
name: "openmpi"
layout: package
next_package: openpmd-api
previous_package: openmc
languages: ['c']
---
## 1.7.5
70 / 7011 files match, 26 filtered matches.

 - [ompi/mca/btl/usnic/test/ompi_btl_usnic_run_tests.c](#ompimcabtlusnictestompi_btl_usnic_run_testsc)
 - [ompi/mca/common/cuda/common_cuda.c](#ompimcacommoncudacommon_cudac)
 - [ompi/mpi/java/c/mpi_MPI.c](#ompimpijavacmpi_mpic)
 - [ompi/debuggers/dlopen_test.c](#ompidebuggersdlopen_testc)
 - [ompi/contrib/vt/vt/vtlib/vt_mallocwrap.c](#ompicontribvtvtvtlibvt_mallocwrapc)
 - [ompi/contrib/vt/vt/vtlib/vt_libwrap.c](#ompicontribvtvtvtlibvt_libwrapc)
 - [ompi/contrib/vt/vt/vtlib/vt_iowrap.c](#ompicontribvtvtvtlibvt_iowrapc)
 - [ompi/contrib/vt/vt/vtlib/vt_plugin_cntr.c](#ompicontribvtvtvtlibvt_plugin_cntrc)
 - [ompi/tools/ompi_info/param.c](#ompitoolsompi_infoparamc)
 - [oshmem/tools/oshmem_info/param.c](#oshmemtoolsoshmem_infoparamc)
 - [orte/tools/orte-info/param.c](#ortetoolsorte-infoparamc)
 - [opal/mca/base/base.h](#opalmcabasebaseh)
 - [opal/mca/base/mca_base_open.c](#opalmcabasemca_base_openc)
 - [opal/mca/base/mca_base_component_find.c](#opalmcabasemca_base_component_findc)
 - [opal/mca/hwloc/hwloc172/hwloc/src/components.c](#opalmcahwlochwloc172hwlocsrccomponentsc)
 - [opal/mca/memory/linux/hooks.c](#opalmcamemorylinuxhooksc)
 - [opal/mca/memory/linux/memory_linux_ptmalloc2.c](#opalmcamemorylinuxmemory_linux_ptmalloc2c)
 - [opal/util/lt_interface.h](#opalutillt_interfaceh)
 - [opal/util/lt_interface.c](#opalutillt_interfacec)
 - [opal/libltdl/ltdl.h](#opallibltdlltdlh)
 - [opal/libltdl/ltdl.c](#opallibltdlltdlc)
 - [opal/libltdl/loaders/preopen.c](#opallibltdlloaderspreopenc)
 - [opal/libltdl/loaders/dlopen.c](#opallibltdlloadersdlopenc)
 - [opal/libltdl/libltdl/lt__private.h](#opallibltdllibltdllt__privateh)
 - [opal/libltdl/libltdl/lt_error.h](#opallibltdllibltdllt_errorh)
 - [test/support/components.c](#testsupportcomponentsc)

### ompi/mca/btl/usnic/test/ompi_btl_usnic_run_tests.c

```c

{% raw %}
41 |     mpi_handle = dlopen("libmpi.so", RTLD_NOW|RTLD_GLOBAL);
77 |     usnic_handle = dlopen(path, RTLD_NOW|RTLD_LOCAL);
{% endraw %}

```
### ompi/mca/common/cuda/common_cuda.c

```c

{% raw %}
333 |             opal_show_help("help-mpi-common-cuda.txt", "dlopen disabled", true);
385 |                 libcuda_handle = opal_lt_dlopenadvise(cudalibs[i], advise);
420 |                 libcuda_handle = opal_lt_dlopen(cudalibs[i]);
449 |         opal_show_help("help-mpi-common-cuda.txt", "dlopen failed", true,
{% endraw %}

```
### ompi/mpi/java/c/mpi_MPI.c

```c

{% raw %}
91 |     if (NULL == (mpilibhandle = dlopen("libmpi." OPAL_DYN_LIB_SUFFIX,
{% endraw %}

```
### ompi/debuggers/dlopen_test.c

```c

{% raw %}
53 |        dlopen value.  If the dlopen value is '' (i.e., empty), then
54 |        there's nothing to dlopen (i.e., OMPI was built with
75 |         fprintf(stderr, "No test file to dlopen (perhaps --enable-static?); skipping\n");
85 |     printf("Trying to lt_dlopen file with dladvise_local: %s\n", filename);
94 |     dlhandle = lt_dlopenadvise(filename, dladvise);
97 |     dlhandle = lt_dlopenext(filename);
115 |     dlhandle = lt_dlopenadvise(filename, dladvise);
118 |     dlhandle = lt_dlopenext(filename);
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_mallocwrap.c

```c

{% raw %}
92 |      dlopen calls malloc which would result in an infinite recursion when
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_libwrap.c

```c

{% raw %}
159 |     libc_handle = dlopen(SHLIBC_PATHNAME,
173 |       printf("VampirTrace: FATAL: dlopen(\""SHLIBC_PATHNAME"\") failed: %s\n",
177 |       vt_error_msg("dlopen(\""SHLIBC_PATHNAME"\") failed: %s\n", dlerror());
262 |         (*lw)->handlev[i] = dlopen((*lw)->attr->shlibs[i],
272 |                    "dlopen(\"%s\") failed: %s",
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_iowrap.c

```c

{% raw %}
120 |       iolib_handle = dlopen( iolib_pathname,
127 |         printf("VampirTrace: FATAL: dlopen(\"%s\") error: %s\n", iolib_pathname, dlerror());
{% endraw %}

```
### ompi/contrib/vt/vt/vtlib/vt_plugin_cntr.c

```c

{% raw %}
212 |     handle = dlopen(buffer, RTLD_NOW);
{% endraw %}

```
### ompi/tools/ompi_info/param.c

```c

{% raw %}
592 |     opal_info_out("libltdl support", "option:dlopen", want_libltdl);
{% endraw %}

```
### oshmem/tools/oshmem_info/param.c

```c

{% raw %}
561 |     opal_info_out("libltdl support", "option:dlopen", want_libltdl);
{% endraw %}

```
### orte/tools/orte-info/param.c

```c

{% raw %}
428 |     orte_info_out("libltdl support", "option:dlopen", want_libltdl);
{% endraw %}

```
### opal/mca/base/base.h

```c

{% raw %}
68 | OPAL_DECLSPEC extern bool mca_base_component_disable_dlopen;
{% endraw %}

```
### opal/mca/base/mca_base_open.c

```c

{% raw %}
48 | bool mca_base_component_disable_dlopen = false;
112 |     mca_base_component_disable_dlopen = false;
113 |     var_id = mca_base_var_register("opal", "mca", "base", "component_disable_dlopen",
118 |                                    &mca_base_component_disable_dlopen);
119 |     (void) mca_base_var_register_synonym(var_id, "opal", "mca", NULL, "component_disable_dlopen",
{% endraw %}

```
### opal/mca/base/mca_base_component_find.c

```c

{% raw %}
202 |     if (open_dso_components && !mca_base_component_disable_dlopen) {
576 |   component_handle = lt_dlopenadvise(target_file->filename, opal_mca_dladvise);
578 |   component_handle = lt_dlopenext(target_file->filename);
{% endraw %}

```
### opal/mca/hwloc/hwloc172/hwloc/src/components.c

```c

{% raw %}
86 |   handle = lt_dlopenext(filename);
{% endraw %}

```
### opal/mca/memory/linux/hooks.c

```c

{% raw %}
863 |    --enable-static --disable-dlopen, because we won't use
{% endraw %}

```
### opal/mca/memory/linux/memory_linux_ptmalloc2.c

```c

{% raw %}
36 |    use --disable-dlopen and therefore -Wl,--export-dynamic isn't used
{% endraw %}

```
### opal/util/lt_interface.h

```c

{% raw %}
65 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopen(const char *filename);
66 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopenext(const char *filename);
70 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopenadvise(const char *filename,
{% endraw %}

```
### opal/util/lt_interface.c

```c

{% raw %}
166 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopen(const char *filename) {
173 |     handle->dlhandle = lt_dlopen(filename);
184 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopenext(const char *filename) {
191 |     handle->dlhandle = lt_dlopenext(filename);
228 | OPAL_DECLSPEC opal_lt_dlhandle opal_lt_dlopenadvise(const char *filename,
236 |     handle->dlhandle = lt_dlopenadvise(filename, advise->dladvise);
{% endraw %}

```
### opal/libltdl/ltdl.h

```c

{% raw %}
76 | LT_SCOPE lt_dlhandle lt_dlopen		(const char *filename);
77 | LT_SCOPE lt_dlhandle lt_dlopenext	(const char *filename);
78 | LT_SCOPE lt_dlhandle lt_dlopenadvise	(const char *filename,
133 |   int		ref_count;	/* number of times lt_dlopened minus
{% endraw %}

```
### opal/libltdl/ltdl.c

```c

{% raw %}
132 | static	int	try_dlopen	      (lt_dlhandle *handle,
135 | static	int	tryall_dlopen	      (lt_dlhandle *handle,
175 |    dlopen an application module.  */
242 | 	 can use _them_ to lt_dlopen its own modules.  */
367 | tryall_dlopen (lt_dlhandle *phandle, const char *filename,
375 |   fprintf (stderr, "tryall_dlopen (%s, %s)\n",
385 |       if ((handle->info.filename == filename) /* dlopen self: 0 == 0 */
485 | tryall_dlopen_module (lt_dlhandle *handle, const char *prefix,
521 |       error += tryall_dlopen_module (handle, (const char *) 0,
524 |   else if (tryall_dlopen (handle, filename, advise, 0) != 0)
539 |      we want the preopened version of it, even if a dlopenable
541 |   if (old_name && tryall_dlopen (handle, old_name,
553 | 	  if (tryall_dlopen_module (handle, (const char *) 0,
561 | 	  if (tryall_dlopen_module (handle, dir, objdir,
568 | 	  if (dir && (tryall_dlopen_module (handle, (const char *) 0,
786 |   if (tryall_dlopen (phandle, filename, advise, 0) != 0)
945 | 	  cur->deplibs[j] = lt_dlopenext(names[depcount-1-i]);
1151 | try_dlopen (lt_dlhandle *phandle, const char *filename, const char *ext,
1168 |   fprintf (stderr, "try_dlopen (%s, %s)\n",
1187 |       if (tryall_dlopen (&newhandle, 0, advise, 0) != 0)
1306 | 	  if (tryall_dlopen (&newhandle, archive_name, advise, vtable) == 0)
1473 | 	  if (tryall_dlopen (&newhandle, attempt, advise, 0) != 0)
1616 | lt_dlopen (const char *filename)
1618 |   return lt_dlopenadvise (filename, NULL);
1627 | lt_dlopenext (const char *filename)
1633 |     handle = lt_dlopenadvise (filename, advise);
1641 | lt_dlopenadvise (const char *filename, lt_dladvise advise)
1663 |       if (try_dlopen (&handle, filename, NULL, advise) != 0)
1672 |       errors += try_dlopen (&handle, filename, archive_ext, advise);
1685 |       errors = try_dlopen (&handle, filename, shlib_ext, advise);
1696 |       errors = try_dlopen (&handle, filename, shared_ext, advise);
1891 |    passing to lt_dlopenext.  The extensions are stripped so that
1894 |    then the same directories that lt_dlopen would search are examined.  */
{% endraw %}

```
### opal/libltdl/loaders/preopen.c

```c

{% raw %}
192 |      lt_dlopenadvise() a DSO -- so if there was a real error when
370 | 		  lt_dlhandle handle = lt_dlopen (symbol->name);
{% endraw %}

```
### opal/libltdl/loaders/dlopen.c

```c

{% raw %}
69 |       vtable->name		= "lt_dlopen";
193 |   module = dlopen (filename, module_flags);
{% endraw %}

```
### opal/libltdl/libltdl/lt__private.h

```c

{% raw %}
111 |   const lt_dlvtable *	vtable;		/* dlopening interface */
{% endraw %}

```
### opal/libltdl/libltdl/lt_error.h

```c

{% raw %}
45 |     LT_ERROR(DLOPEN_NOT_SUPPORTED,  "dlopen support not available\0")	\
{% endraw %}

```
### test/support/components.c

```c

{% raw %}
34 | static bool try_dlopen(const char *dir, const char *fw, const char *comp,
60 |     if (try_dlopen(".", framework, component, comp_handle, &sym) ||
61 |         try_dlopen(dir_concat(BUILDDIR, "src/mca"), framework, 
63 |         try_dlopen(dir_concat(SRCDIR, "src/mca"), framework, 
127 | static bool try_dlopen(const char *dir, const char *fw, const char *comp,
147 |     comp_handle->tch_handle = lt_dlopen(NULL);
165 |     comp_handle->tch_handle = lt_dlopenext(file_name);
{% endraw %}

```