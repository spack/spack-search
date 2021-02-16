---
name: "rose"
layout: package
next_package: xqilla
previous_package: ns-3-dev
languages: ['cpp', 'c']
---
## develop
57 / 31211 files match, 21 filtered matches.

 - [src/midend/astProcessing/plugin.C](#srcmidendastprocessingpluginc)
 - [src/midend/programTransformation/astOutlining/Preprocess.cc](#srcmidendprogramtransformationastoutliningpreprocesscc)
 - [src/midend/programTransformation/astOutlining/Transform.cc](#srcmidendprogramtransformationastoutliningtransformcc)
 - [src/midend/programTransformation/astOutlining/GenerateFunc.cc](#srcmidendprogramtransformationastoutlininggeneratefunccc)
 - [src/midend/programTransformation/astOutlining/Outliner.hh](#srcmidendprogramtransformationastoutliningoutlinerhh)
 - [src/midend/programTransformation/astOutlining/Outliner.cc](#srcmidendprogramtransformationastoutliningoutlinercc)
 - [src/midend/programTransformation/astOutlining/Insert.cc](#srcmidendprogramtransformationastoutlininginsertcc)
 - [src/frontend/Experimental_Csharp_ROSE_Connection/csharp_support.C](#srcfrontendexperimental_csharp_rose_connectioncsharp_supportc)
 - [src/frontend/SageIII/sageInterface/sageBuilder.C](#srcfrontendsageiiisageinterfacesagebuilderc)
 - [tutorial/outliner/outlineTutorial.cc](#tutorialoutlineroutlinetutorialcc)
 - [tests/nonsmoke/functional/roseTests/astOutliningTests/reference/autotuning_lib.c](#testsnonsmokefunctionalrosetestsastoutliningtestsreferenceautotuning_libc)
 - [tests/nonsmoke/functional/CompileTests/C_tests/test2012_19.c](#testsnonsmokefunctionalcompiletestsc_teststest2012_19c)
 - [tests/nonsmoke/functional/CompileTests/C_tests/test2012_102.c](#testsnonsmokefunctionalcompiletestsc_teststest2012_102c)
 - [tests/nonsmoke/functional/CompileTests/C_tests/test2012_28.c](#testsnonsmokefunctionalcompiletestsc_teststest2012_28c)
 - [tests/nonsmoke/functional/CompileTests/PythonExample_tests/pythonDir/pystate.h](#testsnonsmokefunctionalcompiletestspythonexample_testspythondirpystateh)
 - [projects/interpreter/interp_extcall.C](#projectsinterpreterinterp_extcallc)
 - [projects/autoTuning/autoTuningSupport.C](#projectsautotuningautotuningsupportc)
 - [projects/autoTuning/autotuning_lib.c](#projectsautotuningautotuning_libc)
 - [projects/autoTuning/doc/smg2000_harmony.c](#projectsautotuningdocsmg2000_harmonyc)
 - [projects/autoTuning/doc/smg2000_dlopen.c](#projectsautotuningdocsmg2000_dlopenc)
 - [projects/autoTuning/doc/smg2000_checkpoint2.c](#projectsautotuningdocsmg2000_checkpoint2c)

### src/midend/astProcessing/plugin.C

```c

{% raw %}
138 |       void * handle = dlopen(lib_file_name, RTLD_LAZY|RTLD_GLOBAL);
142 |         cout<<"Error in dlopen: error code: "<<dlerror()<<" when loading "<<lib_file_name <<endl;
{% endraw %}

```
### src/midend/programTransformation/astOutlining/Preprocess.cc

```cpp

{% raw %}
51 |   if (use_dlopen)
{% endraw %}

```
### src/midend/programTransformation/astOutlining/Transform.cc

```cpp

{% raw %}
436 |   printf ("In outlineBlock(): use_dlopen = %s \n",use_dlopen ? "true" : "false");
441 |   if (use_dlopen) 
463 |     SgFunctionCallExp* dlopen_call = buildFunctionCallExp(SgName(FIND_FUNCP_DLOPEN),ftype_return,arg_list, p_scope);
464 |     SgExprStatement * assign_stmt = buildAssignStatement(buildVarRefExp(func_name_str+"p",p_scope),dlopen_call);
491 |       printf ("use_dlopen == false: calling generateCall() \n");
495 |       printf ("DONE: use_dlopen == false: calling generateCall() \n");
{% endraw %}

```
### src/midend/programTransformation/astOutlining/GenerateFunc.cc

```cpp

{% raw %}
1101 |       {     // this is to be compatible with dlopen() runtime's function pointer type
{% endraw %}

```
### src/midend/programTransformation/astOutlining/Outliner.hh

```cpp

{% raw %}
72 |   ROSE_DLL_API extern bool use_dlopen; // Outlining the target to a separated file and calling it using a dlopen() scheme. It turns on useNewFile.
{% endraw %}

```
### src/midend/programTransformation/astOutlining/Outliner.cc

```cpp

{% raw %}
42 |   bool use_dlopen=false; // Outlining the target to a separated file and calling it using a dlopen() scheme. It turns on useNewFile.
76 |   if (use_dlopen)  
85 |   if (use_dlopen)
238 |     switches.insert(Switch("use_dlopen")
239 |                     .intrinsicValue(true, use_dlopen)
240 |                     .doc("Use @man{dlopen}(3) to find an outlined function saved into a new source file."));
304 |     if (use_dlopen) {
407 |   if (CommandlineProcessing::isOption (argvList,"-rose:outline:","use_dlopen",true))
410 |       cout<<"Using dlopen() to find an outilned function saved into a new source file ..."<<endl;
411 |     use_dlopen = true;
442 |  if (use_dlopen || temp_variable)    
467 |     cout<<"\t-rose:outline:use_dlopen                       use dlopen() to find the outlined functions saved in new files.It will turn on new_file and parameter_wrapper flags internally"<<endl;
468 |     cout<<"\t-rose:outline:copy_orig_file                   used with dlopen(): single lib source file copied from the entire original input file. All generated outlined functions are appended to the lib source file"<<endl;
{% endraw %}

```
### src/midend/programTransformation/astOutlining/Insert.cc

```cpp

{% raw %}
1522 |    printf ("$$$$$$$$$$$$$$$ In Outliner::insert(): use_dlopen = %s \n",use_dlopen == true ? "true" : "false");
1527 |    if (use_dlopen) 
1544 |      printf ("############ In Outliner::insert(): use_dlopen == true: Calling SageInterface::insertStatementBefore: func = %p name = %s src_global = %p friendFunctionPrototypeList.size() = %zu \n",
1562 |    if (use_dlopen == false && SageInterface::is_Fortran_language() == false ) // C/C++ only
1570 |      printf ("############ Calling insertGlobalPrototype(): use_dlopen == false: func = %p name = %s src_global = %p friendFunctionPrototypeList.size() = %zu \n",
{% endraw %}

```
### src/frontend/Experimental_Csharp_ROSE_Connection/csharp_support.C

```c

{% raw %}
19 |      printf ("In C++ process(): calling dlopen() lib = %s \n",lib.c_str());
21 |      handle = dlopen (lib.c_str(), RTLD_LAZY);
{% endraw %}

```
### src/frontend/SageIII/sageInterface/sageBuilder.C

```c

{% raw %}
16783 |      printf ("In SageBuilder::buildFile(): Outliner::use_dlopen = %s \n",Outliner::use_dlopen ? "true" : "false");
16791 |      if (!Outliner::use_dlopen)
16794 |           printf ("In SageBuilder::buildFile(): (after test for (!Outliner::use_dlopen) == true: project = %p project->get_fileList_ptr()->get_listOfFiles().size() = %" PRIuPTR " \n",project,project->get_fileList_ptr()->get_listOfFiles().size());
16805 |           printf ("In SageBuilder::buildFile(): (after test for (!Outliner::use_dlopen) == false: project = %p project->get_fileList_ptr()->get_listOfFiles().size() = %" PRIuPTR " \n",project,project->get_fileList_ptr()->get_listOfFiles().size());
{% endraw %}

```
### tutorial/outliner/outlineTutorial.cc

```cpp

{% raw %}
143 |       std::cout <<"  use_dlopen          = " <<Outliner::use_dlopen <<"\n";
{% endraw %}

```
### tests/nonsmoke/functional/roseTests/astOutliningTests/reference/autotuning_lib.c

```c

{% raw %}
32 |   functionLib = dlopen(lib_name, RTLD_LAZY);
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/C_tests/test2012_19.c

```c

{% raw %}
5039 | extern void *dlopen (__const char *__file, int __mode) __attribute__ ((__nothrow__));
5584 |  void *dlopen_ref;
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/C_tests/test2012_102.c

```c

{% raw %}
12713 | extern void *dlopen (__const char *__file, int __mode) __attribute__ ((__nothrow__));
12861 |  ret = dlopen(unmeta(buf), 0x00001 | 0x00100);
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/C_tests/test2012_28.c

```c

{% raw %}
5039 | extern void *dlopen (__const char *__file, int __mode) __attribute__ ((__nothrow__));
7836 |  void *dlopen_ref;
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/PythonExample_tests/pythonDir/pystate.h

```c

{% raw %}
26 |     int dlopenflags;
{% endraw %}

```
### projects/interpreter/interp_extcall.C

```c

{% raw %}
266 |      DL(const char *filename, int flag) : dl(dlopen(filename, flag))
285 |      void *libc = dlopen("libc.so.6", RTLD_NOW | RTLD_GLOBAL);
287 |          libc = dlopen("libc.dylib", RTLD_NOW | RTLD_GLOBAL); // Mac OS X
{% endraw %}

```
### projects/autoTuning/autoTuningSupport.C

```c

{% raw %}
29 |     Outliner::use_dlopen= true;
{% endraw %}

```
### projects/autoTuning/autotuning_lib.c

```c

{% raw %}
32 |   functionLib = dlopen(lib_name, RTLD_LAZY);
{% endraw %}

```
### projects/autoTuning/doc/smg2000_harmony.c

```c

{% raw %}
26 |     FunctionLib = dlopen("./unrolled_versions.so",RTLD_LAZY);
{% endraw %}

```
### projects/autoTuning/doc/smg2000_dlopen.c

```c

{% raw %}
20 |   FunctionLib = dlopen ("OUT__1__6755__.so",RTLD_LAZY);
{% endraw %}

```
### projects/autoTuning/doc/smg2000_checkpoint2.c

```c

{% raw %}
51 |   FunctionLib =dlopen("OUT__1__6755__.so", RTLD_LAZY);
{% endraw %}

```