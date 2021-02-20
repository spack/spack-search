---
name: "vpic"
layout: package
next_package: vsearch
previous_package: virtualgl
languages: ['cpp']
---
## develop
1 / 349 files match, 1 filtered matches.

 - [src/util/checkpt/checkpt.cc](#srcutilcheckptcheckptcc)

### src/util/checkpt/checkpt.cc

```cpp

{% raw %}
623 | 
624 |      Note: Currently, this code path is disabled as fname returned by
625 |      dladdr seems not be to useful (it typically is the application's
626 |      name, which dlopen cannot actually open) and there are open
627 |      issues of how to call dlopen (RTLD_LAZY, RTLD_NOW, RTLD_GLOBAL)
628 |      and what and how to call dlclose. */
629 | 
630 |   if( 0 && fname ) {
631 |     dlerror();
632 |     fbase = dlopen( fname, RTLD_LAZY );
633 |     err = dlerror();
634 |     if( err ) WARNING(( "dlopen(%s,RTLD_LAZY): %s", fname, err ));
635 |     else {
636 |       dlerror();
{% endraw %}

```