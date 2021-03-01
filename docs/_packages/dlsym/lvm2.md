---
name: "lvm2"
layout: package
next_package: mariadb
previous_package: lua
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.03.02
2 / 1036 files match, 2 filtered matches.

 - [lib/mm/memlock.c](#libmmmemlockc)
 - [daemons/dmeventd/dmeventd.c](#daemonsdmeventddmeventdc)

### lib/mm/memlock.c

```c

{% raw %}
103 | 	"locale/locale-archive",
104 | 	"/LC_MESSAGES/",
105 | 	"gconv/gconv-modules.cache",
106 | 	"/ld-2.",		/* not using dlopen,dlsym during mlock */
107 | 	"/libaio.so.",		/* not using aio during mlock */
108 | 	"/libattr.so.",		/* not using during mlock (udev) */
109 | 	"/libblkid.so.",	/* not using blkid during mlock (udev) */
110 | 	"/libbz2.so.",		/* not using during mlock (udev) */
111 | 	"/libcap.so.",		/* not using during mlock (systemd) */
112 | 	"/libdl-",		/* not using dlopen,dlsym during mlock */
113 | 	"/libdw-",		/* not using during mlock (udev) */
114 | 	"/libelf-",		/* not using during mlock (udev) */
419 | 	volatile unsigned char *abs_addr;
420 | 
421 | 	if (!_mmap_addr) {
422 | 		_mmap_addr = (unsigned char *) dlsym(RTLD_NEXT, "mmap");
423 | 		if (_mmap_addr[0] == 0xff && _mmap_addr[1] == 0x25) { /* plt */
424 | #ifdef __x86_64__
442 | 
443 | #ifdef __i386__
444 | 	if (!_mmap64_addr) {
445 | 		_mmap64_addr = (unsigned char *) dlsym(RTLD_NEXT, "mmap64");
446 | 		if (_mmap64_addr[0] == 0xff && _mmap64_addr[1] == 0x25) {
447 | 			abs_addr = *(void **)(_mmap64_addr + 2);
{% endraw %}

```
### daemons/dmeventd/dmeventd.c

```c

{% raw %}
323 | /* Lookup DSO symbols we need. */
324 | static int _lookup_symbol(void *dl, void **symbol, const char *name)
325 | {
326 | 	if (!(*symbol = dlsym(dl, name)))
327 | 		return_0;
328 | 
{% endraw %}

```