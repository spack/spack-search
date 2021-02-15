---
name: "fermisciencetools"
layout: package
next_package: fastx-toolkit
previous_package: timemory
languages: ['cpp', 'python']
---
## 11r5p3
16 / 15648 files match

 - [x86_64-unknown-linux-gnu-libc2.17/lib/libgsl.la](#x86_64-unknown-linux-gnu-libc217liblibgslla)
 - [x86_64-unknown-linux-gnu-libc2.17/lib/libxerces-c.la](#x86_64-unknown-linux-gnu-libc217liblibxerces-cla)
 - [x86_64-unknown-linux-gnu-libc2.17/lib/libMinuit2.la](#x86_64-unknown-linux-gnu-libc217liblibminuit2la)
 - [x86_64-unknown-linux-gnu-libc2.17/lib/libcppunit.la](#x86_64-unknown-linux-gnu-libc217liblibcppunitla)
 - [x86_64-unknown-linux-gnu-libc2.17/lib/libfftw3.la](#x86_64-unknown-linux-gnu-libc217liblibfftw3la)
 - [x86_64-unknown-linux-gnu-libc2.17/lib/libgslcblas.la](#x86_64-unknown-linux-gnu-libc217liblibgslcblasla)
 - [x86_64-unknown-linux-gnu-libc2.17/lib/libhealpix_cxx.la](#x86_64-unknown-linux-gnu-libc217liblibhealpix_cxxla)
 - [x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/test/test_sys.py](#x86_64-unknown-linux-gnu-libc217libpython27testtest_syspy)
 - [x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/distutils/tests/setuptools_build_ext.py](#x86_64-unknown-linux-gnu-libc217libpython27distutilstestssetuptools_build_extpy)
 - [x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/ctypes/__init__.py](#x86_64-unknown-linux-gnu-libc217libpython27ctypes__init__py)
 - [x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/ctypes/test/test_find.py](#x86_64-unknown-linux-gnu-libc217libpython27ctypestesttest_findpy)
 - [x86_64-unknown-linux-gnu-libc2.17/include/python2.7/pystate.h](#x86_64-unknown-linux-gnu-libc217includepython27pystateh)
 - [x86_64-unknown-linux-gnu-libc2.17/include/python2.7/pyconfig.h](#x86_64-unknown-linux-gnu-libc217includepython27pyconfigh)
 - [x86_64-unknown-linux-gnu-libc2.17/share/swig/1.3.31/mzscheme/mzrun.swg](#x86_64-unknown-linux-gnu-libc217shareswig1331mzschememzrunswg)
 - [x86_64-unknown-linux-gnu-libc2.17/BUILD_DIR/hmake.out](#x86_64-unknown-linux-gnu-libc217build_dirhmakeout)
 - [x86_64-unknown-linux-gnu-libc2.17/BUILD_DIR/configure.out](#x86_64-unknown-linux-gnu-libc217build_dirconfigureout)

### x86_64-unknown-linux-gnu-libc2.17/lib/libgsl.la

```

{% raw %}
6 | # The name that we can dlopen(3).
35 | # Files to dlopen/dlpreopen
36 | dlopen=''
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/lib/libxerces-c.la

```

{% raw %}
6 | # The name that we can dlopen(3).
35 | # Files to dlopen/dlpreopen
36 | dlopen=''
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/lib/libMinuit2.la

```

{% raw %}
6 | # The name that we can dlopen(3).
29 | # Files to dlopen/dlpreopen
30 | dlopen=''
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/lib/libcppunit.la

```

{% raw %}
6 | # The name that we can dlopen(3).
29 | # Files to dlopen/dlpreopen
30 | dlopen=''
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/lib/libfftw3.la

```

{% raw %}
6 | # The name that we can dlopen(3).
29 | # Files to dlopen/dlpreopen
30 | dlopen=''
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/lib/libgslcblas.la

```

{% raw %}
6 | # The name that we can dlopen(3).
35 | # Files to dlopen/dlpreopen
36 | dlopen=''
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/lib/libhealpix_cxx.la

```

{% raw %}
6 | # The name that we can dlopen(3).
35 | # Files to dlopen/dlpreopen
36 | dlopen=''
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/test/test_sys.py

```python

{% raw %}
248 |     @unittest.skipUnless(hasattr(sys, "setdlopenflags"),
249 |                          'test needs sys.setdlopenflags()')
250 |     def test_dlopenflags(self):
251 |         self.assertTrue(hasattr(sys, "getdlopenflags"))
252 |         self.assertRaises(TypeError, sys.getdlopenflags, 42)
253 |         oldflags = sys.getdlopenflags()
254 |         self.assertRaises(TypeError, sys.setdlopenflags)
255 |         sys.setdlopenflags(oldflags+1)
256 |         self.assertEqual(sys.getdlopenflags(), oldflags+1)
257 |         sys.setdlopenflags(oldflags)
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/distutils/tests/setuptools_build_ext.py

```python

{% raw %}
223 |                 if_dl("   old_flags = sys.getdlopenflags()"),
227 |                 if_dl("     sys.setdlopenflags(dl.RTLD_NOW)"),
230 |                 if_dl("     sys.setdlopenflags(old_flags)"),
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/ctypes/__init__.py

```python

{% raw %}
111 |     from _ctypes import LoadLibrary as _dlopen
140 |     from _ctypes import dlopen as _dlopen
364 |             self._handle = _dlopen(self._name, mode)
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/lib/python2.7/ctypes/test/test_find.py

```python

{% raw %}
67 | # On MAC OSX, it won't work either, because dlopen() needs a full path,
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/include/python2.7/pystate.h

```cpp

{% raw %}
29 | #ifdef HAVE_DLOPEN
30 |     int dlopenflags;
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/include/python2.7/pyconfig.h

```cpp

{% raw %}
183 | /* Define to 1 if you have the `dlopen' function. */
184 | #define HAVE_DLOPEN 1
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/share/swig/1.3.31/mzscheme/mzrun.swg

```

{% raw %}
254 | /*** DLOPEN PATCH ******************************************************
268 |   static char **mz_dlopen_libraries=NULL;
272 |   static void mz_set_dlopen_libraries(const char *_libs)
348 |       mz_dlopen_libraries=(char **) malloc(sizeof(char *)*(k+1));
349 |       mz_dlopen_libraries[0]=libs;
353 | 	  mz_dlopen_libraries[k++]=&libs[i+1];
361 |       mz_dlopen_libraries[k]=NULL;
378 |     if (mz_dlopen_libraries==NULL) {
384 |         for(n=0;mz_dlopen_libraries[n]!=NULL;n++);
391 | 	   fprintf(stderr,"SWIG:mzscheme:loading %s\n",mz_dlopen_libraries[i]);
394 | 	  mz_libraries[i]=(void *) LoadLibrary(mz_dlopen_libraries[i]); 
396 | 	  mz_libraries[i]=(void *) dlopen(mz_dlopen_libraries[i],RTLD_LAZY); 
402 | 	      int L=strlen(mz_dynload_libpaths[k])+strlen("\\")+strlen(mz_dlopen_libraries[i])+1;
405 | 	      sprintf(libp,"%s\\%s",mz_dynload_libpaths[k],mz_dlopen_libraries[i]);
408 | 	      sprintf(libp,"%s/%s",mz_dynload_libpaths[k],mz_dlopen_libraries[i]);
409 | 	      mz_libraries[i]=(void *) dlopen(libp,RTLD_LAZY); 
423 |         for(i=0;mz_dlopen_libraries[i]!=NULL && func==NULL;i++) {
433 | 		    "SWIG:mzscheme:library:%s;dlopen=%p,function=%s,func=%p\n",
434 | 		    mz_dlopen_libraries[i],mz_libraries[i],function,func
444 | /*** DLOPEN PATCH ******************************************************
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/BUILD_DIR/hmake.out

```

{% raw %}
9998 |  PyDoc_STRVAR(setdlopenflags_doc,
{% endraw %}

```
### x86_64-unknown-linux-gnu-libc2.17/BUILD_DIR/configure.out

```

{% raw %}
79 | checking for dlopen in -ldl... yes
532 | checking for dlopen in -ldl... yes
601 | checking for dlopen in -ldl... yes
731 | checking for dlopen in -ldl... yes
929 | checking for dlopen in -ldl... yes
1525 | checking for dlopen in -ldl... yes
2131 | checking for dlopen in -ldl... yes
2159 | checking for dlopen... yes
2781 | checking for dlopen in -ldl... yes
3250 | checking for dlopen in -ldl... yes
{% endraw %}

```