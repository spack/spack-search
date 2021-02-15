---
name: "perl-alien-svn"
layout: package
next_package: chapel
previous_package: clp
languages: []
---
## 1.7.17.0
1 / 1426 files match

 - [src/subversion/Makefile.in](#srcsubversionmakefilein)

### src/subversion/Makefile.in

```

{% raw %}
190 | LT_EXECUTE = $(LIBTOOL) $(LTFLAGS) --mode=execute `for f in $(abs_builddir)/subversion/*/*.la; do echo -dlopen $$f; done`
{% endraw %}

```