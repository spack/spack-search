---
name: "tau"
layout: package
next_package: libnova
previous_package: pruners-ninja
languages: ['cpp', 'bash']
---
## 2.29.1
19 / 3452 files match

 - [src/wrappers/pthread/pthread_wrap.c](#srcwrapperspthreadpthread_wrapc)
 - [src/wrappers/gomp/gomp_wrap.c](#srcwrappersgompgomp_wrapc)
 - [src/wrappers/cuda/cuda_wrap.c](#srcwrapperscudacuda_wrapc)
 - [src/wrappers/cuda/cudart_wrap.cpp](#srcwrapperscudacudart_wrapcpp)
 - [src/wrappers/cuda/cuda_wrap.cpp](#srcwrapperscudacuda_wrapcpp)
 - [src/Profile/TauOpenMPCollectorAPI.cpp](#srcprofiletauopenmpcollectorapicpp)
 - [src/Profile/TauSampling.cpp](#srcprofiletausamplingcpp)
 - [src/Profile/TauShmemSgiF.c](#srcprofiletaushmemsgifc)
 - [src/Profile/CuptiActivity.cpp](#srcprofilecuptiactivitycpp)
 - [src/Profile/TauUtil.cpp](#srcprofiletauutilcpp)
 - [src/Profile/TauGpuAdapterOpenCL.cpp](#srcprofiletaugpuadapteropenclcpp)
 - [src/Profile/TauRocProfiler.cpp](#srcprofiletaurocprofilercpp)
 - [utils/tau_wrap.cpp](#utilstau_wrapcpp)
 - [utils/opari2/build-config/ltmain.sh](#utilsopari2build-configltmainsh)
 - [utils/opari2/build-config/m4/libtool.m4](#utilsopari2build-configm4libtoolm4)
 - [utils/opari2/build-config/m4/ltoptions.m4](#utilsopari2build-configm4ltoptionsm4)
 - [apex/src/wrappers/pthread_wrapper.c](#apexsrcwrapperspthread_wrapperc)
 - [apex/src/apex/apex.cpp](#apexsrcapexapexcpp)
 - [tools/src/contrib/hpctoolkit-4.9.2-r2138.patch](#toolssrccontribhpctoolkit-492-r2138patch)

### src/wrappers/pthread/pthread_wrap.c

```cpp

{% raw %}
86 |     void * syms = dlopen(NULL, RTLD_NOW);
{% endraw %}

```
### src/wrappers/gomp/gomp_wrap.c

```cpp

{% raw %}
48 |         void * syms = dlopen(NULL, RTLD_NOW);
{% endraw %}

```
### src/wrappers/cuda/cuda_wrap.c

```cpp

{% raw %}
21 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
24 |     perror("Error opening library in dlopen call"); 
31 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
49 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
52 |     perror("Error opening library in dlopen call"); 
59 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
77 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
80 |     perror("Error opening library in dlopen call"); 
87 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
105 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
108 |     perror("Error opening library in dlopen call"); 
115 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
133 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
136 |     perror("Error opening library in dlopen call"); 
143 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
161 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
164 |     perror("Error opening library in dlopen call"); 
171 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
189 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
192 |     perror("Error opening library in dlopen call"); 
199 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
217 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
220 |     perror("Error opening library in dlopen call"); 
227 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
245 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
248 |     perror("Error opening library in dlopen call"); 
255 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
273 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
276 |     perror("Error opening library in dlopen call"); 
283 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
301 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
304 |     perror("Error opening library in dlopen call"); 
311 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
329 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
332 |     perror("Error opening library in dlopen call"); 
339 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
357 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
360 |     perror("Error opening library in dlopen call"); 
367 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
390 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
393 |     perror("Error opening library in dlopen call"); 
400 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
418 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
421 |     perror("Error opening library in dlopen call"); 
428 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
446 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
449 |     perror("Error opening library in dlopen call"); 
456 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
474 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
477 |     perror("Error opening library in dlopen call"); 
484 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
505 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
508 |     perror("Error opening library in dlopen call"); 
515 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
533 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
536 |     perror("Error opening library in dlopen call"); 
543 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
561 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
564 |     perror("Error opening library in dlopen call"); 
571 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
589 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
592 |     perror("Error opening library in dlopen call"); 
599 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
617 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
620 |     perror("Error opening library in dlopen call"); 
627 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
645 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
648 |     perror("Error opening library in dlopen call"); 
655 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
673 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
676 |     perror("Error opening library in dlopen call"); 
683 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
701 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
704 |     perror("Error opening library in dlopen call"); 
711 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
729 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
732 |     perror("Error opening library in dlopen call"); 
739 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
757 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
760 |     perror("Error opening library in dlopen call"); 
767 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
785 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
788 |     perror("Error opening library in dlopen call"); 
795 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
813 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
816 |     perror("Error opening library in dlopen call"); 
823 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
841 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
844 |     perror("Error opening library in dlopen call"); 
851 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
869 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
872 |     perror("Error opening library in dlopen call"); 
879 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
897 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
900 |     perror("Error opening library in dlopen call"); 
907 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
925 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
928 |     perror("Error opening library in dlopen call"); 
935 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
953 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
956 |     perror("Error opening library in dlopen call"); 
963 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
981 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
984 |     perror("Error opening library in dlopen call"); 
991 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1009 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1012 |     perror("Error opening library in dlopen call"); 
1019 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1037 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1040 |     perror("Error opening library in dlopen call"); 
1047 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1065 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1068 |     perror("Error opening library in dlopen call"); 
1075 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1093 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1096 |     perror("Error opening library in dlopen call"); 
1103 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1121 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1124 |     perror("Error opening library in dlopen call"); 
1131 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1149 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1152 |     perror("Error opening library in dlopen call"); 
1159 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1177 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1180 |     perror("Error opening library in dlopen call"); 
1187 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1205 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1208 |     perror("Error opening library in dlopen call"); 
1215 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1233 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1236 |     perror("Error opening library in dlopen call"); 
1243 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1261 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1264 |     perror("Error opening library in dlopen call"); 
1271 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1289 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1292 |     perror("Error opening library in dlopen call"); 
1299 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1317 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1320 |     perror("Error opening library in dlopen call"); 
1327 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1345 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1348 |     perror("Error opening library in dlopen call"); 
1355 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1373 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1376 |     perror("Error opening library in dlopen call"); 
1383 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1401 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1404 |     perror("Error opening library in dlopen call"); 
1411 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1429 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1432 |     perror("Error opening library in dlopen call"); 
1439 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1457 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1460 |     perror("Error opening library in dlopen call"); 
1467 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1485 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1488 |     perror("Error opening library in dlopen call"); 
1495 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1513 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1516 |     perror("Error opening library in dlopen call"); 
1523 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1541 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1544 |     perror("Error opening library in dlopen call"); 
1551 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1569 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1572 |     perror("Error opening library in dlopen call"); 
1579 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1597 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1600 |     perror("Error opening library in dlopen call"); 
1607 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1625 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1628 |     perror("Error opening library in dlopen call"); 
1635 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1653 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1656 |     perror("Error opening library in dlopen call"); 
1663 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1681 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1684 |     perror("Error opening library in dlopen call"); 
1691 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1709 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1712 |     perror("Error opening library in dlopen call"); 
1719 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1737 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1740 |     perror("Error opening library in dlopen call"); 
1747 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1765 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1768 |     perror("Error opening library in dlopen call"); 
1775 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1793 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1796 |     perror("Error opening library in dlopen call"); 
1803 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1821 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1824 |     perror("Error opening library in dlopen call"); 
1831 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1849 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1852 |     perror("Error opening library in dlopen call"); 
1859 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1877 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1880 |     perror("Error opening library in dlopen call"); 
1887 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1905 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1908 |     perror("Error opening library in dlopen call"); 
1915 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1933 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1936 |     perror("Error opening library in dlopen call"); 
1943 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1961 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1964 |     perror("Error opening library in dlopen call"); 
1971 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1989 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1992 |     perror("Error opening library in dlopen call"); 
1999 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2017 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2020 |     perror("Error opening library in dlopen call"); 
2027 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2045 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2048 |     perror("Error opening library in dlopen call"); 
2055 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2073 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2076 |     perror("Error opening library in dlopen call"); 
2083 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2101 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2104 |     perror("Error opening library in dlopen call"); 
2111 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2129 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2132 |     perror("Error opening library in dlopen call"); 
2139 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2157 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2160 |     perror("Error opening library in dlopen call"); 
2167 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2185 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2188 |     perror("Error opening library in dlopen call"); 
2195 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2213 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2216 |     perror("Error opening library in dlopen call"); 
2223 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2241 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2244 |     perror("Error opening library in dlopen call"); 
2251 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2269 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2272 |     perror("Error opening library in dlopen call"); 
2279 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2300 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2303 |     perror("Error opening library in dlopen call"); 
2310 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2328 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2331 |     perror("Error opening library in dlopen call"); 
2338 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2356 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2359 |     perror("Error opening library in dlopen call"); 
2366 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2384 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2387 |     perror("Error opening library in dlopen call"); 
2394 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2412 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2415 |     perror("Error opening library in dlopen call"); 
2422 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2443 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2446 |     perror("Error opening library in dlopen call"); 
2453 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2471 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2474 |     perror("Error opening library in dlopen call"); 
2481 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2499 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2502 |     perror("Error opening library in dlopen call"); 
2509 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2527 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2530 |     perror("Error opening library in dlopen call"); 
2537 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2555 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2558 |     perror("Error opening library in dlopen call"); 
2565 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2583 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2586 |     perror("Error opening library in dlopen call"); 
2593 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2611 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2614 |     perror("Error opening library in dlopen call"); 
2621 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2639 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2642 |     perror("Error opening library in dlopen call"); 
2649 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2667 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2670 |     perror("Error opening library in dlopen call"); 
2677 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2695 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2698 |     perror("Error opening library in dlopen call"); 
2705 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2723 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2726 |     perror("Error opening library in dlopen call"); 
2733 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2785 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2788 |     perror("Error opening library in dlopen call"); 
2795 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2826 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2829 |     perror("Error opening library in dlopen call"); 
2836 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2867 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2870 |     perror("Error opening library in dlopen call"); 
2877 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2908 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2911 |     perror("Error opening library in dlopen call"); 
2918 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2936 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2939 |     perror("Error opening library in dlopen call"); 
2946 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2964 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2967 |     perror("Error opening library in dlopen call"); 
2974 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2992 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2995 |     perror("Error opening library in dlopen call"); 
3002 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3020 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3023 |     perror("Error opening library in dlopen call"); 
3030 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3048 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3051 |     perror("Error opening library in dlopen call"); 
3058 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3076 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3079 |     perror("Error opening library in dlopen call"); 
3086 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3104 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3107 |     perror("Error opening library in dlopen call"); 
3114 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3132 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3135 |     perror("Error opening library in dlopen call"); 
3142 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3160 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3163 |     perror("Error opening library in dlopen call"); 
3170 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3188 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3191 |     perror("Error opening library in dlopen call"); 
3198 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3216 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3219 |     perror("Error opening library in dlopen call"); 
3226 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3244 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3247 |     perror("Error opening library in dlopen call"); 
3254 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3272 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3275 |     perror("Error opening library in dlopen call"); 
3282 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3300 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3303 |     perror("Error opening library in dlopen call"); 
3310 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3328 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3331 |     perror("Error opening library in dlopen call"); 
3338 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3356 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3359 |     perror("Error opening library in dlopen call"); 
3366 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3384 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3387 |     perror("Error opening library in dlopen call"); 
3394 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3412 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3415 |     perror("Error opening library in dlopen call"); 
3422 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3440 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3443 |     perror("Error opening library in dlopen call"); 
3450 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3468 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3471 |     perror("Error opening library in dlopen call"); 
3478 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3496 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3499 |     perror("Error opening library in dlopen call"); 
3506 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3524 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3527 |     perror("Error opening library in dlopen call"); 
3534 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3552 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3555 |     perror("Error opening library in dlopen call"); 
3562 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3580 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3583 |     perror("Error opening library in dlopen call"); 
3590 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
{% endraw %}

```
### src/wrappers/cuda/cudart_wrap.cpp

```

{% raw %}
66 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
69 |     perror("Error opening library in dlopen call"); 
76 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
108 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
111 |     perror("Error opening library in dlopen call"); 
118 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
145 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
148 |     perror("Error opening library in dlopen call"); 
155 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
177 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
180 |     perror("Error opening library in dlopen call"); 
187 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
210 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
213 |     perror("Error opening library in dlopen call"); 
220 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
238 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
241 |     perror("Error opening library in dlopen call"); 
248 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
266 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
269 |     perror("Error opening library in dlopen call"); 
276 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
294 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
297 |     perror("Error opening library in dlopen call"); 
304 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
322 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
325 |     perror("Error opening library in dlopen call"); 
332 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
350 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
353 |     perror("Error opening library in dlopen call"); 
360 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
378 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
381 |     perror("Error opening library in dlopen call"); 
388 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
406 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
409 |     perror("Error opening library in dlopen call"); 
416 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
434 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
437 |     perror("Error opening library in dlopen call"); 
444 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
462 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
465 |     perror("Error opening library in dlopen call"); 
472 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
490 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
493 |     perror("Error opening library in dlopen call"); 
500 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
518 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
521 |     perror("Error opening library in dlopen call"); 
528 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
546 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
549 |     perror("Error opening library in dlopen call"); 
556 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
574 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
577 |     perror("Error opening library in dlopen call"); 
584 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
602 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
605 |     perror("Error opening library in dlopen call"); 
612 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
630 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
633 |     perror("Error opening library in dlopen call"); 
640 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
658 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
661 |     perror("Error opening library in dlopen call"); 
668 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
686 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
689 |     perror("Error opening library in dlopen call"); 
696 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
718 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
721 |     perror("Error opening library in dlopen call"); 
728 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
749 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
752 |     perror("Error opening library in dlopen call"); 
759 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
777 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
780 |     perror("Error opening library in dlopen call"); 
787 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
805 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
808 |     perror("Error opening library in dlopen call"); 
815 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
833 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
836 |     perror("Error opening library in dlopen call"); 
843 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
861 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
864 |     perror("Error opening library in dlopen call"); 
871 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
892 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
895 |     perror("Error opening library in dlopen call"); 
902 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
925 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
928 |     perror("Error opening library in dlopen call"); 
935 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
953 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
956 |     perror("Error opening library in dlopen call"); 
963 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
981 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
984 |     perror("Error opening library in dlopen call"); 
991 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1023 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1026 |     perror("Error opening library in dlopen call"); 
1033 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1051 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1054 |     perror("Error opening library in dlopen call"); 
1061 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1100 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1103 |     perror("Error opening library in dlopen call"); 
1109 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1134 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1137 |     perror("Error opening library in dlopen call"); 
1144 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1207 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1210 |     perror("Error opening library in dlopen call"); 
1217 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1235 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1238 |     perror("Error opening library in dlopen call"); 
1245 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1263 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1266 |     perror("Error opening library in dlopen call"); 
1273 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1290 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1293 |     perror("Error opening library in dlopen call"); 
1300 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1318 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1321 |     perror("Error opening library in dlopen call"); 
1328 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1346 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1349 |     perror("Error opening library in dlopen call"); 
1356 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1374 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1377 |     perror("Error opening library in dlopen call"); 
1384 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1401 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1404 |     perror("Error opening library in dlopen call"); 
1411 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1428 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1431 |     perror("Error opening library in dlopen call"); 
1438 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1459 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1462 |     perror("Error opening library in dlopen call"); 
1469 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1487 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1490 |     perror("Error opening library in dlopen call"); 
1497 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1515 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1518 |     perror("Error opening library in dlopen call"); 
1525 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1543 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1546 |     perror("Error opening library in dlopen call"); 
1553 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1571 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1574 |     perror("Error opening library in dlopen call"); 
1581 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1599 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1602 |     perror("Error opening library in dlopen call"); 
1609 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1627 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1630 |     perror("Error opening library in dlopen call"); 
1637 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1655 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1658 |     perror("Error opening library in dlopen call"); 
1665 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1688 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1691 |     perror("Error opening library in dlopen call"); 
1698 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1716 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1719 |     perror("Error opening library in dlopen call"); 
1726 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1744 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1747 |     perror("Error opening library in dlopen call"); 
1754 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1776 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1779 |     perror("Error opening library in dlopen call"); 
1786 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1807 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1810 |     perror("Error opening library in dlopen call"); 
1817 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1838 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1841 |     perror("Error opening library in dlopen call"); 
1848 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1869 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1872 |     perror("Error opening library in dlopen call"); 
1879 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1902 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1905 |     perror("Error opening library in dlopen call"); 
1912 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1934 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1937 |     perror("Error opening library in dlopen call"); 
1944 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1962 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1965 |     perror("Error opening library in dlopen call"); 
1972 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1990 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
1993 |     perror("Error opening library in dlopen call"); 
2000 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2021 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2024 |     perror("Error opening library in dlopen call"); 
2031 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2052 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2055 |     perror("Error opening library in dlopen call"); 
2062 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2083 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2086 |     perror("Error opening library in dlopen call"); 
2093 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2114 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2117 |     perror("Error opening library in dlopen call"); 
2124 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2145 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2148 |     perror("Error opening library in dlopen call"); 
2155 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2173 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2176 |     perror("Error opening library in dlopen call"); 
2183 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2201 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2204 |     perror("Error opening library in dlopen call"); 
2211 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2229 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2232 |     perror("Error opening library in dlopen call"); 
2239 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2260 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2263 |     perror("Error opening library in dlopen call"); 
2270 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2291 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2294 |     perror("Error opening library in dlopen call"); 
2301 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2319 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2322 |     perror("Error opening library in dlopen call"); 
2329 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2347 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2350 |     perror("Error opening library in dlopen call"); 
2357 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2375 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2378 |     perror("Error opening library in dlopen call"); 
2385 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2403 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2406 |     perror("Error opening library in dlopen call"); 
2413 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2431 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2434 |     perror("Error opening library in dlopen call"); 
2441 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2459 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2462 |     perror("Error opening library in dlopen call"); 
2469 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2487 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2490 |     perror("Error opening library in dlopen call"); 
2497 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2515 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2518 |     perror("Error opening library in dlopen call"); 
2525 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2543 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2546 |     perror("Error opening library in dlopen call"); 
2553 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2571 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2574 |     perror("Error opening library in dlopen call"); 
2581 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2599 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2602 |     perror("Error opening library in dlopen call"); 
2609 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2627 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2630 |     perror("Error opening library in dlopen call"); 
2637 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2655 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2658 |     perror("Error opening library in dlopen call"); 
2665 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2683 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2686 |     perror("Error opening library in dlopen call"); 
2693 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2711 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2714 |     perror("Error opening library in dlopen call"); 
2721 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2739 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2742 |     perror("Error opening library in dlopen call"); 
2749 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2767 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2770 |     perror("Error opening library in dlopen call"); 
2777 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2795 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2798 |     perror("Error opening library in dlopen call"); 
2805 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2823 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2826 |     perror("Error opening library in dlopen call"); 
2833 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2851 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2854 |     perror("Error opening library in dlopen call"); 
2861 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2879 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2882 |     perror("Error opening library in dlopen call"); 
2889 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2907 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2910 |     perror("Error opening library in dlopen call"); 
2917 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2935 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2938 |     perror("Error opening library in dlopen call"); 
2945 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2963 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2966 |     perror("Error opening library in dlopen call"); 
2973 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2991 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
2994 |     perror("Error opening library in dlopen call"); 
3001 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3025 |     cudart_handle = (void *) dlopen(cudart_orig_libname, RTLD_NOW); 
3028 |     perror("Error opening library in dlopen call"); 
3035 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
{% endraw %}

```
### src/wrappers/cuda/cuda_wrap.cpp

```

{% raw %}
21 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
24 |     perror("Error opening library in dlopen call"); 
31 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
49 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
52 |     perror("Error opening library in dlopen call"); 
59 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
77 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
80 |     perror("Error opening library in dlopen call"); 
87 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
105 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
108 |     perror("Error opening library in dlopen call"); 
115 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
133 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
136 |     perror("Error opening library in dlopen call"); 
143 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
161 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
164 |     perror("Error opening library in dlopen call"); 
171 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
189 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
192 |     perror("Error opening library in dlopen call"); 
199 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
217 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
220 |     perror("Error opening library in dlopen call"); 
227 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
245 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
248 |     perror("Error opening library in dlopen call"); 
255 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
273 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
276 |     perror("Error opening library in dlopen call"); 
283 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
301 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
304 |     perror("Error opening library in dlopen call"); 
311 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
329 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
332 |     perror("Error opening library in dlopen call"); 
339 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
357 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
360 |     perror("Error opening library in dlopen call"); 
367 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
390 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
393 |     perror("Error opening library in dlopen call"); 
400 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
418 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
421 |     perror("Error opening library in dlopen call"); 
428 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
446 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
449 |     perror("Error opening library in dlopen call"); 
456 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
474 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
477 |     perror("Error opening library in dlopen call"); 
484 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
505 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
508 |     perror("Error opening library in dlopen call"); 
515 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
533 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
536 |     perror("Error opening library in dlopen call"); 
543 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
561 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
564 |     perror("Error opening library in dlopen call"); 
571 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
589 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
592 |     perror("Error opening library in dlopen call"); 
599 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
617 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
620 |     perror("Error opening library in dlopen call"); 
627 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
645 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
648 |     perror("Error opening library in dlopen call"); 
655 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
673 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
676 |     perror("Error opening library in dlopen call"); 
683 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
701 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
704 |     perror("Error opening library in dlopen call"); 
711 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
729 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
732 |     perror("Error opening library in dlopen call"); 
739 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
757 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
760 |     perror("Error opening library in dlopen call"); 
767 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
785 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
788 |     perror("Error opening library in dlopen call"); 
795 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
813 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
816 |     perror("Error opening library in dlopen call"); 
823 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
841 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
844 |     perror("Error opening library in dlopen call"); 
851 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
869 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
872 |     perror("Error opening library in dlopen call"); 
879 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
897 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
900 |     perror("Error opening library in dlopen call"); 
907 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
925 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
928 |     perror("Error opening library in dlopen call"); 
935 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
953 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
956 |     perror("Error opening library in dlopen call"); 
963 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
981 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
984 |     perror("Error opening library in dlopen call"); 
991 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1009 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1012 |     perror("Error opening library in dlopen call"); 
1019 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1037 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1040 |     perror("Error opening library in dlopen call"); 
1047 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1065 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1068 |     perror("Error opening library in dlopen call"); 
1075 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1093 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1096 |     perror("Error opening library in dlopen call"); 
1103 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1121 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1124 |     perror("Error opening library in dlopen call"); 
1131 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1149 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1152 |     perror("Error opening library in dlopen call"); 
1159 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1177 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1180 |     perror("Error opening library in dlopen call"); 
1187 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1205 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1208 |     perror("Error opening library in dlopen call"); 
1215 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1233 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1236 |     perror("Error opening library in dlopen call"); 
1243 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1261 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1264 |     perror("Error opening library in dlopen call"); 
1271 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1289 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1292 |     perror("Error opening library in dlopen call"); 
1299 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1317 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1320 |     perror("Error opening library in dlopen call"); 
1327 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1345 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1348 |     perror("Error opening library in dlopen call"); 
1355 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1373 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1376 |     perror("Error opening library in dlopen call"); 
1383 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1401 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1404 |     perror("Error opening library in dlopen call"); 
1411 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1429 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1432 |     perror("Error opening library in dlopen call"); 
1439 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1457 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1460 |     perror("Error opening library in dlopen call"); 
1467 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1485 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1488 |     perror("Error opening library in dlopen call"); 
1495 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1513 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1516 |     perror("Error opening library in dlopen call"); 
1523 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1541 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1544 |     perror("Error opening library in dlopen call"); 
1551 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1569 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1572 |     perror("Error opening library in dlopen call"); 
1579 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1597 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1600 |     perror("Error opening library in dlopen call"); 
1607 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1625 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1628 |     perror("Error opening library in dlopen call"); 
1635 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1653 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1656 |     perror("Error opening library in dlopen call"); 
1663 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1681 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1684 |     perror("Error opening library in dlopen call"); 
1691 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1709 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1712 |     perror("Error opening library in dlopen call"); 
1719 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1737 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1740 |     perror("Error opening library in dlopen call"); 
1747 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1765 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1768 |     perror("Error opening library in dlopen call"); 
1775 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1793 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1796 |     perror("Error opening library in dlopen call"); 
1803 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1821 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1824 |     perror("Error opening library in dlopen call"); 
1831 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1849 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1852 |     perror("Error opening library in dlopen call"); 
1859 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1877 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1880 |     perror("Error opening library in dlopen call"); 
1887 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1905 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1908 |     perror("Error opening library in dlopen call"); 
1915 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1933 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1936 |     perror("Error opening library in dlopen call"); 
1943 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1961 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1964 |     perror("Error opening library in dlopen call"); 
1971 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1989 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1992 |     perror("Error opening library in dlopen call"); 
1999 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2017 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2020 |     perror("Error opening library in dlopen call"); 
2027 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2045 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2048 |     perror("Error opening library in dlopen call"); 
2055 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2073 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2076 |     perror("Error opening library in dlopen call"); 
2083 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2101 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2104 |     perror("Error opening library in dlopen call"); 
2111 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2129 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2132 |     perror("Error opening library in dlopen call"); 
2139 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2157 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2160 |     perror("Error opening library in dlopen call"); 
2167 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2185 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2188 |     perror("Error opening library in dlopen call"); 
2195 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2213 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2216 |     perror("Error opening library in dlopen call"); 
2223 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2241 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2244 |     perror("Error opening library in dlopen call"); 
2251 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2269 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2272 |     perror("Error opening library in dlopen call"); 
2279 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2300 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2303 |     perror("Error opening library in dlopen call"); 
2310 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2328 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2331 |     perror("Error opening library in dlopen call"); 
2338 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2356 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2359 |     perror("Error opening library in dlopen call"); 
2366 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2384 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2387 |     perror("Error opening library in dlopen call"); 
2394 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2412 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2415 |     perror("Error opening library in dlopen call"); 
2422 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2443 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2446 |     perror("Error opening library in dlopen call"); 
2453 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2471 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2474 |     perror("Error opening library in dlopen call"); 
2481 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2499 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2502 |     perror("Error opening library in dlopen call"); 
2509 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2527 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2530 |     perror("Error opening library in dlopen call"); 
2537 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2555 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2558 |     perror("Error opening library in dlopen call"); 
2565 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2583 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2586 |     perror("Error opening library in dlopen call"); 
2593 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2611 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2614 |     perror("Error opening library in dlopen call"); 
2621 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2639 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2642 |     perror("Error opening library in dlopen call"); 
2649 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2667 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2670 |     perror("Error opening library in dlopen call"); 
2677 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2695 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2698 |     perror("Error opening library in dlopen call"); 
2705 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2723 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2726 |     perror("Error opening library in dlopen call"); 
2733 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2785 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2788 |     perror("Error opening library in dlopen call"); 
2795 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2826 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2829 |     perror("Error opening library in dlopen call"); 
2836 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2867 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2870 |     perror("Error opening library in dlopen call"); 
2877 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2908 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2911 |     perror("Error opening library in dlopen call"); 
2918 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2936 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2939 |     perror("Error opening library in dlopen call"); 
2946 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2964 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2967 |     perror("Error opening library in dlopen call"); 
2974 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2992 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2995 |     perror("Error opening library in dlopen call"); 
3002 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3020 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3023 |     perror("Error opening library in dlopen call"); 
3030 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3048 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3051 |     perror("Error opening library in dlopen call"); 
3058 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3076 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3079 |     perror("Error opening library in dlopen call"); 
3086 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3104 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3107 |     perror("Error opening library in dlopen call"); 
3114 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3132 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3135 |     perror("Error opening library in dlopen call"); 
3142 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3160 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3163 |     perror("Error opening library in dlopen call"); 
3170 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3188 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3191 |     perror("Error opening library in dlopen call"); 
3198 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3216 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3219 |     perror("Error opening library in dlopen call"); 
3226 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3244 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3247 |     perror("Error opening library in dlopen call"); 
3254 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3272 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3275 |     perror("Error opening library in dlopen call"); 
3282 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3300 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3303 |     perror("Error opening library in dlopen call"); 
3310 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3328 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3331 |     perror("Error opening library in dlopen call"); 
3338 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3356 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3359 |     perror("Error opening library in dlopen call"); 
3366 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3384 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3387 |     perror("Error opening library in dlopen call"); 
3394 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3412 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3415 |     perror("Error opening library in dlopen call"); 
3422 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3440 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3443 |     perror("Error opening library in dlopen call"); 
3450 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3468 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3471 |     perror("Error opening library in dlopen call"); 
3478 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3496 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3499 |     perror("Error opening library in dlopen call"); 
3506 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3524 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3527 |     perror("Error opening library in dlopen call"); 
3534 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3552 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3555 |     perror("Error opening library in dlopen call"); 
3562 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3580 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3583 |     perror("Error opening library in dlopen call"); 
3590 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
{% endraw %}

```
### src/Profile/TauOpenMPCollectorAPI.cpp

```

{% raw %}
932 |         void * handle = dlopen(libname, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### src/Profile/TauSampling.cpp

```

{% raw %}
499 | extern "C" void Tau_sampling_dlopen()
501 |   fprintf(stderr, "TAU: got a dlopen\n");
1048 |   // NOTE: This code ought to be at the start of a dlopen trap as well
{% endraw %}

```
### src/Profile/TauShmemSgiF.c

```cpp

{% raw %}
23 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
26 |     perror("Error opening library in dlopen call"); 
33 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
54 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
57 |     perror("Error opening library in dlopen call"); 
64 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
85 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
88 |     perror("Error opening library in dlopen call"); 
95 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
116 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
119 |     perror("Error opening library in dlopen call"); 
126 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
147 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
150 |     perror("Error opening library in dlopen call"); 
157 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
178 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
181 |     perror("Error opening library in dlopen call"); 
188 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
209 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
212 |     perror("Error opening library in dlopen call"); 
219 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
240 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
243 |     perror("Error opening library in dlopen call"); 
250 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
271 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
274 |     perror("Error opening library in dlopen call"); 
281 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
304 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
307 |     perror("Error opening library in dlopen call"); 
314 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
337 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
340 |     perror("Error opening library in dlopen call"); 
347 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
368 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
371 |     perror("Error opening library in dlopen call"); 
378 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
399 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
402 |     perror("Error opening library in dlopen call"); 
409 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
430 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
433 |     perror("Error opening library in dlopen call"); 
440 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
461 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
464 |     perror("Error opening library in dlopen call"); 
471 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
492 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
495 |     perror("Error opening library in dlopen call"); 
502 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
523 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
526 |     perror("Error opening library in dlopen call"); 
533 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
554 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
557 |     perror("Error opening library in dlopen call"); 
564 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
585 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
588 |     perror("Error opening library in dlopen call"); 
595 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
616 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
619 |     perror("Error opening library in dlopen call"); 
626 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
647 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
650 |     perror("Error opening library in dlopen call"); 
657 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
680 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
683 |     perror("Error opening library in dlopen call"); 
690 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
713 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
716 |     perror("Error opening library in dlopen call"); 
723 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
746 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
749 |     perror("Error opening library in dlopen call"); 
756 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
779 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
782 |     perror("Error opening library in dlopen call"); 
789 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
812 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
815 |     perror("Error opening library in dlopen call"); 
822 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
845 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
848 |     perror("Error opening library in dlopen call"); 
855 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
878 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
881 |     perror("Error opening library in dlopen call"); 
888 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
911 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
914 |     perror("Error opening library in dlopen call"); 
921 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
942 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
945 |     perror("Error opening library in dlopen call"); 
952 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
973 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
976 |     perror("Error opening library in dlopen call"); 
983 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1004 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1007 |     perror("Error opening library in dlopen call"); 
1014 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1035 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1038 |     perror("Error opening library in dlopen call"); 
1045 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1066 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1069 |     perror("Error opening library in dlopen call"); 
1076 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1099 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1102 |     perror("Error opening library in dlopen call"); 
1109 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1132 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1135 |     perror("Error opening library in dlopen call"); 
1142 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1165 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1168 |     perror("Error opening library in dlopen call"); 
1175 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1198 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1201 |     perror("Error opening library in dlopen call"); 
1208 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1231 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1234 |     perror("Error opening library in dlopen call"); 
1241 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1264 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1267 |     perror("Error opening library in dlopen call"); 
1274 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1297 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1300 |     perror("Error opening library in dlopen call"); 
1307 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1328 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1331 |     perror("Error opening library in dlopen call"); 
1338 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1359 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1362 |     perror("Error opening library in dlopen call"); 
1369 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1392 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1395 |     perror("Error opening library in dlopen call"); 
1402 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1425 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1428 |     perror("Error opening library in dlopen call"); 
1435 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1458 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1461 |     perror("Error opening library in dlopen call"); 
1468 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1491 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1494 |     perror("Error opening library in dlopen call"); 
1501 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1524 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1527 |     perror("Error opening library in dlopen call"); 
1534 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1557 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1560 |     perror("Error opening library in dlopen call"); 
1567 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1588 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1591 |     perror("Error opening library in dlopen call"); 
1598 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1619 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1622 |     perror("Error opening library in dlopen call"); 
1629 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1650 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1653 |     perror("Error opening library in dlopen call"); 
1660 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1681 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1684 |     perror("Error opening library in dlopen call"); 
1691 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1712 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1715 |     perror("Error opening library in dlopen call"); 
1722 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1743 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1746 |     perror("Error opening library in dlopen call"); 
1753 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1774 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1777 |     perror("Error opening library in dlopen call"); 
1784 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1805 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1808 |     perror("Error opening library in dlopen call"); 
1815 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1837 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1840 |     perror("Error opening library in dlopen call"); 
1847 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1876 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1879 |     perror("Error opening library in dlopen call"); 
1886 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1913 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1916 |     perror("Error opening library in dlopen call"); 
1923 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1949 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1952 |     perror("Error opening library in dlopen call"); 
1959 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
1980 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
1983 |     perror("Error opening library in dlopen call"); 
1990 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2011 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2014 |     perror("Error opening library in dlopen call"); 
2021 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2042 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2045 |     perror("Error opening library in dlopen call"); 
2052 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2073 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2076 |     perror("Error opening library in dlopen call"); 
2083 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2104 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2107 |     perror("Error opening library in dlopen call"); 
2114 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2136 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2139 |     perror("Error opening library in dlopen call"); 
2146 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2172 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2175 |     perror("Error opening library in dlopen call"); 
2182 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2203 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2206 |     perror("Error opening library in dlopen call"); 
2213 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2234 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2237 |     perror("Error opening library in dlopen call"); 
2244 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2265 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2268 |     perror("Error opening library in dlopen call"); 
2275 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2296 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2299 |     perror("Error opening library in dlopen call"); 
2306 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2328 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2331 |     perror("Error opening library in dlopen call"); 
2338 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2367 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2370 |     perror("Error opening library in dlopen call"); 
2377 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2404 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2407 |     perror("Error opening library in dlopen call"); 
2414 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2440 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2443 |     perror("Error opening library in dlopen call"); 
2450 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2471 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2474 |     perror("Error opening library in dlopen call"); 
2481 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2502 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2505 |     perror("Error opening library in dlopen call"); 
2512 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2533 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2536 |     perror("Error opening library in dlopen call"); 
2543 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2564 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2567 |     perror("Error opening library in dlopen call"); 
2574 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2595 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2598 |     perror("Error opening library in dlopen call"); 
2605 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2627 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2630 |     perror("Error opening library in dlopen call"); 
2637 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2663 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2666 |     perror("Error opening library in dlopen call"); 
2673 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2694 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2697 |     perror("Error opening library in dlopen call"); 
2704 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2725 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2728 |     perror("Error opening library in dlopen call"); 
2735 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2756 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2759 |     perror("Error opening library in dlopen call"); 
2766 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2789 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2792 |     perror("Error opening library in dlopen call"); 
2799 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2822 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2825 |     perror("Error opening library in dlopen call"); 
2832 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2855 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2858 |     perror("Error opening library in dlopen call"); 
2865 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2888 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2891 |     perror("Error opening library in dlopen call"); 
2898 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2921 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2924 |     perror("Error opening library in dlopen call"); 
2931 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2954 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2957 |     perror("Error opening library in dlopen call"); 
2964 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
2987 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
2990 |     perror("Error opening library in dlopen call"); 
2997 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3020 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3023 |     perror("Error opening library in dlopen call"); 
3030 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3053 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3056 |     perror("Error opening library in dlopen call"); 
3063 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3086 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3089 |     perror("Error opening library in dlopen call"); 
3096 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3119 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3122 |     perror("Error opening library in dlopen call"); 
3129 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3152 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3155 |     perror("Error opening library in dlopen call"); 
3162 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3185 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3188 |     perror("Error opening library in dlopen call"); 
3195 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3219 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3222 |     perror("Error opening library in dlopen call"); 
3229 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3252 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3255 |     perror("Error opening library in dlopen call"); 
3262 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3285 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3288 |     perror("Error opening library in dlopen call"); 
3295 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3317 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3320 |     perror("Error opening library in dlopen call"); 
3327 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3348 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3351 |     perror("Error opening library in dlopen call"); 
3358 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3381 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3384 |     perror("Error opening library in dlopen call"); 
3391 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3414 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3417 |     perror("Error opening library in dlopen call"); 
3424 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3447 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3450 |     perror("Error opening library in dlopen call"); 
3457 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3480 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3483 |     perror("Error opening library in dlopen call"); 
3490 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3513 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3516 |     perror("Error opening library in dlopen call"); 
3523 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3546 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3549 |     perror("Error opening library in dlopen call"); 
3556 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3579 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3582 |     perror("Error opening library in dlopen call"); 
3589 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3610 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3613 |     perror("Error opening library in dlopen call"); 
3620 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3641 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3644 |     perror("Error opening library in dlopen call"); 
3651 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3672 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3675 |     perror("Error opening library in dlopen call"); 
3682 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3703 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3706 |     perror("Error opening library in dlopen call"); 
3713 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3734 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3737 |     perror("Error opening library in dlopen call"); 
3744 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3765 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3768 |     perror("Error opening library in dlopen call"); 
3775 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3796 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3799 |     perror("Error opening library in dlopen call"); 
3806 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3827 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3830 |     perror("Error opening library in dlopen call"); 
3837 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3859 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3862 |     perror("Error opening library in dlopen call"); 
3869 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3895 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3898 |     perror("Error opening library in dlopen call"); 
3905 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3926 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3929 |     perror("Error opening library in dlopen call"); 
3936 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3957 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3960 |     perror("Error opening library in dlopen call"); 
3967 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
3988 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
3991 |     perror("Error opening library in dlopen call"); 
3998 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4020 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4023 |     perror("Error opening library in dlopen call"); 
4030 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4056 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4059 |     perror("Error opening library in dlopen call"); 
4066 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4089 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4092 |     perror("Error opening library in dlopen call"); 
4099 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4122 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4125 |     perror("Error opening library in dlopen call"); 
4132 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4155 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4158 |     perror("Error opening library in dlopen call"); 
4165 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4188 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4191 |     perror("Error opening library in dlopen call"); 
4198 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4219 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4222 |     perror("Error opening library in dlopen call"); 
4229 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4250 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4253 |     perror("Error opening library in dlopen call"); 
4260 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4282 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4285 |     perror("Error opening library in dlopen call"); 
4292 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4319 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4322 |     perror("Error opening library in dlopen call"); 
4329 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4351 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4354 |     perror("Error opening library in dlopen call"); 
4361 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4382 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4385 |     perror("Error opening library in dlopen call"); 
4392 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4413 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4416 |     perror("Error opening library in dlopen call"); 
4423 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4444 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4447 |     perror("Error opening library in dlopen call"); 
4454 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4475 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4478 |     perror("Error opening library in dlopen call"); 
4485 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4515 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4518 |     perror("Error opening library in dlopen call"); 
4525 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4546 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4549 |     perror("Error opening library in dlopen call"); 
4556 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4577 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4580 |     perror("Error opening library in dlopen call"); 
4587 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4608 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4611 |     perror("Error opening library in dlopen call"); 
4618 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4639 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4642 |     perror("Error opening library in dlopen call"); 
4649 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4670 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4673 |     perror("Error opening library in dlopen call"); 
4680 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4701 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4704 |     perror("Error opening library in dlopen call"); 
4711 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4732 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4735 |     perror("Error opening library in dlopen call"); 
4742 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4763 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4766 |     perror("Error opening library in dlopen call"); 
4773 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4796 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4799 |     perror("Error opening library in dlopen call"); 
4806 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4829 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4832 |     perror("Error opening library in dlopen call"); 
4839 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4860 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4863 |     perror("Error opening library in dlopen call"); 
4870 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4891 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4894 |     perror("Error opening library in dlopen call"); 
4901 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4922 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4925 |     perror("Error opening library in dlopen call"); 
4932 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4953 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4956 |     perror("Error opening library in dlopen call"); 
4963 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
4984 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
4987 |     perror("Error opening library in dlopen call"); 
4994 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5015 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5018 |     perror("Error opening library in dlopen call"); 
5025 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5046 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5049 |     perror("Error opening library in dlopen call"); 
5056 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5077 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5080 |     perror("Error opening library in dlopen call"); 
5087 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5108 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5111 |     perror("Error opening library in dlopen call"); 
5118 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5139 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5142 |     perror("Error opening library in dlopen call"); 
5149 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5172 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5175 |     perror("Error opening library in dlopen call"); 
5182 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5205 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5208 |     perror("Error opening library in dlopen call"); 
5215 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5238 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5241 |     perror("Error opening library in dlopen call"); 
5248 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5271 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5274 |     perror("Error opening library in dlopen call"); 
5281 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5304 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5307 |     perror("Error opening library in dlopen call"); 
5314 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5337 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5340 |     perror("Error opening library in dlopen call"); 
5347 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5370 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5373 |     perror("Error opening library in dlopen call"); 
5380 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5403 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5406 |     perror("Error opening library in dlopen call"); 
5413 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5434 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5437 |     perror("Error opening library in dlopen call"); 
5444 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5465 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5468 |     perror("Error opening library in dlopen call"); 
5475 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5496 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5499 |     perror("Error opening library in dlopen call"); 
5506 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5527 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5530 |     perror("Error opening library in dlopen call"); 
5537 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5558 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5561 |     perror("Error opening library in dlopen call"); 
5568 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5591 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5594 |     perror("Error opening library in dlopen call"); 
5601 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5624 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5627 |     perror("Error opening library in dlopen call"); 
5634 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5657 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5660 |     perror("Error opening library in dlopen call"); 
5667 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5690 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5693 |     perror("Error opening library in dlopen call"); 
5700 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5723 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5726 |     perror("Error opening library in dlopen call"); 
5733 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5756 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5759 |     perror("Error opening library in dlopen call"); 
5766 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5789 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5792 |     perror("Error opening library in dlopen call"); 
5799 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5820 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5823 |     perror("Error opening library in dlopen call"); 
5830 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5851 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5854 |     perror("Error opening library in dlopen call"); 
5861 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5884 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5887 |     perror("Error opening library in dlopen call"); 
5894 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5917 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5920 |     perror("Error opening library in dlopen call"); 
5927 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5950 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5953 |     perror("Error opening library in dlopen call"); 
5960 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
5983 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
5986 |     perror("Error opening library in dlopen call"); 
5993 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6016 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6019 |     perror("Error opening library in dlopen call"); 
6026 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6049 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6052 |     perror("Error opening library in dlopen call"); 
6059 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6080 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6083 |     perror("Error opening library in dlopen call"); 
6090 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6111 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6114 |     perror("Error opening library in dlopen call"); 
6121 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6142 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6145 |     perror("Error opening library in dlopen call"); 
6152 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6173 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6176 |     perror("Error opening library in dlopen call"); 
6183 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6204 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6207 |     perror("Error opening library in dlopen call"); 
6214 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6235 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6238 |     perror("Error opening library in dlopen call"); 
6245 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6266 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6269 |     perror("Error opening library in dlopen call"); 
6276 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6297 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6300 |     perror("Error opening library in dlopen call"); 
6307 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6329 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6332 |     perror("Error opening library in dlopen call"); 
6339 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6368 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6371 |     perror("Error opening library in dlopen call"); 
6378 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6405 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6408 |     perror("Error opening library in dlopen call"); 
6415 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6441 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6444 |     perror("Error opening library in dlopen call"); 
6451 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6472 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6475 |     perror("Error opening library in dlopen call"); 
6482 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6503 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6506 |     perror("Error opening library in dlopen call"); 
6513 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6534 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6537 |     perror("Error opening library in dlopen call"); 
6544 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6565 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6568 |     perror("Error opening library in dlopen call"); 
6575 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6596 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6599 |     perror("Error opening library in dlopen call"); 
6606 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6628 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6631 |     perror("Error opening library in dlopen call"); 
6638 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6664 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6667 |     perror("Error opening library in dlopen call"); 
6674 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6695 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6698 |     perror("Error opening library in dlopen call"); 
6705 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6726 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6729 |     perror("Error opening library in dlopen call"); 
6736 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6757 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6760 |     perror("Error opening library in dlopen call"); 
6767 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6788 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6791 |     perror("Error opening library in dlopen call"); 
6798 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6820 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6823 |     perror("Error opening library in dlopen call"); 
6830 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6859 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6862 |     perror("Error opening library in dlopen call"); 
6869 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6896 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6899 |     perror("Error opening library in dlopen call"); 
6906 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6932 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6935 |     perror("Error opening library in dlopen call"); 
6942 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6963 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6966 |     perror("Error opening library in dlopen call"); 
6973 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
6994 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
6997 |     perror("Error opening library in dlopen call"); 
7004 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7025 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7028 |     perror("Error opening library in dlopen call"); 
7035 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7056 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7059 |     perror("Error opening library in dlopen call"); 
7066 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7087 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7090 |     perror("Error opening library in dlopen call"); 
7097 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7119 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7122 |     perror("Error opening library in dlopen call"); 
7129 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7155 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7158 |     perror("Error opening library in dlopen call"); 
7165 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7186 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7189 |     perror("Error opening library in dlopen call"); 
7196 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7217 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7220 |     perror("Error opening library in dlopen call"); 
7227 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7248 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7251 |     perror("Error opening library in dlopen call"); 
7258 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7281 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7284 |     perror("Error opening library in dlopen call"); 
7291 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7314 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7317 |     perror("Error opening library in dlopen call"); 
7324 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7347 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7350 |     perror("Error opening library in dlopen call"); 
7357 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7380 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7383 |     perror("Error opening library in dlopen call"); 
7390 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7413 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7416 |     perror("Error opening library in dlopen call"); 
7423 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7446 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7449 |     perror("Error opening library in dlopen call"); 
7456 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7479 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7482 |     perror("Error opening library in dlopen call"); 
7489 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7512 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7515 |     perror("Error opening library in dlopen call"); 
7522 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7545 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7548 |     perror("Error opening library in dlopen call"); 
7555 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7578 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7581 |     perror("Error opening library in dlopen call"); 
7588 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7611 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7614 |     perror("Error opening library in dlopen call"); 
7621 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7644 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7647 |     perror("Error opening library in dlopen call"); 
7654 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7677 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7680 |     perror("Error opening library in dlopen call"); 
7687 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7711 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7714 |     perror("Error opening library in dlopen call"); 
7721 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7744 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7747 |     perror("Error opening library in dlopen call"); 
7754 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7777 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7780 |     perror("Error opening library in dlopen call"); 
7787 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7809 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7812 |     perror("Error opening library in dlopen call"); 
7819 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7840 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7843 |     perror("Error opening library in dlopen call"); 
7850 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7873 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7876 |     perror("Error opening library in dlopen call"); 
7883 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7906 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7909 |     perror("Error opening library in dlopen call"); 
7916 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7939 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7942 |     perror("Error opening library in dlopen call"); 
7949 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
7972 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
7975 |     perror("Error opening library in dlopen call"); 
7982 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8005 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8008 |     perror("Error opening library in dlopen call"); 
8015 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8038 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8041 |     perror("Error opening library in dlopen call"); 
8048 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8071 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8074 |     perror("Error opening library in dlopen call"); 
8081 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8102 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8105 |     perror("Error opening library in dlopen call"); 
8112 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8133 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8136 |     perror("Error opening library in dlopen call"); 
8143 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8164 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8167 |     perror("Error opening library in dlopen call"); 
8174 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8195 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8198 |     perror("Error opening library in dlopen call"); 
8205 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8226 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8229 |     perror("Error opening library in dlopen call"); 
8236 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8257 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8260 |     perror("Error opening library in dlopen call"); 
8267 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8288 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8291 |     perror("Error opening library in dlopen call"); 
8298 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8319 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8322 |     perror("Error opening library in dlopen call"); 
8329 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8351 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8354 |     perror("Error opening library in dlopen call"); 
8361 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8387 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8390 |     perror("Error opening library in dlopen call"); 
8397 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8418 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8421 |     perror("Error opening library in dlopen call"); 
8428 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8449 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8452 |     perror("Error opening library in dlopen call"); 
8459 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8480 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8483 |     perror("Error opening library in dlopen call"); 
8490 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8512 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8515 |     perror("Error opening library in dlopen call"); 
8522 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8548 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8551 |     perror("Error opening library in dlopen call"); 
8558 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8581 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8584 |     perror("Error opening library in dlopen call"); 
8591 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8614 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8617 |     perror("Error opening library in dlopen call"); 
8624 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8647 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8650 |     perror("Error opening library in dlopen call"); 
8657 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8680 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8683 |     perror("Error opening library in dlopen call"); 
8690 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8711 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8714 |     perror("Error opening library in dlopen call"); 
8721 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8742 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8745 |     perror("Error opening library in dlopen call"); 
8752 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8774 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8777 |     perror("Error opening library in dlopen call"); 
8784 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8811 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8814 |     perror("Error opening library in dlopen call"); 
8821 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8843 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8846 |     perror("Error opening library in dlopen call"); 
8853 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8874 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8877 |     perror("Error opening library in dlopen call"); 
8884 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8905 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8908 |     perror("Error opening library in dlopen call"); 
8915 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8936 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8939 |     perror("Error opening library in dlopen call"); 
8946 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
8967 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
8970 |     perror("Error opening library in dlopen call"); 
8977 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9005 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
9008 |     perror("Error opening library in dlopen call"); 
9015 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9036 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
9039 |     perror("Error opening library in dlopen call"); 
9046 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9067 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
9070 |     perror("Error opening library in dlopen call"); 
9077 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9098 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
9101 |     perror("Error opening library in dlopen call"); 
9108 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9130 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
9133 |     perror("Error opening library in dlopen call"); 
9140 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
9163 |     tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); 
9166 |     perror("Error opening library in dlopen call"); 
9173 |       perror("Error obtaining symbol info from dlopen'ed lib"); 
{% endraw %}

```
### src/Profile/CuptiActivity.cpp

```

{% raw %}
486 |     static void *libcuda_handle = (void *)dlopen("libcuda.so", RTLD_NOW);
488 |         perror("Error opening libcuda.so in dlopen call");
493 |         perror("Error obtaining cuInit symbol info from dlopen'ed lib");
{% endraw %}

```
### src/Profile/TauUtil.cpp

```

{% raw %}
631 |   void* handle = dlopen(path, RTLD_NOW);
{% endraw %}

```
### src/Profile/TauGpuAdapterOpenCL.cpp

```

{% raw %}
267 |     handle = (void *)dlopen(libname, RTLD_NOW); 
270 |     perror("Error opening library in dlopen call"); 
276 |     perror("Error obtaining symbol info from dlopen'ed lib"); 
{% endraw %}

```
### src/Profile/TauRocProfiler.cpp

```

{% raw %}
650 |   void* handle = dlopen(kAqlProfileLib, RTLD_NOW);
{% endraw %}

```
### utils/tau_wrap.cpp

```

{% raw %}
879 |            << "    tau_handle = (void *) dlopen(tau_orig_libname, RTLD_NOW); \n\n"
881 |            << "    perror(\"Error opening library in dlopen call\"); \n"
891 |            << "      perror(\"Error obtaining symbol info from dlopen'ed lib\"); \n"
{% endraw %}

```
### utils/opari2/build-config/ltmain.sh

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
7344 | 	      if test yes = "$build_libtool_libs" && test yes = "$dlopen_support"; then
7412 | 	  # This library was specified with -dlopen.
7532 | 	    func_fatal_help "libraries can '-dlopen' only libtool libraries: $file"
7543 | 	passes="conv scan dlopen dlpreopen link"
7569 | 	dlopen) libs=$dlfiles ;;
7597 |       if test dlopen = "$pass"; then
7818 | 	    if test dlpreopen = "$pass" || test yes != "$dlopen_support" || test no = "$build_libtool_libs"; then
7819 | 	      # If there is no dlopen support or we're linking statically,
7847 | 	dlopen=
7877 | 	  test -n "$dlopen" && func_append dlfiles " $dlopen"
7923 | 	# This library was specified with -dlopen.
7924 | 	if test dlopen = "$pass"; then
7926 | 	    && func_fatal_error "cannot -dlopen a convenience library: '$lib'"
7928 | 	     test yes != "$dlopen_support" ||
7931 | 	    # If there is no dlname, no dlopen support or we're linking
7940 | 	fi # $pass = dlopen
7996 | 	      # (otherwise, the dlopen module name will be incorrect).  We do
7998 | 	      # We recover the dlopen module name by 'saving' the la file
8022 | 	      # Otherwise, use the dlname, so that lt_dlopen finds it.
8166 | 	  # systems (darwin).  Don't bleat about dlopened modules though!
8167 | 	  dlopenmodule=
8170 | 	      dlopenmodule=$dlpremoduletest
8174 | 	  if test -z "$dlopenmodule" && test yes = "$shouldnotlink" && test link = "$pass"; then
8271 | 		    # if the lib is a (non-dlopened) module then we cannot
8275 | 		      if test "X$dlopenmodule" != "X$lib"; then
8427 | 	      echo "*** a static module, that should work as long as the dlopening application"
8428 | 	      echo "*** is linked with the -dlopen flag to resolve symbols at runtime."
8572 |       if test dlopen != "$pass"; then
8705 | 	func_warning "'-dlopen' is ignored for archives"
8772 | 	|| func_warning "'-dlopen self' is ignored for libtool libraries"
9466 | 	    echo "*** a static module, that should work as long as the dlopening"
9467 | 	    echo "*** application is linked with the -dlopen flag."
9485 | 	    echo "*** or is declared to -dlopen it."
10097 | 	func_warning "'-dlopen' is ignored for objects"
10217 | 	&& test unknown,unknown,unknown = "$dlopen_support,$dlopen_self,$dlopen_self_static" \
10218 | 	&& func_warning "'LT_INIT([dlopen])' not used. Assuming no dlopen support."
10249 | 	# is going to be dlopening itself or any libraries.
10916 | # The name that we can dlopen(3).
10945 | # Files to dlopen/dlpreopen
10946 | dlopen='$dlfiles'
{% endraw %}

```
### utils/opari2/build-config/m4/libtool.m4

```

{% raw %}
1836 | # _LT_TRY_DLOPEN_SELF (ACTION-IF-TRUE, ACTION-IF-TRUE-W-USCORE,
1839 | m4_defun([_LT_TRY_DLOPEN_SELF],
1897 |   void *self = dlopen (0, LT_DLGLOBAL|LT_DLLAZY_OR_NOW);
1930 | ])# _LT_TRY_DLOPEN_SELF
1933 | # LT_SYS_DLOPEN_SELF
1935 | AC_DEFUN([LT_SYS_DLOPEN_SELF],
1937 | if test yes != "$enable_dlopen"; then
1938 |   enable_dlopen=unknown
1939 |   enable_dlopen_self=unknown
1940 |   enable_dlopen_self_static=unknown
1942 |   lt_cv_dlopen=no
1943 |   lt_cv_dlopen_libs=
1947 |     lt_cv_dlopen=load_add_on
1948 |     lt_cv_dlopen_libs=
1949 |     lt_cv_dlopen_self=yes
1953 |     lt_cv_dlopen=LoadLibrary
1954 |     lt_cv_dlopen_libs=
1958 |     lt_cv_dlopen=dlopen
1959 |     lt_cv_dlopen_libs=
1964 |     AC_CHECK_LIB([dl], [dlopen],
1965 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],[
1966 |     lt_cv_dlopen=dyld
1967 |     lt_cv_dlopen_libs=
1968 |     lt_cv_dlopen_self=yes
1975 |     lt_cv_dlopen=dlopen
1976 |     lt_cv_dlopen_libs=
1977 |     lt_cv_dlopen_self=no
1982 | 	  [lt_cv_dlopen=shl_load],
1984 | 	    [lt_cv_dlopen=shl_load lt_cv_dlopen_libs=-ldld],
1985 | 	[AC_CHECK_FUNC([dlopen],
1986 | 	      [lt_cv_dlopen=dlopen],
1987 | 	  [AC_CHECK_LIB([dl], [dlopen],
1988 | 		[lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-ldl],
1989 | 	    [AC_CHECK_LIB([svld], [dlopen],
1990 | 		  [lt_cv_dlopen=dlopen lt_cv_dlopen_libs=-lsvld],
1992 | 		    [lt_cv_dlopen=dld_link lt_cv_dlopen_libs=-ldld])
2001 |   if test no = "$lt_cv_dlopen"; then
2002 |     enable_dlopen=no
2004 |     enable_dlopen=yes
2007 |   case $lt_cv_dlopen in
2008 |   dlopen)
2016 |     LIBS="$lt_cv_dlopen_libs $LIBS"
2018 |     AC_CACHE_CHECK([whether a program can dlopen itself],
2019 | 	  lt_cv_dlopen_self, [dnl
2020 | 	  _LT_TRY_DLOPEN_SELF(
2021 | 	    lt_cv_dlopen_self=yes, lt_cv_dlopen_self=yes,
2022 | 	    lt_cv_dlopen_self=no, lt_cv_dlopen_self=cross)
2025 |     if test yes = "$lt_cv_dlopen_self"; then
2027 |       AC_CACHE_CHECK([whether a statically linked program can dlopen itself],
2028 | 	  lt_cv_dlopen_self_static, [dnl
2029 | 	  _LT_TRY_DLOPEN_SELF(
2030 | 	    lt_cv_dlopen_self_static=yes, lt_cv_dlopen_self_static=yes,
2031 | 	    lt_cv_dlopen_self_static=no,  lt_cv_dlopen_self_static=cross)
2041 |   case $lt_cv_dlopen_self in
2042 |   yes|no) enable_dlopen_self=$lt_cv_dlopen_self ;;
2043 |   *) enable_dlopen_self=unknown ;;
2046 |   case $lt_cv_dlopen_self_static in
2047 |   yes|no) enable_dlopen_self_static=$lt_cv_dlopen_self_static ;;
2048 |   *) enable_dlopen_self_static=unknown ;;
2051 | _LT_DECL([dlopen_support], [enable_dlopen], [0],
2052 | 	 [Whether dlopen is supported])
2053 | _LT_DECL([dlopen_self], [enable_dlopen_self], [0],
2054 | 	 [Whether dlopen of programs is supported])
2055 | _LT_DECL([dlopen_self_static], [enable_dlopen_self_static], [0],
2056 | 	 [Whether dlopen of statically linked programs is supported])
2057 | ])# LT_SYS_DLOPEN_SELF
2060 | AU_ALIAS([AC_LIBTOOL_DLOPEN_SELF], [LT_SYS_DLOPEN_SELF])
2062 | dnl AC_DEFUN([AC_LIBTOOL_DLOPEN_SELF], [])
6187 |     [Compiler flag to allow reflexive dlopens])
6300 |   LT_SYS_DLOPEN_SELF
{% endraw %}

```
### utils/opari2/build-config/m4/ltoptions.m4

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
### apex/src/wrappers/pthread_wrapper.c

```cpp

{% raw %}
46 |     void * syms = dlopen(NULL, RTLD_NOW);
{% endraw %}

```
### apex/src/apex/apex.cpp

```

{% raw %}
1135 |         void * plugin_handle = dlopen(path, RTLD_NOW);
{% endraw %}

```
### tools/src/contrib/hpctoolkit-4.9.2-r2138.patch

```

{% raw %}
37 | +void Tau_sampling_dlopen();
87 | @@ -397,6 +410,7 @@ monitor_dlopen(const char *path, int fla
90 |    csprof_dlopen(path, flags, handle);
91 | +  Tau_sampling_dlopen();
{% endraw %}

```