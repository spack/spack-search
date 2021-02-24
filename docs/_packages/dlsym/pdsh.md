---
name: "pdsh"
layout: package
next_package: psm
previous_package: petsc
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.31
8 / 162 files match, 4 filtered matches.

 - [src/qsnet/qswutil.c](#srcqsnetqswutilc)
 - [src/pdsh/ltdl.h](#srcpdshltdlh)
 - [src/pdsh/ltdl.c](#srcpdshltdlc)
 - [src/pdsh/mod.c](#srcpdshmodc)

### src/qsnet/qswutil.c

```c

{% raw %}
206 | {
207 |     static int (*init_svc) (int);
208 | 
209 |     if (!(init_svc = dlsym (elan3h, "elan3_init_neterr_svc"))) 
210 |         return (0);
211 | 
217 | {
218 |     static int (*reg_svc) (void);
219 | 
220 |     if (!(reg_svc = dlsym (elan3h, "elan3_register_neterr_svc"))) 
221 |         return (0);
222 | 
227 | {
228 |     static int (*run_svc) ();
229 | 
230 |     if (!(run_svc = dlsym (elan3h, "elan3_run_neterr_svc"))) 
231 |         return (0);
232 | 
238 | {
239 |     static int (*load_svc) (int, char *);
240 | 
241 |     if (!(load_svc = dlsym (elan3h, "elan3_load_neterr_svc"))) 
242 |         return (0);
243 | 
{% endraw %}

```
### src/pdsh/ltdl.h

```c

{% raw %}
169 | /* Portable libltdl versions of the system dlopen() API. */
170 | LT_SCOPE	lt_dlhandle lt_dlopen		LT_PARAMS((const char *filename));
171 | LT_SCOPE	lt_dlhandle lt_dlopenext	LT_PARAMS((const char *filename));
172 | LT_SCOPE	lt_ptr	    lt_dlsym		LT_PARAMS((lt_dlhandle handle,
173 | 						     const char *name));
174 | LT_SCOPE	const char *lt_dlerror		LT_PARAMS((void));
220 | typedef struct {
221 |   const char *name;
222 |   lt_ptr      address;
223 | } lt_dlsymlist;
224 | 
225 | LT_SCOPE	int	lt_dlpreload	LT_PARAMS((const lt_dlsymlist *preloaded));
226 | LT_SCOPE	int	lt_dlpreload_default
227 | 				LT_PARAMS((const lt_dlsymlist *preloaded));
228 | 
229 | #define LTDL_SET_PRELOADED_SYMBOLS() 		LT_STMT_START{	\
230 | 	extern const lt_dlsymlist lt_preloaded_symbols[];		\
231 | 	lt_dlpreload_default(lt_preloaded_symbols);			\
232 | 						}LT_STMT_END
{% endraw %}

```
### src/pdsh/ltdl.c

```c

{% raw %}
1138 |      lt_module module;
1139 |      const char *symbol;
1140 | {
1141 |   lt_ptr address = dlsym (module, symbol);
1142 | 
1143 |   if (!address)
1948 | 
1949 | /* emulate dynamic linking using preloaded_symbols */
1950 | 
1951 | typedef struct lt_dlsymlists_t
1952 | {
1953 |   struct lt_dlsymlists_t       *next;
1954 |   const lt_dlsymlist	       *syms;
1955 | } lt_dlsymlists_t;
1956 | 
1957 | static	const lt_dlsymlist     *default_preloaded_symbols	= 0;
1958 | static	lt_dlsymlists_t	       *preloaded_symbols		= 0;
1959 | 
1960 | static int
1979 | static int
1980 | presym_free_symlists ()
1981 | {
1982 |   lt_dlsymlists_t *lists;
1983 | 
1984 |   LT_DLMUTEX_LOCK ();
1986 |   lists = preloaded_symbols;
1987 |   while (lists)
1988 |     {
1989 |       lt_dlsymlists_t	*tmp = lists;
1990 | 
1991 |       lists = lists->next;
2008 | 
2009 | static int
2010 | presym_add_symlist (preloaded)
2011 |      const lt_dlsymlist *preloaded;
2012 | {
2013 |   lt_dlsymlists_t *tmp;
2014 |   lt_dlsymlists_t *lists;
2015 |   int		   errors   = 0;
2016 | 
2026 |       lists = lists->next;
2027 |     }
2028 | 
2029 |   tmp = LT_EMALLOC (lt_dlsymlists_t, 1);
2030 |   if (tmp)
2031 |     {
2032 |       memset (tmp, 0, sizeof(lt_dlsymlists_t));
2033 |       tmp->syms = preloaded;
2034 |       tmp->next = preloaded_symbols;
2049 |      lt_user_data loader_data;
2050 |      const char *filename;
2051 | {
2052 |   lt_dlsymlists_t *lists;
2053 |   lt_module	   module = (lt_module) 0;
2054 | 
2072 | 
2073 |   while (lists)
2074 |     {
2075 |       const lt_dlsymlist *syms = lists->syms;
2076 | 
2077 |       while (syms->name)
2110 |      lt_module module;
2111 |      const char *symbol;
2112 | {
2113 |   lt_dlsymlist *syms = (lt_dlsymlist*) module;
2114 | 
2115 |   ++syms;
2263 | 
2264 | int
2265 | lt_dlpreload (preloaded)
2266 |      const lt_dlsymlist *preloaded;
2267 | {
2268 |   int errors = 0;
2288 | 
2289 | int
2290 | lt_dlpreload_default (preloaded)
2291 |      const lt_dlsymlist *preloaded;
2292 | {
2293 |   LT_DLMUTEX_LOCK ();
3863 | }
3864 | 
3865 | lt_ptr
3866 | lt_dlsym (handle, symbol)
3867 |      lt_dlhandle handle;
3868 |      const char *symbol;
{% endraw %}

```
### src/pdsh/mod.c

```c

{% raw %}
831 |     }
832 |   
833 |     /* load all module info from the pdsh_module structure */
834 |     if (!(mod->pmod = lt_dlsym(mod->handle, "pdsh_module_info"))) {
835 |         err("%p:[%s] can't resolve pdsh module\n", mod->filename);
836 |         goto fail;
837 |     }
838 | 
839 |     if ((priority = lt_dlsym(mod->handle, "pdsh_module_priority"))) 
840 |         mod->priority = *priority;
841 | 
{% endraw %}

```