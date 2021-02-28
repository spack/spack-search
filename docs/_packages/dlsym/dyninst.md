---
name: "dyninst"
layout: package
next_package: unifyfs
previous_package: grass
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 10.2.1
4 / 1296 files match, 3 filtered matches.

 - [common/src/serialize-xml.C](#commonsrcserialize-xmlc)
 - [proccontrol/src/int_thread_db.C](#proccontrolsrcint_thread_dbc)
 - [dyninstAPI_RT/src/RTmutatedBinary_ELF.c](#dyninstapi_rtsrcrtmutatedbinary_elfc)

### common/src/serialize-xml.C

```c

{% raw %}
148 |       return NULL;
149 |     }
150 | 
151 |     my_xmlNewTextWriterFilename = (xmlTextWriterPtr(*)(const char *,int))dlsym(hXML,"xmlNewTextWriterFilename");
152 |     my_xmlTextWriterStartDocument = (int(*)(xmlTextWriterPtr, const char *, const char *, const char * ))dlsym(hXML,"xmlTextWriterStartDocument");
153 |     my_xmlTextWriterStartElement = (int(*)(xmlTextWriterPtr, const xmlChar *))dlsym(hXML,"xmlTextWriterStartElement");
154 |     my_xmlTextWriterWriteFormatElement = (int(*)(xmlTextWriterPtr,const xmlChar *,const char *,...))dlsym(hXML,"xmlTextWriterWriteFormatElement");
155 |     my_xmlTextWriterEndDocument = (int(*)(xmlTextWriterPtr))dlsym(hXML,"xmlTextWriterEndDocument");
156 |     my_xmlFreeTextWriter = (void(*)(xmlTextWriterPtr))dlsym(hXML,"xmlFreeTextWriter");
157 |     my_xmlTextWriterWriteFormatAttribute = (int(*)(xmlTextWriterPtr, const xmlChar *,const char *,...))dlsym(hXML,"xmlTextWriterWriteFormatAttribute");
158 |     my_xmlTextWriterEndElement = (int(*)(xmlTextWriterPtr))dlsym(hXML,"xmlTextWriterEndElement");
159 | 
160 | #endif
{% endraw %}

```
### proccontrol/src/int_thread_db.C

```c

{% raw %}
306 | #else
307 | #define TDB_BIND(SYM) \
308 |    do { \
309 |      p_ ## SYM = (SYM ## _t) dlsym(libhandle, #SYM); \
310 |      if (!p_ ## SYM) { \
311 |        const char *errmsg = dlerror();                                       \
{% endraw %}

```
### dyninstAPI_RT/src/RTmutatedBinary_ELF.c

```c

{% raw %}
307 | 	return 0;
308 |      }
309 | 
310 |      Elf_version = (unsigned (*)(unsigned)) dlsym(elfHandle, "elf_version");
311 |      Elf_begin = (Elf *(*)(int,Elf_Cmd,Elf *)) dlsym(elfHandle, "elf_begin");
312 |      Elf_getscn = (Elf_Scn *(*)(Elf *, size_t)) dlsym(elfHandle, "elf_getscn");
313 |      Elf_nextscn = (Elf_Scn *(*)(Elf *, Elf_Scn *)) dlsym(elfHandle, "elf_nextscn");
314 |      Elf_getdata = (Elf_Data *(*)(Elf_Scn *, Elf_Data *)) dlsym(elfHandle, "elf_getdata");
315 |      Elf32_getehdr = (Elf32_Ehdr *(*)(Elf *)) dlsym(elfHandle, "elf32_getehdr");
316 |      Elf32_getshdr = (Elf32_Shdr *(*)(Elf_Scn *)) dlsym(elfHandle, "elf32_getshdr");
317 |      Elf64_getehdr = (Elf64_Ehdr *(*)(Elf *)) dlsym(elfHandle, "elf64_getehdr");
318 |      Elf64_getshdr = (Elf64_Shdr *(*)(Elf_Scn *)) dlsym(elfHandle, "elf64_getshdr");
319 |      Elf_errmsg = (const char *(*)(int)) dlsym(elfHandle, "elf_errmsg");
320 |      Elf_errno = (int (*)(void)) dlsym(elfHandle, "elf_errno");
321 |      Elf_end = (int (*)(Elf *)) dlsym(elfHandle, "elf_end");
322 | 
323 | 	Elf_version(EV_CURRENT);
{% endraw %}

```