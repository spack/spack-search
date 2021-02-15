---
name: "ace"
layout: package
next_package: gconf
previous_package: libxft
languages: ['html', 'cpp', 'pl']
---
## 6.5.12
20 / 8830 files match

 - [ACE-INSTALL.html](#ace-installhtml)
 - [bin/valgrind.supp](#binvalgrindsupp)
 - [bin/fuzz.pl](#binfuzzpl)
 - [rpmbuild/ace-tao.spec](#rpmbuildace-taospec)
 - [include/makeinclude/platform_macosx_jaguar.GNU](#includemakeincludeplatform_macosx_jaguargnu)
 - [ace/DLL_Manager.h](#acedll_managerh)
 - [ace/Strategies_T.cpp](#acestrategies_tcpp)
 - [ace/config-macosx-jaguar.h](#aceconfig-macosx-jaguarh)
 - [ace/OS_NS_dlfcn.h](#aceos_ns_dlfcnh)
 - [ace/config-hpux-11.00.h](#aceconfig-hpux-1100h)
 - [ace/config-macosx-tiger.h](#aceconfig-macosx-tigerh)
 - [ace/config-macosx-panther.h](#aceconfig-macosx-pantherh)
 - [ace/config-macosx-leopard.h](#aceconfig-macosx-leopardh)
 - [ace/DLL.cpp](#acedllcpp)
 - [ace/OS_NS_dlfcn.inl](#aceos_ns_dlfcninl)
 - [ace/DLL_Manager.cpp](#acedll_managercpp)
 - [ace/os_include/os_dlfcn.h](#aceos_includeos_dlfcnh)
 - [tests/Unload_libACE.cpp](#testsunload_libacecpp)
 - [tests/Bug_2980_Regression_Test.cpp](#testsbug_2980_regression_testcpp)
 - [apps/JAWS/clients/WebSTONE/src/nsapi-includes/base/dll.h](#appsjawsclientswebstonesrcnsapi-includesbasedllh)

### ACE-INSTALL.html

```html

{% raw %}
2259 |       <code>dlopen</code>, you should use <code>RTLD_NOW</code>.  The
{% endraw %}

```
### bin/valgrind.supp

```

{% raw %}
99 |    <dlopen>
106 |   <dlopen2>
113 |    fun:dlopen_doit
119 |    <dlopen3>
131 |    fun:dlopen_doit
137 |   <dlopen4>
144 |    fun:dlopen_doit
150 |   <dlopen5>
157 |    fun:dlopen_doit
163 |    <dlopen6>
175 |    fun:dlopen_doit
181 |    <dlopen7>
200 |    fun:dlopen_doit
224 |    fun:dlopen_doit
{% endraw %}

```
### bin/fuzz.pl

```pl

{% raw %}
627 |     $OS_NS_dlfcn_symbols = "dlclose|dlerror|dlopen|dlsym";
{% endraw %}

```
### rpmbuild/ace-tao.spec

```

{% raw %}
2235 | # NOTE - Some of the TAO service modules need to be found by dlopen at
2269 | # NOTE - Some of the TAO service modules need to be found by dlopen() at
{% endraw %}

```
### include/makeinclude/platform_macosx_jaguar.GNU

```

{% raw %}
23 | ## dlcompat package (not part of base Darwin) is needed for dlopen() on 10.2.
{% endraw %}

```
### ace/DLL_Manager.h

```cpp

{% raw %}
87 |    *        ACE with the @c ACE_MUST_HELP_DLOPEN_SEARCH_PATH config macro.
147 |   /// Builds array of DLL names to try to dlopen, based on platform
190 |   /// initialized by a call to dlopen().
{% endraw %}

```
### ace/Strategies_T.cpp

```

{% raw %}
117 |   ACE_SHLIB_HANDLE handle = ACE_OS::dlopen (this->dll_name_);
{% endraw %}

```
### ace/config-macosx-jaguar.h

```cpp

{% raw %}
156 | // dlcompat package (not part of base Darwin) is needed for dlopen().
{% endraw %}

```
### ace/OS_NS_dlfcn.h

```cpp

{% raw %}
45 |   ACE_SHLIB_HANDLE dlopen (const ACE_TCHAR *filename,
{% endraw %}

```
### ace/config-hpux-11.00.h

```cpp

{% raw %}
304 | // dlopen() takes a char* instead of const char*
{% endraw %}

```
### ace/config-macosx-tiger.h

```cpp

{% raw %}
185 | // dlcompat package (not part of base Darwin) is needed for dlopen().
{% endraw %}

```
### ace/config-macosx-panther.h

```cpp

{% raw %}
158 | // dlcompat package (not part of base Darwin) is needed for dlopen().
{% endraw %}

```
### ace/config-macosx-leopard.h

```cpp

{% raw %}
215 | // dlcompat package (not part of base Darwin) is needed for dlopen().
{% endraw %}

```
### ace/DLL.cpp

```

{% raw %}
111 | // ACE_SHLIB_HANDLE which is obtained on making the ACE_OS::dlopen call.
{% endraw %}

```
### ace/OS_NS_dlfcn.inl

```

{% raw %}
50 |   // kernel has, not the actual struct.  On 64-bit HP-UX using dlopen,
109 | ACE_OS::dlopen (const ACE_TCHAR *fname,
112 |   ACE_OS_TRACE ("ACE_OS::dlopen");
116 |   ACE_OSCALL (::dlopen (ACE_TEXT_ALWAYS_CHAR (fname), mode), void *, 0, handle);
{% endraw %}

```
### ace/DLL_Manager.cpp

```

{% raw %}
90 |           ** underlying dlopen() implementation to "Do The Right Thing" in
92 |           ** rules, etc. except when ACE_MUST_HELP_DLOPEN_SEARCH_PATH is set.
96 |           ** pathname to dlopen() is a potential security hole; therefore,
97 |           ** do not use ACE_MUST_HELP_DLOPEN_SEARCH_PATH unless necessary
103 | #if defined (ACE_MUST_HELP_DLOPEN_SEARCH_PATH)
465 |   this->handle_ = ACE_OS::dlopen (dll_name, open_mode);
{% endraw %}

```
### ace/os_include/os_dlfcn.h

```cpp

{% raw %}
54 |    // Dynamic loading-related types - used for dlopen and family.
{% endraw %}

```
### tests/Unload_libACE.cpp

```

{% raw %}
7 |  *    but uses dlopen() to dynamically load libACE
170 |           handle = dlopen (buf, RTLD_LAZY);
177 |                            "%s@LM_ERROR@ dlopen() returned NULL\n",
186 |                   printf ("%s@LM_DEBUG@ dlopen() did not find %s\n",
{% endraw %}

```
### tests/Bug_2980_Regression_Test.cpp

```

{% raw %}
77 |       dllHandle = dlopen (dllFile, RTLD_NOW);
82 |       dllHandle = dlopen (DllTestName, RTLD_NOW);
{% endraw %}

```
### apps/JAWS/clients/WebSTONE/src/nsapi-includes/base/dll.h

```cpp

{% raw %}
33 | #elif defined(DLL_DLOPEN)
35 | typedef void *DLHANDLE;  /* DLOPEN */
56 | #elif defined(DLL_DLOPEN)
57 | #define dll_open(libfn) dlopen(libfn, DLL_DLOPEN_FLAGS)
75 | #elif defined(DLL_DLOPEN)
92 | #elif defined(DLL_DLOPEN)
109 | #elif defined(DLL_DLOPEN)
{% endraw %}

```