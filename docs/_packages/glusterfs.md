---
name: "glusterfs"
layout: package
next_package: file
previous_package: htslib
languages: ['c']
---
## 7.3
14 / 2186 files match

 - [libglusterfs/src/xlator.c](#libglusterfssrcxlatorc)
 - [glusterfsd/src/glusterfsd.c](#glusterfsdsrcglusterfsdc)
 - [rpc/rpc-lib/src/rpc-transport.h](#rpcrpc-libsrcrpc-transporth)
 - [rpc/rpc-lib/src/rpc-transport.c](#rpcrpc-libsrcrpc-transportc)
 - [xlators/features/cloudsync/src/cloudsync.c](#xlatorsfeaturescloudsyncsrccloudsyncc)
 - [xlators/features/cloudsync/src/cloudsync-plugins/src/cvlt/src/libcvlt.h](#xlatorsfeaturescloudsyncsrccloudsync-pluginssrccvltsrclibcvlth)
 - [xlators/features/cloudsync/src/cloudsync-plugins/src/cvlt/src/libcvlt.c](#xlatorsfeaturescloudsyncsrccloudsync-pluginssrccvltsrclibcvltc)
 - [xlators/protocol/server/src/authenticate.c](#xlatorsprotocolserversrcauthenticatec)

### libglusterfs/src/xlator.c

```c

{% raw %}
206 |     handle = dlopen(name, RTLD_NOW);
370 |     handle = dlopen(name, RTLD_NOW);
{% endraw %}

```
### glusterfsd/src/glusterfsd.c

```c

{% raw %}
1993 |     libhandle = dlopen(libpathfull, RTLD_NOW);
2087 |     libhandle = dlopen(libpathfull, RTLD_NOW);
{% endraw %}

```
### rpc/rpc-lib/src/rpc-transport.h

```c

{% raw %}
196 |     void *dl_handle; /* handle of dlopen() */
{% endraw %}

```
### rpc/rpc-lib/src/rpc-transport.c

```c

{% raw %}
297 |     handle = dlopen(name, RTLD_NOW);
{% endraw %}

```
### xlators/features/cloudsync/src/cloudsync.c

```c

{% raw %}
108 |         handle = dlopen(libpath, RTLD_NOW);
{% endraw %}

```
### xlators/features/cloudsync/src/cloudsync-plugins/src/cvlt/src/libcvlt.h

```c

{% raw %}
56 |     void *handle;                  /* handle returned from dlopen   */
{% endraw %}

```
### xlators/features/cloudsync/src/cloudsync-plugins/src/cvlt/src/libcvlt.c

```c

{% raw %}
80 |     arch->handle = dlopen(LIBARCHIVE_SO, RTLD_NOW);
{% endraw %}

```
### xlators/protocol/server/src/authenticate.c

```c

{% raw %}
51 |     handle = dlopen(auth_file, RTLD_LAZY);
54 |                "dlopen(%s): %s\n", auth_file, dlerror());
{% endraw %}

```