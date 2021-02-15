---
name: "tfel"
layout: package
next_package: multiverso
previous_package: libnftnl
languages: ['cpp']
---
## 3.3.0
10 / 6979 files match

 - [src/System/ExternalLibraryManager.cxx](#srcsystemexternallibrarymanagercxx)
 - [include/TFEL/System/getFunction.h](#includetfelsystemgetfunctionh)
 - [include/TFEL/System/ExternalLibraryManager.hxx](#includetfelsystemexternallibrarymanagerhxx)
 - [docs/web/release-notes-3.1.1.md](#docswebrelease-notes-311md)
 - [docs/mfront/ansys/usermat.cpp](#docsmfrontansysusermatcpp)
 - [docs/mfront/general/mfront.tex.in](#docsmfrontgeneralmfronttexin)
 - [docs/mfront/abaqus/umat.cpp](#docsmfrontabaqusumatcpp)
 - [docs/mfront/abaqus/vumat-sp.cpp](#docsmfrontabaqusvumat-spcpp)
 - [docs/mfront/abaqus/vumat-dp.cpp](#docsmfrontabaqusvumat-dpcpp)
 - [docs/mfront/lsdyna/mfront-lsdyna.cxx](#docsmfrontlsdynamfront-lsdynacxx)

### src/System/ExternalLibraryManager.cxx

```

{% raw %}
139 |       return ::dlopen(l.c_str(), RTLD_NOW);
{% endraw %}

```
### include/TFEL/System/getFunction.h

```cpp

{% raw %}
33 |  * \param l: link to library opened through dlopen
41 |  * \param l: link to library opened through dlopen
51 |  * \param l: link to library opened through dlopen
104 |  * \param LibraryHandlerPtr, link to library opened through dlopen
113 |  * \param l: library opened through dlopen
125 |  * \param LibraryHandlerPtr, link to library opened through dlopen
141 |  * \param LibraryHandlerPtr, link to library opened through dlopen
170 |  * \param[in] l: link to library opened through dlopen
220 |  * \param[in] l: link to library opened through dlopen
266 |  * \param[in] l: link to library opened through dlopen
381 |   * \param LibraryHandlerPtr, link to library opened through dlopen
411 |   * \param[in] lib: handler to the library opened through dlopen
425 |   * \param l: library opened through dlopen
457 |  * \param[in] l: link to library opened through dlopen
500 |  * \param[in] l: link to library opened through dlopen
529 | * \param LibraryHandlerPtr, link to library opened through dlopen
544 |  * \param LibraryHandlerPtr, link to library opened through dlopen
559 |  * \param LibraryHandlerPtr, link to library opened through dlopen
574 |  * \param LibraryHandlerPtr, link to library opened through dlopen
589 |  * \param LibraryHandlerPtr, link to library opened through dlopen
606 |  * \param LibraryHandlerPtr, link to library opened through dlopen
621 |  * \param LibraryHandlerPtr, link to library opened through dlopen
637 |  * \param LibraryHandlerPtr, link to library opened through dlopen
653 |  * \param LibraryHandlerPtr, link to library opened through dlopen
669 |  * \param LibraryHandlerPtr, link to library opened through dlopen
685 |  * \param LibraryHandlerPtr, link to library opened through dlopen
702 |  * \param LibraryHandlerPtr, link to library opened through dlopen
728 |  * \param LibraryHandlerPtr, link to library opened through dlopen
755 |  * \param LibraryHandlerPtr, link to library opened through dlopen
784 |  * \param LibraryHandlerPtr, link to library opened through dlopen
814 |  * \param LibraryHandlerPtr, link to library opened through dlopen
845 |  * \param LibraryHandlerPtr, link to library opened through dlopen
874 |  * \param LibraryHandlerPtr, link to library opened through dlopen
889 |  * \param LibraryHandlerPtr, link to library opened through dlopen
904 |  * \param LibraryHandlerPtr, link to library opened through dlopen
920 |  * \param LibraryHandlerPtr, link to library opened through dlopen
937 |  * \param LibraryHandlerPtr, link to library opened through dlopen
956 |  * \param LibraryHandlerPtr, link to library opened through dlopen
976 |  * \param LibraryHandlerPtr, link to library opened through dlopen
997 |  * \param LibraryHandlerPtr, link to library opened through dlopen
1020 |  * \param LibraryHandlerPtr, link to library opened through dlopen
1044 |  * \param LibraryHandlerPtr, link to library opened through dlopen
1069 |  * \param LibraryHandlerPtr, link to library opened through dlopen
1097 |  * \param LibraryHandlerPtr, link to library opened through dlopen
1127 |  * \param LibraryHandlerPtr, link to library opened through dlopen
1159 |  * \param LibraryHandlerPtr, link to library opened through dlopen
1192 |  * \param LibraryHandlerPtr, link to library opened through dlopen
1226 |  * \param LibraryHandlerPtr, link to library opened through dlopen
{% endraw %}

```
### include/TFEL/System/ExternalLibraryManager.hxx

```

{% raw %}
43 |  * \brief a wrapper around the ::dlopen system call
45 |  * \param[in] b : boolean allowing ::dlopen to fail. If ::dlopen
{% endraw %}

```
### docs/web/release-notes-3.1.1.md

```

{% raw %}
152 | - directly using `dlopen/dlsym`.
{% endraw %}

```
### docs/mfront/ansys/usermat.cpp

```

{% raw %}
244 |           const auto l = ::dlopen(library.c_str(), RTLD_NOW);
{% endraw %}

```
### docs/mfront/general/mfront.tex.in

```

{% raw %}
1735 | externes se fait par l'appel aux fonctions {\tt dlopen}, {\tt dlsym} et
{% endraw %}

```
### docs/mfront/abaqus/umat.cpp

```

{% raw %}
386 |       libptr l = ::dlopen(lib.c_str(),RTLD_NOW);
{% endraw %}

```
### docs/mfront/abaqus/vumat-sp.cpp

```

{% raw %}
375 |       libptr l = ::dlopen(lib.c_str(),RTLD_NOW);
{% endraw %}

```
### docs/mfront/abaqus/vumat-dp.cpp

```

{% raw %}
375 |       libptr l = ::dlopen(lib.c_str(),RTLD_NOW);
{% endraw %}

```
### docs/mfront/lsdyna/mfront-lsdyna.cxx

```

{% raw %}
195 |           const auto l = ::dlopen(library.c_str(), RTLD_NOW);
{% endraw %}

```