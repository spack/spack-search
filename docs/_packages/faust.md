---
name: "faust"
layout: package
next_package: faodel
previous_package: libwindowswm
languages: ['cpp']
---
## 2.27.2
4 / 3150 files match

 - [architecture/pure.cpp](#architecturepurecpp)
 - [architecture/AU/AUPublic/AUBase/ComponentBase.cpp](#architectureauaupublicaubasecomponentbasecpp)
 - [architecture/unsupported-arch/q.cpp](#architectureunsupported-archqcpp)
 - [embedded/faustremote/dns_avahi/config.h](#embeddedfaustremotedns_avahiconfigh)

### architecture/pure.cpp

```

{% raw %}
375 |    This is implemented using C linkage to facilitate dlopen access. */
{% endraw %}

```
### architecture/AU/AUPublic/AUBase/ComponentBase.cpp

```

{% raw %}
248 | 		void* theImage = dlopen("/System/Library/Frameworks/AudioUnit.framework/AudioUnit", RTLD_LAZY);
300 | 	void *theImage = dlopen("/System/Library/Frameworks/CoreServices.framework/CoreServices", RTLD_LAZY);
{% endraw %}

```
### architecture/unsupported-arch/q.cpp

```

{% raw %}
292 |    client. Implemented using C linkage to facilitate dlopen access. */
{% endraw %}

```
### embedded/faustremote/dns_avahi/config.h

```cpp

{% raw %}
70 | /* Have dlopen() */
71 | #define HAVE_DLOPEN 1
{% endraw %}

```