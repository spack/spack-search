---
name: "libmesh"
layout: package
next_package: libmicrohttpd
previous_package: libluv
languages: ['cpp']
---
## master
118 / 9244 files match, 1 filtered matches.

 - [contrib/fparser/fparser_ad.cc](#contribfparserfparser_adcc)

### contrib/fparser/fparser_ad.cc

```cpp

{% raw %}
1099 |   std::string libname = _jitdir + "/" + _master_hash + ".so";
1100 | 
1101 |   // attempt to open the cache file
1102 |   _lib = dlopen(libname.c_str(), RTLD_NOW);
1103 |   return (_lib != NULL);
1104 | }
1153 |   }
1154 | 
1155 |   // load compiled object
1156 |   _lib = dlopen(_object_so.c_str(), RTLD_NOW);
1157 |   if (_lib == NULL) {
1158 |     std::cerr << "JIT object load failed.\n";
{% endraw %}

```