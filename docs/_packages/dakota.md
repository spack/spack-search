---
name: "dakota"
layout: package
next_package: dbus
previous_package: czmq
languages: ['c']
---
## 6.12
28 / 13171 files match, 4 filtered matches.

 - [packages/external/acro/tpl/ampl/funcadd1.c](#packagesexternalacrotplamplfuncadd1c)
 - [packages/external/ampl/funcadd1.c](#packagesexternalamplfuncadd1c)
 - [packages/external/nidr/nidrgen.c](#packagesexternalnidrnidrgenc)
 - [packages/external/nidr/nidr.c](#packagesexternalnidrnidrc)

### packages/external/acro/tpl/ampl/funcadd1.c

```c

{% raw %}
241 | 	h = dlopen(name, RTLD_NOW);
{% endraw %}

```
### packages/external/ampl/funcadd1.c

```c

{% raw %}
241 | 	h = dlopen(name, RTLD_NOW);
{% endraw %}

```
### packages/external/nidr/nidrgen.c

```c

{% raw %}
1442 | 	h = dlopen(lname, RTLD_NOW);
5795 | 		fprintf(stderr, "\ndlopen for \"%s\" is NOT SUPPORTED\n", libname);
{% endraw %}

```
### packages/external/nidr/nidr.c

```c

{% raw %}
559 | nidr_dlopen(const char *libname)
562 | 	botch("dlopen for \"%s\" is NOT SUPPORTED", libname);
572 | 		return dlopen(libname, RTLD_NOW);
579 | 			buf = (char*)Alloc("nidr_dlopen", L1);
584 | 		if ((h = dlopen(buf, RTLD_NOW)))
587 | 	if (!(h = dlopen(libname, RTLD_NOW))) {
590 | 			buf = (char*)Alloc("nidr_dlopen", L1);
596 | 		if (!(h = dlopen(buf, RTLD_NOW)))
597 | 			h = dlopen(libname, RTLD_NOW); 	/* for dlerror */
1093 | 	h = nidr_dlopen(lname = (const char*)kw->f.vf);
1537 | 	h = nidr_dlopen(libname);
{% endraw %}

```