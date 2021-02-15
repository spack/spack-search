---
name: "rocm-openmp-extras"
layout: package
next_package: py-notebook
previous_package: libtheora
languages: ['bash', 'cmake', 'cpp', 'python']
---
## 4.0.0
136 / 100137 files match

 - [rocm-openmp-extras/flang/test/f90_correct/inc/oop734.mk](#rocm-openmp-extrasflangtestf90_correctincoop734mk)
 - [rocm-openmp-extras/llvm-project/clang/lib/StaticAnalyzer/Checkers/GenericTaintChecker.cpp](#rocm-openmp-extrasllvm-projectclanglibstaticanalyzercheckersgenerictaintcheckercpp)
 - [rocm-openmp-extras/llvm-project/clang/docs/ControlFlowIntegrityDesign.rst](#rocm-openmp-extrasllvm-projectclangdocscontrolflowintegritydesignrst)
 - [rocm-openmp-extras/llvm-project/openmp/runtime/src/z_Linux_util.cpp](#rocm-openmp-extrasllvm-projectopenmpruntimesrcz_linux_utilcpp)
 - [rocm-openmp-extras/llvm-project/openmp/runtime/src/ompt-general.cpp](#rocm-openmp-extrasllvm-projectopenmpruntimesrcompt-generalcpp)
 - [rocm-openmp-extras/llvm-project/openmp/runtime/src/kmp_alloc.cpp](#rocm-openmp-extrasllvm-projectopenmpruntimesrckmp_alloccpp)
 - [rocm-openmp-extras/llvm-project/openmp/runtime/src/thirdparty/ittnotify/ittnotify_config.h](#rocm-openmp-extrasllvm-projectopenmpruntimesrcthirdpartyittnotifyittnotify_configh)
 - [rocm-openmp-extras/llvm-project/openmp/libomptarget/src/rtl.cpp](#rocm-openmp-extrasllvm-projectopenmplibomptargetsrcrtlcpp)
 - [rocm-openmp-extras/llvm-project/openmp/libomptarget/plugins/ve/src/rtl.cpp](#rocm-openmp-extrasllvm-projectopenmplibomptargetpluginsvesrcrtlcpp)
 - [rocm-openmp-extras/llvm-project/openmp/libomptarget/plugins/generic-elf-64bit/src/rtl.cpp](#rocm-openmp-extrasllvm-projectopenmplibomptargetpluginsgeneric-elf-64bitsrcrtlcpp)
 - [rocm-openmp-extras/llvm-project/openmp/libomptarget/test/offloading/dynamic_module_load.c](#rocm-openmp-extrasllvm-projectopenmplibomptargettestoffloadingdynamic_module_loadc)
 - [rocm-openmp-extras/llvm-project/openmp/tools/multiplex/ompt-multiplex.h](#rocm-openmp-extrasllvm-projectopenmptoolsmultiplexompt-multiplexh)
 - [rocm-openmp-extras/llvm-project/lldb/unittests/ObjectFile/MachO/TestObjectFileMachO.cpp](#rocm-openmp-extrasllvm-projectlldbunittestsobjectfilemachotestobjectfilemachocpp)
 - [rocm-openmp-extras/llvm-project/lldb/include/lldb/Target/Process.h](#rocm-openmp-extrasllvm-projectlldbincludelldbtargetprocessh)
 - [rocm-openmp-extras/llvm-project/lldb/source/Plugins/Platform/MacOSX/PlatformAppleSimulator.cpp](#rocm-openmp-extrasllvm-projectlldbsourcepluginsplatformmacosxplatformapplesimulatorcpp)
 - [rocm-openmp-extras/llvm-project/lldb/source/Plugins/Platform/MacOSX/objcxx/PlatformiOSSimulatorCoreSimulatorSupport.mm](#rocm-openmp-extrasllvm-projectlldbsourcepluginsplatformmacosxobjcxxplatformiossimulatorcoresimulatorsupportmm)
 - [rocm-openmp-extras/llvm-project/lldb/source/Plugins/Platform/Android/PlatformAndroid.cpp](#rocm-openmp-extrasllvm-projectlldbsourcepluginsplatformandroidplatformandroidcpp)
 - [rocm-openmp-extras/llvm-project/lldb/source/Plugins/Platform/POSIX/PlatformPOSIX.cpp](#rocm-openmp-extrasllvm-projectlldbsourcepluginsplatformposixplatformposixcpp)
 - [rocm-openmp-extras/llvm-project/lldb/source/Plugins/DynamicLoader/MacOSX-DYLD/DynamicLoaderMacOS.cpp](#rocm-openmp-extrasllvm-projectlldbsourcepluginsdynamicloadermacosx-dylddynamicloadermacoscpp)
 - [rocm-openmp-extras/llvm-project/lldb/source/Plugins/DynamicLoader/POSIX-DYLD/DynamicLoaderPOSIXDYLD.cpp](#rocm-openmp-extrasllvm-projectlldbsourcepluginsdynamicloaderposix-dylddynamicloaderposixdyldcpp)
 - [rocm-openmp-extras/llvm-project/lldb/source/Target/Process.cpp](#rocm-openmp-extrasllvm-projectlldbsourcetargetprocesscpp)
 - [rocm-openmp-extras/llvm-project/lldb/source/Symbol/LocateSymbolFileMacOSX.cpp](#rocm-openmp-extrasllvm-projectlldbsourcesymbollocatesymbolfilemacosxcpp)
 - [rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/dlopen_other_executable/TestDlopenOtherExecutable.py](#rocm-openmp-extrasllvm-projectlldbtestapifunctionalitiesdlopen_other_executabletestdlopenotherexecutablepy)
 - [rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/dlopen_other_executable/main.c](#rocm-openmp-extrasllvm-projectlldbtestapifunctionalitiesdlopen_other_executablemainc)
 - [rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/load_using_paths/TestLoadUsingPaths.py](#rocm-openmp-extrasllvm-projectlldbtestapifunctionalitiesload_using_pathstestloadusingpathspy)
 - [rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/load_unload/TestLoadUnload.py](#rocm-openmp-extrasllvm-projectlldbtestapifunctionalitiesload_unloadtestloadunloadpy)
 - [rocm-openmp-extras/llvm-project/lldb/test/API/tools/lldb-vscode/breakpoint/main.cpp](#rocm-openmp-extrasllvm-projectlldbtestapitoolslldb-vscodebreakpointmaincpp)
 - [rocm-openmp-extras/llvm-project/lldb/test/API/macosx/find-dsym/deep-bundle/TestDeepBundle.py](#rocm-openmp-extrasllvm-projectlldbtestapimacosxfind-dsymdeep-bundletestdeepbundlepy)
 - [rocm-openmp-extras/llvm-project/lldb/test/API/macosx/find-dsym/bundle-with-dot-in-filename/TestBundleWithDotInFilename.py](#rocm-openmp-extrasllvm-projectlldbtestapimacosxfind-dsymbundle-with-dot-in-filenametestbundlewithdotinfilenamepy)
 - [rocm-openmp-extras/llvm-project/lldb/test/API/macosx/find-dsym/bundle-with-dot-in-filename/main.c](#rocm-openmp-extrasllvm-projectlldbtestapimacosxfind-dsymbundle-with-dot-in-filenamemainc)
 - [rocm-openmp-extras/llvm-project/lldb/packages/Python/lldbsuite/test/make/dylib.h](#rocm-openmp-extrasllvm-projectlldbpackagespythonlldbsuitetestmakedylibh)
 - [rocm-openmp-extras/llvm-project/lldb/tools/debugserver/source/MacOSX/DarwinLog/DarwinLogCollector.cpp](#rocm-openmp-extrasllvm-projectlldbtoolsdebugserversourcemacosxdarwinlogdarwinlogcollectorcpp)
 - [rocm-openmp-extras/llvm-project/lld/ELF/SyntheticSections.cpp](#rocm-openmp-extrasllvm-projectlldelfsyntheticsectionscpp)
 - [rocm-openmp-extras/llvm-project/lld/ELF/Config.h](#rocm-openmp-extrasllvm-projectlldelfconfigh)
 - [rocm-openmp-extras/llvm-project/lld/ELF/InputFiles.cpp](#rocm-openmp-extrasllvm-projectlldelfinputfilescpp)
 - [rocm-openmp-extras/llvm-project/lld/ELF/Driver.cpp](#rocm-openmp-extrasllvm-projectlldelfdrivercpp)
 - [rocm-openmp-extras/llvm-project/lld/ELF/Relocations.cpp](#rocm-openmp-extrasllvm-projectlldelfrelocationscpp)
 - [rocm-openmp-extras/llvm-project/lld/test/ELF/dt_flags.s](#rocm-openmp-extrasllvm-projectlldtestelfdt_flagss)
 - [rocm-openmp-extras/llvm-project/lld/docs/Partitions.rst](#rocm-openmp-extrasllvm-projectllddocspartitionsrst)
 - [rocm-openmp-extras/llvm-project/lld/docs/ld.lld.1](#rocm-openmp-extrasllvm-projectllddocsldlld1)
 - [rocm-openmp-extras/llvm-project/llvm/unittests/Support/DynamicLibrary/DynamicLibraryTest.cpp](#rocm-openmp-extrasllvm-projectllvmunittestssupportdynamiclibrarydynamiclibrarytestcpp)
 - [rocm-openmp-extras/llvm-project/llvm/lib/ExecutionEngine/Orc/LLJIT.cpp](#rocm-openmp-extrasllvm-projectllvmlibexecutionengineorclljitcpp)
 - [rocm-openmp-extras/llvm-project/llvm/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c](#rocm-openmp-extrasllvm-projectllvmlibexecutionengineinteljiteventsjitprofilingc)
 - [rocm-openmp-extras/llvm-project/llvm/lib/ExecutionEngine/IntelJITEvents/ittnotify_config.h](#rocm-openmp-extrasllvm-projectllvmlibexecutionengineinteljiteventsittnotify_configh)
 - [rocm-openmp-extras/llvm-project/llvm/lib/Support/Windows/DynamicLibrary.inc](#rocm-openmp-extrasllvm-projectllvmlibsupportwindowsdynamiclibraryinc)
 - [rocm-openmp-extras/llvm-project/llvm/lib/Support/Unix/DynamicLibrary.inc](#rocm-openmp-extrasllvm-projectllvmlibsupportunixdynamiclibraryinc)
 - [rocm-openmp-extras/llvm-project/llvm/include/llvm/ExecutionEngine/Orc/LLJIT.h](#rocm-openmp-extrasllvm-projectllvmincludellvmexecutionengineorclljith)
 - [rocm-openmp-extras/llvm-project/llvm/include/llvm/ExecutionEngine/Orc/TargetProcessControl.h](#rocm-openmp-extrasllvm-projectllvmincludellvmexecutionengineorctargetprocesscontrolh)
 - [rocm-openmp-extras/llvm-project/llvm/include/llvm/Config/config.h.cmake](#rocm-openmp-extrasllvm-projectllvmincludellvmconfigconfighcmake)
 - [rocm-openmp-extras/llvm-project/llvm/include/llvm/BinaryFormat/DynamicTags.def](#rocm-openmp-extrasllvm-projectllvmincludellvmbinaryformatdynamictagsdef)
 - [rocm-openmp-extras/llvm-project/llvm/include/llvm/Support/DynamicLibrary.h](#rocm-openmp-extrasllvm-projectllvmincludellvmsupportdynamiclibraryh)
 - [rocm-openmp-extras/llvm-project/llvm/include/llvm-c/LinkTimeOptimizer.h](#rocm-openmp-extrasllvm-projectllvmincludellvm-clinktimeoptimizerh)
 - [rocm-openmp-extras/llvm-project/llvm/cmake/config-ix.cmake](#rocm-openmp-extrasllvm-projectllvmcmakeconfig-ixcmake)
 - [rocm-openmp-extras/llvm-project/llvm/tools/llvm-jitlink/llvm-jitlink.cpp](#rocm-openmp-extrasllvm-projectllvmtoolsllvm-jitlinkllvm-jitlinkcpp)
 - [rocm-openmp-extras/llvm-project/llvm/tools/lli/lli.cpp](#rocm-openmp-extrasllvm-projectllvmtoolsllillicpp)
 - [rocm-openmp-extras/llvm-project/libcxx/src/include/refstring.h](#rocm-openmp-extrasllvm-projectlibcxxsrcincluderefstringh)
 - [rocm-openmp-extras/llvm-project/libcxx/lib/abi/3.9/x86_64-apple-darwin16.abilist](#rocm-openmp-extrasllvm-projectlibcxxlibabi39x86_64-apple-darwin16abilist)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/ubsan/ubsan_value.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibubsanubsan_valuecpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/msan/tests/msan_test.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibmsantestsmsan_testcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/cfi/cfi.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibcficficpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/asan/asan_malloc_mac.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibasanasan_malloc_maccpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/asan/asan_internal.h](#rocm-openmp-extrasllvm-projectcompiler-rtlibasanasan_internalh)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/asan/asan_interceptors.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibasanasan_interceptorscpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/asan/asan_rtl.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibasanasan_rtlcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/asan/tests/asan_test.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibasantestsasan_testcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_netbsd.h](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_platform_limits_netbsdh)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_linux.h](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_linuxh)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform.h](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_platformh)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_symbolizer_libcdep.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_symbolizer_libcdepcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_common_interceptors.inc](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_common_interceptorsinc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_freebsd.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_platform_limits_freebsdcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_mac.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_maccpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_freebsd.h](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_platform_limits_freebsdh)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_netbsd.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_platform_limits_netbsdcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_linux.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_linuxcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_coverage_fuchsia.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_coverage_fuchsiacpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_unwind_linux_libcdep.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibsanitizer_commonsanitizer_unwind_linux_libcdepcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/gwp_asan/guarded_pool_allocator.h](#rocm-openmp-extrasllvm-projectcompiler-rtlibgwp_asanguarded_pool_allocatorh)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/dfsan/done_abilist.txt](#rocm-openmp-extrasllvm-projectcompiler-rtlibdfsandone_abilisttxt)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/dfsan/dfsan_custom.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibdfsandfsan_customcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/dfsan/libc_ubuntu1404_abilist.txt](#rocm-openmp-extrasllvm-projectcompiler-rtlibdfsanlibc_ubuntu1404_abilisttxt)
 - [rocm-openmp-extras/llvm-project/compiler-rt/lib/tsan/rtl/tsan_interceptors_posix.cpp](#rocm-openmp-extrasllvm-projectcompiler-rtlibtsanrtltsan_interceptors_posixcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/msan/dtls_test.c](#rocm-openmp-extrasllvm-projectcompiler-rttestmsandtls_testc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/msan/dlopen_executable.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestmsandlopen_executablecpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/msan/dlerror.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestmsandlerrorcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/cfi/cross-dso/shadow_is_read_only.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestcficross-dsoshadow_is_read_onlycpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/cfi/cross-dso/icall/dlopen.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestcficross-dsoicalldlopencpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/start-deactivated.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcasesposixstart-deactivatedcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/coverage-module-unloaded.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcasesposixcoverage-module-unloadedcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/shared-lib-test.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcasesposixshared-lib-testcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/global-registration.c](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcasesposixglobal-registrationc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/dlclose-test.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcasesposixdlclose-testcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/asan-symbolize-sanity-test.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcasesposixasan-symbolize-sanity-testcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/init-order-dlopen.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcaseslinuxinit-order-dlopencpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/activation-options.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcaseslinuxactivation-optionscpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/pthread_create_from_constructor.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcaseslinuxpthread_create_from_constructorcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/function-sections-are-bad.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcaseslinuxfunction-sections-are-badcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/stress_dtls.c](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcaseslinuxstress_dtlsc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/asan_dlopen_test.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcaseslinuxasan_dlopen_testcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/dlopen-mixed-c-cxx.c](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcaseslinuxdlopen-mixed-c-cxxc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/stack-trace-dlclose.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcaseslinuxstack-trace-dlclosecpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Darwin/init_for_dlopen.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestasantestcasesdarwininit_for_dlopencpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/sanitizer_common/TestCases/get_module_and_offset_for_pc.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestsanitizer_commontestcasesget_module_and_offset_for_pccpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/sanitizer_common/TestCases/Linux/deepbind.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestsanitizer_commontestcaseslinuxdeepbindcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/sanitizer_common/TestCases/Darwin/print-stack-trace-in-code-loaded-after-fork.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestsanitizer_commontestcasesdarwinprint-stack-trace-in-code-loaded-after-forkcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/dfsan/custom.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestdfsancustomcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/lsan/TestCases/Linux/use_tls_dynamic.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttestlsantestcaseslinuxuse_tls_dynamiccpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/load_shared_lib.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttesttsanload_shared_libcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/ignore_lib1.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttesttsanignore_lib1cpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/dl_iterate_phdr.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttesttsandl_iterate_phdrcpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/dlclose.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttesttsandlclosecpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/dtls.c](#rocm-openmp-extrasllvm-projectcompiler-rttesttsandtlsc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/ignore_lib6.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttesttsanignore_lib6cpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/ignore_lib5.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttesttsanignore_lib5cpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/ignore_lib3.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttesttsanignore_lib3cpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/ignore_lib2.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttesttsanignore_lib2cpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/ignore_lib4.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttesttsanignore_lib4cpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/Darwin/dlopen.cpp](#rocm-openmp-extrasllvm-projectcompiler-rttesttsandarwindlopencpp)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Posix/gcov-dlopen.c](#rocm-openmp-extrasllvm-projectcompiler-rttestprofileposixgcov-dlopenc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Posix/instrprof-dlopen.test](#rocm-openmp-extrasllvm-projectcompiler-rttestprofileposixinstrprof-dlopentest)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Linux/instrprof-dlopen.test](#rocm-openmp-extrasllvm-projectcompiler-rttestprofilelinuxinstrprof-dlopentest)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c](#rocm-openmp-extrasllvm-projectcompiler-rttestprofileinputsinstrprof-dlopen-mainc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c](#rocm-openmp-extrasllvm-projectcompiler-rttestprofileinputsinstrprof-value-prof-visibilityc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c](#rocm-openmp-extrasllvm-projectcompiler-rttestprofileinputsinstrprof-dlopen-dlclose-mainc)
 - [rocm-openmp-extras/llvm-project/compiler-rt/cmake/config-ix.cmake](#rocm-openmp-extrasllvm-projectcompiler-rtcmakeconfig-ixcmake)
 - [rocm-openmp-extras/llvm-project/polly/lib/External/isl/ltmain.sh](#rocm-openmp-extrasllvm-projectpollylibexternalislltmainsh)
 - [rocm-openmp-extras/llvm-project/polly/lib/External/isl/m4/libtool.m4](#rocm-openmp-extrasllvm-projectpollylibexternalislm4libtoolm4)
 - [rocm-openmp-extras/llvm-project/polly/lib/External/isl/m4/ltoptions.m4](#rocm-openmp-extrasllvm-projectpollylibexternalislm4ltoptionsm4)
 - [rocm-openmp-extras/llvm-project/polly/lib/External/ppcg/ltmain.sh](#rocm-openmp-extrasllvm-projectpollylibexternalppcgltmainsh)
 - [rocm-openmp-extras/llvm-project/polly/lib/External/ppcg/m4/libtool.m4](#rocm-openmp-extrasllvm-projectpollylibexternalppcgm4libtoolm4)
 - [rocm-openmp-extras/llvm-project/polly/lib/External/ppcg/m4/ltoptions.m4](#rocm-openmp-extrasllvm-projectpollylibexternalppcgm4ltoptionsm4)
 - [rocm-openmp-extras/llvm-project/polly/tools/GPURuntime/GPUJIT.c](#rocm-openmp-extrasllvm-projectpollytoolsgpuruntimegpujitc)
 - [rocm-openmp-extras/llvm-project/libcxxabi/src/include/refstring.h](#rocm-openmp-extrasllvm-projectlibcxxabisrcincluderefstringh)
 - [rocm-openmp-extras/llvm-project/libcxxabi/test/test_demangle.pass.cpp](#rocm-openmp-extrasllvm-projectlibcxxabitesttest_demanglepasscpp)
 - [rocm-openmp-extras/llvm-project/clang-tools-extra/clangd/xpc/test-client/ClangdXPCTestClient.cpp](#rocm-openmp-extrasllvm-projectclang-tools-extraclangdxpctest-clientclangdxpctestclientcpp)
 - [test/omptests/fast_test/main.cpp](#testomptestsfast_testmaincpp)

### rocm-openmp-extras/flang/test/f90_correct/inc/oop734.mk

```

{% raw %}
14 | 	@cat $(TEST).rslt | grep -v dlopen | grep -v mktemp > tmp || true
{% endraw %}

```
### rocm-openmp-extras/llvm-project/clang/lib/StaticAnalyzer/Checkers/GenericTaintChecker.cpp

```

{% raw %}
869 |                         .Case("dlopen", 0)
{% endraw %}

```
### rocm-openmp-extras/llvm-project/clang/docs/ControlFlowIntegrityDesign.rst

```

{% raw %}
531 | dlopen-ed/dlclose-d periodically, even frequently.
650 | performance in the handling of dlopen(). It is recommended that
{% endraw %}

```
### rocm-openmp-extras/llvm-project/openmp/runtime/src/z_Linux_util.cpp

```

{% raw %}
1358 |      handler. Mathworks: dlsym() is unsafe. We call dlsym and dlopen
{% endraw %}

```
### rocm-openmp-extras/llvm-project/openmp/runtime/src/ompt-general.cpp

```

{% raw %}
253 |       void *h = dlopen(fname, RTLD_LAZY);
276 |     void *h = dlopen(fname, RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/openmp/runtime/src/kmp_alloc.cpp

```

{% raw %}
1256 |   h_memkind = dlopen(kmp_mk_lib_name, RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/openmp/runtime/src/thirdparty/ittnotify/ittnotify_config.h

```cpp

{% raw %}
300 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
352 | void* dlopen(const char*, int) __attribute__((weak));
355 | #define DL_SYMBOLS (dlopen && dlsym && dlclose)
{% endraw %}

```
### rocm-openmp-extras/llvm-project/openmp/libomptarget/src/rtl.cpp

```

{% raw %}
106 |   void *handle = dlopen("libomptarget.so", RTLD_NOW);
108 |     DP("dlopen() failed: %s\n", dlerror());
130 |     if (!found) // Not finding quick check files is a faster fail than dlopen
134 |     void *dynlib_handle = dlopen(full_plugin_name.c_str(), RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/openmp/libomptarget/plugins/ve/src/rtl.cpp

```

{% raw %}
248 |   // 2) Use dlopen to load the file and dlsym to retrieve the symbols.
{% endraw %}

```
### rocm-openmp-extras/llvm-project/openmp/libomptarget/plugins/generic-elf-64bit/src/rtl.cpp

```

{% raw %}
214 |   // 2) Use dlopen to load the file and dlsym to retrieve the symbols.
233 |   DynLibTy Lib = {tmp_name, dlopen(tmp_name, RTLD_LAZY)};
{% endraw %}

```
### rocm-openmp-extras/llvm-project/openmp/libomptarget/test/offloading/dynamic_module_load.c

```cpp

{% raw %}
18 |   void *Handle = dlopen(argv[1], RTLD_NOW);
22 |     printf("dlopen() failed: %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/openmp/tools/multiplex/ompt-multiplex.h

```cpp

{% raw %}
1057 |       void *h = dlopen(tool_libs_buffer + progress, RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/unittests/ObjectFile/MachO/TestObjectFileMachO.cpp

```

{% raw %}
45 |   void *libobjc = dlopen("/usr/lib/libobjc.A.dylib", RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/include/lldb/Target/Process.h

```cpp

{% raw %}
2834 |   std::unique_ptr<UtilityFunction> m_dlopen_utility_func_up;
2835 |   llvm::once_flag m_dlopen_utility_func_flag_once;
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/source/Plugins/Platform/MacOSX/PlatformAppleSimulator.cpp

```

{% raw %}
234 |       dlopen(core_sim_path.c_str(), RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/source/Plugins/Platform/MacOSX/objcxx/PlatformiOSSimulatorCoreSimulatorSupport.mm

```

{% raw %}
23 | // against it, so we dlopen()
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/source/Plugins/Platform/Android/PlatformAndroid.cpp

```

{% raw %}
364 |   std::vector<const char *> dl_open_names = { "__dl_dlopen", "dlopen" };
378 |               extern "C" void* dlopen(const char*, int) asm("__dl_dlopen");
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/source/Plugins/Platform/POSIX/PlatformPOSIX.cpp

```

{% raw %}
468 |   expr_options.SetTrapExceptions(false); // dlopen can't throw exceptions, so
489 |   // __lldb_dlopen_result for consistency. The wrapper returns a void * but
492 |   static const char *dlopen_wrapper_code = R"(
493 |   struct __lldb_dlopen_result {
502 |   void * __lldb_dlopen_wrapper (const char *name, 
505 |                                 __lldb_dlopen_result *result_ptr)
509 |       result_ptr->image_ptr = dlopen(name, 2);
523 |       result_ptr->image_ptr = dlopen(buffer, 2);
535 |   static const char *dlopen_wrapper_name = "__lldb_dlopen_wrapper";
537 |   // Insert the dlopen shim defines into our generic expression:
539 |   expr.append(dlopen_wrapper_code);
543 |   std::unique_ptr<UtilityFunction> dlopen_utility_func_up(process
546 |                                                   dlopen_wrapper_name,
549 |     error.SetErrorStringWithFormat("dlopen error: could not make utility"
553 |   if (!dlopen_utility_func_up->Install(diagnostics, exe_ctx)) {
554 |     error.SetErrorStringWithFormat("dlopen error: could not install utility"
562 |   FunctionCaller *do_dlopen_function = nullptr;
585 |   do_dlopen_function = dlopen_utility_func_up->MakeFunctionCaller(
588 |     error.SetErrorStringWithFormat("dlopen error: could not make function"
593 |   do_dlopen_function = dlopen_utility_func_up->GetFunctionCaller();
594 |   if (!do_dlopen_function) {
595 |     error.SetErrorString("dlopen error: could not get function caller.");
600 |   return dlopen_utility_func_up;
616 |     error.SetErrorString("dlopen error: no thread available to call dlopen.");
626 |   UtilityFunction *dlopen_utility_func;
628 |   FunctionCaller *do_dlopen_function = nullptr;
632 |   dlopen_utility_func = process->GetLoadImageUtilityFunction(
637 |   if (!dlopen_utility_func)
640 |   do_dlopen_function = dlopen_utility_func->GetFunctionCaller();
641 |   if (!do_dlopen_function) {
642 |     error.SetErrorString("dlopen error: could not get function caller.");
645 |   arguments = do_dlopen_function->GetArgumentValues();
655 |     error.SetErrorStringWithFormat("dlopen error: could not allocate memory"
668 |     error.SetErrorStringWithFormat("dlopen error: could not write path string:"
680 |     error.SetErrorStringWithFormat("dlopen error: could not allocate memory"
699 |   // to avoid having to call malloc in the dlopen function.
729 |       error.SetErrorStringWithFormat("dlopen error: could not allocate memory"
745 |       error.SetErrorStringWithFormat("dlopen error: could not write path array:"
757 |       error.SetErrorStringWithFormat("dlopen error: could not allocate memory"
778 |   if (!do_dlopen_function->WriteFunctionArguments(exe_ctx, 
782 |     error.SetErrorStringWithFormat("dlopen error: could not write function "
792 |       llvm::make_scope_exit([do_dlopen_function, &exe_ctx, func_args_addr] {
793 |         do_dlopen_function->DeallocateFunctionResults(exe_ctx, func_args_addr);
802 |   options.SetTrapExceptions(false); // dlopen can't throw exceptions, so
811 |     error.SetErrorString("dlopen error: Unable to get TypeSystemClang");
820 |   ExpressionResults results = do_dlopen_function->ExecuteFunction(
823 |     error.SetErrorStringWithFormat("dlopen error: failed executing "
824 |                                    "dlopen wrapper function: %s", 
829 |   // Read the dlopen token from the return area:
833 |     error.SetErrorStringWithFormat("dlopen error: could not read the return "
838 |   // The dlopen succeeded!
843 |       // exit from the dlopen function, so we can just read it from there:
853 |   std::string dlopen_error_str;
857 |     error.SetErrorStringWithFormat("dlopen error: could not read error string: "
863 |                                                     dlopen_error_str, 
866 |     error.SetErrorStringWithFormat("dlopen error: %s",
867 |                                    dlopen_error_str.c_str());
869 |     error.SetErrorStringWithFormat("dlopen failed for unknown reasons.");
904 |               extern "C" void* dlopen(const char*, int);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/source/Plugins/DynamicLoader/MacOSX-DYLD/DynamicLoaderMacOS.cpp

```

{% raw %}
450 |     // _dyld_start) - so we should not allow dlopen calls. But if we found more
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/source/Plugins/DynamicLoader/POSIX-DYLD/DynamicLoaderPOSIXDYLD.cpp

```

{% raw %}
260 | // loaded modules (via dlopen).
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/source/Target/Process.cpp

```

{% raw %}
6122 |   llvm::call_once(m_dlopen_utility_func_flag_once,
6123 |                   [&] { m_dlopen_utility_func_up = factory(); });
6124 |   return m_dlopen_utility_func_up.get();
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/source/Symbol/LocateSymbolFileMacOSX.cpp

```

{% raw %}
59 |     void *handle = dlopen ("/System/Library/PrivateFrameworks/DebugSymbols.framework/DebugSymbols", RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/dlopen_other_executable/TestDlopenOtherExecutable.py

```python

{% raw %}
11 |     # glibc's dlopen doesn't support opening executables.
17 |         # Launch and stop before the dlopen call.
26 |         # Continue so that dlopen is called.
28 |             "// break after dlopen", lldb.SBFileSpec("main.c"))
40 |         # Test that we hit the breakpoint after dlopen.
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/dlopen_other_executable/main.c

```cpp

{% raw %}
5 |   // dlopen the 'other' test executable.
6 |   int h = dlopen("other", RTLD_LAZY);
7 |   assert(h && "dlopen failed?");
8 |   return i; // break after dlopen
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/load_using_paths/TestLoadUsingPaths.py

```python

{% raw %}
40 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/functionalities/load_unload/TestLoadUnload.py

```python

{% raw %}
95 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
152 |     @skipIfWindows  # Windows doesn't have dlopen and friends, dynamic libraries work differently
233 |         # Break at main.cpp before the call to dlopen().
309 |         """Test breakpoint by name works correctly with dlopen'ing."""
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/tools/lldb-vscode/breakpoint/main.cpp

```

{% raw %}
24 |   void *handle = dlopen(libother_name, RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/macosx/find-dsym/deep-bundle/TestDeepBundle.py

```python

{% raw %}
39 |         # Give the inferior time to start up, dlopen a bundle, remove the bundle it linked in
42 |         # Since the library that was dlopen()'ed is now removed, lldb will need to find the
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/macosx/find-dsym/bundle-with-dot-in-filename/TestBundleWithDotInFilename.py

```python

{% raw %}
41 |         # Give the inferior time to start up, dlopen a bundle, remove the bundle it linked in
44 |         # Since the library that was dlopen()'ed is now removed, lldb will need to find the
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/test/API/macosx/find-dsym/bundle-with-dot-in-filename/main.c

```cpp

{% raw %}
9 |     void *handle = dlopen ("com.apple.sbd.xpc/com.apple.sbd", RTLD_NOW);
18 |             // before we've removed the dlopen'ed bundle, lldb will find the bundle
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/packages/Python/lldbsuite/test/make/dylib.h

```cpp

{% raw %}
38 |   return dlopen(fullname, RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lldb/tools/debugserver/source/MacOSX/DarwinLog/DarwinLogCollector.cpp

```

{% raw %}
52 |     dlopen ("/System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport", RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lld/ELF/SyntheticSections.cpp

```

{% raw %}
1317 |   if (config->zNodlopen)
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lld/ELF/Config.h

```cpp

{% raw %}
226 |   bool zNodlopen;
296 |   // it may not be loaded using dlopen().
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lld/ELF/InputFiles.cpp

```

{% raw %}
881 |     // dynamic loaders require the presence of an attribute section for dlopen
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lld/ELF/Driver.cpp

```

{% raw %}
437 |          s == "nodelete" || s == "nodlopen" || s == "noexecstack" ||
1059 |   config->zNodlopen = hasZOption(args, "nodlopen");
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lld/ELF/Relocations.cpp

```

{% raw %}
213 |   // being suitable for being dynamically loaded via dlopen. GOT[e0] is the
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lld/test/ELF/dt_flags.s

```

{% raw %}
6 | # RUN:   -z nodelete -z nodlopen -z origin -Bsymbolic %t %t.so -o %t1
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lld/docs/Partitions.rst

```

{% raw %}
27 | the program will use ``dlopen``/``dlsym`` or similar functions to dynamically
29 | and call it. Note, however, that the standard ``dlopen`` function does not
30 | allow specifying a load address. On Android, the ``android_dlopen_ext``
{% endraw %}

```
### rocm-openmp-extras/llvm-project/lld/docs/ld.lld.1

```

{% raw %}
697 | .It Cm nodlopen
701 | .Xr dlopen 3 .
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/unittests/Support/DynamicLibrary/DynamicLibraryTest.cpp

```

{% raw %}
32 | #if defined(_WIN32) || (defined(HAVE_DLFCN_H) && defined(HAVE_DLOPEN))
173 |   EXPECT_EQ(Err, "dlopen() not supported on this platform");
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/lib/ExecutionEngine/Orc/LLJIT.cpp

```

{% raw %}
121 | /// some runtime API, including __cxa_atexit, dlopen, and dlclose.
527 |   using DLOpenType = void *(*)(const char *Name, int Mode);
534 |     DLOpenType dlopen = nullptr;
559 |     if (auto Err = hookUpFunction(DlFcn.dlopen, "dlopen"))
667 |     HelperSymbols[J.mangleAndIntern("__lljit.dlopen_helper")] =
668 |         JITEvaluatedSymbol(pointerToJITTargetAddress(dlopenHelper),
737 |     addHelperAndWrapper(*M, "dlopen",
739 |                         GlobalValue::DefaultVisibility, "__lljit.dlopen_helper",
770 |   void *jit_dlopen(const char *Path, int Mode) {
798 |     // Fall through to dlopen if no JITDylib found for Path.
799 |     return DlFcn.dlopen(Path, Mode);
802 |   static void *dlopenHelper(void *Self, const char *Path, int Mode) {
803 |     return static_cast<MachOPlatformSupport *>(Self)->jit_dlopen(Path, Mode);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/lib/ExecutionEngine/IntelJITEvents/jitprofiling.c

```cpp

{% raw %}
347 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
356 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/lib/ExecutionEngine/IntelJITEvents/ittnotify_config.h

```cpp

{% raw %}
245 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/lib/Support/Windows/DynamicLibrary.inc

```

{% raw %}
34 | void *DynamicLibrary::HandleSet::DLOpen(const char *File, std::string *Err) {
36 |   // simillar to dlopen(NULL, RTLD_LAZY|RTLD_GLOBAL)
130 |   // Try EXE first, mirroring what dlsym(dlopen(NULL)) does.
135 |     // This is different behaviour than what Posix dlsym(dlopen(NULL)) does.
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/lib/Support/Unix/DynamicLibrary.inc

```

{% raw %}
12 | #if defined(HAVE_DLFCN_H) && defined(HAVE_DLOPEN)
26 | void *DynamicLibrary::HandleSet::DLOpen(const char *File, std::string *Err) {
27 |   void *Handle = ::dlopen(File, RTLD_LAZY|RTLD_GLOBAL);
35 |   // with the handle of dlopen(NULL, RTLD_GLOBAL).
51 | #else // !HAVE_DLOPEN
55 | void *DynamicLibrary::HandleSet::DLOpen(const char *File, std::string *Err) {
56 |   if (Err) *Err = "dlopen() not supported on this platform";
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/include/llvm/ExecutionEngine/Orc/LLJIT.h

```cpp

{% raw %}
459 | /// functions (dlopen, dlclose, dlsym, dlerror) that work for JITDylibs as
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/include/llvm/ExecutionEngine/Orc/TargetProcessControl.h

```cpp

{% raw %}
116 |   /// dlopen in the target process).
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/include/llvm/Config/config.h.cmake

```cmake

{% raw %}
54 | /* Define if dlopen() is available on this platform. */
55 | #cmakedefine HAVE_DLOPEN ${HAVE_DLOPEN}
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/include/llvm/BinaryFormat/DynamicTags.def

```

{% raw %}
195 |                                                 // by rld on dlopen() calls.
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/include/llvm/Support/DynamicLibrary.h

```cpp

{% raw %}
90 |       /// SO_Linker - Search as a call to dlsym(dlopen(NULL)) would when
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/include/llvm-c/LinkTimeOptimizer.h

```cpp

{% raw %}
49 |   /// linker to use dlopen() interface to dynamically load LinkTimeOptimizer.
50 |   /// extern "C" helps, because dlopen() interface uses name to find the symbol.
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/cmake/config-ix.cmake

```cmake

{% raw %}
99 |   check_library_exists(dl dlopen "" HAVE_LIBDL)
249 |   check_symbol_exists(dlopen dlfcn.h HAVE_DLOPEN)
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/tools/llvm-jitlink/llvm-jitlink.cpp

```

{% raw %}
71 |     Dylibs("dlopen", cl::desc("Dynamic libraries to load before linking"),
{% endraw %}

```
### rocm-openmp-extras/llvm-project/llvm/tools/lli/lli.cpp

```

{% raw %}
123 |     Dylibs("dlopen", cl::desc("Dynamic libraries to load before linking"),
{% endraw %}

```
### rocm-openmp-extras/llvm-project/libcxx/src/include/refstring.h

```cpp

{% raw %}
46 |     void* handle = dlopen("/usr/lib/libstdc++.6.dylib", RTLD_NOLOAD);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/libcxx/lib/abi/3.9/x86_64-apple-darwin16.abilist

```

{% raw %}
2358 | {'type': 'U', 'name': '_dlopen'}
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/ubsan/ubsan_value.cpp

```

{% raw %}
35 |   static bool AttemptedDlopen = false;
39 |   // Prevent threads from racing to dlopen().
44 |     if (!AttemptedDlopen) {
45 |       ObjCHandle = dlopen(
53 |       AttemptedDlopen = true;
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/msan/tests/msan_test.cpp

```

{% raw %}
3138 | #ifndef MSAN_TEST_DISABLE_DLOPEN
3182 |   // Having at least one dlopen'ed library in the process makes this more
3184 |   void *lib = dlopen(path, RTLD_LAZY);
3194 | TEST(MemorySanitizer, dlopen) {
3198 |   // We need to clear shadow for globals when doing dlopen.  In order to test
3202 |   // start out clean after dlopen.
3204 |     void *lib = dlopen(path, RTLD_LAZY);
3219 | // Regression test for a crash in dlopen() interceptor.
3220 | TEST(MemorySanitizer, dlopenFailed) {
3222 |   void *lib = dlopen(path, RTLD_LAZY);
3226 | #endif // MSAN_TEST_DISABLE_DLOPEN
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/cfi/cfi.cpp

```

{% raw %}
209 | //    dlopen(RTLD_NOLOAD | RTLD_LAZY)
414 | // Setup shadow for dlopen()ed libraries.
415 | // The actual shadow setup happens after dlopen() returns, which means that
418 | // In glibc, mmap inside dlopen is not interceptable.
422 | INTERCEPTOR(void*, dlopen, const char *filename, int flag) {
425 |   void *handle = REAL(dlopen)(filename, flag);
446 |   INTERCEPT_FUNCTION(dlopen);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/asan/asan_malloc_mac.cpp

```

{% raw %}
67 | bool HandleDlopenInit() {
68 |   static_assert(SANITIZER_SUPPORTS_INIT_FOR_DLOPEN,
69 |                 "Expected SANITIZER_SUPPORTS_INIT_FOR_DLOPEN to be true");
73 |   // dlopen().
74 |   auto init_str = GetEnv("APPLE_ASAN_INIT_FOR_DLOPEN");
79 |   // When we are loaded via `dlopen()` path we still initialize the malloc zone
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/asan/asan_internal.h

```cpp

{% raw %}
121 | // ASan library being loaded via `dlopen()`. Platforms may perform any
122 | // `dlopen()` specific initialization inside this function.
123 | bool HandleDlopenInit();
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/asan/asan_interceptors.cpp

```

{% raw %}
128 | // Strict init-order checking is dlopen-hostile:
130 | #define COMMON_INTERCEPTOR_ON_DLOPEN(filename, flag)                           \
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/asan/asan_rtl.cpp

```

{% raw %}
410 |   // dlopen() and the platform supports it.
411 |   if (SANITIZER_SUPPORTS_INIT_FOR_DLOPEN && UNLIKELY(HandleDlopenInit())) {
413 |     VReport(1, "AddressSanitizer init is being performed for dlopen().\n");
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/asan/tests/asan_test.cpp

```

{% raw %}
1119 | // pthread_exit tries to perform unwinding stuff that leads to dlopen'ing
1120 | // libgcc_s.so. dlopen in its turn calls malloc to store "libgcc_s.so" string
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_netbsd.h

```cpp

{% raw %}
22 | void *__sanitizer_get_link_map_by_dlopen_handle(void *handle);
23 | # define GET_LINK_MAP_BY_DLOPEN_HANDLE(handle) \
24 |     (link_map *)__sanitizer_get_link_map_by_dlopen_handle(handle)
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_linux.h

```cpp

{% raw %}
26 | struct link_map;  // Opaque type returned by dlopen().
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform.h

```cpp

{% raw %}
323 | // pthread_exit() performs unwinding that leads to dlopen'ing libgcc_s.so.
324 | // dlopen mallocs "libgcc_s.so" string which confuses LSan, it fails to realize
356 | // `dlopen()`.
358 | #define SANITIZER_SUPPORTS_INIT_FOR_DLOPEN 1
360 | #define SANITIZER_SUPPORTS_INIT_FOR_DLOPEN 0
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_symbolizer_libcdep.cpp

```

{% raw %}
211 |   // dlopen/dlclose interceptors invalidate the module list, but when
214 | #if !SANITIZER_INTERCEPT_DLOPEN_DLCLOSE
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_common_interceptors.inc

```

{% raw %}
23 | //   COMMON_INTERCEPTOR_ON_DLOPEN
208 | #ifndef COMMON_INTERCEPTOR_ON_DLOPEN
209 | #define COMMON_INTERCEPTOR_ON_DLOPEN(filename, flag) \
6199 | #if SANITIZER_INTERCEPT_DLOPEN_DLCLOSE
6200 | INTERCEPTOR(void*, dlopen, const char *filename, int flag) {
6202 |   COMMON_INTERCEPTOR_ENTER_NOIGNORE(ctx, dlopen, filename, flag);
6204 |   COMMON_INTERCEPTOR_ON_DLOPEN(filename, flag);
6205 |   void *res = REAL(dlopen)(filename, flag);
6219 | #define INIT_DLOPEN_DLCLOSE          \
6220 |   COMMON_INTERCEPT_FUNCTION(dlopen); \
6223 | #define INIT_DLOPEN_DLCLOSE
10178 |   INIT_DLOPEN_DLCLOSE;
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_freebsd.cpp

```

{% raw %}
93 | void *__sanitizer_get_link_map_by_dlopen_handle(void *handle) {
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_mac.cpp

```

{% raw %}
983 |   void *dlopen_addr = dlsym(RTLD_DEFAULT, "pthread_create");
984 |   RAW_CHECK(dladdr(dlopen_addr, &info_pthread_create));
988 |         "loaded too late (e.g. via dlopen). Please launch the executable "
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_freebsd.h

```cpp

{% raw %}
27 | void *__sanitizer_get_link_map_by_dlopen_handle(void *handle);
28 | #define GET_LINK_MAP_BY_DLOPEN_HANDLE(handle) \
29 |   (link_map *)__sanitizer_get_link_map_by_dlopen_handle(handle)
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_platform_limits_netbsd.cpp

```

{% raw %}
374 | void *__sanitizer_get_link_map_by_dlopen_handle(void* handle) {
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_linux.cpp

```

{% raw %}
2211 |         "You are trying to dlopen a %s shared library with RTLD_DEEPBIND flag"
2215 |         "RTLD_DEEPBIND from dlopen flags.\n",
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_coverage_fuchsia.cpp

```

{% raw %}
68 |   // dlopen call on a secondary thread will run constructors that get here.
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/sanitizer_common/sanitizer_unwind_linux_libcdep.cpp

```

{% raw %}
19 | #include <dlfcn.h>  // for dlopen()
100 |   void *p = dlopen("libcorkscrew.so", RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/gwp_asan/guarded_pool_allocator.h

```cpp

{% raw %}
202 |     // may not be safe for the allocator (i.e. the unwinder calls dlopen(),
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/dfsan/done_abilist.txt

```

{% raw %}
152 | fun:dlopen=custom
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/dfsan/dfsan_custom.cpp

```

{% raw %}
349 | // dlopen() ultimately calls mmap() down inside the loader, which generally
353 | __dfsw_dlopen(const char *filename, int flag, dfsan_label filename_label,
355 |   void *handle = dlopen(filename, flag);
356 |   link_map *map = GET_LINK_MAP_BY_DLOPEN_HANDLE(handle);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/dfsan/libc_ubuntu1404_abilist.txt

```

{% raw %}
789 | fun:__libc_dlopen_mode=uninstrumented
1562 | fun:dlopen=uninstrumented
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/lib/tsan/rtl/tsan_interceptors_posix.cpp

```

{% raw %}
2165 |   // dlopen/dlclose allocate/free dynamic-linker-internal memory, which is later
2168 |   // produce false reports. Ignoring malloc/free in dlopen/dlclose is not enough
2169 |   // because some libc functions call __libc_dlopen.
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/msan/dtls_test.c

```cpp

{% raw %}
52 |   void *handle = dlopen(path, RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/msan/dlopen_executable.cpp

```

{% raw %}
11 |   void *p = dlopen(0, RTLD_NOW);
15 |   // CHECK: #0 {{.*}} in main{{.*}}dlopen_executable.cpp:[[@LINE-2]]
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/msan/dlerror.cpp

```

{% raw %}
8 |   void *p = dlopen("/bad/file/name", RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/cfi/cross-dso/shadow_is_read_only.cpp

```

{% raw %}
6 | // RUN: %expect_crash %t dlopen %t-cfi-so.so 2>&1 | FileCheck %s
8 | // RUN: %expect_crash %t dlopen %t-nocfi-so.so 2>&1 | FileCheck %s
59 |   const bool test_dlopen = strcmp(argv[1], "dlopen") == 0;
72 |     void *handle = dlopen(lib, RTLD_NOW);
77 |     if (test_dlopen)
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/cfi/cross-dso/icall/dlopen.cpp

```

{% raw %}
39 | // Tests calls into dlopen-ed library.
98 |   void *handle = dlopen(name.c_str(), RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/start-deactivated.cpp

```

{% raw %}
2 | // library is instrumented. Memory errors before dlopen are not detected.
76 |   void *dso = dlopen(path.c_str(), RTLD_NOW);
78 |     fprintf(stderr, "dlopen failed: %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/coverage-module-unloaded.cpp

```

{% raw %}
27 |   void *handle1 = dlopen(argv[1], RTLD_LAZY);  // %dynamiclib1
32 |   void *handle2 = dlopen(argv[2], RTLD_LAZY);  // %dynamiclib2
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/shared-lib-test.cpp

```

{% raw %}
23 |   void *lib = dlopen(path.c_str(), RTLD_NOW);
25 |     printf("error in dlopen(): %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/global-registration.c

```cpp

{% raw %}
39 |     void *handle = dlopen(libpath, RTLD_NOW);
41 |       fprintf(stderr, "dlopen: %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/dlclose-test.cpp

```

{% raw %}
3 | // 1. application dlopens foo.so
52 |   void *lib = dlopen(path.c_str(), RTLD_NOW);
54 |     printf("error in dlopen(): %s\n", dlerror());
100 | void at_dlopen() {
101 |   printf("%s: I am being dlopened\n", __FILE__);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Posix/asan-symbolize-sanity-test.cpp

```

{% raw %}
27 |   void *lib = dlopen(path.c_str(), RTLD_NOW);
29 |     printf("error in dlopen(): %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/init-order-dlopen.cpp

```

{% raw %}
7 | // dlopen() can not be intercepted on Android, making strict_init_order nearly
38 |   void *handle = dlopen(path.c_str(), RTLD_NOW);
40 |     printf("error in dlopen(): %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/activation-options.cpp

```

{% raw %}
56 |   void *dso = dlopen(path.c_str(), RTLD_NOW);
58 |     fprintf(stderr, "dlopen failed: %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/pthread_create_from_constructor.cpp

```

{% raw %}
1 | // from dlopened shared library constructor. The deadlock happens only in shared
10 | // dlopen() can not be intercepted on Android
43 |   void *handle = dlopen(path.c_str(), RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/function-sections-are-bad.cpp

```

{% raw %}
18 |   void *handle = dlopen(path, RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/stress_dtls.c

```cpp

{% raw %}
2 | // Stress test dynamic TLS + dlopen + threads.
5 | // it fails with ~17 DSOs dlopen-ed.
84 |     void *handle = dlopen(buf, RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/asan_dlopen_test.cpp

```

{% raw %}
0 | // Test that dlopen of dynamic runtime is prohibited.
12 |   dlopen(RT, RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/dlopen-mixed-c-cxx.c

```cpp

{% raw %}
36 |   void *handle = dlopen(argv[1], RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Linux/stack-trace-dlclose.cpp

```

{% raw %}
28 |   void *handle = dlopen(SO_DIR "/stack_trace_dlclose.so", RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/asan/TestCases/Darwin/init_for_dlopen.cpp

```

{% raw %}
2 | // Check that trying to dlopen() the ASan dylib fails.
7 | // RUN: APPLE_ASAN_INIT_FOR_DLOPEN=0 %env_asan_opts=abort_on_error=0 not \
10 | // RUN: env -u APPLE_ASAN_INIT_FOR_DLOPEN %env_asan_opts=abort_on_error=0 not \
14 | // Check that we can successfully dlopen the ASan dylib when we set the right
16 | // RUN: env APPLE_ASAN_INIT_FOR_DLOPEN=1 %run %t %shared_libasan 2>&1 | \
30 |   void *handle = dlopen(dylib_path, RTLD_LAZY);
32 |     fprintf(stderr, "Failed to dlopen: %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/sanitizer_common/TestCases/get_module_and_offset_for_pc.cpp

```

{% raw %}
36 |   void *handle = dlopen(SO_DIR "/get_module_and_offset_for_pc.so", RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/sanitizer_common/TestCases/Linux/deepbind.cpp

```

{% raw %}
8 |   // CHECK: You are trying to dlopen a <arbitrary path> shared library with RTLD_DEEPBIND flag
9 |   void *lib = dlopen("<arbitrary path>", RTLD_NOW | RTLD_DEEPBIND);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/sanitizer_common/TestCases/Darwin/print-stack-trace-in-code-loaded-after-fork.cpp

```

{% raw %}
50 |   void *handle = dlopen(library_to_load, RTLD_NOW | RTLD_LOCAL);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/dfsan/custom.cpp

```

{% raw %}
351 | void test_dlopen() {
352 |   void *map = dlopen(NULL, RTLD_NOW);
356 |   map = dlopen("/nonexistent", RTLD_NOW);
964 |   test_dlopen();
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/lsan/TestCases/Linux/use_tls_dynamic.cpp

```

{% raw %}
25 |   void *handle = dlopen(path.c_str(), RTLD_LAZY);
45 | // allocation of a new TLS storage chunk when loaded with dlopen(). We use it
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/load_shared_lib.cpp

```

{% raw %}
58 |   void *lib = dlopen(path.c_str(), RTLD_NOW);
60 |     printf("error in dlopen(): %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/ignore_lib1.cpp

```

{% raw %}
29 |   void *h = dlopen(lib.c_str(), RTLD_GLOBAL | RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/dl_iterate_phdr.cpp

```

{% raw %}
41 |     void *lib = dlopen(path.c_str(), RTLD_NOW);
43 |       printf("error in dlopen: %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/dlclose.cpp

```

{% raw %}
35 |   lib = dlopen((std::string(argv[0]) + std::string("-so.so")).c_str(),
38 |     printf("error in dlopen: %s\n", dlerror());
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/dtls.c

```cpp

{% raw %}
37 |   void *handle = dlopen(path, RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/ignore_lib6.cpp

```

{% raw %}
33 |   void *h = dlopen(lib.c_str(), RTLD_GLOBAL | RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/ignore_lib5.cpp

```

{% raw %}
62 |   void *h = dlopen(lib.c_str(), RTLD_GLOBAL | RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/ignore_lib3.cpp

```

{% raw %}
24 |   void *h = dlopen(lib.c_str(), RTLD_GLOBAL | RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/ignore_lib2.cpp

```

{% raw %}
21 |   dlopen(lib0.c_str(), RTLD_GLOBAL | RTLD_NOW);
22 |   dlopen(lib1.c_str(), RTLD_GLOBAL | RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/ignore_lib4.cpp

```

{% raw %}
39 |   void *h = dlopen(lib.c_str(), RTLD_GLOBAL | RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/tsan/Darwin/dlopen.cpp

```

{% raw %}
1 | // interceptors work automatically), dlopen'ing a TSanified library from a
15 | // Launching a non-instrumented binary that dlopen's an instrumented library should fail.
30 |   void *handle = dlopen(argv[1], RTLD_NOW);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Posix/gcov-dlopen.c

```cpp

{% raw %}
0 | /// atexit(3) not supported in dlopen(3)ed+dlclose(3)d DSO
13 | /// Test with two dlopened libraries.
14 | // RUN: rm -f gcov-dlopen.gcda func1.gcda func2.gcda
16 | // RUN: llvm-cov gcov -t gcov-dlopen.gcda | FileCheck %s
23 | /// Test with three dlopened libraries.
25 | // RUN: rm -f gcov-dlopen.gcda func1.gcda func2.gcda func3.gcda
27 | // RUN: llvm-cov gcov -t gcov-dlopen.gcda | FileCheck %s --check-prefix=LIB3
39 |   void *f1_handle = dlopen("func1.so", RTLD_LAZY | RTLD_GLOBAL);
46 |   void *f2_handle = dlopen("func2.so", RTLD_LAZY | RTLD_GLOBAL);
57 |   void *f3_handle = dlopen("func3.so", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Posix/instrprof-dlopen.test

```

{% raw %}
1 | RUN: %clang_profgen -o %t.d/func.shared -fPIC -shared %S/../Inputs/instrprof-dlopen-func.c
2 | RUN: %clang_profgen -o %t.d/func2.shared -fPIC -shared %S/../Inputs/instrprof-dlopen-func2.c
3 | RUN: %clang -o %t-local -fPIC -DDLOPEN_FUNC_DIR=\"%t.d\" -DDLOPEN_FLAGS="RTLD_LAZY | RTLD_LOCAL" %S/../Inputs/instrprof-dlopen-main.c
4 | RUN: %clang -o %t-global -fPIC -DDLOPEN_FUNC_DIR=\"%t.d\" -DDLOPEN_FLAGS="RTLD_LAZY | RTLD_GLOBAL" %S/../Inputs/instrprof-dlopen-main.c
6 | RUN: %clang -c -o %t.d/main.o %S/../Inputs/instrprof-dlopen-main.c
7 | RUN: %clang_profgen -o %t-static %S/../Inputs/instrprof-dlopen-func.c %S/../Inputs/instrprof-dlopen-func2.c %t.d/main.o
17 | RUN: %clang_profuse=%t-static.profdata -o %t-func.static.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-func.c
18 | RUN: %clang_profuse=%t-local.profdata -o %t-func.local.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-func.c
19 | RUN: %clang_profuse=%t-global.profdata -o %t-func.global.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-func.c
23 | RUN: %clang_profuse=%t-static.profdata -o %t-func2.static.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-func2.c
24 | RUN: %clang_profuse=%t-local.profdata -o %t-func2.local.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-func2.c
25 | RUN: %clang_profuse=%t-global.profdata -o %t-func2.global.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-func2.c
29 | RUN: %clang_profuse=%t-static.profdata -o %t-main.static.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-main.c
30 | RUN: %clang_profuse=%t-local.profdata -o %t-main.local.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-main.c
31 | RUN: %clang_profuse=%t-local.profdata -o %t-main.global.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-main.c
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Linux/instrprof-dlopen.test

```

{% raw %}
1 | RUN: %clang_profgen -o %t.d/func.shared -fPIC -shared -fdata-sections -ffunction-sections -fuse-ld=gold -Wl,--gc-sections  %S/../Inputs/instrprof-dlopen-func.c
2 | RUN: %clang_profgen -o %t.d/func2.shared -fPIC -shared -fdata-sections -ffunction-sections -fuse-ld=gold -Wl,--gc-sections  %S/../Inputs/instrprof-dlopen-func2.c
3 | RUN: %clang -o %t-local -fPIC -DDLOPEN_FUNC_DIR=\"%t.d\" -DDLOPEN_FLAGS="RTLD_LAZY | RTLD_LOCAL" %S/../Inputs/instrprof-dlopen-main.c
4 | RUN: %clang -o %t-global -fPIC -DDLOPEN_FUNC_DIR=\"%t.d\" -DDLOPEN_FLAGS="RTLD_LAZY | RTLD_GLOBAL" %S/../Inputs/instrprof-dlopen-main.c
6 | RUN: %clang -c -o %t.d/main.o %S/../Inputs/instrprof-dlopen-main.c
7 | RUN: %clang_profgen -fdata-sections -ffunction-sections -fuse-ld=gold -Wl,--gc-sections  -o %t-static %S/../Inputs/instrprof-dlopen-func.c %S/../Inputs/instrprof-dlopen-func2.c %t.d/main.o
17 | RUN: %clang_profuse=%t-static.profdata -o %t-func.static.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-func.c
18 | RUN: %clang_profuse=%t-local.profdata -o %t-func.local.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-func.c
19 | RUN: %clang_profuse=%t-global.profdata -o %t-func.global.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-func.c
23 | RUN: %clang_profuse=%t-static.profdata -o %t-func2.static.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-func2.c
24 | RUN: %clang_profuse=%t-local.profdata -o %t-func2.local.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-func2.c
25 | RUN: %clang_profuse=%t-global.profdata -o %t-func2.global.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-func2.c
29 | RUN: %clang_profuse=%t-static.profdata -o %t-main.static.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-main.c
30 | RUN: %clang_profuse=%t-local.profdata -o %t-main.local.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-main.c
31 | RUN: %clang_profuse=%t-local.profdata -o %t-main.global.ll -S -emit-llvm %S/../Inputs/instrprof-dlopen-main.c
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-main.c

```cpp

{% raw %}
4 | #ifdef DLOPEN_FUNC_DIR
12 | #ifdef DLOPEN_FUNC_DIR
14 |   void *f1_handle = dlopen(DLOPEN_FUNC_DIR"/func.shared", DLOPEN_FLAGS);
16 |     fprintf(stderr, "unable to open '" DLOPEN_FUNC_DIR "/func.shared': %s\n",
27 |   void *f2_handle = dlopen(DLOPEN_FUNC_DIR"/func2.shared", DLOPEN_FLAGS);
29 |     fprintf(stderr, "unable to open '" DLOPEN_FUNC_DIR "/func2.shared': %s\n",
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-value-prof-visibility.c

```cpp

{% raw %}
3 | #ifdef DLOPEN_FUNC_DIR
28 | #ifdef DLOPEN_FUNC_DIR
29 |   void *Handle = dlopen(DLOPEN_FUNC_DIR "/func.shared", RTLD_NOW);
31 |     fprintf(stderr, "unable to open '" DLOPEN_FUNC_DIR "/func.shared': %s\n",
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/test/profile/Inputs/instrprof-dlopen-dlclose-main.c

```cpp

{% raw %}
6 |   void *f1_handle = dlopen("func.shared", RTLD_LAZY | RTLD_GLOBAL);
19 |   void *f2_handle = dlopen("func2.shared", RTLD_LAZY | RTLD_GLOBAL);
33 |   void *f3_handle = dlopen("func3.shared", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/compiler-rt/cmake/config-ix.cmake

```cmake

{% raw %}
128 | check_library_exists(dl dlopen "" COMPILER_RT_HAS_LIBDL)
{% endraw %}

```
### rocm-openmp-extras/llvm-project/polly/lib/External/isl/ltmain.sh

```bash

{% raw %}
2262 |     opt_dlopen=
2323 |         --dlopen|-dlopen)
2324 |                         opt_dlopen="${opt_dlopen+$opt_dlopen
2440 |       # Only execute mode is allowed to have -dlopen flags.
2441 |       if test -n "$opt_dlopen" && test execute != "$opt_mode"; then
2442 |         func_error "unrecognized option '-dlopen'"
3668 |   -dlopen FILE      add the directory containing FILE to the library path
3670 | This mode sets the library path environment variable according to '-dlopen'
3725 |   -dlopen FILE      '-dlpreopen' FILE if it cannot be dlopened at runtime
3734 |   -module           build a library that can dlopened
3842 |     # Handle -dlopen flags immediately.
3843 |     for file in $opt_dlopen; do
3862 | 	# Skip this library if it cannot be dlopened.
3889 | 	func_warning "'-dlopen' is ignored for non-libtool libraries and objects"
6582 | 	    dlopen_self=$dlopen_self_static
6588 | 	    dlopen_self=$dlopen_self_static
6594 | 	    dlopen_self=$dlopen_self_static
6652 | 	    elif test dlfiles = "$prev" && test yes != "$dlopen_self"; then
6742 | 		    if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
6909 |       -dlopen)
7346 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7414 | 	  # This library was specified with -dlopen.
7534 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7545 | 	passes="conv scan dlopen dlpreopen link"
7571 | 	dlopen) libs=$dlfiles ;;
7602 |       if test dlopen = "$pass"; then
7822 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7823 | 	      # If there is no dlopen support or we're linking statically,
7851 | 	dlopen=
7881 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7927 | 	# This library was specified with -dlopen.
7928 | 	if test dlopen = "$pass"; then
7930 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7932 | 	     test yes != "$dlopen_support" ||
7935 | 	    # If there is no dlname, no dlopen support or we're linking
7944 | 	fi # $pass = dlopen
8000 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
8002 | 	      # We recover the dlopen module name by 'saving' the la file
8026 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8155 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8156 | 	  dlopenmodule=
8159 | 	      dlopenmodule=$dlpremoduletest
8163 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8260 | 		    # if the lib is a (non-dlopened) module then we cannot
8264 | 		      if test "X$dlopenmodule" != "X$lib"; then
8416 | 	      echo "*** a static module, that should work as long as the dlopening application"
8417 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8561 |       if test dlopen != "$pass"; then
8691 | 	func_warning "'-dlopen' is ignored for archives"
8758 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9455 | 	    echo "*** a static module, that should work as long as the dlopening"
9456 | 	    echo "*** application is linked with the -dlopen flag."
9474 | 	    echo "*** or is declared to -dlopen it."
10086 | 	func_warning "'-dlopen' is ignored for objects"
10206 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10207 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10888 | # The name that we can dlopen(3).
10917 | # Files to dlopen/dlpreopen
10918 | dlopen='$dlfiles'
{% endraw %}

```
### rocm-openmp-extras/llvm-project/polly/lib/External/isl/m4/libtool.m4

```

{% raw %}
1820 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1823 | m4_defun([_LT_TRY_DLOPEN_SELF],
1881 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1914 | ])# _LT_TRY_DLOPEN_SELF
1917 | # LT_SYS_DLOPEN_SELF
1919 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1921 | if test yes != "$enable_dlopen"; then
1922 |   enable_dlopen=unknown
1923 |   enable_dlopen_self=unknown
1924 |   enable_dlopen_self_static=unknown
1926 |   lt_cv_dlopen=no
1927 |   lt_cv_dlopen_libs=
1931 |     lt_cv_dlopen=load_add_on
1932 |     lt_cv_dlopen_libs=
1933 |     lt_cv_dlopen_self=yes
1937 |     lt_cv_dlopen=LoadLibrary
1938 |     lt_cv_dlopen_libs=
1942 |     lt_cv_dlopen=dlopen
1943 |     lt_cv_dlopen_libs=
1948 |     AC_CHECK_LIB([dl], [dlopen],
1949 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1950 |     lt_cv_dlopen=dyld
1951 |     lt_cv_dlopen_libs=
1952 |     lt_cv_dlopen_self=yes
1959 |     lt_cv_dlopen=dlopen
1960 |     lt_cv_dlopen_libs=
1961 |     lt_cv_dlopen_self=no
1966 | 	  [lt_cv_dlopen=shl_load],
1968 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1969 | 	[AC_CHECK_FUNC([dlopen],
1970 | 	      [lt_cv_dlopen=dlopen],
1971 | 	  [AC_CHECK_LIB([dl], [dlopen],
1972 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1973 | 	    [AC_CHECK_LIB([svld], [dlopen],
1974 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1976 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
1985 |   if test no = "$lt_cv_dlopen"; then
1986 |     enable_dlopen=no
1988 |     enable_dlopen=yes
1991 |   case $lt_cv_dlopen in
1992 |   dlopen)
2000 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2002 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2003 | 	  lt_cv_dlopen_self, [dnl
2004 | 	  _LT_TRY_DLOPEN_SELF(
2005 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2006 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2009 |     if test yes = "$lt_cv_dlopen_self"; then
2011 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2012 | 	  lt_cv_dlopen_self_static, [dnl
2013 | 	  _LT_TRY_DLOPEN_SELF(
2014 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2015 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2025 |   case $lt_cv_dlopen_self in
2026 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2027 |   *) enable_dlopen_self=unknown ;;
2030 |   case $lt_cv_dlopen_self_static in
2031 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2032 |   *) enable_dlopen_self_static=unknown ;;
2035 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2036 | 	 [Whether dlopen is supported])
2037 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2038 | 	 [Whether dlopen of programs is supported])
2039 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2040 | 	 [Whether dlopen of statically linked programs is supported])
2041 | ])# LT_SYS_DLOPEN_SELF
2044 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2046 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6140 |     [Compiler flag to allow reflexive dlopens])
6253 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### rocm-openmp-extras/llvm-project/polly/lib/External/isl/m4/ltoptions.m4

```

{% raw %}
70 |   _LT_UNLESS_OPTIONS([LT_INIT], [dlopen], [enable_dlopen=no
107 | # dlopen
109 | LT_OPTION_DEFINE([LT_INIT], [dlopen], [enable_dlopen=yes
112 | AU_DEFUN([AC_LIBTOOL_DLOPEN],
113 | [_LT_SET_OPTION([LT_INIT], [dlopen])
116 | put the 'dlopen' option into LT_INIT's first parameter.])
120 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN], [])
{% endraw %}

```
### rocm-openmp-extras/llvm-project/polly/lib/External/ppcg/ltmain.sh

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
### rocm-openmp-extras/llvm-project/polly/lib/External/ppcg/m4/libtool.m4

```

{% raw %}
1752 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1755 | m4_defun([_LT_TRY_DLOPEN_SELF],
1813 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1846 | ])# _LT_TRY_DLOPEN_SELF
1849 | # LT_SYS_DLOPEN_SELF
1851 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1853 | if test "x$enable_dlopen" != xyes; then
1854 |   enable_dlopen=unknown
1855 |   enable_dlopen_self=unknown
1856 |   enable_dlopen_self_static=unknown
1858 |   lt_cv_dlopen=no
1859 |   lt_cv_dlopen_libs=
1863 |     lt_cv_dlopen="load_add_on"
1864 |     lt_cv_dlopen_libs=
1865 |     lt_cv_dlopen_self=yes
1869 |     lt_cv_dlopen="LoadLibrary"
1870 |     lt_cv_dlopen_libs=
1874 |     lt_cv_dlopen="dlopen"
1875 |     lt_cv_dlopen_libs=
1880 |     AC_CHECK_LIB([dl], [dlopen],
1881 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],[
1882 |     lt_cv_dlopen="dyld"
1883 |     lt_cv_dlopen_libs=
1884 |     lt_cv_dlopen_self=yes
1890 | 	  [lt_cv_dlopen="shl_load"],
1892 | 	    [lt_cv_dlopen="shl_load" lt_cv_dlopen_libs="-ldld"],
1893 | 	[AC_CHECK_FUNC([dlopen],
1894 | 	      [lt_cv_dlopen="dlopen"],
1895 | 	  [AC_CHECK_LIB([dl], [dlopen],
1896 | 		[lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-ldl"],
1897 | 	    [AC_CHECK_LIB([svld], [dlopen],
1898 | 		  [lt_cv_dlopen="dlopen" lt_cv_dlopen_libs="-lsvld"],
1900 | 		    [lt_cv_dlopen="dld_link" lt_cv_dlopen_libs="-ldld"])
1909 |   if test "x$lt_cv_dlopen" != xno; then
1910 |     enable_dlopen=yes
1912 |     enable_dlopen=no
1915 |   case $lt_cv_dlopen in
1916 |   dlopen)
1924 |     LIBS="$lt_cv_dlopen_libs $LIBS"
1926 |     AC_CACHE_CHECK([whether a program can dlopen itself],
1927 | 	  lt_cv_dlopen_self, [dnl
1928 | 	  _LT_TRY_DLOPEN_SELF(
1929 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
1930 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
1933 |     if test "x$lt_cv_dlopen_self" = xyes; then
1935 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
1936 | 	  lt_cv_dlopen_self_static, [dnl
1937 | 	  _LT_TRY_DLOPEN_SELF(
1938 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
1939 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
1949 |   case $lt_cv_dlopen_self in
1950 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
1951 |   *) enable_dlopen_self=unknown ;;
1954 |   case $lt_cv_dlopen_self_static in
1955 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
1956 |   *) enable_dlopen_self_static=unknown ;;
1959 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
1960 | 	 [Whether dlopen is supported])
1961 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
1962 | 	 [Whether dlopen of programs is supported])
1963 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
1964 | 	 [Whether dlopen of statically linked programs is supported])
1965 | ])# LT_SYS_DLOPEN_SELF
1968 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
1970 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
5670 |     [Compiler flag to allow reflexive dlopens])
5783 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### rocm-openmp-extras/llvm-project/polly/lib/External/ppcg/m4/ltoptions.m4

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
### rocm-openmp-extras/llvm-project/polly/tools/GPURuntime/GPUJIT.c

```cpp

{% raw %}
223 |   HandleOpenCLBeignet = dlopen("/usr/local/lib/beignet/libcl.so", RTLD_LAZY);
224 |   HandleOpenCL = dlopen("libOpenCL.so", RTLD_LAZY);
1047 |   HandleCuda = dlopen("libcuda.so", RTLD_LAZY);
1053 |   HandleCudaRT = dlopen("libcudart.so", RTLD_LAZY);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/libcxxabi/src/include/refstring.h

```cpp

{% raw %}
50 |     void* handle = dlopen("/usr/lib/libstdc++.6.dylib", RTLD_NOLOAD);
{% endraw %}

```
### rocm-openmp-extras/llvm-project/libcxxabi/test/test_demangle.pass.cpp

```

{% raw %}
157 |     {"_ZN11ImageLoader29decrementDlopenReferenceCountEv", "ImageLoader::decrementDlopenReferenceCount()"},
502 |     {"_ZZ6dlopenE8__func__", "dlopen::__func__"},
503 |     {"_ZZ16dlopen_preflightE8__func__", "dlopen_preflight::__func__"},
{% endraw %}

```
### rocm-openmp-extras/llvm-project/clang-tools-extra/clangd/xpc/test-client/ClangdXPCTestClient.cpp

```

{% raw %}
50 |   void *dlHandle = dlopen(LibPath.c_str(), RTLD_LOCAL | RTLD_FIRST);
{% endraw %}

```
### test/omptests/fast_test/main.cpp

```

{% raw %}
29 |     void *h = dlopen(lib.c_str(),RTLD_NOW);
{% endraw %}

```