---
name: "sollya"
layout: package
next_package: papi
previous_package: plumed
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 7.0
4 / 1132 files match, 2 filtered matches.

 - [library.c](#libraryc)
 - [external.c](#externalc)

### library.c

```c

{% raw %}
582 |   }
583 | 
584 |   dlerror();
585 |   myFunction = (int (*)(sollya_mpfi_t, sollya_mpfi_t, int)) dlsym(libHandle->libraryDescriptor, functionName);
586 |   if ((error = dlerror()) != NULL) {
587 |     printMessage(1, SOLLYA_MSG_EXTERNAL_FUNC_OR_PROC_NOT_FOUND_IN_LIBRARY, "Error: could not find function \"%s\" in library \"%s\" for binding: %s\n",functionName,libraryName,error);
763 |     currLibHandle = (libraryHandle *) currLibList->value;
764 |     if (!(currLibHandle->shallowCopy)) {
765 |       dlerror();
766 |       myFunction = (int (*)(void)) dlsym(currLibHandle->libraryDescriptor, "sollya_external_lib_close");
767 |       if (dlerror() == NULL) {
768 | 	enterExternalCode();
830 |   }
831 | 
832 |   dlerror();
833 |   myFunction = (void (*)(mpfr_t, mp_prec_t)) dlsym(libHandle->libraryDescriptor, functionName);
834 |   if ((error = dlerror()) != NULL) {
835 |     printMessage(1, SOLLYA_MSG_EXTERNAL_FUNC_OR_PROC_NOT_FOUND_IN_LIBRARY, "Error: could not find function \"%s\" in library \"%s\" for binding: %s\n",functionName,libraryName,error);
1009 |     currLibHandle = (libraryHandle *) currLibList->value;
1010 |     if (!(currLibHandle->shallowCopy)) {
1011 |       dlerror();
1012 |       myFunction = (int (*)(void)) dlsym(currLibHandle->libraryDescriptor, "sollya_external_lib_close");
1013 |       if (dlerror() == NULL) {
1014 | 	enterExternalCode();
1073 |   }
1074 | 
1075 |   dlerror();
1076 |   myFunction = dlsym(libHandle->libraryDescriptor, procedureName);
1077 |   if ((error = dlerror()) != NULL) {
1078 |     printMessage(1, SOLLYA_MSG_EXTERNAL_FUNC_OR_PROC_NOT_FOUND_IN_LIBRARY, "Error: could not find function \"%s\" in library \"%s\" for binding: %s\n",procedureName,libraryName,error);
1277 |     currLibHandle = (libraryHandle *) currLibList->value;
1278 |     if (!(currLibHandle->shallowCopy)) {
1279 |       dlerror();
1280 |       myFunction = (int (*)(void)) dlsym(currLibHandle->libraryDescriptor, "sollya_external_lib_close");
1281 |       if (dlerror() == NULL) {
1282 | 	enterExternalCode();
{% endraw %}

```
### external.c

```c

{% raw %}
317 |   }
318 | 
319 |   dlerror(); /* Clear any existing error */
320 |   myFunction = (void (*)(mpfr_t, mpfr_t)) dlsym(descr, "f");
321 |   if ((error = dlerror()) != NULL) {
322 |     printMessage(1, SOLLYA_MSG_EXTERNALPLOT_DID_NOT_FIND_FUNCTION_F, "Error: the function f cannot be found in library %s (%s)\n",library,error);
{% endraw %}

```