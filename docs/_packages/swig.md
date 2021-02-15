---
name: "swig"
layout: package
next_package: findutils
previous_package: qemu
languages: []
---
## 2.0.12
4 / 3828 files match

 - [configure.ac](#configureac)
 - [Lib/d/wrapperloader.swg](#libdwrapperloaderswg)
 - [Lib/mzscheme/mzrun.swg](#libmzschememzrunswg)
 - [Source/Modules/mzscheme.cxx](#sourcemodulesmzschemecxx)

### configure.ac

```

{% raw %}
381 | AC_CHECK_LIB(dl, dlopen)	# Dynamic linking for SunOS/Solaris and SYSV
{% endraw %}

```
### Lib/d/wrapperloader.swg

```

{% raw %}
119 |         void *dlopen(CCPTR file, int mode);
129 |       return dlopen(swigToCString(libName), RTLD_NOW);
{% endraw %}

```
### Lib/mzscheme/mzrun.swg

```

{% raw %}
263 |   static char **mz_dlopen_libraries=NULL;
267 |   static void mz_set_dlopen_libraries(const char *_libs)
343 |       mz_dlopen_libraries=(char **) malloc(sizeof(char *)*(k+1));
344 |       mz_dlopen_libraries[0]=libs;
348 | 	  mz_dlopen_libraries[k++]=&libs[i+1];
356 |       mz_dlopen_libraries[k]=NULL;
373 |     if (mz_dlopen_libraries==NULL) {
379 |         for(n=0;mz_dlopen_libraries[n]!=NULL;n++);
386 | 	   fprintf(stderr,"SWIG:mzscheme:loading %s\n",mz_dlopen_libraries[i]);
389 | 	  mz_libraries[i]=(void *) LoadLibrary(mz_dlopen_libraries[i]); 
391 | 	  mz_libraries[i]=(void *) dlopen(mz_dlopen_libraries[i],RTLD_LAZY); 
397 | 	      int L=strlen(mz_dynload_libpaths[k])+strlen("\\")+strlen(mz_dlopen_libraries[i])+1;
400 | 	      sprintf(libp,"%s\\%s",mz_dynload_libpaths[k],mz_dlopen_libraries[i]);
403 | 	      sprintf(libp,"%s/%s",mz_dynload_libpaths[k],mz_dlopen_libraries[i]);
404 | 	      mz_libraries[i]=(void *) dlopen(libp,RTLD_LAZY); 
418 |         for(i=0;mz_dlopen_libraries[i]!=NULL && func==NULL;i++) {
428 | 		    "SWIG:mzscheme:library:%s;dlopen=%p,function=%s,func=%p\n",
429 | 		    mz_dlopen_libraries[i],mz_libraries[i],function,func
{% endraw %}

```
### Source/Modules/mzscheme.cxx

```

{% raw %}
175 | 	Printf(f_init, "mz_set_dlopen_libraries(\"%s\");\n", load_libraries);
{% endraw %}

```