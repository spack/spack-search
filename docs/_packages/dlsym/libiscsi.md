---
name: "libiscsi"
layout: package
next_package: slurm
previous_package: libunwind
library_name: dlsym
matches: ['dlsym']
languages: ['c']
---
## 1.18.0
2 / 307 files match, 2 filtered matches.

 - [test-tool/iscsi-test-cu.c](#test-tooliscsi-test-cuc)
 - [examples/ld_iscsi.c](#examplesld_iscsic)

### test-tool/iscsi-test-cu.c

```c

{% raw %}
1213 |          * This allows such tests to do their mutates and then call out
1214 |          * to the real queueing function once they have modified the data.
1215 |          */
1216 |         real_iscsi_queue_pdu = dlsym(RTLD_NEXT, "iscsi_queue_pdu");
1217 | 
1218 |         if ((mp_num_sds == 0) || (mp_sds[0]->iscsi_url == NULL
{% endraw %}

```
### examples/ld_iscsi.c

```c

{% raw %}
595 | 		debug = atoi(getenv("LD_ISCSI_DEBUG"));
596 | 	}
597 | 
598 | 	real_open = dlsym(RTLD_NEXT, "open");
599 | 	if (real_open == NULL) {
600 | 		LD_ISCSI_DPRINTF(0,"Failed to dlsym(open)");
601 | 		exit(10);
602 | 	}
603 | 
604 | 	real_close = dlsym(RTLD_NEXT, "close");
605 | 	if (real_close == NULL) {
606 | 		LD_ISCSI_DPRINTF(0,"Failed to dlsym(close)");
607 | 		exit(10);
608 | 	}
609 | 
610 | 	real_fxstat = dlsym(RTLD_NEXT, "__fxstat");
611 | 	if (real_fxstat == NULL) {
612 | 		LD_ISCSI_DPRINTF(0,"Failed to dlsym(__fxstat)");
613 | 		exit(10);
614 | 	}
615 | 
616 | 	real_lxstat = dlsym(RTLD_NEXT, "__lxstat");
617 | 	if (real_lxstat == NULL) {
618 | 		LD_ISCSI_DPRINTF(0,"Failed to dlsym(__lxstat)");
619 | 		exit(10);
620 | 	}
621 | 	real_xstat = dlsym(RTLD_NEXT, "__xstat");
622 | 	if (real_xstat == NULL) {
623 | 		LD_ISCSI_DPRINTF(0,"Failed to dlsym(__xstat)");
624 | 		exit(10);
625 | 	}
626 | 
627 | 	real_lseek = dlsym(RTLD_NEXT, "lseek");
628 | 	if (real_lseek == NULL) {
629 | 		LD_ISCSI_DPRINTF(0,"Failed to dlsym(lseek)");
630 | 		exit(10);
631 | 	}
632 | 
633 | 	real_read = dlsym(RTLD_NEXT, "read");
634 | 	if (real_read == NULL) {
635 | 		LD_ISCSI_DPRINTF(0,"Failed to dlsym(read)");
636 | 		exit(10);
637 | 	}
638 | 
639 | 	real_pread = dlsym(RTLD_NEXT, "pread");
640 | 	if (real_pread == NULL) {
641 | 		LD_ISCSI_DPRINTF(0,"Failed to dlsym(pread)");
642 | 		exit(10);
643 | 	}
644 | 
645 | 	real_write = dlsym(RTLD_NEXT, "write");
646 | 	if (real_write == NULL) {
647 | 		LD_ISCSI_DPRINTF(0,"Failed to dlsym(write)");
648 | 		exit(10);
649 | 	}
650 | 
651 | 	real_pwrite = dlsym(RTLD_NEXT, "pwrite");
652 | 	if (real_pwrite == NULL) {
653 | 		LD_ISCSI_DPRINTF(0,"Failed to dlsym(pwrite)");
654 | 		exit(10);
655 | 	}
656 | 
657 | 	real_dup2 = dlsym(RTLD_NEXT, "dup2");
658 | 	if (real_dup2 == NULL) {
659 | 		LD_ISCSI_DPRINTF(0,"Failed to dlsym(dup2)");
660 | 		exit(10);
661 | 	}
662 | 
663 | #if defined(_LARGEFILE64_SOURCE) && _FILE_OFFSET_BITS != 64
664 | 	real_fxstat64 = dlsym(RTLD_NEXT, "__fxstat64");
665 | 	if (real_fxstat64 == NULL) {
666 | 		LD_ISCSI_DPRINTF(0,"Failed to dlsym(__fxstat64)");
667 | 	}
668 | 
669 | 	real_lxstat64 = dlsym(RTLD_NEXT, "__lxstat64");
670 | 	if (real_lxstat64 == NULL) {
671 | 		LD_ISCSI_DPRINTF(0,"Failed to dlsym(_lxstat64)");
672 | 	}
673 | 
674 | 	real_xstat64 = dlsym(RTLD_NEXT, "__xstat64");
675 | 	if (real_xstat64 == NULL) {
676 | 		LD_ISCSI_DPRINTF(0,"Failed to dlsym(__xstat64)");
677 | 	}
678 | #endif
{% endraw %}

```