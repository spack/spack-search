---
name: "unixodbc"
layout: package
next_package: libxsmm
previous_package: silo
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.3.4
29 / 845 files match, 18 filtered matches.

 - [exe/dltest.c](#exedltestc)
 - [extras/vms.c](#extrasvmsc)
 - [odbcinst/SQLConfigDataSource.c](#odbcinstsqlconfigdatasourcec)
 - [odbcinst/SQLCreateDataSource.c](#odbcinstsqlcreatedatasourcec)
 - [odbcinst/ODBCINSTConstructProperties.c](#odbcinstodbcinstconstructpropertiesc)
 - [odbcinst/SQLConfigDriver.c](#odbcinstsqlconfigdriverc)
 - [odbcinst/_SQLDriverConnectPrompt.c](#odbcinst_sqldriverconnectpromptc)
 - [odbcinst/SQLManageDataSources.c](#odbcinstsqlmanagedatasourcesc)
 - [DriverManager/SQLConnect.c](#drivermanagersqlconnectc)
 - [libltdl/ltdl.h](#libltdlltdlh)
 - [libltdl/ltdl.c](#libltdlltdlc)
 - [libltdl/loaders/dyld.c](#libltdlloadersdyldc)
 - [libltdl/loaders/loadlibrary.c](#libltdlloadersloadlibraryc)
 - [libltdl/loaders/shl_load.c](#libltdlloadersshl_loadc)
 - [libltdl/loaders/load_add_on.c](#libltdlloadersload_add_onc)
 - [libltdl/loaders/dld_link.c](#libltdlloadersdld_linkc)
 - [libltdl/loaders/preopen.c](#libltdlloaderspreopenc)
 - [libltdl/loaders/dlopen.c](#libltdlloadersdlopenc)

### exe/dltest.c

```c

{% raw %}
84 | 	printf( "SUCCESS: Loaded %s\n", argv[1] );
85 | 	if ( argc > 2 )
86 | 	{
87 | 		pFunc = (void (*)()) lt_dlsym( hDLL, argv[2] );
88 | /* PAH - lt_dlerror() is not a good indicator of success    */
89 | /*		if ( (pError = lt_dlerror()) != NULL )              */
{% endraw %}

```
### extras/vms.c

```c

{% raw %}
29 | } vms_dl;
30 | 
31 | 
32 | int vms_dlsym	    (vms_dl	*, void	**, int);
33 | void * lt_dlsym	    (void *, const char *);
34 | 
35 | int lt_dlinit (void)
148 |     ** Attempt to load a symbol at this stage to
149 |     ** validate that the shared file can be loaded
150 |     */
151 |     lt_dlsym (dh, "Fake_Symbol_Name");
152 |     if (!((error_status ^ LIB$_KEYNOTFOU) & ~7)) error_status = SS$_NORMAL;
153 | 
166 |     return 0;
167 | }
168 | 
169 | void * lt_dlsym (void *handle, const char *name)
170 | {
171 |     vms_dl			*dh;
182 | 
183 |     /* firstly attempt with flags set to 0 case insensitive */
184 |     flags = 0;
185 |     status = vms_dlsym (dh, &ptr, flags);
186 |     if (!($VMS_STATUS_SUCCESS(status)))
187 |     {
190 | 	*/
191 |         flags = LIB$M_FIS_MIXEDCASE;
192 | 
193 | 	status = vms_dlsym (dh, &ptr, flags);
194 | 	if (!($VMS_STATUS_SUCCESS(status)))
195 | 	{
201 |     return ptr;
202 | }
203 | 
204 | int vms_dlsym (
205 |     vms_dl	*dh,
206 |     void	**ptr,
{% endraw %}

```
### odbcinst/SQLConfigDataSource.c

```c

{% raw %}
103 | 		nReturn = FALSE;
104 | 		if ( (hDLL = lt_dlopen( szDriverSetup ))  )
105 | 		{
106 | 			pFunc = (BOOL (*)(HWND, WORD, LPCSTR, LPCSTR )) lt_dlsym( hDLL, "ConfigDSN" );
107 | 			pFuncW = (BOOL (*)(HWND, WORD, LPCWSTR, LPCWSTR )) lt_dlsym( hDLL, "ConfigDSNW" );
108 | 			if ( pFunc )
109 |             {
{% endraw %}

```
### odbcinst/SQLCreateDataSource.c

```c

{% raw %}
204 |     if ( hDLL )
205 |     {
206 |         /* change the name, as it avoids it finding it in the calling lib */
207 |         pSQLCreateDataSource = (BOOL (*)(HWND, LPCSTR))lt_dlsym( hDLL, "ODBCCreateDataSource" );
208 |         if ( pSQLCreateDataSource )
209 |             return pSQLCreateDataSource( ( *(hODBCInstWnd->szUI) ? hODBCInstWnd->hWnd : NULL ), pszDS );
218 |         if ( hDLL )
219 |         {
220 |             /* change the name, as it avoids linker finding it in the calling lib */
221 |             pSQLCreateDataSource = (BOOL (*)(HWND,LPCSTR))lt_dlsym( hDLL, "ODBCCreateDataSource" );
222 |             if ( pSQLCreateDataSource )
223 |                 return pSQLCreateDataSource( ( *(hODBCInstWnd->szUI) ? hODBCInstWnd->hWnd : NULL ), pszDS );
{% endraw %}

```
### odbcinst/ODBCINSTConstructProperties.c

```c

{% raw %}
172 | 		return ODBCINST_ERROR;
173 | 	}
174 | 
175 | 	pODBCINSTGetProperties = (int(*)(struct tODBCINSTPROPERTY*)) lt_dlsym( hDLL, "ODBCINSTGetProperties" );
176 | 
177 | /*	PAH - This can be true even when we found the symbol.
{% endraw %}

```
### odbcinst/SQLConfigDriver.c

```c

{% raw %}
104 | 		/* errors in here are ignored, according to the spec; perhaps I should ret error and let app ignore? */
105 | 		if ( (hDLL = lt_dlopen( szDriverSetup ))  )
106 | 		{
107 | 			pConfigDriver = (BOOL (*)(HWND, WORD, LPCSTR, LPCSTR, LPCSTR, WORD, WORD * )) lt_dlsym( hDLL, "ConfigDriver" );
108 | 			pConfigDriverW = (BOOL (*)(HWND, WORD, LPCWSTR, LPCWSTR, LPCWSTR, WORD, WORD * )) lt_dlsym( hDLL, "ConfigDriverW" );
109 | /*			if ( lt_dlerror() == NULL ) */
110 |             if ( pConfigDriver )
{% endraw %}

```
### odbcinst/_SQLDriverConnectPrompt.c

```c

{% raw %}
34 |     if ( hDLL )
35 |     {
36 |         /* change the name, as it avoids it finding it in the calling lib */
37 |         pODBCDriverConnectPrompt = (BOOL (*)( HWND, SQLCHAR *, SQLSMALLINT ))lt_dlsym( hDLL, "ODBCDriverConnectPrompt" );
38 |         if ( pODBCDriverConnectPrompt ) 
39 | 		{
59 |         if ( hDLL )
60 |         {
61 |             /* change the name, as it avoids linker finding it in the calling lib */
62 |         	pODBCDriverConnectPrompt = (BOOL (*)(HWND, SQLCHAR *, SQLSMALLINT ))lt_dlsym( hDLL, "ODBCDriverConnectPrompt" );
63 |         	if ( pODBCDriverConnectPrompt ) 
64 | 			{
{% endraw %}

```
### odbcinst/SQLManageDataSources.c

```c

{% raw %}
151 |     if ( hDLL )
152 |     {
153 |         /* change the name (SQLManageDataSources to ODBCManageDataSources) to prevent us from calling ourself */
154 |         pSQLManageDataSources = (BOOL (*)(HWND))lt_dlsym( hDLL, "ODBCManageDataSources" );
155 |         if ( pSQLManageDataSources )
156 |             return pSQLManageDataSources( ( *(hODBCInstWnd->szUI) ? hODBCInstWnd->hWnd : NULL ) );
167 |         {
168 |             /* change the name (SQLManageDataSources to ODBCManageDataSources) to prevent us from calling ourself   */
169 |             /* its only safe to use hWnd if szUI was specified by the caller                                        */
170 |             pSQLManageDataSources = (BOOL (*)(HWND))lt_dlsym( hDLL, "ODBCManageDataSources" );
171 |             if ( pSQLManageDataSources )
172 |                 return pSQLManageDataSources( ( *(hODBCInstWnd->szUI) ? hODBCInstWnd->hWnd : NULL ) );
{% endraw %}

```
### DriverManager/SQLConnect.c

```c

{% raw %}
1152 |      */
1153 | 
1154 |     connection -> ini_func.func =
1155 |             (SQLRETURN (*)()) lt_dlsym( connection -> dl_handle,
1156 |                     ODBC_INI_FUNCTION );
1157 | 
1158 |     connection -> fini_func.func =
1159 |             (SQLRETURN (*)()) lt_dlsym( connection -> dl_handle,
1160 |                     ODBC_FINI_FUNCTION );
1161 | 
1191 |         char name[ 128 ];
1192 | 
1193 |         connection -> functions[ i ].func =
1194 |             (SQLRETURN (*)()) lt_dlsym( connection -> dl_handle,
1195 |                     connection -> functions[ i ].name );
1196 | 
1209 |                 sprintf( name, "%sA", connection -> functions[ i ].name );
1210 |             }
1211 |             connection -> functions[ i ].funcA =
1212 |                 (SQLRETURN (*)()) lt_dlsym( connection -> dl_handle, name );
1213 | 
1214 |             if ( connection -> functions[ i ].funcA &&
1230 | 
1231 |             sprintf( name, "%sW", connection -> functions[ i ].name );
1232 |             connection -> functions[ i ].funcW =
1233 |                 (SQLRETURN (*)()) lt_dlsym( connection -> dl_handle, name );
1234 |         }
1235 |         else
2381 |             }
2382 |         }
2383 | 
2384 |         if ( !( cl_connect = (int(*)(void*, struct driver_helper_funcs* ))lt_dlsym( connection -> cl_handle,
2385 |                         "CLConnect" )))
2386 |         {
{% endraw %}

```
### libltdl/ltdl.h

```c

{% raw %}
77 | LT_SCOPE lt_dlhandle lt_dlopenext	(const char *filename);
78 | LT_SCOPE lt_dlhandle lt_dlopenadvise	(const char *filename,
79 | 					 lt_dladvise advise);
80 | LT_SCOPE void *	    lt_dlsym		(lt_dlhandle handle, const char *name);
81 | LT_SCOPE const char *lt_dlerror		(void);
82 | LT_SCOPE int	    lt_dlclose		(lt_dlhandle handle);
91 | typedef struct {
92 |   const char *name;
93 |   void       *address;
94 | } lt_dlsymlist;
95 | 
96 | typedef int lt_dlpreload_callback_func (lt_dlhandle handle);
97 | 
98 | LT_SCOPE int	lt_dlpreload	     (const lt_dlsymlist *preloaded);
99 | LT_SCOPE int	lt_dlpreload_default (const lt_dlsymlist *preloaded);
100 | LT_SCOPE int	lt_dlpreload_open    (const char *originator,
101 | 				      lt_dlpreload_callback_func *func);
102 | 
103 | #define lt_preloaded_symbols	lt__PROGRAM__LTX_preloaded_symbols
104 | /* Ensure C linkage.  */
105 | extern LT_DLSYM_CONST lt_dlsymlist lt__PROGRAM__LTX_preloaded_symbols[];
106 | 
107 | #define LTDL_SET_PRELOADED_SYMBOLS() \
{% endraw %}

```
### libltdl/ltdl.c

```c

{% raw %}
176 | static int
177 | loader_init_callback (lt_dlhandle handle)
178 | {
179 |   lt_get_vtable *vtable_func = (lt_get_vtable *) lt_dlsym (handle, "get_vtable");
180 |   return loader_init (vtable_func, 0);
181 | }
217 | LT_SCOPE const lt_dlvtable *	get_vtable (lt_user_data data);
218 | LT_END_C_DECLS
219 | #ifdef HAVE_LIBDLLOADER
220 | extern LT_DLSYM_CONST lt_dlsymlist preloaded_symbols[];
221 | #endif
222 | 
2002 | }
2003 | 
2004 | void *
2005 | lt_dlsym (lt_dlhandle place, const char *symbol)
2006 | {
2007 |   size_t lensym;
{% endraw %}

```
### libltdl/loaders/dyld.c

```c

{% raw %}
34 | /* Use the preprocessor to rename non-static symbols to avoid namespace
35 |    collisions when the loader code is statically linked into libltdl.
36 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
37 |    be fetched from the preloaded symbol list by lt_dlsym():  */
38 | #define get_vtable	dyld_LTX_get_vtable
39 | 
{% endraw %}

```
### libltdl/loaders/loadlibrary.c

```c

{% raw %}
38 | /* Use the preprocessor to rename non-static symbols to avoid namespace
39 |    collisions when the loader code is statically linked into libltdl.
40 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
41 |    be fetched from the preloaded symbol list by lt_dlsym():  */
42 | #define get_vtable	loadlibrary_LTX_get_vtable
43 | 
{% endraw %}

```
### libltdl/loaders/shl_load.c

```c

{% raw %}
34 | /* Use the preprocessor to rename non-static symbols to avoid namespace
35 |    collisions when the loader code is statically linked into libltdl.
36 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
37 |    be fetched from the preloaded symbol list by lt_dlsym():  */
38 | #define get_vtable	shl_load_LTX_get_vtable
39 | 
{% endraw %}

```
### libltdl/loaders/load_add_on.c

```c

{% raw %}
34 | /* Use the preprocessor to rename non-static symbols to avoid namespace
35 |    collisions when the loader code is statically linked into libltdl.
36 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
37 |    be fetched from the preloaded symbol list by lt_dlsym():  */
38 | #define get_vtable	load_add_on_LTX_get_vtable
39 | 
{% endraw %}

```
### libltdl/loaders/dld_link.c

```c

{% raw %}
34 | /* Use the preprocessor to rename non-static symbols to avoid namespace
35 |    collisions when the loader code is statically linked into libltdl.
36 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
37 |    be fetched from the preloaded symbol list by lt_dlsym():  */
38 | #define get_vtable	dld_link_LTX_get_vtable
39 | 
{% endraw %}

```
### libltdl/loaders/preopen.c

```c

{% raw %}
34 | /* Use the preprocessor to rename non-static symbols to avoid namespace
35 |    collisions when the loader code is statically linked into libltdl.
36 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
37 |    be fetched from the preloaded symbol list by lt_dlsym():  */
38 | #define get_vtable	preopen_LTX_get_vtable
39 | 
96 | typedef struct symlist_chain
97 | {
98 |   struct symlist_chain *next;
99 |   const lt_dlsymlist   *symlist;
100 | } symlist_chain;
101 | 
102 | 
103 | static int add_symlist   (const lt_dlsymlist *symlist);
104 | static int free_symlists (void);
105 | 
107 | static symlist_chain	       *preloaded_symlists		= 0;
108 | 
109 | /* A symbol list preloaded before lt_init() was called.  */
110 | static const	lt_dlsymlist   *default_preloaded_symbols	= 0;
111 | 
112 | 
164 | 
165 |   for (lists = preloaded_symlists; lists; lists = lists->next)
166 |     {
167 |       const lt_dlsymlist *symbol;
168 |       for (symbol= lists->symlist; symbol->name; ++symbol)
169 | 	{
174 | 		 In this case we pretend that we never saw the module and
175 | 	         hope that some other loader will be able to load the module
176 | 	         and have access to its symbols */
177 | 	      const lt_dlsymlist *next_symbol = symbol +1;
178 | 	      if (next_symbol->address && next_symbol->name)
179 | 		{
207 | static void *
208 | vm_sym (lt_user_data LT__UNUSED loader_data, lt_module module, const char *name)
209 | {
210 |   lt_dlsymlist	       *symbol = (lt_dlsymlist*) module;
211 | 
212 |   symbol +=2;			/* Skip header (originator then libname). */
252 | 
253 | /* Add a new symbol list to the global chain.  */
254 | static int
255 | add_symlist (const lt_dlsymlist *symlist)
256 | {
257 |   symlist_chain *lists;
289 | 
290 | /* Save a default symbol list for later.  */
291 | int
292 | lt_dlpreload_default (const lt_dlsymlist *preloaded)
293 | {
294 |   default_preloaded_symbols = preloaded;
299 | /* Add a symbol list to the global chain, or with a NULL argument,
300 |    revert to just the default list.  */
301 | int
302 | lt_dlpreload (const lt_dlsymlist *preloaded)
303 | {
304 |   int errors = 0;
338 |       if ((originator && streq (list->symlist->name, originator))
339 |           || (!originator && streq (list->symlist->name, "@PROGRAM@")))
340 | 	{
341 | 	  const lt_dlsymlist *symbol;
342 | 	  unsigned int idx = 0;
343 | 
{% endraw %}

```
### libltdl/loaders/dlopen.c

```c

{% raw %}
34 | /* Use the preprocessor to rename non-static symbols to avoid namespace
35 |    collisions when the loader code is statically linked into libltdl.
36 |    Use the "<module_name>_LTX_" prefix so that the symbol addresses can
37 |    be fetched from the preloaded symbol list by lt_dlsym():  */
38 | #define get_vtable	dlopen_LTX_get_vtable
39 | 
223 | static void *
224 | vm_sym (lt_user_data LT__UNUSED loader_data, lt_module module, const char *name)
225 | {
226 |   void *address = dlsym (module, name);
227 | 
228 |   if (!address)
{% endraw %}

```