---
name: "wireshark"
layout: package
next_package: mariadb
previous_package: med
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.6.0
3 / 6137 files match, 1 filtered matches.

 - [caputils/capture-pcap-util-unix.c](#caputilscapture-pcap-util-unixc)

### caputils/capture-pcap-util-unix.c

```c

{% raw %}
364 | 	if (!initialized) {
365 | 		p_pcap_set_tstamp_precision =
366 | 		    (int (*)(pcap_t *, int))
367 | 		      dlsym(RTLD_NEXT, "pcap_set_tstamp_precision");
368 | 		initialized = TRUE;
369 | 	}
396 | 	if (!initialized) {
397 | 		p_pcap_get_tstamp_precision =
398 | 		    (int (*)(pcap_t *))
399 | 		      dlsym(RTLD_NEXT, "pcap_get_tstamp_precision");
400 | 		initialized = TRUE;
401 | 	}
{% endraw %}

```