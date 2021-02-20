---
name: "haproxy"
layout: package
next_package: hashcat
previous_package: guile
languages: ['c']
---
## 2.1.0
1 / 593 files match, 1 filtered matches.

 - [src/i386-linux-vsys.c](#srci386-linux-vsysc)

### src/i386-linux-vsys.c

```c

{% raw %}
185 | 	 * vsyscall32 = 1, which randomizes the VDSO address.
186 | 	 */
187 | #ifdef USE_VSYSCALL_DLSYM
188 | 	void *handle = dlopen("linux-gate.so.1", RTLD_NOW);
189 | 	if (handle) {
190 | 		void *ptr;
{% endraw %}

```