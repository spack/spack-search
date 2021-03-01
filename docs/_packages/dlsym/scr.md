---
name: "scr"
layout: package
next_package: shc
previous_package: scorep
library_name: dlsym
matches: ['dlsym']
languages: ['c']
---
## 2.0.0
1 / 220 files match, 1 filtered matches.

 - [src/scr_interpose.c](#srcscr_interposec)

### src/scr_interpose.c

```c

{% raw %}
589 | ==============================================================================
590 | */
591 | 
592 | static void* mydlsym(const char *name)
593 | {
594 |   void *p = dlsym(RTLD_NEXT, name);
595 |   if (!p) {
596 |     fprintf(stderr,"dlsym(RTLD_NEXT, %s) failed: %s\n", name, dlerror());
597 |     exit(1);
598 |   }
606 | 
607 |   /* interpose MPI functions */
608 |   if (scri_real_mpi_init == NULL) {
609 |     scri_real_mpi_init = (int (*)(int *, char ***)) mydlsym("MPI_Init");
610 |   }
611 |   if (scri_real_mpi_fini == NULL) {
612 |     scri_real_mpi_fini = (int (*)()) mydlsym("MPI_Finalize");
613 |   }
614 | 
615 |   /* interpose open/close functions */
616 |   if (scri_real_open == NULL) {
617 |     scri_real_open  = (int (*)(const char *, int, ...)) mydlsym("open");
618 |   }
619 |   /*
620 |   scri_real_open  = (int (*)(const char *, int, mode_t)) mydlsym("open");
621 |   */
622 |   if (scri_real_close == NULL) {
623 |     scri_real_close = (int (*)(int fd)) mydlsym("close");
624 |   }
625 | 
626 |   /* interpose fopen/fclose functions */
627 |   if (scri_real_fopen == NULL) {
628 |     scri_real_fopen  = (FILE* (*)(const char *, const char *)) mydlsym("fopen");
629 |   }
630 |   if (scri_real_fclose == NULL) {
631 |     scri_real_fclose = (int (*)(FILE*)) mydlsym("fclose");
632 |   }
633 | 
634 |   /* interpose mkdir */
635 |   if (scri_real_mkdir == NULL) {
636 |     scri_real_mkdir = (int (*)(const char*, mode_t)) mydlsym("mkdir");
637 |   }
638 | 
639 |   /* interpose read/write functions */
640 | /*
641 |   real_read  = (ssize_t (*)(int fd, void *buf, size_t count))       mydlsym("read");
642 |   real_write = (ssize_t (*)(int fd, const void *buf, size_t count)) mydlsym("write");
643 | */
644 | 
{% endraw %}

```