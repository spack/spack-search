---
name: "powerapi"
layout: package
next_package: premake-core
previous_package: postgresql
languages: ['cpp', 'c']
---
## 1.1.1
2 / 246 files match, 2 filtered matches.

 - [src/pwr/pluginMeta.h](#srcpwrpluginmetah)
 - [src/pwr/dynamic.cc](#srcpwrdynamiccc)

### src/pwr/pluginMeta.h

```c

{% raw %}
25 |   public:
26 | 	PluginMeta( std::string libName ) {
27 | 
28 |     	void* m_lib = dlopen( libName.c_str(), RTLD_LAZY);
29 | 		assert(m_lib);
30 | 
{% endraw %}

```
### src/pwr/dynamic.cc

```cpp

{% raw %}
21 | plugin_dev_t* DistCntxt::getDev( std::string lib, std::string name )
22 | {
23 | 	DBGX("lib %s name=`%s`\n", lib.c_str(), name.c_str() );
24 |     void* ptr = dlopen( lib.c_str(), RTLD_LAZY);
25 |     if ( NULL == ptr ) {
26 |         printf("error: can't find plugin library `%s`\n", lib.c_str());
{% endraw %}

```