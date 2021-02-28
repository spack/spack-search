---
name: "mono"
layout: package
next_package: erlang
previous_package: meson
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.10.1.57
25 / 82201 files match, 5 filtered matches.

 - [mono/utils/mono-dl-posix.c](#monoutilsmono-dl-posixc)
 - [mono/mini/mini-llvm.c](#monominimini-llvmc)
 - [mono/mini/llvm-jit.h](#monominillvm-jith)
 - [mono/mini/aot-compiler.c](#monominiaot-compilerc)
 - [libgc/dyn_load.c](#libgcdyn_loadc)

### mono/utils/mono-dl-posix.c

```c

{% raw %}
77 | void*
78 | mono_dl_lookup_symbol (MonoDl *module, const char *name)
79 | {
80 | 	return dlsym (module->handle, name);
81 | }
82 | 
{% endraw %}

```
### mono/mini/mini-llvm.c

```c

{% raw %}
7806 | #endif
7807 | 
7808 | static char*
7809 | dlsym_cb (const char *name, void **symbol)
7810 | {
7811 | 	MonoDl *current;
8380 | 	module->lmodule = LLVMModuleCreateWithName (name);
8381 | 	module->context = LLVMGetGlobalContext ();
8382 | 
8383 | 	module->mono_ee = (MonoEERef*)mono_llvm_create_ee (LLVMCreateModuleProviderForExistingModule (module->lmodule), alloc_cb, emitted_cb, exception_cb, dlsym_cb, &module->ee);
8384 | 
8385 | 	add_intrinsics (module->lmodule);
{% endraw %}

```
### mono/mini/llvm-jit.h

```c

{% raw %}
27 | typedef void* MonoEERef;
28 | 
29 | MonoEERef
30 | mono_llvm_create_ee (LLVMModuleProviderRef MP, AllocCodeMemoryCb *alloc_cb, FunctionEmittedCb *emitted_cb, ExceptionTableCb *exception_cb, DlSymCb *dlsym_cb, LLVMExecutionEngineRef *ee);
31 | 
32 | void
{% endraw %}

```
### mono/mini/aot-compiler.c

```c

{% raw %}
165 | 	gboolean metadata_only;
166 | 	gboolean bind_to_runtime_version;
167 | 	MonoAotMode mode;
168 | 	gboolean no_dlsym;
169 | 	gboolean static_link;
170 | 	gboolean asm_only;
719 | add_to_global_symbol_table (MonoAotCompile *acfg)
720 | {
721 | #ifdef TARGET_WIN32_MSVC
722 | 	return acfg->aot_opts.no_dlsym || link_shared_library (acfg);
723 | #else
724 | 	return acfg->aot_opts.no_dlsym;
725 | #endif
726 | }
731 | 	if (add_to_global_symbol_table (acfg))
732 | 		g_ptr_array_add (acfg->globals, g_strdup (name));
733 | 
734 | 	if (acfg->aot_opts.no_dlsym) {
735 | 		mono_img_writer_emit_local_symbol (acfg->w, name, NULL, func);
736 | 	} else {
7353 | 			opts->nthreads = atoi (arg + strlen ("threads="));
7354 | 		} else if (str_begins_with (arg, "static")) {
7355 | 			opts->static_link = TRUE;
7356 | 			opts->no_dlsym = TRUE;
7357 | 		} else if (str_begins_with (arg, "asmonly")) {
7358 | 			opts->asm_only = TRUE;
{% endraw %}

```
### libgc/dyn_load.c

```c

{% raw %}
150 | 	/* at program startup.						*/
151 | 	if( dynStructureAddr == 0 ) {
152 | 	  void* startupSyms = dlopen(0, RTLD_LAZY);
153 | 	  dynStructureAddr = (ElfW(Dyn)*)dlsym(startupSyms, "_DYNAMIC");
154 | 		}
155 | #   else
{% endraw %}

```