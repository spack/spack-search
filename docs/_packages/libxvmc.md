---
name: "libxvmc"
layout: package
next_package: libyogrt
previous_package: libxsmm
languages: ['c']
---
## 1.0.9
4 / 24 files match, 1 filtered matches.

 - [wrapper/XvMCWrapper.c](#wrapperxvmcwrapperc)

### wrapper/XvMCWrapper.c

```c

{% raw %}
203 |  */
204 | 
205 | 
206 | static void  *dlopenversion(const char *lib, const char *version, int flag)
207 | {
208 |   void *ret;
221 |       strncat( curName, version, verLen);
222 |     }
223 |   }
224 |   ret = dlopen(curName, flag);
225 |   free(curName);
226 |   return ret;
238 |     wrapperPreInit = 1;
239 |     xW.preInitialised = 0;
240 |     xW.initialised = 0;
241 |     xvhandle = dlopenversion("libXv.so", XV_SOVERSION, RTLD_LAZY | RTLD_GLOBAL);
242 |     if (!xvhandle) {
243 | 	fprintf(stderr,"XvMCWrapper: Warning! Could not open shared "
244 | 		"library \"libXv.so" XV_SOVERSION "\"\nThis may cause relocation "
245 | 		"errors later.\nError was: \"%s\".\n",dlerror());
246 |     }
247 |     handle2 = dlopenversion("libXvMC.so", XVMC_SOVERSION, RTLD_LAZY | RTLD_GLOBAL);
248 |     if (!handle2) {
249 | 	fprintf(stderr,"XvMCWrapper: Could not load XvMC "
304 | 	strncpy(nameBuffer + nameLen, ".so", BUFLEN-nameLen-1);
305 | 	nameBuffer[BUFLEN-1] = 0;
306 | 	XFree(clientName);
307 | 	handle = dlopenversion(nameBuffer, XVMC_SOVERSION,RTLD_LAZY);
308 |     } else {
309 | 	/*
349 | 		return;
350 | 	    }
351 | 	}
352 | 	handle = dlopen(nameBuffer,RTLD_LAZY);
353 |     }
354 |     if (!handle) {
{% endraw %}

```