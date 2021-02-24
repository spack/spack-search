---
name: "legion"
layout: package
next_package: pmdk
previous_package: gnupg
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## master
7 / 2126 files match, 3 filtered matches.

 - [runtime/realm/codedesc.cc](#runtimerealmcodedesccc)
 - [runtime/realm/module.cc](#runtimerealmmodulecc)
 - [runtime/realm/python/python_module.cc](#runtimerealmpythonpython_modulecc)

### runtime/realm/codedesc.cc

```cpp

{% raw %}
370 |       } else {
371 | 	// try to load it - empty string for dso_name means the main executable
372 | 	const char *dso_name = dsoref->dso_name.c_str();
373 | 	handle = dlopen(*dso_name ? dso_name : 0, RTLD_NOW | RTLD_LOCAL);
374 | 	if(!handle) {
375 | 	  log_codetrans.warning() << "could not open DSO '" << dsoref->dso_name << "': " << dlerror();
{% endraw %}

```
### runtime/realm/module.cc

```cpp

{% raw %}
172 |       assert(dlerror() == 0);
173 | 
174 |       // open so file, resolving all symbols but not polluting global namespace
175 |       void *handle = dlopen(filename, RTLD_NOW | RTLD_LOCAL);
176 | 
177 |       if(handle != 0) {
{% endraw %}

```
### runtime/realm/python/python_module.cc

```cpp

{% raw %}
160 |     handle = dlmopen(lmid, python_lib, RTLD_DEEPBIND | RTLD_GLOBAL | RTLD_NOW);
161 | #else
162 |     // life is so much easier if we use dlopen (but we only get one copy then)
163 |     handle = dlopen(python_lib, RTLD_GLOBAL | RTLD_LAZY);
164 | #endif
165 |     if (!handle) {
{% endraw %}

```