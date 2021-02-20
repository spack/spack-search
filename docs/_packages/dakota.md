---
name: "dakota"
layout: package
next_package: darshan-runtime
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
238 | 			"return %d from NSCreateObjectFileImageFromFile(\"%s\")\n",
239 | 			irc, name);
240 | #else
241 | 	h = dlopen(name, RTLD_NOW);
242 | #endif
243 | 	if (!h && warned && (f = fopen(name,"rb"))) {
{% endraw %}

```
### packages/external/ampl/funcadd1.c

```c

{% raw %}
238 | 			"return %d from NSCreateObjectFileImageFromFile(\"%s\")\n",
239 | 			irc, name);
240 | #else
241 | 	h = dlopen(name, RTLD_NOW);
242 | #endif
243 | 	if (!h && warned && (f = fopen(name,"rb"))) {
{% endraw %}

```
### packages/external/nidr/nidrgen.c

```c

{% raw %}
1439 | 	const char *s;
1440 | 	void *h, (*Botch)(const char*, ...);
1441 | 
1442 | 	h = dlopen(lname, RTLD_NOW);
1443 | 	if (!h) {
1444 | 		Botch = botch;
5792 | 		libread1(0, libname, 0, 2);
5793 | #else
5794 | 		{
5795 | 		fprintf(stderr, "\ndlopen for \"%s\" is NOT SUPPORTED\n", libname);
5796 | 		return usage(1);
5797 | 		}
{% endraw %}

```
### packages/external/nidr/nidr.c

```c

{% raw %}
556 | 	}
557 | 
558 |  void *
559 | nidr_dlopen(const char *libname)
560 | {
561 | #ifdef NO_NIDR_DYNLIB /*{{*/
562 | 	botch("dlopen for \"%s\" is NOT SUPPORTED", libname);
563 | 	return (void*)libname;
564 | #else /*}{*/
569 | 
570 | 	b = nidr_basename(libname);
571 | 	if (b > libname)
572 | 		return dlopen(libname, RTLD_NOW);
573 | 	buf = buf0;
574 | 	buflen = sizeof(buf0);
576 | 	if (nidr_exedir) {
577 | 		L1 = L + nidr_exedir_len + 1;
578 | 		if (L1 > buflen) {
579 | 			buf = (char*)Alloc("nidr_dlopen", L1);
580 | 			buflen = L1;
581 | 			}
582 | 		memcpy(buf, nidr_exedir, nidr_exedir_len);
583 | 		strcpy(buf + nidr_exedir_len, libname);
584 | 		if ((h = dlopen(buf, RTLD_NOW)))
585 | 			goto ret;
586 | 		}
587 | 	if (!(h = dlopen(libname, RTLD_NOW))) {
588 | 		L1 = L + 3;
589 | 		if (L1 > buflen) {
590 | 			buf = (char*)Alloc("nidr_dlopen", L1);
591 | 			buflen = L1;
592 | 			}
593 | 		buf[0] = '.';
594 | 		buf[1] = Slash;
595 | 		strcpy(buf+2, libname);
596 | 		if (!(h = dlopen(buf, RTLD_NOW)))
597 | 			h = dlopen(libname, RTLD_NOW); 	/* for dlerror */
598 | 		}
599 |  ret:
1090 | 		*tryagain = 0;
1091 | 	if (kw->kind & KWKind_Loaded)
1092 | 		return (KeyWord*)kw->f.vs;
1093 | 	h = nidr_dlopen(lname = (const char*)kw->f.vf);
1094 | 	if (!h) {
1095 | #ifndef NO_DLERROR
1534 | 	NIDR_KWlib *Lib;
1535 | 	void *h;
1536 | 
1537 | 	h = nidr_dlopen(libname);
1538 | 	if (!h) {
1539 | #ifndef NO_DLERROR
{% endraw %}

```