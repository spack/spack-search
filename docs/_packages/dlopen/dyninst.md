---
name: "dyninst"
layout: package
next_package: rsyslog
previous_package: libfuse
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 10.2.1
17 / 1296 files match, 12 filtered matches.

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
140 | 
141 | #else
142 | 
143 |     hXML = dlopen("libxml2.so", RTLD_LAZY);
144 | 
145 |     if (hXML == NULL)
{% endraw %}

```
### proccontrol/src/int_thread_db.C

```c

{% raw %}
341 | bool thread_db_process::tdb_loaded_result = false;
342 | 
343 | #if !defined(THREAD_DB_STATIC)
344 | static void *dlopenThreadDB(char *path)
345 | {
346 |    std::string filename;
368 | #endif
369 | 
370 |    pthrd_printf("Opening thread_db with %s\n", filename.c_str());
371 |    void *libhandle = dlopen(filename.c_str(), RTLD_LAZY);
372 |    if (!libhandle && !alt_filename.empty()) {
373 |    pthrd_printf("Opening thread_db with %s\n", alt_filename.c_str());
374 |       libhandle = dlopen(alt_filename.c_str(), RTLD_LAZY);
375 |    }
376 |    if (!libhandle) {
382 | }
383 | 
384 | #else
385 | static void *dlopenThreadDB(char *)
386 | {
387 |    return (void *) 0x1;  //Return anything non-NULL
394 |       return tdb_loaded_result;
395 |    tdb_loaded = true;
396 | 
397 |    void *libhandle = dlopenThreadDB(THREAD_DB_PATH_STR);
398 |    if (!libhandle)
399 |       return false;
{% endraw %}

```
### proccontrol/src/loadLibrary/codegen-linux.C

```c

{% raw %}
18 | #define __RTLD_DLOPEN 0x80000000
19 | #endif
20 | 
21 | static const char DL_OPEN_FUNC_EXPORTED[] = "dlopen";
22 | static const char DL_OPEN_LIBC_FUNC_EXPORTED[] = "__libc_dlopen_mode";
23 | static const char DL_OPEN_FUNC_NAME[] = "do_dlopen";
24 | 
25 | 
26 | bool Codegen::generateInt() {
27 |    Address dlopen_addr = 0;
28 | 
29 |     int mode = DLOPEN_MODE;
32 |     Address var_addr = 0;
33 |     Address mprotect_addr = 0;
34 |     do {
35 |        dlopen_addr = findSymbolAddr(DL_OPEN_FUNC_EXPORTED, true); 
36 |        if (dlopen_addr) {
37 |           break;
38 |        }
41 |        // Note: this is more robust than the next approach
42 |        useHiddenFunction = true;
43 |        needsStackUnprotect = true;
44 |        dlopen_addr = findSymbolAddr(DL_OPEN_FUNC_NAME, true);
45 |        var_addr = findSymbolAddr("__stack_prot");
46 |        mprotect_addr = findSymbolAddr("mprotect", true);
47 |        if (dlopen_addr && var_addr && mprotect_addr) {
48 |           break;
49 |        }
55 |        useHiddenFunction = false;
56 |        needsStackUnprotect = false;
57 |        mode |= __RTLD_DLOPEN;
58 |        dlopen_addr = findSymbolAddr(DL_OPEN_LIBC_FUNC_EXPORTED, true);
59 |        if (dlopen_addr) {
60 |           break;
61 |        }
62 |        fprintf(stderr, "Couldn't find dlopen address, bailing\n");
63 |        // We can't go farther without parsing
64 |        return false;
65 |     } while(0);
66 | 
67 |     assert(dlopen_addr);
68 | 
69 |     std::vector<Address> arguments;
90 |       if (!generateStackUnprotect(var_addr, mprotect_addr)) return false;
91 |     }
92 | 
93 |     if (!generateCall(dlopen_addr, arguments)) return false;
94 |     
95 |     return true;
96 | }
97 | 
98 | Address Codegen::buildLinuxArgStruct(Address libbase, unsigned mode) {
99 |    struct libc_dlopen_args_32 {
100 |       uint32_t namePtr;
101 |       uint32_t mode;
102 |       uint32_t linkMapPtr;
103 |    };
104 |    
105 |    struct libc_dlopen_args_64 {
106 |       uint64_t namePtr;
107 |       uint32_t mode;
109 |    };
110 |    
111 |    // Construct the argument to the internal function
112 |    struct libc_dlopen_args_32 args32;
113 |    struct libc_dlopen_args_64 args64;
114 |    unsigned argsSize = 0;
115 |    void *argsPtr = NULL;
{% endraw %}

```
### proccontrol/src/loadLibrary/codegen-freebsd.C

```c

{% raw %}
14 | 
15 | static const int DLOPEN_MODE = RTLD_NOW | RTLD_GLOBAL;
16 | 
17 | const char DL_OPEN_FUNC_EXPORTED[] = "dlopen";
18 | 
19 | bool Codegen::generateInt() {
37 |       return false;
38 |     }
39 | 
40 |     Address dlopenAddr = objSymReader->getSymbolOffset(lookupSym);
41 | 
42 |     // But we still need the load addr...
45 |       std::string canonical = resolve_file_path((*li)->getName());
46 |       if (canonical == interp) {
47 | 	found = true;
48 | 	dlopenAddr += (*li)->getLoadAddress();
49 | 	break;
50 |       }
65 |     
66 |     generatePreamble();
67 |     
68 |     if (!generateCall(dlopenAddr, arguments)) return false;
69 |     
70 |     return true;
{% endraw %}

```
### dyninstAPI_RT/src/RTmutatedBinary_ELF.c

```c

{% raw %}
295 | 
296 | //     elfHandle = dlopen("/usr/lib/libelf.so.1", RTLD_NOW);
297 | 
298 |      elfHandle = dlopen("libelf.so", RTLD_NOW);
299 |      if(! elfHandle){
300 |         error_msg = dlerror();
566 | 			}
567 | 			if( shdr->sh_addr != 0){
568 | 				/* if the addr is zero, then there is 
569 | 					no PLT entry for dlopen.  if there is
570 | 					no entry for dlopen the mutatee must not
571 | 					call it.  -- what about calling it from
572 | 					a shared lib that is statically loaded?
574 | 
575 | 			/* WHY IS THERE A POUND DEFINE HERE? 
576 | 
577 | 				well, we need to intercept the dlopen calls from the mutated binary
578 | 				because our trampolines expect the shared libraries to be in
579 | 				a particular location and if they are not where they are expected
580 | 				our trampolines can jump off into nothingness, or even worse, some
581 | 				random bit of executable code.  
582 | 
583 | 				So we must intercept the dlopen call and then check to be sure
584 | 				the shared libraries are loaded in the same place as before.  If
585 | 				they are not we exit with a message to the user saying this is
705 | 			tmpPtr = elfData->d_buf;
706 | 
707 | 			while(*tmpPtr) { 
708 | 				handle = dlopen(tmpPtr, RTLD_LAZY);
709 | 				if(handle){
710 | 
{% endraw %}

```
### dyninstAPI_RT/src/RTlinux.c

```c

{% raw %}
176 |  * For now, removing dependence of static version of this library
177 |  * on libdl.
178 |  */
179 | typedef struct dlopen_args {
180 |   const char *libname;
181 |   int mode;
182 |   void *result;
183 |   void *caller;
184 | } dlopen_args_t;
185 | 
186 | void *(*DYNINST_do_dlopen)(dlopen_args_t *) = NULL;
187 | 
188 | static int get_dlopen_error() {
189 |    char *err_str;
190 |    err_str = dlerror();
193 |       return 1;
194 |    }
195 |    else {
196 |       sprintf(gLoadLibraryErrorString,"unknown error with dlopen");
197 |       return 0;
198 |    }
203 | {
204 |    void *res;
205 |    gLoadLibraryErrorString[0]='\0';
206 |    res = dlopen(libname, RTLD_LAZY | RTLD_GLOBAL);
207 |    if (res)
208 |    {
209 |       return 1;
210 |    }
211 | 
212 |    get_dlopen_error();
213 | #if defined(arch_x86)
214 |    /* dlopen on recent glibcs has a "security check" so that
215 |       only registered modules can call it. Unfortunately, progs
216 |       that don't include libdl break this check, so that we
217 |       can only call _dl_open (the dlopen worker function) from
218 |       within glibc. We do this by calling do_dlopen
219 |       We fool this check by calling an addr written by the
220 |       mutator */
221 |    if (strstr(gLoadLibraryErrorString, "invalid caller") != NULL &&
222 |        DYNINST_do_dlopen != NULL) {
223 |       dlopen_args_t args;
224 |       args.libname = libname;
225 |       args.mode = RTLD_NOW | RTLD_GLOBAL;
226 |       args.result = 0;
227 |       args.caller = (void *)DYNINST_do_dlopen;
228 |       // There's a do_dlopen function in glibc. However, it's _not_
229 |       // exported; thus, getting the address is a bit of a pain.
230 | 
231 |       (*DYNINST_do_dlopen)(&args);
232 |       // Duplicate the above
233 |       if (args.result != NULL)
235 |          return 1;
236 |       }
237 |       else
238 |          get_dlopen_error();
239 |    }
240 | #endif
{% endraw %}

```
### dyninstAPI_RT/src/RTfreebsd.c

```c

{% raw %}
181 | }
182 | 
183 | #if !defined(DYNINST_RT_STATIC_LIB)
184 | static int get_dlopen_error() {
185 |     const char *err_str;
186 |     err_str = dlerror();
189 |         return 1;
190 |     }
191 | 
192 |     sprintf(gLoadLibraryErrorString, "unknown error withe dlopen");
193 |     return 0;
194 | }
197 | {
198 |     void *res;
199 |     gLoadLibraryErrorString[0] = '\0';
200 |     res = dlopen(libname, RTLD_NOW | RTLD_GLOBAL);
201 |     if( res ) return 1;
202 | 
203 |     get_dlopen_error();
204 |     return 0;
205 | }
{% endraw %}

```
### dyninstAPI/src/mapped_object.h

```c

{% raw %}
376 |     bool dirtyCalled_;//see comment for setDirtyCalled
377 | 
378 |     image  *image_; // pointer to image if processed is true
379 |     bool dlopenUsed; //mark this shared object as opened by dlopen
380 |     AddressSpace *proc_; // Parent process
381 | 
{% endraw %}

```
### dyninstAPI/src/BPatch_process.C

```c

{% raw %}
1027 |             std::string("functions called DYNINSTloadLibrary -- not fatal but weird");
1028 |          BPatch_reportError(BPatchSerious, 100, msg.c_str());
1029 |       }
1030 |       BPatch_function *dlopen_func = bpfv[0];
1031 |       if (dlopen_func == NULL)
1032 |         break;
1033 | 
1037 |       BPatch_Vector<BPatch_snippet *> args;
1038 |       BPatch_constExpr nameArg(libname);
1039 |       args.push_back(&nameArg);
1040 |       BPatch_funcCallExpr call_dlopen(*dlopen_func, args);
1041 | 
1042 |       if (!oneTimeCodeInternal(call_dlopen, NULL, NULL, NULL, true)) {
1043 |          BPatch_variableExpr *dlerror_str_var =
1044 |             image->findVariable("gLoadLibraryErrorString");
{% endraw %}

```
### dyninstAPI/src/mapped_object.C

```c

{% raw %}
79 |   dirty_(false),
80 |   dirtyCalled_(false),
81 |   image_(img),
82 |   dlopenUsed(false),
83 |   proc_(proc),
84 |   analyzed_(false),
219 |    dirty_(s->dirty_),
220 |    dirtyCalled_(s->dirtyCalled_),
221 |    image_(s->image_),
222 |    dlopenUsed(s->dlopenUsed),
223 |    proc_(child),
224 |    analyzed_(s->analyzed_),
{% endraw %}

```
### dyninstAPI/src/linux-aarch64.C

```c

{% raw %}
45 | 
46 | #define DLOPEN_MODE (RTLD_NOW | RTLD_GLOBAL)
47 | 
48 | const char DL_OPEN_FUNC_EXPORTED[] = "dlopen";
49 | const char DL_OPEN_FUNC_INTERNAL[] = "_dl_open";
50 | const char DL_OPEN_FUNC_NAME[] = "do_dlopen";
51 | const char DL_OPEN_LIBC_FUNC_EXPORTED[] = "__libc_dlopen_mode";
52 | 
53 | Address PCProcess::getLibcStartMainParam(PCThread *) {
{% endraw %}

```
### dyninstAPI/src/linux-power.C

```c

{% raw %}
45 | 
46 | #define DLOPEN_MODE (RTLD_NOW | RTLD_GLOBAL)
47 | 
48 | const char DL_OPEN_FUNC_EXPORTED[] = "dlopen";
49 | const char DL_OPEN_FUNC_INTERNAL[] = "_dl_open";
50 | const char DL_OPEN_FUNC_NAME[] = "do_dlopen";
51 | const char DL_OPEN_LIBC_FUNC_EXPORTED[] = "__libc_dlopen_mode";
52 | 
53 | Address PCProcess::getLibcStartMainParam(PCThread *) {
{% endraw %}

```