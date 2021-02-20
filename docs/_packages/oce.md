---
name: "oce"
layout: package
next_package: ocl-icd
previous_package: ocaml
languages: ['c']
---
## 0.16
9 / 38793 files match, 1 filtered matches.

 - [src/IncludeLibrary/IncludeLibrary_osd_dlopen.h](#srcincludelibraryincludelibrary_osd_dlopenh)

### src/IncludeLibrary/IncludeLibrary_osd_dlopen.h

```c

{% raw %}
64 |  return ret ;
65 | }
66 | 
67 | inline void *osd_dlopen( char *Path , int LazyMode )
68 | {
69 |  void *handle ;
101 | #elif defined(sun) || defined(SOLARIS)  || defined(IRIX) || defined(sgi) || defined(linux) || defined(LIN) || defined(__FreeBSD__)
102 |  if ( Path != NULL ) {
103 |    if ( LazyMode )
104 |      handle = dlopen( Path , RTLD_LAZY | RTLD_GLOBAL );
105 |    else
106 |      handle = dlopen( Path , RTLD_GLOBAL );
107 |  }
108 |  else
109 |    handle = dlopen( Path , RTLD_NOW );
110 | #elif defined(WNT)
111 |  if ( Path != NULL )
116 | #else
117 |  if ( Path != NULL ) {
118 |    if ( LazyMode )
119 |      handle = dlopen( Path , RTLD_LAZY );
120 |    else
121 |      handle = dlopen( Path , RTLD_NOW );
122 |  }
123 |  else
124 |    handle = dlopen( Path , RTLD_NOW );
125 | #endif
126 | 
128 |  return handle ;
129 | }
130 | 
131 | inline char *osd_dlopenerror( char *Path )
132 | {
133 | 
134 | #if defined (__hpux) || defined(HPUX)
135 |    if ( Path != NULL && errno != 0 ) {
136 |      strcpy( chartmp , "dlopen(\"" ) ;
137 |      strcat( chartmp , Path ) ;
138 |      strcat( chartmp , "\") perror " ) ;
150 |                   MAKELANGID( LANG_NEUTRAL, SUBLANG_NEUTRAL ), &chartmp[i] , 450, NULL);
151 |    //strcat( chartmp ,  GetLastError()  ) ;
152 | #else
153 |    strcpy( chartmp , "dlopen(\"" ) ;
154 |    strcat( chartmp , Path ) ;
155 |    strcat( chartmp , "\") : " ) ;
193 | #else
194 | // cout << "Search of " << signature << " with handle " << hex << handle << dec << endl ;
195 |  if ( handle == NULL )
196 |    handle = osd_dlopen( NULL , 0 ) ;
197 | #endif
198 | 
{% endraw %}

```