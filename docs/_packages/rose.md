---
name: "rose"
layout: package
next_package: xqilla
previous_package: ns-3-dev
languages: ['cmake', 'cpp', 'bash']
---
## develop
57 / 31211 files match

 - [rose_config.h.in.cmake](#rose_confighincmake)
 - [src/3rdPartyLibraries/libharu-2.1.0/ltmain.sh](#src3rdpartylibrarieslibharu-210ltmainsh)
 - [src/3rdPartyLibraries/libharu-2.1.0/aclocal.m4](#src3rdpartylibrarieslibharu-210aclocalm4)
 - [src/roseSupport/utility_functions.C](#srcrosesupportutility_functionsc)
 - [src/midend/astProcessing/plugin.h](#srcmidendastprocessingpluginh)
 - [src/midend/astProcessing/plugin.C](#srcmidendastprocessingpluginc)
 - [src/midend/programTransformation/astOutlining/Preprocess.cc](#srcmidendprogramtransformationastoutliningpreprocesscc)
 - [src/midend/programTransformation/astOutlining/Transform.cc](#srcmidendprogramtransformationastoutliningtransformcc)
 - [src/midend/programTransformation/astOutlining/GenerateFunc.cc](#srcmidendprogramtransformationastoutlininggeneratefunccc)
 - [src/midend/programTransformation/astOutlining/Outliner.hh](#srcmidendprogramtransformationastoutliningoutlinerhh)
 - [src/midend/programTransformation/astOutlining/Outliner.cc](#srcmidendprogramtransformationastoutliningoutlinercc)
 - [src/midend/programTransformation/astOutlining/Insert.cc](#srcmidendprogramtransformationastoutlininginsertcc)
 - [src/frontend/OpenFortranParser_SAGE_Connection/Problems.txt](#srcfrontendopenfortranparser_sage_connectionproblemstxt)
 - [src/frontend/Experimental_Csharp_ROSE_Connection/csharp_support.C](#srcfrontendexperimental_csharp_rose_connectioncsharp_supportc)
 - [src/frontend/SageIII/sageInterface/sageBuilder.C](#srcfrontendsageiiisageinterfacesagebuilderc)
 - [src/frontend/SageIII/sage_support/cmdline.cpp](#srcfrontendsageiiisage_supportcmdlinecpp)
 - [src/frontend/SageIII/sage_support/sage_support.cpp](#srcfrontendsageiiisage_supportsage_supportcpp)
 - [tutorial/outliner/outlineTutorial.cc](#tutorialoutlineroutlinetutorialcc)
 - [tests/nonsmoke/functional/readFileTwice.C](#testsnonsmokefunctionalreadfiletwicec)
 - [tests/nonsmoke/functional/roseTests/astOutliningTests/test_20_2019.cpp](#testsnonsmokefunctionalrosetestsastoutliningteststest_20_2019cpp)
 - [tests/nonsmoke/functional/roseTests/astOutliningTests/Makefile.am](#testsnonsmokefunctionalrosetestsastoutliningtestsmakefileam)
 - [tests/nonsmoke/functional/roseTests/astOutliningTests/reference/autotuning_lib.h](#testsnonsmokefunctionalrosetestsastoutliningtestsreferenceautotuning_libh)
 - [tests/nonsmoke/functional/roseTests/astOutliningTests/reference/autotuning_lib.c](#testsnonsmokefunctionalrosetestsastoutliningtestsreferenceautotuning_libc)
 - [tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/ltmain.sh](#testsnonsmokefunctionalruntestsfortrantestslanl_popnetcdf-411ltmainsh)
 - [tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/aclocal.m4](#testsnonsmokefunctionalruntestsfortrantestslanl_popnetcdf-411aclocalm4)
 - [tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/m4/libtool.m4](#testsnonsmokefunctionalruntestsfortrantestslanl_popnetcdf-411m4libtoolm4)
 - [tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/m4/ltoptions.m4](#testsnonsmokefunctionalruntestsfortrantestslanl_popnetcdf-411m4ltoptionsm4)
 - [tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/udunits/ltmain.sh](#testsnonsmokefunctionalruntestsfortrantestslanl_popnetcdf-411udunitsltmainsh)
 - [tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/udunits/aclocal.m4](#testsnonsmokefunctionalruntestsfortrantestslanl_popnetcdf-411udunitsaclocalm4)
 - [tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/udunits/m4/libtool.m4](#testsnonsmokefunctionalruntestsfortrantestslanl_popnetcdf-411udunitsm4libtoolm4)
 - [tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/udunits/m4/ltoptions.m4](#testsnonsmokefunctionalruntestsfortrantestslanl_popnetcdf-411udunitsm4ltoptionsm4)
 - [tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/libcf/ltmain.sh](#testsnonsmokefunctionalruntestsfortrantestslanl_popnetcdf-411libcfltmainsh)
 - [tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/libcf/aclocal.m4](#testsnonsmokefunctionalruntestsfortrantestslanl_popnetcdf-411libcfaclocalm4)
 - [tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/libcf/m4/libtool.m4](#testsnonsmokefunctionalruntestsfortrantestslanl_popnetcdf-411libcfm4libtoolm4)
 - [tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/libcf/m4/ltoptions.m4](#testsnonsmokefunctionalruntestsfortrantestslanl_popnetcdf-411libcfm4ltoptionsm4)
 - [tests/nonsmoke/functional/CompileTests/C_tests/test2012_19.c](#testsnonsmokefunctionalcompiletestsc_teststest2012_19c)
 - [tests/nonsmoke/functional/CompileTests/C_tests/test2012_102.c](#testsnonsmokefunctionalcompiletestsc_teststest2012_102c)
 - [tests/nonsmoke/functional/CompileTests/C_tests/test2012_28.c](#testsnonsmokefunctionalcompiletestsc_teststest2012_28c)
 - [tests/nonsmoke/functional/CompileTests/UnparseHeadersTests/Makefile.am](#testsnonsmokefunctionalcompiletestsunparseheaderstestsmakefileam)
 - [tests/nonsmoke/functional/CompileTests/PythonExample_tests/pythonDir/pystate.h](#testsnonsmokefunctionalcompiletestspythonexample_testspythondirpystateh)
 - [tests/nonsmoke/functional/CompileTests/PythonExample_tests/pythonDir/pyconfig.h](#testsnonsmokefunctionalcompiletestspythonexample_testspythondirpyconfigh)
 - [scripts/buildExampleRoseWorkspaceDirectory/config/ltmain.sh](#scriptsbuildexampleroseworkspacedirectoryconfigltmainsh)
 - [projects/SATIrE/m4/libtool.m4](#projectssatirem4libtoolm4)
 - [projects/SATIrE/m4/ltoptions.m4](#projectssatirem4ltoptionsm4)
 - [projects/interpreter/interp_extcall.C](#projectsinterpreterinterp_extcallc)
 - [projects/PolyOpt2/config/libtool.m4](#projectspolyopt2configlibtoolm4)
 - [projects/PolyOpt2/config/ltoptions.m4](#projectspolyopt2configltoptionsm4)
 - [projects/PolyOpt2/config/ltmain.sh](#projectspolyopt2configltmainsh)
 - [projects/autoTuning/autotuning_lib.h](#projectsautotuningautotuning_libh)
 - [projects/autoTuning/Makefile.am](#projectsautotuningmakefileam)
 - [projects/autoTuning/autoTuningSupport.C](#projectsautotuningautotuningsupportc)
 - [projects/autoTuning/autotuning_lib.c](#projectsautotuningautotuning_libc)
 - [projects/autoTuning/tests/Makefile.am](#projectsautotuningtestsmakefileam)
 - [projects/autoTuning/doc/smg2000_harmony.c](#projectsautotuningdocsmg2000_harmonyc)
 - [projects/autoTuning/doc/smg2000_dlopen.c](#projectsautotuningdocsmg2000_dlopenc)
 - [projects/autoTuning/doc/codeTriageTransformation.tex](#projectsautotuningdoccodetriagetransformationtex)
 - [projects/autoTuning/doc/smg2000_checkpoint2.c](#projectsautotuningdocsmg2000_checkpoint2c)

### rose_config.h.in.cmake

```cmake

{% raw %}
471 | /* Define if the OS needs help to load dependent libraries for dlopen(). */
473 | #undef LTDL_DLOPEN_DEPLIBS
{% endraw %}

```
### src/3rdPartyLibraries/libharu-2.1.0/ltmain.sh

```bash

{% raw %}
522 |   -dlopen)
523 |     prevopt="-dlopen"
607 |   # Only execute mode is allowed to have -dlopen flags.
609 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1148 | 	    dlopen_self=$dlopen_self_static
1153 | 	    dlopen_self=$dlopen_self_static
1209 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1301 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1458 |       -dlopen)
1845 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1918 | 	  # This library was specified with -dlopen.
2059 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2071 | 	passes="conv scan dlopen dlpreopen link"
2084 | 	dlopen) libs="$dlfiles" ;;
2092 |       if test "$pass" = dlopen; then
2271 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2272 | 	      # If there is no dlopen support or we're linking statically,
2305 | 	dlopen=
2326 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2369 | 	# This library was specified with -dlopen.
2370 | 	if test "$pass" = dlopen; then
2372 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2376 | 	     test "$dlopen_support" != yes ||
2378 | 	    # If there is no dlname, no dlopen support or we're linking
2387 | 	fi # $pass = dlopen
2440 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2815 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2816 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2967 |       if test "$pass" != dlopen; then
3068 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3135 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3778 | 	    $echo "*** a static module, that should work as long as the dlopening"
3779 | 	    $echo "*** application is linked with the -dlopen flag."
3797 | 	    $echo "*** or is declared to -dlopen it."
4207 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4339 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4340 | 	   test "$dlopen_self_static" = unknown; then
4341 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5679 | # The name that we can dlopen(3).
5702 | # Files to dlopen/dlpreopen
5703 | dlopen='$dlfiles'
6318 |     # Handle -dlopen flags immediately.
6347 | 	# Skip this library if it cannot be dlopened.
6372 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6732 |   -dlopen FILE      add the directory containing FILE to the library path
6734 | This mode sets the library path environment variable according to \`-dlopen'
6783 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6792 |   -module           build a library that can dlopened
{% endraw %}

```
### src/3rdPartyLibraries/libharu-2.1.0/aclocal.m4

```

{% raw %}
205 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
820 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
823 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
879 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
908 | ])# _LT_AC_TRY_DLOPEN_SELF
911 | # AC_LIBTOOL_DLOPEN_SELF
913 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
915 | if test "x$enable_dlopen" != xyes; then
916 |   enable_dlopen=unknown
917 |   enable_dlopen_self=unknown
918 |   enable_dlopen_self_static=unknown
920 |   lt_cv_dlopen=no
921 |   lt_cv_dlopen_libs=
925 |     lt_cv_dlopen="load_add_on"
926 |     lt_cv_dlopen_libs=
927 |     lt_cv_dlopen_self=yes
931 |     lt_cv_dlopen="LoadLibrary"
932 |     lt_cv_dlopen_libs=
936 |     lt_cv_dlopen="dlopen"
937 |     lt_cv_dlopen_libs=
942 |     AC_CHECK_LIB([dl], [dlopen],
943 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
944 |     lt_cv_dlopen="dyld"
945 |     lt_cv_dlopen_libs=
946 |     lt_cv_dlopen_self=yes
952 | 	  [lt_cv_dlopen="shl_load"],
954 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-dld"],
955 | 	[AC_CHECK_FUNC([dlopen],
956 | 	      [lt_cv_dlopen="dlopen"],
957 | 	  [AC_CHECK_LIB([dl], [dlopen],
958 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
959 | 	    [AC_CHECK_LIB([svld], [dlopen],
960 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
962 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-dld"])
971 |   if test "x$lt_cv_dlopen" != xno; then
972 |     enable_dlopen=yes
974 |     enable_dlopen=no
977 |   case $lt_cv_dlopen in
978 |   dlopen)
986 |     LIBS="$lt_cv_dlopen_libs $LIBS"
988 |     AC_CACHE_CHECK([whether a program can dlopen itself],
989 | 	  lt_cv_dlopen_self, [dnl
990 | 	  _LT_AC_TRY_DLOPEN_SELF(
991 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
992 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
995 |     if test "x$lt_cv_dlopen_self" = xyes; then
997 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
998 |     	  lt_cv_dlopen_self_static, [dnl
999 | 	  _LT_AC_TRY_DLOPEN_SELF(
1000 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1001 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1011 |   case $lt_cv_dlopen_self in
1012 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1013 |   *) enable_dlopen_self=unknown ;;
1016 |   case $lt_cv_dlopen_self_static in
1017 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1018 |   *) enable_dlopen_self_static=unknown ;;
1021 | ])# AC_LIBTOOL_DLOPEN_SELF
1894 | # AC_LIBTOOL_DLOPEN
1896 | # enable checks for dlopen support
1897 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
1899 | ])# AC_LIBTOOL_DLOPEN
2687 | AC_LIBTOOL_DLOPEN_SELF
4358 | # Whether dlopen is supported.
4359 | dlopen_support=$enable_dlopen
4361 | # Whether dlopen of programs is supported.
4362 | dlopen_self=$enable_dlopen_self
4364 | # Whether dlopen of statically linked programs is supported.
4365 | dlopen_self_static=$enable_dlopen_self_static
4373 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### src/roseSupport/utility_functions.C

```cpp

{% raw %}
17 | #include "plugin.h"  // dlopen() is not available on Windows
{% endraw %}

```
### src/midend/astProcessing/plugin.h

```cpp

{% raw %}
60 | #include <dlfcn.h> // dlopen()
{% endraw %}

```
### src/midend/astProcessing/plugin.C

```cpp

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
442 |     // if dlopen() is used, insert a lib call to find the function pointer from a shared lib file
443 |     // e.g. OUT__2__8072__p = findFunctionUsingDlopen("OUT__2__8072__", "OUT__2__8072__.so");
461 | // OUT_1_test_26_2020_0p = findFunctionUsingDlopen("OUT_1_test_26_2020_0","test_26_2020/rose_test_26_2020_lib.so");  
463 |     SgFunctionCallExp* dlopen_call = buildFunctionCallExp(SgName(FIND_FUNCP_DLOPEN),ftype_return,arg_list, p_scope);
464 |     SgExprStatement * assign_stmt = buildAssignStatement(buildVarRefExp(func_name_str+"p",p_scope),dlopen_call);
491 |       printf ("use_dlopen == false: calling generateCall() \n");
495 |       printf ("DONE: use_dlopen == false: calling generateCall() \n");
1038 |    // a dynamic shared library.  Any undefined symbols will cause an error when loading the library using dlopen().
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
86 |   const std::string FIND_FUNCP_DLOPEN="findFunctionUsingDlopen";
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
303 |     //    use_dlopen = false;
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
1525 |    // insert a pointer to function declaration if use_dlopen is true
1527 |    if (use_dlopen) 
1544 |      printf ("############ In Outliner::insert(): use_dlopen == true: Calling SageInterface::insertStatementBefore: func = %p name = %s src_global = %p friendFunctionPrototypeList.size() = %zu \n",
1559 | //   We still generate the prototype even they are not needed if dlopen() is used. 
1562 |    if (use_dlopen == false && SageInterface::is_Fortran_language() == false ) // C/C++ only
1570 |      printf ("############ Calling insertGlobalPrototype(): use_dlopen == false: func = %p name = %s src_global = %p friendFunctionPrototypeList.size() = %zu \n",
1763 |          //if (!use_dlopen)
{% endraw %}

```
### src/frontend/OpenFortranParser_SAGE_Connection/Problems.txt

```

{% raw %}
76 | passage within the dlopen man page:
81 |        in  the  library  are  resolved  before dlopen() returns.
{% endraw %}

```
### src/frontend/Experimental_Csharp_ROSE_Connection/csharp_support.C

```cpp

{% raw %}
19 |      printf ("In C++ process(): calling dlopen() lib = %s \n",lib.c_str());
21 |      handle = dlopen (lib.c_str(), RTLD_LAZY);
{% endraw %}

```
### src/frontend/SageIII/sageInterface/sageBuilder.C

```cpp

{% raw %}
3102 |        // Liao 12/14/2012. This is not true for some functions (e.g. findFunctionUsingDlopen() on top of dlopen()) returning a function type
16783 |      printf ("In SageBuilder::buildFile(): Outliner::use_dlopen = %s \n",Outliner::use_dlopen ? "true" : "false");
16787 |   // I think that the default value for Outliner::use_dlopen is false, so that when the
16791 |      if (!Outliner::use_dlopen)
16794 |           printf ("In SageBuilder::buildFile(): (after test for (!Outliner::use_dlopen) == true: project = %p project->get_fileList_ptr()->get_listOfFiles().size() = %" PRIuPTR " \n",project,project->get_fileList_ptr()->get_listOfFiles().size());
16805 |           printf ("In SageBuilder::buildFile(): (after test for (!Outliner::use_dlopen) == false: project = %p project->get_fileList_ptr()->get_listOfFiles().size() = %" PRIuPTR " \n",project,project->get_fileList_ptr()->get_listOfFiles().size());
16815 |        // So we only turn this on if Outliner:: use_dlopen is used for now
{% endraw %}

```
### src/frontend/SageIII/sage_support/cmdline.cpp

```

{% raw %}
5756 |      optionCount = sla(argv, "-rose:outline:", "($)", "use_dlopen",1);
{% endraw %}

```
### src/frontend/SageIII/sage_support/sage_support.cpp

```

{% raw %}
1789 |      switches.insert(Switch("xxx_use_dlopen")
1790 |                     .intrinsicValue(true, use_dlopen)
1791 |                     .doc("Use @man{dlopen}(3) to find an outlined function saved into a new source file."));
{% endraw %}

```
### tutorial/outliner/outlineTutorial.cc

```cpp

{% raw %}
143 |       std::cout <<"  use_dlopen          = " <<Outliner::use_dlopen <<"\n";
{% endraw %}

```
### tests/nonsmoke/functional/readFileTwice.C

```cpp

{% raw %}
116 |        // a dynamic shared library.  Any undefined symbols will cause an error when loading the library using dlopen().
{% endraw %}

```
### tests/nonsmoke/functional/roseTests/astOutliningTests/test_20_2019.cpp

```

{% raw %}
0 | // tool_G -roseoutline:use_dlopen -rose:outline:copy_orig_file -rose:unparseHeaderFiles -c test_20.cpp
{% endraw %}

```
### tests/nonsmoke/functional/roseTests/astOutliningTests/Makefile.am

```

{% raw %}
311 | # Test outlining to a separate file using dlopen
313 | dlopen_test_targets  = $(addprefix dlopen_,  $(addsuffix .passed, $(C_TESTS_REQUIRED_TO_PASS)))
314 | dlopen_test_targets  += $(addprefix dlopen_,  $(addsuffix .passed, $(CXX_TESTS_REQUIRED_TO_PASS)))
315 | C_CXX_RESULTS +=  $(dlopen_test_targets)
316 | dlopen_test_flags =				\
317 | 	-rose:outline:use_dlopen		\
321 | $(dlopen_test_targets): dlopen_%.passed: % outline
323 | 		TITLE="outine dlopen $(notdir $<) [$@]" \
325 | 		CMD="$$(pwd)/outline$(EXEEXT) $(TEST_INCLUDES) $(dlopen_test_flags) -c $(abspath $<)" \
329 | dlopen2_test_targets  = $(addprefix dlopen2_,  $(addsuffix .passed, $(C_TESTS_REQUIRED_TO_PASS)))
330 | dlopen2_test_targets  += $(addprefix dlopen2_,  $(addsuffix .passed, $(CXX_TESTS_REQUIRED_TO_PASS)))
331 | C_CXX_RESULTS += $(dlopen2_test_targets)  
332 | dlopen2_test_flags =				\
333 | 	-rose:outline:use_dlopen		\
338 | $(dlopen2_test_targets): dlopen2_%.passed: % outline
340 | 		TITLE="outine dlopen2 $(notdir $<) [$@]" \
342 | 		CMD="$$(pwd)/outline$(EXEEXT) $(TEST_INCLUDES) $(dlopen2_test_flags) -c $(abspath $<)" \
348 | # Similar to dlopen3, additionally
350 | dlopen3_test_targets = $(addprefix dlopen3_,  $(addsuffix .passed, $(CXX2_TESTS_REQUIRED_TO_PASS)))
351 | C_CXX_RESULTS += $(dlopen3_test_targets)  
352 | dlopen3_test_flags =				\
353 | 	-rose:outline:use_dlopen		\
358 | $(dlopen3_test_targets): dlopen3_%.passed: % outline
360 | 		TITLE="outine dlopen3 $(notdir $<) [$@]" \
362 | 		CMD="$$(pwd)/outline$(EXEEXT) $(TEST_INCLUDES) $(dlopen3_test_flags) -c $(abspath $<)" \
366 | # shortcut to test the dlopen feature
367 | test_dlopen3: $(dlopen3_test_targets)
373 | dlopen4_test_targets = $(addprefix dlopen4_,  $(CXX4_TESTS_REQUIRED_TO_RUN))
374 | dlopen4_test_lib_targets = $(addprefix rose_, $(addsuffix .cpp, $(addsuffix _lib, $(basename $(CXX4_TESTS_REQUIRED_TO_RUN)))))
375 | dlopen4_test_lib_so_targets = $(addprefix rose_, $(addsuffix .so, $(addsuffix _lib, $(basename $(CXX4_TESTS_REQUIRED_TO_RUN)))))
376 | C_CXX_RESULTS += $(dlopen4_test_targets)
378 | dlopen4_test_flags = -fpermissive	\
380 | 	-rose:outline:use_dlopen		\
383 | 	-rose:unparseHeaderFilesRootFolder unparseHeaderRoot_dlopen4
384 | $(dlopen4_test_targets): dlopen4_%: % outline
385 | 	./outline$(EXEEXT) $(TEST_INCLUDES) $(dlopen4_test_flags) -c $(abspath $<) -rose:output $@
388 | $(CXX4_TESTS_OBJECT_REQUIRED_TO_RUN): %.o: dlopen4_%.cpp
389 | $(dlopen4_test_lib_targets): rose_%_lib.cpp: dlopen4_%.cpp
391 | # shortcut to test the dlopen feature
392 | test_dlopen: $(dlopen_test_targets) $(dlopen2_test_targets) $(dlopen3_test_targets) $(dlopen4_test_targets)
393 | test_dlopen4: $(dlopen4_test_targets)
396 | $(dlopen4_test_lib_so_targets):%.so: %.cpp
415 | #	rm -rf ${dlopen4_test_lib_targets}
416 | C_CXX_RESULTS += $(dlopen4_test_lib_targets) $(CXX4_TESTS_OBJECT_REQUIRED_TO_RUN) $(dlopen4_test_targets) $(dlopen4_test_lib_so_targets) $(PASSING_CXX_TEST_Executables)
{% endraw %}

```
### tests/nonsmoke/functional/roseTests/astOutliningTests/reference/autotuning_lib.h

```cpp

{% raw %}
12 | // dlopen support  
16 | funcPointerT findFunctionUsingDlopen(char* function_name, char* lib_name);
{% endraw %}

```
### tests/nonsmoke/functional/roseTests/astOutliningTests/reference/autotuning_lib.c

```cpp

{% raw %}
26 | // internal one with direct use with dlopen()
27 | static funcPointerT findWithDlopen(const char* function_name, const char* lib_name)
32 |   functionLib = dlopen(lib_name, RTLD_LAZY);
90 | funcPointerT findFunctionUsingDlopen(char* function_name, char* lib_name)
100 |    result = findWithDlopen(function_name,lib_name);
104 |   result = findWithDlopen(function_name,lib_name);
{% endraw %}

```
### tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/ltmain.sh

```bash

{% raw %}
737 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
787 |       -dlopen=*|--mode=*|--tag=*)
876 |   # Only execute mode is allowed to have -dlopen flags.
878 |     func_error "unrecognized option \`-dlopen'"
1504 |   -dlopen FILE      add the directory containing FILE to the library path
1506 | This mode sets the library path environment variable according to \`-dlopen'
1559 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1568 |   -module           build a library that can dlopened
1643 |     # Handle -dlopen flags immediately.
1660 | 	# Skip this library if it cannot be dlopened.
1687 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
3603 | 	    dlopen_self=$dlopen_self_static
3609 | 	    dlopen_self=$dlopen_self_static
3615 | 	    dlopen_self=$dlopen_self_static
3668 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
3752 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3909 |       -dlopen)
4287 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4354 | 	  # This library was specified with -dlopen.
4469 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
4480 | 	passes="conv scan dlopen dlpreopen link"
4506 | 	dlopen) libs="$dlfiles" ;;
4532 |       if test "$pass" = dlopen; then
4744 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
4745 | 	      # If there is no dlopen support or we're linking statically,
4775 | 	dlopen=
4805 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
4845 | 	# This library was specified with -dlopen.
4846 | 	if test "$pass" = dlopen; then
4848 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
4851 | 	     test "$dlopen_support" != yes ||
4853 | 	    # If there is no dlname, no dlopen support or we're linking
4862 | 	fi # $pass = dlopen
4920 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5046 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5047 | 	  dlopenmodule=""
5050 | 	      dlopenmodule="$dlpremoduletest"
5054 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5151 | 		    # if the lib is a (non-dlopened) module then we can not
5155 | 		      if test "X$dlopenmodule" != "X$lib"; then
5307 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5308 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5443 |       if test "$pass" != dlopen; then
5542 | 	func_warning "\`-dlopen' is ignored for archives"
5609 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6271 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6272 | 	    $ECHO "*** application is linked with the -dlopen flag."
6290 | 	    $ECHO "*** or is declared to -dlopen it."
6857 | 	func_warning "\`-dlopen' is ignored for objects"
6972 |         && test "$dlopen_support" = unknown \
6973 | 	&& test "$dlopen_self" = unknown \
6974 | 	&& test "$dlopen_self_static" = unknown && \
6975 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
7602 | # The name that we can dlopen(3).
7631 | # Files to dlopen/dlpreopen
7632 | dlopen='$dlfiles'
{% endraw %}

```
### tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/aclocal.m4

```

{% raw %}
214 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
926 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
929 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
985 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1014 | ])# _LT_AC_TRY_DLOPEN_SELF
1017 | # AC_LIBTOOL_DLOPEN_SELF
1019 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1021 | if test "x$enable_dlopen" != xyes; then
1022 |   enable_dlopen=unknown
1023 |   enable_dlopen_self=unknown
1024 |   enable_dlopen_self_static=unknown
1026 |   lt_cv_dlopen=no
1027 |   lt_cv_dlopen_libs=
1031 |     lt_cv_dlopen="load_add_on"
1032 |     lt_cv_dlopen_libs=
1033 |     lt_cv_dlopen_self=yes
1037 |     lt_cv_dlopen="LoadLibrary"
1038 |     lt_cv_dlopen_libs=
1042 |     lt_cv_dlopen="dlopen"
1043 |     lt_cv_dlopen_libs=
1048 |     AC_CHECK_LIB([dl], [dlopen],
1049 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1050 |     lt_cv_dlopen="dyld"
1051 |     lt_cv_dlopen_libs=
1052 |     lt_cv_dlopen_self=yes
1058 | 	  [lt_cv_dlopen="shl_load"],
1060 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1061 | 	[AC_CHECK_FUNC([dlopen],
1062 | 	      [lt_cv_dlopen="dlopen"],
1063 | 	  [AC_CHECK_LIB([dl], [dlopen],
1064 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1065 | 	    [AC_CHECK_LIB([svld], [dlopen],
1066 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1068 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1077 |   if test "x$lt_cv_dlopen" != xno; then
1078 |     enable_dlopen=yes
1080 |     enable_dlopen=no
1083 |   case $lt_cv_dlopen in
1084 |   dlopen)
1092 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1094 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1095 | 	  lt_cv_dlopen_self, [dnl
1096 | 	  _LT_AC_TRY_DLOPEN_SELF(
1097 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1098 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1101 |     if test "x$lt_cv_dlopen_self" = xyes; then
1103 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1104 |     	  lt_cv_dlopen_self_static, [dnl
1105 | 	  _LT_AC_TRY_DLOPEN_SELF(
1106 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1107 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1117 |   case $lt_cv_dlopen_self in
1118 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1119 |   *) enable_dlopen_self=unknown ;;
1122 |   case $lt_cv_dlopen_self_static in
1123 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1124 |   *) enable_dlopen_self_static=unknown ;;
1127 | ])# AC_LIBTOOL_DLOPEN_SELF
2027 | # AC_LIBTOOL_DLOPEN
2029 | # enable checks for dlopen support
2030 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2032 | ])# AC_LIBTOOL_DLOPEN
2830 | AC_LIBTOOL_DLOPEN_SELF
4547 | # Whether dlopen is supported.
4548 | dlopen_support=$enable_dlopen
4550 | # Whether dlopen of programs is supported.
4551 | dlopen_self=$enable_dlopen_self
4553 | # Whether dlopen of statically linked programs is supported.
4554 | dlopen_self_static=$enable_dlopen_self_static
4562 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/m4/libtool.m4

```

{% raw %}
1630 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1633 | m4_defun([_LT_TRY_DLOPEN_SELF],
1689 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1718 | ])# _LT_TRY_DLOPEN_SELF
1721 | # LT_SYS_DLOPEN_SELF
1723 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1725 | if test "x$enable_dlopen" != xyes; then
1726 |   enable_dlopen=unknown
1727 |   enable_dlopen_self=unknown
1728 |   enable_dlopen_self_static=unknown
1730 |   lt_cv_dlopen=no
1731 |   lt_cv_dlopen_libs=
1735 |     lt_cv_dlopen="load_add_on"
1736 |     lt_cv_dlopen_libs=
1737 |     lt_cv_dlopen_self=yes
1741 |     lt_cv_dlopen="LoadLibrary"
1742 |     lt_cv_dlopen_libs=
1746 |     lt_cv_dlopen="dlopen"
1747 |     lt_cv_dlopen_libs=
1752 |     AC_CHECK_LIB([dl], [dlopen],
1753 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1754 |     lt_cv_dlopen="dyld"
1755 |     lt_cv_dlopen_libs=
1756 |     lt_cv_dlopen_self=yes
1762 | 	  [lt_cv_dlopen="shl_load"],
1764 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1765 | 	[AC_CHECK_FUNC([dlopen],
1766 | 	      [lt_cv_dlopen="dlopen"],
1767 | 	  [AC_CHECK_LIB([dl], [dlopen],
1768 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1769 | 	    [AC_CHECK_LIB([svld], [dlopen],
1770 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1772 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1781 |   if test "x$lt_cv_dlopen" != xno; then
1782 |     enable_dlopen=yes
1784 |     enable_dlopen=no
1787 |   case $lt_cv_dlopen in
1788 |   dlopen)
1796 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1798 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1799 | 	  lt_cv_dlopen_self, [dnl
1800 | 	  _LT_TRY_DLOPEN_SELF(
1801 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1802 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1805 |     if test "x$lt_cv_dlopen_self" = xyes; then
1807 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1808 | 	  lt_cv_dlopen_self_static, [dnl
1809 | 	  _LT_TRY_DLOPEN_SELF(
1810 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1811 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1821 |   case $lt_cv_dlopen_self in
1822 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1823 |   *) enable_dlopen_self=unknown ;;
1826 |   case $lt_cv_dlopen_self_static in
1827 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1828 |   *) enable_dlopen_self_static=unknown ;;
1831 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1832 | 	 [Whether dlopen is supported])
1833 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1834 | 	 [Whether dlopen of programs is supported])
1835 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1836 | 	 [Whether dlopen of statically linked programs is supported])
1837 | ])# LT_SYS_DLOPEN_SELF
1840 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1842 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5120 |     [Compiler flag to allow reflexive dlopens])
5236 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/m4/ltoptions.m4

```

{% raw %}
69 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
104 | # dlopen
106 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
109 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
110 | [_LT_SET_OPTION([LT_INIT], [dlopen])
113 | put the `dlopen' option into LT_INIT's first parameter.])
117 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/udunits/ltmain.sh

```bash

{% raw %}
737 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
787 |       -dlopen=*|--mode=*|--tag=*)
876 |   # Only execute mode is allowed to have -dlopen flags.
878 |     func_error "unrecognized option \`-dlopen'"
1504 |   -dlopen FILE      add the directory containing FILE to the library path
1506 | This mode sets the library path environment variable according to \`-dlopen'
1559 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1568 |   -module           build a library that can dlopened
1643 |     # Handle -dlopen flags immediately.
1660 | 	# Skip this library if it cannot be dlopened.
1687 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
3603 | 	    dlopen_self=$dlopen_self_static
3609 | 	    dlopen_self=$dlopen_self_static
3615 | 	    dlopen_self=$dlopen_self_static
3668 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
3752 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3909 |       -dlopen)
4287 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4354 | 	  # This library was specified with -dlopen.
4469 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
4480 | 	passes="conv scan dlopen dlpreopen link"
4506 | 	dlopen) libs="$dlfiles" ;;
4532 |       if test "$pass" = dlopen; then
4744 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
4745 | 	      # If there is no dlopen support or we're linking statically,
4775 | 	dlopen=
4805 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
4845 | 	# This library was specified with -dlopen.
4846 | 	if test "$pass" = dlopen; then
4848 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
4851 | 	     test "$dlopen_support" != yes ||
4853 | 	    # If there is no dlname, no dlopen support or we're linking
4862 | 	fi # $pass = dlopen
4920 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5046 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5047 | 	  dlopenmodule=""
5050 | 	      dlopenmodule="$dlpremoduletest"
5054 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5151 | 		    # if the lib is a (non-dlopened) module then we can not
5155 | 		      if test "X$dlopenmodule" != "X$lib"; then
5307 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5308 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5443 |       if test "$pass" != dlopen; then
5542 | 	func_warning "\`-dlopen' is ignored for archives"
5609 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6271 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6272 | 	    $ECHO "*** application is linked with the -dlopen flag."
6290 | 	    $ECHO "*** or is declared to -dlopen it."
6857 | 	func_warning "\`-dlopen' is ignored for objects"
6972 |         && test "$dlopen_support" = unknown \
6973 | 	&& test "$dlopen_self" = unknown \
6974 | 	&& test "$dlopen_self_static" = unknown && \
6975 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
7602 | # The name that we can dlopen(3).
7631 | # Files to dlopen/dlpreopen
7632 | dlopen='$dlfiles'
{% endraw %}

```
### tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/udunits/aclocal.m4

```

{% raw %}
214 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
926 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
929 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
985 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1014 | ])# _LT_AC_TRY_DLOPEN_SELF
1017 | # AC_LIBTOOL_DLOPEN_SELF
1019 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1021 | if test "x$enable_dlopen" != xyes; then
1022 |   enable_dlopen=unknown
1023 |   enable_dlopen_self=unknown
1024 |   enable_dlopen_self_static=unknown
1026 |   lt_cv_dlopen=no
1027 |   lt_cv_dlopen_libs=
1031 |     lt_cv_dlopen="load_add_on"
1032 |     lt_cv_dlopen_libs=
1033 |     lt_cv_dlopen_self=yes
1037 |     lt_cv_dlopen="LoadLibrary"
1038 |     lt_cv_dlopen_libs=
1042 |     lt_cv_dlopen="dlopen"
1043 |     lt_cv_dlopen_libs=
1048 |     AC_CHECK_LIB([dl], [dlopen],
1049 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1050 |     lt_cv_dlopen="dyld"
1051 |     lt_cv_dlopen_libs=
1052 |     lt_cv_dlopen_self=yes
1058 | 	  [lt_cv_dlopen="shl_load"],
1060 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1061 | 	[AC_CHECK_FUNC([dlopen],
1062 | 	      [lt_cv_dlopen="dlopen"],
1063 | 	  [AC_CHECK_LIB([dl], [dlopen],
1064 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1065 | 	    [AC_CHECK_LIB([svld], [dlopen],
1066 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1068 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1077 |   if test "x$lt_cv_dlopen" != xno; then
1078 |     enable_dlopen=yes
1080 |     enable_dlopen=no
1083 |   case $lt_cv_dlopen in
1084 |   dlopen)
1092 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1094 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1095 | 	  lt_cv_dlopen_self, [dnl
1096 | 	  _LT_AC_TRY_DLOPEN_SELF(
1097 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1098 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1101 |     if test "x$lt_cv_dlopen_self" = xyes; then
1103 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1104 |     	  lt_cv_dlopen_self_static, [dnl
1105 | 	  _LT_AC_TRY_DLOPEN_SELF(
1106 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1107 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1117 |   case $lt_cv_dlopen_self in
1118 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1119 |   *) enable_dlopen_self=unknown ;;
1122 |   case $lt_cv_dlopen_self_static in
1123 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1124 |   *) enable_dlopen_self_static=unknown ;;
1127 | ])# AC_LIBTOOL_DLOPEN_SELF
2027 | # AC_LIBTOOL_DLOPEN
2029 | # enable checks for dlopen support
2030 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2032 | ])# AC_LIBTOOL_DLOPEN
2830 | AC_LIBTOOL_DLOPEN_SELF
4547 | # Whether dlopen is supported.
4548 | dlopen_support=$enable_dlopen
4550 | # Whether dlopen of programs is supported.
4551 | dlopen_self=$enable_dlopen_self
4553 | # Whether dlopen of statically linked programs is supported.
4554 | dlopen_self_static=$enable_dlopen_self_static
4562 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/udunits/m4/libtool.m4

```

{% raw %}
1630 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1633 | m4_defun([_LT_TRY_DLOPEN_SELF],
1689 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1718 | ])# _LT_TRY_DLOPEN_SELF
1721 | # LT_SYS_DLOPEN_SELF
1723 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1725 | if test "x$enable_dlopen" != xyes; then
1726 |   enable_dlopen=unknown
1727 |   enable_dlopen_self=unknown
1728 |   enable_dlopen_self_static=unknown
1730 |   lt_cv_dlopen=no
1731 |   lt_cv_dlopen_libs=
1735 |     lt_cv_dlopen="load_add_on"
1736 |     lt_cv_dlopen_libs=
1737 |     lt_cv_dlopen_self=yes
1741 |     lt_cv_dlopen="LoadLibrary"
1742 |     lt_cv_dlopen_libs=
1746 |     lt_cv_dlopen="dlopen"
1747 |     lt_cv_dlopen_libs=
1752 |     AC_CHECK_LIB([dl], [dlopen],
1753 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1754 |     lt_cv_dlopen="dyld"
1755 |     lt_cv_dlopen_libs=
1756 |     lt_cv_dlopen_self=yes
1762 | 	  [lt_cv_dlopen="shl_load"],
1764 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1765 | 	[AC_CHECK_FUNC([dlopen],
1766 | 	      [lt_cv_dlopen="dlopen"],
1767 | 	  [AC_CHECK_LIB([dl], [dlopen],
1768 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1769 | 	    [AC_CHECK_LIB([svld], [dlopen],
1770 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1772 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1781 |   if test "x$lt_cv_dlopen" != xno; then
1782 |     enable_dlopen=yes
1784 |     enable_dlopen=no
1787 |   case $lt_cv_dlopen in
1788 |   dlopen)
1796 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1798 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1799 | 	  lt_cv_dlopen_self, [dnl
1800 | 	  _LT_TRY_DLOPEN_SELF(
1801 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1802 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1805 |     if test "x$lt_cv_dlopen_self" = xyes; then
1807 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1808 | 	  lt_cv_dlopen_self_static, [dnl
1809 | 	  _LT_TRY_DLOPEN_SELF(
1810 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1811 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1821 |   case $lt_cv_dlopen_self in
1822 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1823 |   *) enable_dlopen_self=unknown ;;
1826 |   case $lt_cv_dlopen_self_static in
1827 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1828 |   *) enable_dlopen_self_static=unknown ;;
1831 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1832 | 	 [Whether dlopen is supported])
1833 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1834 | 	 [Whether dlopen of programs is supported])
1835 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1836 | 	 [Whether dlopen of statically linked programs is supported])
1837 | ])# LT_SYS_DLOPEN_SELF
1840 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1842 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5120 |     [Compiler flag to allow reflexive dlopens])
5236 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/udunits/m4/ltoptions.m4

```

{% raw %}
69 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
104 | # dlopen
106 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
109 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
110 | [_LT_SET_OPTION([LT_INIT], [dlopen])
113 | put the `dlopen' option into LT_INIT's first parameter.])
117 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/libcf/ltmain.sh

```bash

{% raw %}
737 |       -dlopen)		test "$#" -eq 0 && func_missing_arg "$opt" && break
787 |       -dlopen=*|--mode=*|--tag=*)
876 |   # Only execute mode is allowed to have -dlopen flags.
878 |     func_error "unrecognized option \`-dlopen'"
1504 |   -dlopen FILE      add the directory containing FILE to the library path
1506 | This mode sets the library path environment variable according to \`-dlopen'
1559 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
1568 |   -module           build a library that can dlopened
1643 |     # Handle -dlopen flags immediately.
1660 | 	# Skip this library if it cannot be dlopened.
1687 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
3603 | 	    dlopen_self=$dlopen_self_static
3609 | 	    dlopen_self=$dlopen_self_static
3615 | 	    dlopen_self=$dlopen_self_static
3668 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
3752 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
3909 |       -dlopen)
4287 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
4354 | 	  # This library was specified with -dlopen.
4469 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
4480 | 	passes="conv scan dlopen dlpreopen link"
4506 | 	dlopen) libs="$dlfiles" ;;
4532 |       if test "$pass" = dlopen; then
4744 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
4745 | 	      # If there is no dlopen support or we're linking statically,
4775 | 	dlopen=
4805 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
4845 | 	# This library was specified with -dlopen.
4846 | 	if test "$pass" = dlopen; then
4848 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
4851 | 	     test "$dlopen_support" != yes ||
4853 | 	    # If there is no dlname, no dlopen support or we're linking
4862 | 	fi # $pass = dlopen
4920 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
5046 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
5047 | 	  dlopenmodule=""
5050 | 	      dlopenmodule="$dlpremoduletest"
5054 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
5151 | 		    # if the lib is a (non-dlopened) module then we can not
5155 | 		      if test "X$dlopenmodule" != "X$lib"; then
5307 | 	      $ECHO "*** a static module, that should work as long as the dlopening application"
5308 | 	      $ECHO "*** is linked with the -dlopen flag to resolve symbols at runtime."
5443 |       if test "$pass" != dlopen; then
5542 | 	func_warning "\`-dlopen' is ignored for archives"
5609 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
6271 | 	    $ECHO "*** a static module, that should work as long as the dlopening"
6272 | 	    $ECHO "*** application is linked with the -dlopen flag."
6290 | 	    $ECHO "*** or is declared to -dlopen it."
6857 | 	func_warning "\`-dlopen' is ignored for objects"
6972 |         && test "$dlopen_support" = unknown \
6973 | 	&& test "$dlopen_self" = unknown \
6974 | 	&& test "$dlopen_self_static" = unknown && \
6975 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
7602 | # The name that we can dlopen(3).
7631 | # Files to dlopen/dlpreopen
7632 | dlopen='$dlfiles'
{% endraw %}

```
### tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/libcf/aclocal.m4

```

{% raw %}
214 | AC_PROVIDE_IFELSE([AC_LIBTOOL_DLOPEN], enable_dlopen=yes, enable_dlopen=no)
926 | # _LT_AC_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
929 | AC_DEFUN([_LT_AC_TRY_DLOPEN_SELF],
985 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1014 | ])# _LT_AC_TRY_DLOPEN_SELF
1017 | # AC_LIBTOOL_DLOPEN_SELF
1019 | AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF],
1021 | if test "x$enable_dlopen" != xyes; then
1022 |   enable_dlopen=unknown
1023 |   enable_dlopen_self=unknown
1024 |   enable_dlopen_self_static=unknown
1026 |   lt_cv_dlopen=no
1027 |   lt_cv_dlopen_libs=
1031 |     lt_cv_dlopen="load_add_on"
1032 |     lt_cv_dlopen_libs=
1033 |     lt_cv_dlopen_self=yes
1037 |     lt_cv_dlopen="LoadLibrary"
1038 |     lt_cv_dlopen_libs=
1042 |     lt_cv_dlopen="dlopen"
1043 |     lt_cv_dlopen_libs=
1048 |     AC_CHECK_LIB([dl], [dlopen],
1049 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1050 |     lt_cv_dlopen="dyld"
1051 |     lt_cv_dlopen_libs=
1052 |     lt_cv_dlopen_self=yes
1058 | 	  [lt_cv_dlopen="shl_load"],
1060 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1061 | 	[AC_CHECK_FUNC([dlopen],
1062 | 	      [lt_cv_dlopen="dlopen"],
1063 | 	  [AC_CHECK_LIB([dl], [dlopen],
1064 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1065 | 	    [AC_CHECK_LIB([svld], [dlopen],
1066 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1068 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1077 |   if test "x$lt_cv_dlopen" != xno; then
1078 |     enable_dlopen=yes
1080 |     enable_dlopen=no
1083 |   case $lt_cv_dlopen in
1084 |   dlopen)
1092 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1094 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1095 | 	  lt_cv_dlopen_self, [dnl
1096 | 	  _LT_AC_TRY_DLOPEN_SELF(
1097 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1098 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1101 |     if test "x$lt_cv_dlopen_self" = xyes; then
1103 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1104 |     	  lt_cv_dlopen_self_static, [dnl
1105 | 	  _LT_AC_TRY_DLOPEN_SELF(
1106 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1107 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1117 |   case $lt_cv_dlopen_self in
1118 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1119 |   *) enable_dlopen_self=unknown ;;
1122 |   case $lt_cv_dlopen_self_static in
1123 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1124 |   *) enable_dlopen_self_static=unknown ;;
1127 | ])# AC_LIBTOOL_DLOPEN_SELF
2027 | # AC_LIBTOOL_DLOPEN
2029 | # enable checks for dlopen support
2030 | AC_DEFUN([AC_LIBTOOL_DLOPEN],
2032 | ])# AC_LIBTOOL_DLOPEN
2830 | AC_LIBTOOL_DLOPEN_SELF
4547 | # Whether dlopen is supported.
4548 | dlopen_support=$enable_dlopen
4550 | # Whether dlopen of programs is supported.
4551 | dlopen_self=$enable_dlopen_self
4553 | # Whether dlopen of statically linked programs is supported.
4554 | dlopen_self_static=$enable_dlopen_self_static
4562 | # Compiler flag to allow reflexive dlopens.
{% endraw %}

```
### tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/libcf/m4/libtool.m4

```

{% raw %}
1630 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1633 | m4_defun([_LT_TRY_DLOPEN_SELF],
1689 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1718 | ])# _LT_TRY_DLOPEN_SELF
1721 | # LT_SYS_DLOPEN_SELF
1723 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1725 | if test "x$enable_dlopen" != xyes; then
1726 |   enable_dlopen=unknown
1727 |   enable_dlopen_self=unknown
1728 |   enable_dlopen_self_static=unknown
1730 |   lt_cv_dlopen=no
1731 |   lt_cv_dlopen_libs=
1735 |     lt_cv_dlopen="load_add_on"
1736 |     lt_cv_dlopen_libs=
1737 |     lt_cv_dlopen_self=yes
1741 |     lt_cv_dlopen="LoadLibrary"
1742 |     lt_cv_dlopen_libs=
1746 |     lt_cv_dlopen="dlopen"
1747 |     lt_cv_dlopen_libs=
1752 |     AC_CHECK_LIB([dl], [dlopen],
1753 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1754 |     lt_cv_dlopen="dyld"
1755 |     lt_cv_dlopen_libs=
1756 |     lt_cv_dlopen_self=yes
1762 | 	  [lt_cv_dlopen="shl_load"],
1764 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1765 | 	[AC_CHECK_FUNC([dlopen],
1766 | 	      [lt_cv_dlopen="dlopen"],
1767 | 	  [AC_CHECK_LIB([dl], [dlopen],
1768 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1769 | 	    [AC_CHECK_LIB([svld], [dlopen],
1770 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1772 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1781 |   if test "x$lt_cv_dlopen" != xno; then
1782 |     enable_dlopen=yes
1784 |     enable_dlopen=no
1787 |   case $lt_cv_dlopen in
1788 |   dlopen)
1796 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1798 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1799 | 	  lt_cv_dlopen_self, [dnl
1800 | 	  _LT_TRY_DLOPEN_SELF(
1801 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1802 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1805 |     if test "x$lt_cv_dlopen_self" = xyes; then
1807 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1808 | 	  lt_cv_dlopen_self_static, [dnl
1809 | 	  _LT_TRY_DLOPEN_SELF(
1810 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1811 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1821 |   case $lt_cv_dlopen_self in
1822 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1823 |   *) enable_dlopen_self=unknown ;;
1826 |   case $lt_cv_dlopen_self_static in
1827 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1828 |   *) enable_dlopen_self_static=unknown ;;
1831 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1832 | 	 [Whether dlopen is supported])
1833 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1834 | 	 [Whether dlopen of programs is supported])
1835 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1836 | 	 [Whether dlopen of statically linked programs is supported])
1837 | ])# LT_SYS_DLOPEN_SELF
1840 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1842 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5120 |     [Compiler flag to allow reflexive dlopens])
5236 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### tests/nonsmoke/functional/RunTests/FortranTests/LANL_POP/netcdf-4.1.1/libcf/m4/ltoptions.m4

```

{% raw %}
69 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
104 | # dlopen
106 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
109 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
110 | [_LT_SET_OPTION([LT_INIT], [dlopen])
113 | put the `dlopen' option into LT_INIT's first parameter.])
117 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/C_tests/test2012_19.c

```cpp

{% raw %}
5039 | extern void *dlopen (__const char *__file, int __mode) __attribute__ ((__nothrow__));
5584 |  void *dlopen_ref;
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/C_tests/test2012_102.c

```cpp

{% raw %}
12713 | extern void *dlopen (__const char *__file, int __mode) __attribute__ ((__nothrow__));
12861 |  ret = dlopen(unmeta(buf), 0x00001 | 0x00100);
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/C_tests/test2012_28.c

```cpp

{% raw %}
5039 | extern void *dlopen (__const char *__file, int __mode) __attribute__ ((__nothrow__));
7836 |  void *dlopen_ref;
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/UnparseHeadersTests/Makefile.am

```

{% raw %}
43 | # -rose:outline:use_dlopen -rose:outline:copy_orig_file -rose:outline:temp_variable -I. -rose:outline:exclude_headers -rose:outline:output_path . -rose:unparseHeaderFiles -rose:unparseHeaderFilesRootFolder unparsedHeaders -rose:applicationRootDirectory /home/quinlan1/ROSE/git_rose_development/tests/nonsmoke/functional/CompileTests/UnparseHeadersTests/test0
46 | # rm -fr unparsedHeaders unparsedHeaders.; ../TestUnparseHeaders  -rose:verbose 0 -DXXXSKIP_ROSE_BUILTIN_DECLARATIONS -std=c++03 -fpermissive -c -rose:outline:use_dlopen -rose:outline:copy_orig_file -rose:outline:temp_variable -I. -rose:outline:exclude_headers -rose:outline:output_path . -rose:unparseHeaderFiles -rose:unparseHeaderFilesRootFolder unparsedHeaders -rose:applicationRootDirectory /home/quinlan1/ROSE/git_rose_development/tests/nonsmoke/functional/CompileTests/UnparseHeadersTests/test0 -I/home/quinlan1/ROSE/ROSE_GARDEN/codeSegregation /home/quinlan1/ROSE/git_rose_development/tests/nonsmoke/functional/CompileTests/UnparseHeadersTests/test0/Simple0.C -o /data1/ROSE_CompileTree/git-LINUX-64bit-6.1.0-EDG50-BOOST_1_60-dq-development-rc-cxx-only/tests/nonsmoke/functional/CompileTests/UnparseHeadersTests/test0/Simple0.o
50 | # OUTLINER_SWITCHES = -rose:outline:use_dlopen -rose:outline:copy_orig_file -rose:outline:temp_variable -rose:outline:exclude_headers -rose:outline:output_path .
51 | OUTLINER_SWITCHES = -rose:outline:use_dlopen -rose:outline:copy_orig_file -rose:outline:temp_variable -rose:outline:exclude_headers
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/PythonExample_tests/pythonDir/pystate.h

```cpp

{% raw %}
25 | #ifdef HAVE_DLOPEN
26 |     int dlopenflags;
{% endraw %}

```
### tests/nonsmoke/functional/CompileTests/PythonExample_tests/pythonDir/pyconfig.h

```cpp

{% raw %}
360 | /* Define if you have the dlopen function.  */
361 | #define HAVE_DLOPEN 1
{% endraw %}

```
### scripts/buildExampleRoseWorkspaceDirectory/config/ltmain.sh

```bash

{% raw %}
542 |   -dlopen)
543 |     prevopt="-dlopen"
627 |   # Only execute mode is allowed to have -dlopen flags.
629 |     $echo "$modename: unrecognized option \`-dlopen'" 1>&2
1168 | 	    dlopen_self=$dlopen_self_static
1174 | 	    dlopen_self=$dlopen_self_static
1180 |         dlopen_self=$dlopen_self_static
1237 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
1329 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1486 |       -dlopen)
1873 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
1946 | 	  # This library was specified with -dlopen.
2087 | 	    $echo "$modename: libraries can \`-dlopen' only libtool libraries: $file" 1>&2
2099 | 	passes="conv scan dlopen dlpreopen link"
2112 | 	dlopen) libs="$dlfiles" ;;
2117 |       if test "$pass" = dlopen; then
2296 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
2297 | 	      # If there is no dlopen support or we're linking statically,
2330 | 	dlopen=
2351 | 	  test -n "$dlopen" && dlfiles="$dlfiles $dlopen"
2394 | 	# This library was specified with -dlopen.
2395 | 	if test "$pass" = dlopen; then
2397 | 	    $echo "$modename: cannot -dlopen a convenience library: \`$lib'" 1>&2
2401 | 	     test "$dlopen_support" != yes ||
2403 | 	    # If there is no dlname, no dlopen support or we're linking
2412 | 	fi # $pass = dlopen
2465 | 	  # Otherwise, use the dlname, so that lt_dlopen finds it.
2842 | 	      $echo "*** a static module, that should work as long as the dlopening application"
2843 | 	      $echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
2994 |       if test "$pass" != dlopen; then
3095 | 	$echo "$modename: warning: \`-dlopen' is ignored for archives" 1>&2
3162 | 	$echo "$modename: warning: \`-dlopen self' is ignored for libtool libraries" 1>&2
3797 | 	    $echo "*** a static module, that should work as long as the dlopening"
3798 | 	    $echo "*** application is linked with the -dlopen flag."
3816 | 	    $echo "*** or is declared to -dlopen it."
4226 | 	$echo "$modename: warning: \`-dlopen' is ignored for objects" 1>&2
4360 | 	if test "$dlopen_support" = unknown && test "$dlopen_self" = unknown &&
4361 | 	   test "$dlopen_self_static" = unknown; then
4362 | 	  $echo "$modename: warning: \`AC_LIBTOOL_DLOPEN' not used. Assuming no dlopen support."
5712 | # The name that we can dlopen(3).
5735 | # Files to dlopen/dlpreopen
5736 | dlopen='$dlfiles'
6351 |     # Handle -dlopen flags immediately.
6380 | 	# Skip this library if it cannot be dlopened.
6405 | 	$echo "$modename: warning \`-dlopen' is ignored for non-libtool libraries and objects" 1>&2
6768 |   -dlopen FILE      add the directory containing FILE to the library path
6770 | This mode sets the library path environment variable according to \`-dlopen'
6819 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
6828 |   -module           build a library that can dlopened
{% endraw %}

```
### projects/SATIrE/m4/libtool.m4

```

{% raw %}
1682 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1685 | m4_defun([_LT_TRY_DLOPEN_SELF],
1743 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1776 | ])# _LT_TRY_DLOPEN_SELF
1779 | # LT_SYS_DLOPEN_SELF
1781 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1783 | if test "x$enable_dlopen" != xyes; then
1784 |   enable_dlopen=unknown
1785 |   enable_dlopen_self=unknown
1786 |   enable_dlopen_self_static=unknown
1788 |   lt_cv_dlopen=no
1789 |   lt_cv_dlopen_libs=
1793 |     lt_cv_dlopen="load_add_on"
1794 |     lt_cv_dlopen_libs=
1795 |     lt_cv_dlopen_self=yes
1799 |     lt_cv_dlopen="LoadLibrary"
1800 |     lt_cv_dlopen_libs=
1804 |     lt_cv_dlopen="dlopen"
1805 |     lt_cv_dlopen_libs=
1810 |     AC_CHECK_LIB([dl], [dlopen],
1811 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1812 |     lt_cv_dlopen="dyld"
1813 |     lt_cv_dlopen_libs=
1814 |     lt_cv_dlopen_self=yes
1820 | 	  [lt_cv_dlopen="shl_load"],
1822 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1823 | 	[AC_CHECK_FUNC([dlopen],
1824 | 	      [lt_cv_dlopen="dlopen"],
1825 | 	  [AC_CHECK_LIB([dl], [dlopen],
1826 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1827 | 	    [AC_CHECK_LIB([svld], [dlopen],
1828 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1830 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1839 |   if test "x$lt_cv_dlopen" != xno; then
1840 |     enable_dlopen=yes
1842 |     enable_dlopen=no
1845 |   case $lt_cv_dlopen in
1846 |   dlopen)
1854 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1856 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1857 | 	  lt_cv_dlopen_self, [dnl
1858 | 	  _LT_TRY_DLOPEN_SELF(
1859 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1860 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1863 |     if test "x$lt_cv_dlopen_self" = xyes; then
1865 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1866 | 	  lt_cv_dlopen_self_static, [dnl
1867 | 	  _LT_TRY_DLOPEN_SELF(
1868 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1869 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1879 |   case $lt_cv_dlopen_self in
1880 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1881 |   *) enable_dlopen_self=unknown ;;
1884 |   case $lt_cv_dlopen_self_static in
1885 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1886 |   *) enable_dlopen_self_static=unknown ;;
1889 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1890 | 	 [Whether dlopen is supported])
1891 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1892 | 	 [Whether dlopen of programs is supported])
1893 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1894 | 	 [Whether dlopen of statically linked programs is supported])
1895 | ])# LT_SYS_DLOPEN_SELF
1898 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1900 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5585 |     [Compiler flag to allow reflexive dlopens])
5701 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### projects/SATIrE/m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
105 | # dlopen
107 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
110 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
111 | [_LT_SET_OPTION([LT_INIT], [dlopen])
114 | put the `dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### projects/interpreter/interp_extcall.C

```cpp

{% raw %}
266 |      DL(const char *filename, int flag) : dl(dlopen(filename, flag))
285 |      void *libc = dlopen("libc.so.6", RTLD_NOW | RTLD_GLOBAL);
287 |          libc = dlopen("libc.dylib", RTLD_NOW | RTLD_GLOBAL); // Mac OS X
{% endraw %}

```
### projects/PolyOpt2/config/libtool.m4

```

{% raw %}
1758 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1761 | m4_defun([_LT_TRY_DLOPEN_SELF],
1819 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1852 | ])# _LT_TRY_DLOPEN_SELF
1855 | # LT_SYS_DLOPEN_SELF
1857 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1859 | if test "x$enable_dlopen" != xyes; then
1860 |   enable_dlopen=unknown
1861 |   enable_dlopen_self=unknown
1862 |   enable_dlopen_self_static=unknown
1864 |   lt_cv_dlopen=no
1865 |   lt_cv_dlopen_libs=
1869 |     lt_cv_dlopen="load_add_on"
1870 |     lt_cv_dlopen_libs=
1871 |     lt_cv_dlopen_self=yes
1875 |     lt_cv_dlopen="LoadLibrary"
1876 |     lt_cv_dlopen_libs=
1880 |     lt_cv_dlopen="dlopen"
1881 |     lt_cv_dlopen_libs=
1886 |     AC_CHECK_LIB([dl], [dlopen],
1887 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1888 |     lt_cv_dlopen="dyld"
1889 |     lt_cv_dlopen_libs=
1890 |     lt_cv_dlopen_self=yes
1896 | 	  [lt_cv_dlopen="shl_load"],
1898 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1899 | 	[AC_CHECK_FUNC([dlopen],
1900 | 	      [lt_cv_dlopen="dlopen"],
1901 | 	  [AC_CHECK_LIB([dl], [dlopen],
1902 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1903 | 	    [AC_CHECK_LIB([svld], [dlopen],
1904 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1906 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1915 |   if test "x$lt_cv_dlopen" != xno; then
1916 |     enable_dlopen=yes
1918 |     enable_dlopen=no
1921 |   case $lt_cv_dlopen in
1922 |   dlopen)
1930 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1932 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1933 | 	  lt_cv_dlopen_self, [dnl
1934 | 	  _LT_TRY_DLOPEN_SELF(
1935 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1936 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1939 |     if test "x$lt_cv_dlopen_self" = xyes; then
1941 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1942 | 	  lt_cv_dlopen_self_static, [dnl
1943 | 	  _LT_TRY_DLOPEN_SELF(
1944 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1945 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1955 |   case $lt_cv_dlopen_self in
1956 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1957 |   *) enable_dlopen_self=unknown ;;
1960 |   case $lt_cv_dlopen_self_static in
1961 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1962 |   *) enable_dlopen_self_static=unknown ;;
1965 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1966 | 	 [Whether dlopen is supported])
1967 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1968 | 	 [Whether dlopen of programs is supported])
1969 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1970 | 	 [Whether dlopen of statically linked programs is supported])
1971 | ])# LT_SYS_DLOPEN_SELF
1974 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1976 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5676 |     [Compiler flag to allow reflexive dlopens])
5789 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### projects/PolyOpt2/config/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
105 | # dlopen
107 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
110 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
111 | [_LT_SET_OPTION([LT_INIT], [dlopen])
114 | put the `dlopen' option into LT_INIT's first parameter.])
118 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### projects/PolyOpt2/config/ltmain.sh

```bash

{% raw %}
1075 |       --dlopen|-dlopen)
1077 | 			opt_dlopen="${opt_dlopen+$opt_dlopen
1202 |     # Only execute mode is allowed to have -dlopen flags.
1203 |     if test -n "$opt_dlopen" && test "$opt_mode" != execute; then
1204 |       func_error "unrecognized option \`-dlopen'"
2352 |   -dlopen FILE      add the directory containing FILE to the library path
2354 | This mode sets the library path environment variable according to \`-dlopen'
2409 |   -dlopen FILE      \`-dlpreopen' FILE if it cannot be dlopened at runtime
2418 |   -module           build a library that can dlopened
2524 |     # Handle -dlopen flags immediately.
2525 |     for file in $opt_dlopen; do
2544 | 	# Skip this library if it cannot be dlopened.
2571 | 	func_warning "\`-dlopen' is ignored for non-libtool libraries and objects"
5183 | 	    dlopen_self=$dlopen_self_static
5189 | 	    dlopen_self=$dlopen_self_static
5195 | 	    dlopen_self=$dlopen_self_static
5253 | 	    elif test "$prev" = dlfiles && test "$dlopen_self" != yes; then
5337 | 		    if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5499 |       -dlopen)
5902 | 	      if test "$build_libtool_libs" = yes && test "$dlopen_support" = yes; then
5970 | 	  # This library was specified with -dlopen.
6087 | 	    func_fatal_help "libraries can \`-dlopen' only libtool libraries: $file"
6098 | 	passes="conv scan dlopen dlpreopen link"
6124 | 	dlopen) libs="$dlfiles" ;;
6155 |       if test "$pass" = dlopen; then
6374 | 	    if test "$pass" = dlpreopen || test "$dlopen_support" != yes || test "$build_libtool_libs" = no; then
6375 | 	      # If there is no dlopen support or we're linking statically,
6405 | 	dlopen=
6435 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
6481 | 	# This library was specified with -dlopen.
6482 | 	if test "$pass" = dlopen; then
6484 | 	    func_fatal_error "cannot -dlopen a convenience library: \`$lib'"
6487 | 	     test "$dlopen_support" != yes ||
6489 | 	    # If there is no dlname, no dlopen support or we're linking
6498 | 	fi # $pass = dlopen
6554 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
6556 | 	      # We recover the dlopen module name by 'saving' the la file
6580 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
6709 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
6710 | 	  dlopenmodule=""
6713 | 	      dlopenmodule="$dlpremoduletest"
6717 | 	  if test -z "$dlopenmodule" && test "$shouldnotlink" = yes && test "$pass" = link; then
6814 | 		    # if the lib is a (non-dlopened) module then we can not
6818 | 		      if test "X$dlopenmodule" != "X$lib"; then
6970 | 	      echo "*** a static module, that should work as long as the dlopening application"
6971 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
7115 |       if test "$pass" != dlopen; then
7214 | 	func_warning "\`-dlopen' is ignored for archives"
7281 | 	func_warning "\`-dlopen self' is ignored for libtool libraries"
7960 | 	    echo "*** a static module, that should work as long as the dlopening"
7961 | 	    echo "*** application is linked with the -dlopen flag."
7979 | 	    echo "*** or is declared to -dlopen it."
8590 | 	func_warning "\`-dlopen' is ignored for objects"
8708 |         && test "$dlopen_support" = unknown \
8709 | 	&& test "$dlopen_self" = unknown \
8710 | 	&& test "$dlopen_self_static" = unknown && \
8711 | 	  func_warning "\`LT_INIT([dlopen])' not used. Assuming no dlopen support."
9392 | # The name that we can dlopen(3).
9421 | # Files to dlopen/dlpreopen
9422 | dlopen='$dlfiles'
{% endraw %}

```
### projects/autoTuning/autotuning_lib.h

```cpp

{% raw %}
12 | // dlopen support  
16 | funcPointerT findFunctionUsingDlopen(const char* function_name, const char* lib_name);
{% endraw %}

```
### projects/autoTuning/Makefile.am

```

{% raw %}
18 | # this lib contains supporting functions for dlopen(), checkpointing, etc
{% endraw %}

```
### projects/autoTuning/autoTuningSupport.C

```cpp

{% raw %}
29 |     Outliner::use_dlopen= true;
{% endraw %}

```
### projects/autoTuning/autotuning_lib.c

```cpp

{% raw %}
26 | // internal one with direct use with dlopen()
27 | static funcPointerT findWithDlopen(const char* function_name, const char* lib_name)
32 |   functionLib = dlopen(lib_name, RTLD_LAZY);
90 | funcPointerT findFunctionUsingDlopen(const char* function_name, const char* lib_name)
100 |    result = findWithDlopen(function_name,lib_name);
104 |   result = findWithDlopen(function_name,lib_name);
{% endraw %}

```
### projects/autoTuning/tests/Makefile.am

```

{% raw %}
43 | # And using outlining support dlopen(): this is not necessary now since autoTuning will turn on -rose:outline:use_dlopen transparently
45 | 	../autoTuning  -c -rose:outline:use_dlopen -rose:output $@ $(ROSE_FLAGS) $(AT_FLAGS) $(EQUAL_PATH3) $(ROSE_PROF3) $(srcdir)/jacobi.c 
{% endraw %}

```
### projects/autoTuning/doc/smg2000_harmony.c

```cpp

{% raw %}
26 |     FunctionLib = dlopen("./unrolled_versions.so",RTLD_LAZY);
{% endraw %}

```
### projects/autoTuning/doc/smg2000_dlopen.c

```cpp

{% raw %}
0 | /* header for dlopen() etc */
20 |   FunctionLib = dlopen ("OUT__1__6755__.so",RTLD_LAZY);
{% endraw %}

```
### projects/autoTuning/doc/codeTriageTransformation.tex

```

{% raw %}
196 | \lstinline{-rose:outline:use_dlopen} will transform the code to use
197 | \lstinline{dlopen()} and \lstinline{dlsym()} to dynamically load the
279 | \item using \lstinline{dlopen()} to open a specified .so file containing
283 | \lstinline{dlopen()} opening the library source file so multiple variants of the file can be used to test optimization choices empirically when the program is restarted multiple times.
298 | \lstinputlisting{smg2000_dlopen.c}
392 | immediately before the line where \lstinline{dlopen()} is invoked to evaluate multiple
{% endraw %}

```
### projects/autoTuning/doc/smg2000_checkpoint2.c

```cpp

{% raw %}
51 |   FunctionLib =dlopen("OUT__1__6755__.so", RTLD_LAZY);
{% endraw %}

```