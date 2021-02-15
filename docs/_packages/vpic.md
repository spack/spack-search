---
name: "vpic"
layout: package
next_package: py-pyarrow
previous_package: libmonitor
languages: ['cpp']
---
## develop
1 / 349 files match

 - [src/util/checkpt/checkpt.cc](#srcutilcheckptcheckptcc)

### src/util/checkpt/checkpt.cc

```cpp

{% raw %}
626 |      name, which dlopen cannot actually open) and there are open
627 |      issues of how to call dlopen (RTLD_LAZY, RTLD_NOW, RTLD_GLOBAL)
632 |     fbase = dlopen( fname, RTLD_LAZY );
634 |     if( err ) WARNING(( "dlopen(%s,RTLD_LAZY): %s", fname, err ));
{% endraw %}

```