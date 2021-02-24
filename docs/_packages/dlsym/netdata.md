---
name: "netdata"
layout: package
next_package: wget
previous_package: openwsman
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.22.1
1 / 1590 files match, 1 filtered matches.

 - [collectors/ebpf_process.plugin/ebpf_process.c](#collectorsebpf_processpluginebpf_processc)

### collectors/ebpf_process.plugin/ebpf_process.c

```c

{% raw %}
676 |         error("[EBPF_PROCESS] Cannot load %s.", lpath);
677 |         return -1;
678 |     } else {
679 |         load_bpf_file = dlsym(libnetdata, "load_bpf_file");
680 |         if ((err = dlerror()) != NULL) {
681 |             error("[EBPF_PROCESS] Cannot find load_bpf_file: %s", err);
682 |             return -1;
683 |         }
684 | 
685 |         map_fd =  dlsym(libnetdata, "map_fd");
686 |         if ((err = dlerror()) != NULL) {
687 |             error("[EBPF_PROCESS] Cannot find map_fd: %s", err);
688 |             return -1;
689 |         }
690 | 
691 |         bpf_map_lookup_elem = dlsym(libnetdata, "bpf_map_lookup_elem");
692 |         if ((err = dlerror()) != NULL) {
693 |             error("[EBPF_PROCESS] Cannot find bpf_map_lookup_elem: %s", err);
695 |         }
696 | 
697 |         if(mode == 1) {
698 |             set_bpf_perf_event = dlsym(libnetdata, "set_bpf_perf_event");
699 |             if ((err = dlerror()) != NULL) {
700 |                 error("[EBPF_PROCESS] Cannot find set_bpf_perf_event: %s", err);
701 |                 return -1;
702 |             }
703 | 
704 |             perf_event_unmap =  dlsym(libnetdata, "perf_event_unmap");
705 |             if ((err = dlerror()) != NULL) {
706 |                 error("[EBPF_PROCESS] Cannot find perf_event_unmap: %s", err);
707 |                 return -1;
708 |             }
709 | 
710 |             perf_event_mmap_header =  dlsym(libnetdata, "perf_event_mmap_header");
711 |             if ((err = dlerror()) != NULL) {
712 |                 error("[EBPF_PROCESS] Cannot find perf_event_mmap_header: %s", err);
713 |                 return -1;
714 |             }
715 | 
716 |             netdata_perf_loop_multi = dlsym(libnetdata, "netdata_perf_loop_multi");
717 |             if ((err = dlerror()) != NULL) {
718 |                 error("[EBPF_PROCESS] Cannot find netdata_perf_loop_multi: %s", err);
{% endraw %}

```