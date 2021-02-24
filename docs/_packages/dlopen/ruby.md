---
name: "ruby"
layout: package
next_package: dbus
previous_package: bird
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.7.1
25 / 9819 files match, 4 filtered matches.

 - [addr2line.c](#addr2linec)
 - [mjit_worker.c](#mjit_workerc)
 - [dln.c](#dlnc)
 - [ext/fiddle/handle.c](#extfiddlehandlec)

### addr2line.c

```c

{% raw %}
1730 | 	    char *strtab = file + dynstr_shdr->sh_offset;
1731 | 	    ElfW(Sym) *symtab = (ElfW(Sym) *)(file + dynsym_shdr->sh_offset);
1732 | 	    int symtab_count = (int)(dynsym_shdr->sh_size / sizeof(ElfW(Sym)));
1733 |             void *handle = dlopen(NULL, RTLD_NOW|RTLD_LOCAL);
1734 |             if (handle) {
1735 |                 for (j = 0; j < symtab_count; j++) {
{% endraw %}

```
### mjit_worker.c

```c

{% raw %}
873 |     CRITICAL_SECTION_FINISH(3, "in compact_all_jit_code to keep .o files");
874 | 
875 |     if (success) {
876 |         void *handle = dlopen(so_file, RTLD_NOW);
877 |         if (handle == NULL) {
878 |             mjit_warning("failure in loading code from compacted '%s': %s", so_file, dlerror());
920 | {
921 |     void *handle, *func;
922 | 
923 |     handle = dlopen(so_file, RTLD_NOW);
924 |     if (handle == NULL) {
925 |         mjit_warning("failure in loading code from '%s': %s", so_file, dlerror());
{% endraw %}

```
### dln.c

```c

{% raw %}
1337 | #endif
1338 | 
1339 | 	/* Load file */
1340 | 	if ((handle = (void*)dlopen(file, RTLD_LAZY|RTLD_GLOBAL)) == NULL) {
1341 | 	    error = dln_strerror();
1342 | 	    goto failed;
{% endraw %}

```
### ext/fiddle/handle.c

```c

{% raw %}
165 | # endif
166 | 	){
167 | # ifdef _WIN32_WCE
168 | 	ptr = dlopen("coredll.dll", cflag);
169 | # else
170 | 	(void)cflag;
173 |     }
174 |     else
175 | #endif
176 | 	ptr = dlopen(clib, cflag);
177 | #if defined(HAVE_DLERROR)
178 |     if( !ptr && (err = dlerror()) ){
{% endraw %}

```