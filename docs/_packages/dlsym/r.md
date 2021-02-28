---
name: "r"
layout: package
next_package: nspr
previous_package: keepalived
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.3.1
12 / 4124 files match, 8 filtered matches.

 - [src/main/dotcode.c](#srcmaindotcodec)
 - [src/main/Rdynload.c](#srcmainrdynloadc)
 - [src/include/Rdynpriv.h](#srcincluderdynprivh)
 - [src/library/grDevices/src/devQuartz.c](#srclibrarygrdevicessrcdevquartzc)
 - [src/gnuwin32/dynload.c](#srcgnuwin32dynloadc)
 - [src/unix/hpdlfcn.c](#srcunixhpdlfcnc)
 - [src/unix/dynload.c](#srcunixdynloadc)
 - [src/unix/hpdlfcn.h](#srcunixhpdlfcnh)

### src/main/dotcode.c

```c

{% raw %}
276 |     }
277 | 
278 |     /* NB: the actual conversion to the symbol is done in
279 |        R_dlsym in Rdynload.c.  That prepends an underscore (usually),
280 |        and may append one or more underscores.
281 |     */
1377 | 	info = (DllInfo *) R_ExternalPtrAddr(tmp);
1378 | 	if(!info)
1379 | 	    error(_("NULL value for DLLInfoReference when looking for DLL"));
1380 | 	fun = R_dlsym(info, name, symbol);
1381 |     }
1382 | 
{% endraw %}

```
### src/main/Rdynload.c

```c

{% raw %}
148 | attribute_hidden OSDynSymbol *R_osDynSymbol = &Rf_osDynSymbol;
149 | 
150 | void R_init_base(DllInfo *); /* In Registration.c */
151 | DL_FUNC R_dlsym(DllInfo *dll, char const *name,
152 | 		R_RegisteredNativeSymbol *symbol);
153 | 
232 |   Explicitly register the native routines for use in .Call(), .C() and
233 |   .Fortran() functions. These registered values are used to resolve
234 |   symbols in an object that makes a call to this routine, rather than
235 |   the usual dynamic resolution done by dlsym() or the equivalent on
236 |   the different platforms.
237 |  */
440 |     symbol.type = R_ANY_SYM;
441 | 
442 |     snprintf(buf, 1024, "R_unload_%s", dllInfo->name);
443 |     f = (DllInfoUnloadCall) R_dlsym(dllInfo, buf, &symbol);
444 |     if(f) f(dllInfo);
445 | 
556 | #else
557 | 	snprintf(tmp, len, "_%s%s","R_init_", info->name);
558 | #endif
559 | 	f = (DllInfoInitCall) R_osDynSymbol->dlsym(info, tmp);
560 | 	/* If that failed, might have used the package name with
561 | 	   . replaced by _ (as . it not valid in symbol names). */
563 | 	    /* This is potentially unsafe in MBCSs, as '.' might be
564 | 	       part of a character: but is not in UTF-8 */
565 | 	    for(char *p = tmp; *p; p++) if(*p == '.') *p = '_';
566 | 	    f = (DllInfoInitCall) R_osDynSymbol->dlsym(info, tmp);
567 | 	}
568 | 	if(f) f(info);
756 | }
757 | 
758 | DL_FUNC attribute_hidden
759 | R_dlsym(DllInfo *info, char const *name,
760 | 	R_RegisteredNativeSymbol *symbol)
761 | {
784 |     }
785 | #endif
786 | 
787 |     f = (DL_FUNC) R_osDynSymbol->dlsym(info, buf);
788 | #ifdef HAVE_F77_UNDERSCORE
789 |     if (!f && symbol && symbol->type == R_ANY_SYM) {
791 | # ifdef HAVE_F77_EXTRA_UNDERSCORE
792 | 	if(strchr(name, '_')) strcat(buf, "_");
793 | # endif
794 | 	f = (DL_FUNC) R_osDynSymbol->dlsym(info, buf);
795 |     }
796 | #endif
825 | 	if(!doit && !strcmp(pkg, LoadedDLL[i].name)) doit = 2;
826 | 	if(doit && LoadedDLL[i].forceSymbols) doit = 0;
827 | 	if(doit) {
828 | 	    fcnptr = R_dlsym(&LoadedDLL[i], name, symbol); /* R_osDynSymbol->dlsym */
829 | 	    if (fcnptr != (DL_FUNC) NULL) {
830 | 		if(symbol)
1095 | 	    package = translateChar(STRING_ELT(spackage, 0));
1096 | 	else if(TYPEOF(spackage) == EXTPTRSXP &&
1097 | 		R_ExternalPtrTag(spackage) == install("DLLInfo")) {
1098 | 	    f = R_dlsym((DllInfo *) R_ExternalPtrAddr(spackage), name, &symbol);
1099 | 	    package = NULL;
1100 | 	} else
1316 | 	    package = translateChar(STRING_ELT(spackage, 0));
1317 | 	else if(TYPEOF(spackage) == EXTPTRSXP &&
1318 | 		R_ExternalPtrTag(spackage) == install("DLLInfo")) {
1319 | 	    f = R_dlsym((DllInfo *) R_ExternalPtrAddr(spackage), name, &symbol);
1320 | 	    package = NULL;
1321 | 	} else
{% endraw %}

```
### src/include/Rdynpriv.h

```c

{% raw %}
154 |     HINSTANCE (*loadLibrary)(const char *path, int asLocal, int now,
155 | 			     char const *search); 
156 |     /* Load the dynamic library. */
157 |     DL_FUNC (*dlsym)(DllInfo *info, char const *name); 
158 |     /* Low-level symbol lookup in library */
159 |     void (*closeLibrary)(HINSTANCE handle); 
194 | 
195 | DL_FUNC Rf_lookupCachedSymbol(const char *name, const char *pkg, int all);
196 | 
197 | DL_FUNC R_dlsym(DllInfo *info, char const *name, 
198 | 		R_RegisteredNativeSymbol *symbol);
199 | 
{% endraw %}

```
### src/library/grDevices/src/devQuartz.c

```c

{% raw %}
516 | #include <dlfcn.h> /* dynamically find the right entry point on initialization */
517 | __attribute__((constructor)) static void RQ_init() {
518 |     void *r;
519 |     if ((r = dlsym(RTLD_NEXT, "CGFontGetGlyphsForUnichars")) || (r = dlsym(RTLD_NEXT, "CGFontGetGlyphsForUnicodes")) ||
520 | 	(r = dlsym(RTLD_DEFAULT, "CGFontGetGlyphsForUnichars")) || (r = dlsym(RTLD_DEFAULT, "CGFontGetGlyphsForUnicodes")))
521 | 	RQFontGetGlyphsForUnichars = (RQFontGetGlyphsForUnichars_t) r;
522 |     else
{% endraw %}

```
### src/gnuwin32/dynload.c

```c

{% raw %}
103 | void InitFunctionHashing()
104 | {
105 |     R_osDynSymbol->loadLibrary = R_loadLibrary;
106 |     R_osDynSymbol->dlsym = getRoutine;
107 |     R_osDynSymbol->closeLibrary = closeLibrary;
108 |     R_osDynSymbol->getError = R_getDLLError;
{% endraw %}

```
### src/unix/hpdlfcn.c

```c

{% raw %}
197 |  * Symbol Lookup.
198 |  */
199 | 
200 | void *dlsym(void *handle, const char *name)
201 | {
202 |   void *f;
{% endraw %}

```
### src/unix/dynload.c

```c

{% raw %}
57 | 			 const char *search);
58 | static void closeLibrary(void *handle);
59 | static void deleteCachedSymbols(DllInfo *);
60 | static DL_FUNC R_local_dlsym(DllInfo *info, char const *name);
61 | static void getFullDLLPath(SEXP call, char *buf, const char *path);
62 | static void getSystemError(char *buf, int len);
66 | void attribute_hidden InitFunctionHashing()
67 | {
68 |     R_osDynSymbol->loadLibrary = loadLibrary;
69 |     R_osDynSymbol->dlsym = R_local_dlsym;
70 |     R_osDynSymbol->closeLibrary = closeLibrary;
71 |     R_osDynSymbol->getError = getSystemError;
201 |   symbol in a shared object.  A cast would not be legal C.
202 |  */
203 | typedef union {void *p; DL_FUNC fn;} fn_ptr;
204 | static DL_FUNC R_local_dlsym(DllInfo *info, char const *name)
205 | {
206 |     fn_ptr tmp;
207 |     tmp.p = dlsym(info->handle, name);
208 |     return tmp.fn;
209 | }
{% endraw %}

```
### src/unix/hpdlfcn.h

```c

{% raw %}
1 | void *dlsym(void *, const char *);
2 | int dlclose(void *);
3 | char *dlerror(void);
{% endraw %}

```