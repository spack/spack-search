---
name: "fltk"
layout: package
next_package: care
previous_package: gsl
languages: []
---
## 1.3.3
7 / 1482 files match

 - [configure.in](#configurein)
 - [src/Fl_Native_File_Chooser_GTK.cxx](#srcfl_native_file_chooser_gtkcxx)
 - [src/Fl_Window_shape.cxx](#srcfl_window_shapecxx)
 - [src/Fl_x.cxx](#srcfl_xcxx)
 - [src/glut_compatability.cxx](#srcglut_compatabilitycxx)
 - [src/Fl_Preferences.cxx](#srcfl_preferencescxx)
 - [src/Fl_cocoa.mm](#srcfl_cocoamm)

### configure.in

```

{% raw %}
585 | dnl Check for dlopen/dlsym...
926 | 	    AC_SEARCH_LIBS(dlopen, dl)
{% endraw %}

```
### src/Fl_Native_File_Chooser_GTK.cxx

```

{% raw %}
20 | #include <dlfcn.h>   // for dlopen et al
634 | static void* fl_dlopen(const char *filename1, const char *filename2)
636 |   void *ptr = dlopen(filename1, RTLD_LAZY | RTLD_GLOBAL);
637 |   if (!ptr) ptr = dlopen(filename2, RTLD_LAZY | RTLD_GLOBAL);
643 |  * Use dlopen to see if we can load the gtk dynamic libraries that
653 |   ptr_glib    = dlopen("/sw/lib/libglib-2.0.dylib", RTLD_LAZY | RTLD_GLOBAL);
655 |   ptr_glib    = fl_dlopen("libglib-2.0.so", "libglib-2.0.so.0");
659 |   ptr_gtk     = dlopen("/sw/lib/libgtk-x11-2.0.dylib", RTLD_LAZY | RTLD_GLOBAL);
661 |   ptr_gtk     = fl_dlopen("libgtk-x11-2.0.so", "libgtk-x11-2.0.so.0");
669 |     ptr_gtk     = fl_dlopen("libgtk-3.so", "libgtk-3.so.0");
{% endraw %}

```
### src/Fl_Window_shape.cxx

```

{% raw %}
145 |     void *handle = dlopen(NULL, RTLD_LAZY); // search symbols in executable
{% endraw %}

```
### src/Fl_x.cxx

```

{% raw %}
758 |   void *libxrandr_addr = dlopen("libXrandr.so.2", RTLD_LAZY);
759 |   if (!libxrandr_addr)  libxrandr_addr = dlopen("libXrandr.so", RTLD_LAZY);
{% endraw %}

```
### src/glut_compatability.cxx

```

{% raw %}
450 |   if (!rtld_default) rtld_default = dlopen(0, RTLD_LAZY);
{% endraw %}

```
### src/Fl_Preferences.cxx

```

{% raw %}
1774 |     dl = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### src/Fl_cocoa.mm

```

{% raw %}
1502 |       void* h = dlopen(NULL, RTLD_LAZY);
4063 |     carbon = dlopen("/System/Library/Frameworks/Carbon.framework/Carbon", RTLD_LAZY);
{% endraw %}

```