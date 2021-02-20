---
name: "rose"
layout: package
next_package: rr
previous_package: root
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
135 |     for (size_t i=0; i< PluginLibs.size(); i++)
136 |     {
137 |       const char* lib_file_name= PluginLibs[i].c_str();
138 |       void * handle = dlopen(lib_file_name, RTLD_LAZY|RTLD_GLOBAL);
139 | 
140 |       if (!handle)
141 |       {
142 |         cout<<"Error in dlopen: error code: "<<dlerror()<<" when loading "<<lib_file_name <<endl;
143 |         exit(1);
144 |       }
{% endraw %}

```
### src/midend/programTransformation/astOutlining/Preprocess.cc

```cpp

{% raw %}
48 |   checkAndPatchUpOptions();
49 | 
50 |   // insert a header to support outlining for auto tuning
51 |   if (use_dlopen)
52 |   {
53 |     const string file_name = s->get_file_info()->get_filename();
{% endraw %}

```
### src/midend/programTransformation/astOutlining/Transform.cc

```cpp

{% raw %}
433 |   ROSE_ASSERT(func->get_definition()->get_body()->get_parent() == func->get_definition());
434 | 
435 | #if 0
436 |   printf ("In outlineBlock(): use_dlopen = %s \n",use_dlopen ? "true" : "false");
437 | #endif
438 | 
439 |   SgStatement *func_call = NULL;
440 |   SgVarRefExp* wrapper_exp = NULL; 
441 |   if (use_dlopen) 
442 |     // if dlopen() is used, insert a lib call to find the function pointer from a shared lib file
443 |     // e.g. OUT__2__8072__p = findFunctionUsingDlopen("OUT__2__8072__", "OUT__2__8072__.so");
460 | //e.g.
461 | // OUT_1_test_26_2020_0p = findFunctionUsingDlopen("OUT_1_test_26_2020_0","test_26_2020/rose_test_26_2020_lib.so");  
462 |     SgExprListExp* arg_list = buildExprListExp(buildStringVal(func_name_str), buildStringVal(lib_name)); 
463 |     SgFunctionCallExp* dlopen_call = buildFunctionCallExp(SgName(FIND_FUNCP_DLOPEN),ftype_return,arg_list, p_scope);
464 |     SgExprStatement * assign_stmt = buildAssignStatement(buildVarRefExp(func_name_str+"p",p_scope),dlopen_call);
465 |     SageInterface::insertStatementBefore(s, assign_stmt);
466 |     // Generate a function call using the func pointer
488 |   else  // regular function call for other cases
489 |     {
490 | #if 0
491 |       printf ("use_dlopen == false: calling generateCall() \n");
492 | #endif
493 |       func_call = generateCall (func, syms, readOnlyVars, wrapper_name,p_scope);
494 | #if 0
495 |       printf ("DONE: use_dlopen == false: calling generateCall() \n");
496 | #endif
497 |     }
{% endraw %}

```
### src/midend/programTransformation/astOutlining/GenerateFunc.cc

```cpp

{% raw %}
1098 |         ptype = buildPointerType (buildVoidType());
1099 |       }
1100 |       else // use array of pointers, regardless of the pass-by-value vs. pass-by-reference difference
1101 |       {     // this is to be compatible with dlopen() runtime's function pointer type
1102 |         ptype= buildPointerType(buildPointerType(buildVoidType()));
1103 |       }
{% endraw %}

```
### src/midend/programTransformation/astOutlining/Outliner.hh

```cpp

{% raw %}
69 |   ROSE_DLL_API extern bool enable_debug; // output debug information for outliner
70 |   ROSE_DLL_API extern bool exclude_headers; // exclude headers from the new file containing outlined functions
71 |   ROSE_DLL_API extern bool enable_liveness; // enable liveness analysis to reduce restoring statements when temp variables are used
72 |   ROSE_DLL_API extern bool use_dlopen; // Outlining the target to a separated file and calling it using a dlopen() scheme. It turns on useNewFile.
73 | 
74 |   ROSE_DLL_API extern bool enable_template;  // Enabling outlining code blocks inside template functions
{% endraw %}

```
### src/midend/programTransformation/astOutlining/Outliner.cc

```cpp

{% raw %}
39 |   bool enable_debug=true; // 
40 | #endif
41 |   bool exclude_headers=false;
42 |   bool use_dlopen=false; // Outlining the target to a separated file and calling it using a dlopen() scheme. It turns on useNewFile.
43 |   bool enable_template=false; // Outlining code blocks inside C++ templates
44 |   bool select_omp_loop = false;  // Find OpenMP for loops and outline them. This is used for testing purposes.
73 | {
74 |   // Generate a prefix.
75 |   stringstream s;
76 |   if (use_dlopen)  
77 |     s<< g_outlined_func_names2.next();
78 |   else
82 |   // tag.
83 |   const Sg_File_Info* info = stmt->get_startOfConstruct ();
84 |   ROSE_ASSERT (info);
85 |   if (use_dlopen)
86 |   {
87 |     const string file_name = info->get_raw_filename ();
235 |                     .intrinsicValue(true, temp_variable)
236 |                     .doc("Enable using temp variables to reduce pointer dereferencing for outlined functions."));
237 | 
238 |     switches.insert(Switch("use_dlopen")
239 |                     .intrinsicValue(true, use_dlopen)
240 |                     .doc("Use @man{dlopen}(3) to find an outlined function saved into a new source file."));
241 | 
242 |     switches.insert(Switch("enable_template")
301 |         useParameterWrapper = true;
302 |     }
303 |     //    use_dlopen = false;
304 |     if (use_dlopen) {
305 |         // turn on useNewFile as a side effect
306 |         useNewFile= true;
404 |   //  else
405 |   //    temp_variable = false;
406 |  
407 |   if (CommandlineProcessing::isOption (argvList,"-rose:outline:","use_dlopen",true))
408 |   {
409 |     if (enable_debug)
410 |       cout<<"Using dlopen() to find an outilned function saved into a new source file ..."<<endl;
411 |     use_dlopen = true;
412 |   }
413 |   //  else   // this option may be set by other module
439 |     argvList.push_back("-rose:openmp:ast_only");
440 |   }
441 |  
442 |  if (use_dlopen || temp_variable)    
443 |   {
444 |     if (CommandlineProcessing::isOption (argvList,"-rose:outline:","enable_liveness",true))
464 |     cout<<"\t-rose:outline:new_file                         use a new source file for the generated outlined function"<<endl;
465 |     cout<<"\t-rose:outline:output_path                      the path to store newly generated files for outlined functions, if requested by new_file. The original source file's path is used by default."<<endl;
466 |     cout<<"\t-rose:outline:exclude_headers                  do not include any headers in the new file for outlined functions"<<endl;
467 |     cout<<"\t-rose:outline:use_dlopen                       use dlopen() to find the outlined functions saved in new files.It will turn on new_file and parameter_wrapper flags internally"<<endl;
468 |     cout<<"\t-rose:outline:copy_orig_file                   used with dlopen(): single lib source file copied from the entire original input file. All generated outlined functions are appended to the lib source file"<<endl;
469 |     cout<<"\t-rose:outline:enable_template                  support outlining code blocks inside C++ templates (experimental)"<<endl;
470 |     cout<<"\t-rose:outline:enable_debug                     run outliner in a debugging mode"<<endl;
{% endraw %}

```
### src/midend/programTransformation/astOutlining/Insert.cc

```cpp

{% raw %}
1519 |    SgFunctionDeclaration* sourceFileFunctionPrototype = NULL;
1520 | 
1521 | #if 0
1522 |    printf ("$$$$$$$$$$$$$$$ In Outliner::insert(): use_dlopen = %s \n",use_dlopen == true ? "true" : "false");
1523 | #endif
1524 | 
1525 |    // insert a pointer to function declaration if use_dlopen is true
1526 |    // insert it into the original global scope
1527 |    if (use_dlopen) 
1528 |    {
1529 |     // void (*OUT_xxx__p) (void**); // this parameter type depends on the number of variables. If zero variables, empty parameter.
1541 |      SgVariableDeclaration * ptofunc = buildVariableDeclaration(var_name,buildPointerType(ftype), NULL, target_outlined_code->get_scope());
1542 | 
1543 | #if 0
1544 |      printf ("############ In Outliner::insert(): use_dlopen == true: Calling SageInterface::insertStatementBefore: func = %p name = %s src_global = %p friendFunctionPrototypeList.size() = %zu \n",
1545 |           func,func->get_name().str(),src_global,friendFunctionPrototypeList.size());
1546 |         {
1559 | //   We still generate the prototype even they are not needed if dlopen() is used. 
1560 | //   since SageInterface::appendStatementWithDependentDeclaration() depends on it
1561 | // if (SageInterface::is_Fortran_language() == false ) // C/C++ only
1562 |    if (use_dlopen == false && SageInterface::is_Fortran_language() == false ) // C/C++ only
1563 |    {
1564 |      // This is done in the original file (does not effect the separate file if we outline the function there)
1567 |      // insertGlobalPrototype (func, protos, src_global, target_func);
1568 | 
1569 | #if 0
1570 |      printf ("############ Calling insertGlobalPrototype(): use_dlopen == false: func = %p name = %s src_global = %p friendFunctionPrototypeList.size() = %zu \n",
1571 |           func,func->get_name().str(),src_global,friendFunctionPrototypeList.size());
1572 | #endif
{% endraw %}

```
### src/frontend/Experimental_Csharp_ROSE_Connection/csharp_support.C

```c

{% raw %}
16 |      void (*process)(char*,char*) = NULL;
17 |      char *error           = NULL;
18 | 
19 |      printf ("In C++ process(): calling dlopen() lib = %s \n",lib.c_str());
20 | 
21 |      handle = dlopen (lib.c_str(), RTLD_LAZY);
22 | 
23 |      printf ("In C++ process(): handle = %p \n",handle);
{% endraw %}

```
### src/frontend/SageIII/sageInterface/sageBuilder.C

```c

{% raw %}
16780 |      result->set_parent(project);
16781 | 
16782 | #if 0
16783 |      printf ("In SageBuilder::buildFile(): Outliner::use_dlopen = %s \n",Outliner::use_dlopen ? "true" : "false");
16784 | #endif
16785 | 
16788 |   // Java support is used the true branch is taken.  However, if might be the we need
16789 |   // to support the outliner using the code below and so this would be a bug for the
16790 |   // outliner.
16791 |      if (!Outliner::use_dlopen)
16792 |         {
16793 | #if 0
16794 |           printf ("In SageBuilder::buildFile(): (after test for (!Outliner::use_dlopen) == true: project = %p project->get_fileList_ptr()->get_listOfFiles().size() = %" PRIuPTR " \n",project,project->get_fileList_ptr()->get_listOfFiles().size());
16795 | #endif
16796 |        // DQ (3/5/2014): If we added the file above, then don't add it here since it is redundant.
16802 |        else
16803 |         {
16804 | #if 0
16805 |           printf ("In SageBuilder::buildFile(): (after test for (!Outliner::use_dlopen) == false: project = %p project->get_fileList_ptr()->get_listOfFiles().size() = %" PRIuPTR " \n",project,project->get_fileList_ptr()->get_listOfFiles().size());
16806 | #endif
16807 | 
{% endraw %}

```
### tutorial/outliner/outlineTutorial.cc

```cpp

{% raw %}
140 |       std::cout <<"  exclude_headers     = " <<Outliner::exclude_headers <<"\n";
141 |       std::cout <<"  enable_classic      = " <<Outliner::enable_classic <<"\n";
142 |       std::cout <<"  temp_variable       = " <<Outliner::temp_variable <<"\n";
143 |       std::cout <<"  use_dlopen          = " <<Outliner::use_dlopen <<"\n";
144 |       std::cout <<"  handles             = [";
145 |       BOOST_FOREACH (const std::string &handle, Outliner::handles)
{% endraw %}

```
### tests/nonsmoke/functional/roseTests/astOutliningTests/reference/autotuning_lib.c

```c

{% raw %}
29 |   funcPointerT result =0;
30 |   // overhead is too high for iterative algorithm
31 |   // TODO: buffering this?
32 |   functionLib = dlopen(lib_name, RTLD_LAZY);
33 |   dlError = dlerror();
34 |   if( dlError ) {
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/C_tests/test2012_19.c

```c

{% raw %}
5036 | 
5037 | 
5038 | 
5039 | extern void *dlopen (__const char *__file, int __mode) __attribute__ ((__nothrow__));
5040 | 
5041 | 
5581 | 
5582 | typedef struct {
5583 |  cherokee_plugin_info_t *info;
5584 |  void *dlopen_ref;
5585 |  cherokee_boolean_t built_in;
5586 | } cherokee_plugin_loader_entry_t;
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/C_tests/test2012_102.c

```c

{% raw %}
12710 | 
12711 | 
12712 | 
12713 | extern void *dlopen (__const char *__file, int __mode) __attribute__ ((__nothrow__));
12714 | 
12715 | 
12858 |  if (l + (**pp ? strlen(*pp) : 1) > 4096)
12859 |      continue;
12860 |  sprintf(buf, "%s/%s.%s", **pp ? *pp : ".", name, "so");
12861 |  ret = dlopen(unmeta(buf), 0x00001 | 0x00100);
12862 |     }
12863 | 
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/C_tests/test2012_28.c

```c

{% raw %}
5036 | 
5037 | 
5038 | 
5039 | extern void *dlopen (__const char *__file, int __mode) __attribute__ ((__nothrow__));
5040 | 
5041 | 
7833 | 
7834 | typedef struct {
7835 |  cherokee_plugin_info_t *info;
7836 |  void *dlopen_ref;
7837 |  cherokee_boolean_t built_in;
7838 | } cherokee_plugin_loader_entry_t;
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/PythonExample_tests/pythonDir/pystate.h

```c

{% raw %}
23 | 
24 |     int checkinterval;
25 | #ifdef HAVE_DLOPEN
26 |     int dlopenflags;
27 | #endif
28 | 
{% endraw %}

```
### projects/interpreter/interp_extcall.C

```c

{% raw %}
263 |      void *dl;
264 | 
265 |      public:
266 |      DL(const char *filename, int flag) : dl(dlopen(filename, flag))
267 |         {
268 |           if (dl == NULL)
282 |    {
283 |      vector<void *> libs;
284 | 
285 |      void *libc = dlopen("libc.so.6", RTLD_NOW | RTLD_GLOBAL);
286 |      if (NULL==libc)
287 |          libc = dlopen("libc.dylib", RTLD_NOW | RTLD_GLOBAL); // Mac OS X
288 |      if (NULL==libc)
289 |          throw InterpError(string("Couldn't load libc: ") + dlerror());
{% endraw %}

```
### projects/autoTuning/autoTuningSupport.C

```c

{% raw %}
26 |   void autotuning_command_processing(vector<string>&argvList)
27 |   {
28 |     // let outliner get a chance
29 |     Outliner::use_dlopen= true;
30 |     Outliner::commandLineProcessing(argvList);
31 | 
{% endraw %}

```
### projects/autoTuning/autotuning_lib.c

```c

{% raw %}
29 |   funcPointerT result =0;
30 |   // overhead is too high for iterative algorithm
31 |   // TODO: buffering this?
32 |   functionLib = dlopen(lib_name, RTLD_LAZY);
33 |   dlError = dlerror();
34 |   if( dlError ) {
{% endraw %}

```
### projects/autoTuning/doc/smg2000_harmony.c

```c

{% raw %}
23 |   {
24 |     /* Only load the lib for the first time, reuse it later on */
25 |     printf("Opening the .so file ...\n");
26 |     FunctionLib = dlopen("./unrolled_versions.so",RTLD_LAZY);
27 |     dlError = dlerror();
28 |     if( dlError ) {
{% endraw %}

```
### projects/autoTuning/doc/smg2000_dlopen.c

```c

{% raw %}
17 |   /*  Pointer to error string   */
18 |   const char *dlError;		
19 | 
20 |   FunctionLib = dlopen ("OUT__1__6755__.so",RTLD_LAZY);
21 |   dlError = dlerror ();
22 |   if (dlError)
{% endraw %}

```
### projects/autoTuning/doc/smg2000_checkpoint2.c

```c

{% raw %}
48 |   cr_leave_cs (cr);
49 | 
50 |   printf ("Checkpointing: restarting here ..\n");
51 |   FunctionLib =dlopen("OUT__1__6755__.so", RTLD_LAZY);
52 |   // ignore the code to find the outlined function and to time the execution here
53 |   // ...
{% endraw %}

```