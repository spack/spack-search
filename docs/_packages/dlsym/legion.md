---
name: "legion"
layout: package
next_package: pmdk
previous_package: gnupg
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## master
9 / 2129 files match, 5 filtered matches.

 - [runtime/realm/codedesc.cc](#runtimerealmcodedesccc)
 - [runtime/realm/threads.cc](#runtimerealmthreadscc)
 - [runtime/realm/module.cc](#runtimerealmmodulecc)
 - [runtime/realm/python/python_module.cc](#runtimerealmpythonpython_modulecc)
 - [test/realm/taskreg.cc](#testrealmtaskregcc)

### runtime/realm/codedesc.cc

```cpp

{% raw %}
378 | 	modules_loaded[dsoref->dso_name] = handle;
379 |       }
380 | 
381 |       void *ptr = dlsym(handle, dsoref->symbol_name.c_str());
382 |       if(!ptr) {
383 | 	log_codetrans.warning() << "could not find symbol '" << dsoref->symbol_name << "' in  DSO '" << dsoref->dso_name << "': " << dlerror();
{% endraw %}

```
### runtime/realm/threads.cc

```cpp

{% raw %}
1021 |     //   (as of glibc 2.2.5, this is not exported, but if/when it is, it's
1022 |     //   simpler than the __pthread_get_minstack version below)
1023 |     do {
1024 |       void *sym = dlsym(RTLD_DEFAULT, "__static_tls_size");
1025 |       if(!sym) break;
1026 | 
1031 | 
1032 |     // case 3: try __pthread_get_minstack (subtracting out PTHREAD_STACK_MIN)
1033 |     do {
1034 |       void *sym = dlsym(RTLD_DEFAULT, "__pthread_get_minstack");
1035 |       if(!sym) break;
1036 | 
{% endraw %}

```
### runtime/realm/module.cc

```cpp

{% raw %}
176 | 
177 |       if(handle != 0) {
178 | 	// this file should have a "create_realm_module" symbol
179 | 	void *sym = dlsym(handle, "create_realm_module");
180 | 
181 | 	if(sym != 0) {
182 | 	  // TODO: hold onto the handle even if it doesn't create a module?
183 | 	  handles.push_back(handle);
184 | 
185 | 	  Module *m = ((Module *(*)(RuntimeImpl *, std::vector<std::string>&))dlsym)(runtime, cmdline);
186 | 	  if(m)
187 | 	    modules.push_back(m);
{% endraw %}

```
### runtime/realm/python/python_module.cc

```cpp

{% raw %}
87 |   void PythonAPI::get_symbol(T &fn, const char *symbol,
88 |                              bool missing_ok /*= false*/)
89 |   {
90 |     fn = reinterpret_cast<T>(dlsym(handle, symbol));
91 |     if(!fn && !missing_ok) {
92 |       const char *error = dlerror();
108 |     void *handle = 0;
109 |     void *sym = (symver ?
110 | 		   dlvsym(handle, symname, symver) :
111 | 		   dlsym(handle, symname));
112 |     if(sym)
113 |       log_py.debug() << "found symbol: name=" << symname << " ver=" << (symver ? symver : "(none)") << " ptr=" << sym;
147 |     // now that the proxy is loaded, we need to tell it where the real
148 |     //  libpthreads functions are
149 |     {
150 |       void *sym = dlsym(dlmproxy_handle, "dlmproxy_load_symbols");
151 |       assert(sym != 0);
152 |       ((void (*)(void *(*)(const char *, const char *)))sym)(dlmproxy_lookup);
{% endraw %}

```
### test/realm/taskreg.cc

```cpp

{% raw %}
60 | template <typename T>
61 | void lookup_symbol(const char *name, T& addr)
62 | {
63 |   void *res = dlsym(RTLD_DEFAULT, name);
64 |   if(!res) {
65 |     log_app.fatal() << "symbol lookup error: cannot find '" << name << "'";
{% endraw %}

```