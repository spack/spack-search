---
name: "dyninst"
layout: package
next_package: py-wheel
previous_package: taskflow
languages: ['c']
---
## 10.2.1
17 / 1296 files match

 - [common/src/serialize-xml.C](#commonsrcserialize-xmlc)
 - [proccontrol/src/int_thread_db.C](#proccontrolsrcint_thread_dbc)
 - [proccontrol/src/loadLibrary/codegen-linux.C](#proccontrolsrcloadlibrarycodegen-linuxc)
 - [proccontrol/src/loadLibrary/codegen-freebsd.C](#proccontrolsrcloadlibrarycodegen-freebsdc)
 - [dyninstAPI_RT/src/RTmutatedBinary_ELF.c](#dyninstapi_rtsrcrtmutatedbinary_elfc)
 - [dyninstAPI_RT/src/RTlinux.c](#dyninstapi_rtsrcrtlinuxc)
 - [dyninstAPI_RT/src/RTfreebsd.c](#dyninstapi_rtsrcrtfreebsdc)
 - [dyninstAPI/src/mapped_object.h](#dyninstapisrcmapped_objecth)
 - [dyninstAPI/src/BPatch_process.C](#dyninstapisrcbpatch_processc)
 - [dyninstAPI/src/mapped_object.C](#dyninstapisrcmapped_objectc)
 - [dyninstAPI/src/linux-aarch64.C](#dyninstapisrclinux-aarch64c)
 - [dyninstAPI/src/linux-power.C](#dyninstapisrclinux-powerc)

### common/src/serialize-xml.C

```c

{% raw %}
143 |     hXML = dlopen("libxml2.so", RTLD_LAZY);
{% endraw %}

```
### proccontrol/src/int_thread_db.C

```c

{% raw %}
344 | static void *dlopenThreadDB(char *path)
371 |    void *libhandle = dlopen(filename.c_str(), RTLD_LAZY);
374 |       libhandle = dlopen(alt_filename.c_str(), RTLD_LAZY);
385 | static void *dlopenThreadDB(char *)
397 |    void *libhandle = dlopenThreadDB(THREAD_DB_PATH_STR);
{% endraw %}

```
### proccontrol/src/loadLibrary/codegen-linux.C

```c

{% raw %}
21 | static const char DL_OPEN_FUNC_EXPORTED[] = "dlopen";
22 | static const char DL_OPEN_LIBC_FUNC_EXPORTED[] = "__libc_dlopen_mode";
23 | static const char DL_OPEN_FUNC_NAME[] = "do_dlopen";
27 |    Address dlopen_addr = 0;
35 |        dlopen_addr = findSymbolAddr(DL_OPEN_FUNC_EXPORTED, true); 
36 |        if (dlopen_addr) {
44 |        dlopen_addr = findSymbolAddr(DL_OPEN_FUNC_NAME, true);
47 |        if (dlopen_addr && var_addr && mprotect_addr) {
58 |        dlopen_addr = findSymbolAddr(DL_OPEN_LIBC_FUNC_EXPORTED, true);
59 |        if (dlopen_addr) {
62 |        fprintf(stderr, "Couldn't find dlopen address, bailing\n");
67 |     assert(dlopen_addr);
93 |     if (!generateCall(dlopen_addr, arguments)) return false;
99 |    struct libc_dlopen_args_32 {
105 |    struct libc_dlopen_args_64 {
112 |    struct libc_dlopen_args_32 args32;
113 |    struct libc_dlopen_args_64 args64;
{% endraw %}

```
### proccontrol/src/loadLibrary/codegen-freebsd.C

```c

{% raw %}
17 | const char DL_OPEN_FUNC_EXPORTED[] = "dlopen";
40 |     Address dlopenAddr = objSymReader->getSymbolOffset(lookupSym);
48 | 	dlopenAddr += (*li)->getLoadAddress();
68 |     if (!generateCall(dlopenAddr, arguments)) return false;
{% endraw %}

```
### dyninstAPI_RT/src/RTmutatedBinary_ELF.c

```c

{% raw %}
298 |      elfHandle = dlopen("libelf.so", RTLD_NOW);
569 | 					no PLT entry for dlopen.  if there is
570 | 					no entry for dlopen the mutatee must not
577 | 				well, we need to intercept the dlopen calls from the mutated binary
583 | 				So we must intercept the dlopen call and then check to be sure
708 | 				handle = dlopen(tmpPtr, RTLD_LAZY);
{% endraw %}

```
### dyninstAPI_RT/src/RTlinux.c

```c

{% raw %}
179 | typedef struct dlopen_args {
184 | } dlopen_args_t;
186 | void *(*DYNINST_do_dlopen)(dlopen_args_t *) = NULL;
188 | static int get_dlopen_error() {
196 |       sprintf(gLoadLibraryErrorString,"unknown error with dlopen");
206 |    res = dlopen(libname, RTLD_LAZY | RTLD_GLOBAL);
212 |    get_dlopen_error();
217 |       can only call _dl_open (the dlopen worker function) from
218 |       within glibc. We do this by calling do_dlopen
222 |        DYNINST_do_dlopen != NULL) {
223 |       dlopen_args_t args;
227 |       args.caller = (void *)DYNINST_do_dlopen;
231 |       (*DYNINST_do_dlopen)(&args);
238 |          get_dlopen_error();
{% endraw %}

```
### dyninstAPI_RT/src/RTfreebsd.c

```c

{% raw %}
184 | static int get_dlopen_error() {
192 |     sprintf(gLoadLibraryErrorString, "unknown error withe dlopen");
200 |     res = dlopen(libname, RTLD_NOW | RTLD_GLOBAL);
203 |     get_dlopen_error();
{% endraw %}

```
### dyninstAPI/src/mapped_object.h

```c

{% raw %}
379 |     bool dlopenUsed; //mark this shared object as opened by dlopen
{% endraw %}

```
### dyninstAPI/src/BPatch_process.C

```c

{% raw %}
1030 |       BPatch_function *dlopen_func = bpfv[0];
1031 |       if (dlopen_func == NULL)
1040 |       BPatch_funcCallExpr call_dlopen(*dlopen_func, args);
1042 |       if (!oneTimeCodeInternal(call_dlopen, NULL, NULL, NULL, true)) {
{% endraw %}

```
### dyninstAPI/src/mapped_object.C

```c

{% raw %}
82 |   dlopenUsed(false),
222 |    dlopenUsed(s->dlopenUsed),
{% endraw %}

```
### dyninstAPI/src/linux-aarch64.C

```c

{% raw %}
48 | const char DL_OPEN_FUNC_EXPORTED[] = "dlopen";
50 | const char DL_OPEN_FUNC_NAME[] = "do_dlopen";
51 | const char DL_OPEN_LIBC_FUNC_EXPORTED[] = "__libc_dlopen_mode";
{% endraw %}

```
### dyninstAPI/src/linux-power.C

```c

{% raw %}
48 | const char DL_OPEN_FUNC_EXPORTED[] = "dlopen";
50 | const char DL_OPEN_FUNC_NAME[] = "do_dlopen";
51 | const char DL_OPEN_LIBC_FUNC_EXPORTED[] = "__libc_dlopen_mode";
{% endraw %}

```