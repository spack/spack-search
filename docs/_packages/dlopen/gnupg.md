---
name: "gnupg"
layout: package
next_package: gnutls
previous_package: gmt
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.2.15
9 / 1018 files match, 4 filtered matches.

 - [scd/apdu.c](#scdapduc)
 - [common/iobuf.c](#commoniobufc)
 - [common/homedir.c](#commonhomedirc)
 - [common/dynload.h](#commondynloadh)

### scd/apdu.c

```c

{% raw %}
1951 |     {
1952 |       void *handle;
1953 | 
1954 |       handle = dlopen (opt.pcsc_driver, RTLD_LAZY);
1955 |       if (!handle)
1956 |         {
{% endraw %}

```
### common/iobuf.c

```c

{% raw %}
2301 |       {
2302 | 	void *handle;
2303 | 
2304 | 	handle = dlopen ("kernel32.dll", RTLD_LAZY);
2305 | 	if (handle)
2306 | 	  {
{% endraw %}

```
### common/homedir.c

```c

{% raw %}
135 | 
136 |       for (i=0, handle = NULL; !handle && dllnames[i]; i++)
137 |         {
138 |           handle = dlopen (dllnames[i], RTLD_LAZY);
139 |           if (handle)
140 |             {
{% endraw %}

```
### common/dynload.h

```c

{% raw %}
39 | # define RTLD_LAZY 0
40 | 
41 | static inline void *
42 | dlopen (const char *name, int flag)
43 | {
44 |   void *hd;
{% endraw %}

```