---
name: "linux-headers"
layout: package
next_package: dateutils
previous_package: wonton
languages: ['cpp']
---
## 4.9.10
5 / 50920 files match

 - [Documentation/filesystems/ramfs-rootfs-initramfs.txt](#documentationfilesystemsramfs-rootfs-initramfstxt)
 - [tools/testing/selftests/x86/test_syscall_vdso.c](#toolstestingselftestsx86test_syscall_vdsoc)
 - [tools/lib/traceevent/event-plugin.c](#toolslibtraceeventevent-pluginc)
 - [tools/perf/ui/setup.c](#toolsperfuisetupc)
 - [tools/perf/util/usage.c](#toolsperfutilusagec)

### Documentation/filesystems/ramfs-rootfs-initramfs.txt

```

{% raw %}
252 | over 400k.  With uClibc it's 7k.  Also note that glibc dlopens libnss to do
{% endraw %}

```
### tools/testing/selftests/x86/test_syscall_vdso.c

```cpp

{% raw %}
390 | 	 * syscall_addr = dlsym(dlopen("linux-gate.so.1", RTLD_NOW), "__kernel_vsyscall");
{% endraw %}

```
### tools/lib/traceevent/event-plugin.c

```cpp

{% raw %}
303 | 	handle = dlopen(plugin, RTLD_NOW | RTLD_GLOBAL);
{% endraw %}

```
### tools/perf/ui/setup.c

```cpp

{% raw %}
18 | 	perf_gtk_handle = dlopen(PERF_GTK_DSO, RTLD_LAZY);
22 | 		perf_gtk_handle = dlopen(buf, RTLD_LAZY);
{% endraw %}

```
### tools/perf/util/usage.c

```cpp

{% raw %}
40 | /* If we are in a dlopen()ed .so write to a global variable would segfault
{% endraw %}

```