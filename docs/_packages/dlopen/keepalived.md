---
name: "keepalived"
layout: package
next_package: kitty
previous_package: kcov
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.0.12
3 / 286 files match, 3 filtered matches.

 - [keepalived/vrrp/vrrp_ipset.c](#keepalivedvrrpvrrp_ipsetc)
 - [keepalived/vrrp/vrrp_iptables_calls.c](#keepalivedvrrpvrrp_iptables_callsc)
 - [keepalived/core/libnl_link.c](#keepalivedcorelibnl_linkc)

### keepalived/vrrp/vrrp_ipset.c

```c

{% raw %}
282 | 
283 | #ifdef _LIBIPSET_DYNAMIC_
284 | 	/* Attempt to open the ipset library */
285 | 	if (!(libipset_handle = dlopen("libipset.so", RTLD_NOW)) &&
286 | 	    !(libipset_handle = dlopen(IPSET_LIB_NAME, RTLD_NOW))) {
287 | 		log_message(LOG_INFO, "Unable to load ipset library - %s", dlerror());
288 | 		return false;
{% endraw %}

```
### keepalived/vrrp/vrrp_iptables_calls.c

```c

{% raw %}
413 | 	if (libxtables_handle)
414 | 		return true;
415 | 
416 | 	if (!(libxtables_handle = dlopen("libxtables.so", RTLD_NOW)) &&
417 | 	    !(libxtables_handle = dlopen(XTABLES_LIB_NAME, RTLD_NOW))) {
418 | 		log_message(LOG_INFO, "Unable to load xtables library - %s", dlerror());
419 | 		return false;
885 | {
886 | 	if (!libip4tc_handle && block_ipv4) {
887 | 		/* Attempt to open the ip4tc library */
888 | 		if (!(libip4tc_handle = dlopen("libip4tc.so", RTLD_NOW)) &&
889 | 		    !(libip4tc_handle = dlopen(IP4TC_LIB_NAME, RTLD_NOW))) {
890 | 			log_message(LOG_INFO, "Unable to load ip4tc library - %s", dlerror());
891 | 			using_libip4tc = false;
907 | 
908 | 	if (!libip6tc_handle && block_ipv6) {
909 | 		/* Attempt to open the ip6tc library */
910 | 		if (!(libip6tc_handle = dlopen("libip6tc.so", RTLD_NOW)) &&
911 | 		    !(libip6tc_handle = dlopen(IP6TC_LIB_NAME, RTLD_NOW))) {
912 | 			log_message(LOG_INFO, "Unable to load ip6tc library - %s", dlerror());
913 | 			using_libip6tc = false;
{% endraw %}

```
### keepalived/core/libnl_link.c

```c

{% raw %}
73 | 	/* Attempt to open the necessary libraries */
74 | #ifdef _HAVE_LIBNL1_
75 | #ifdef _WITH_LVS_
76 | 	if (!(libnl_handle = dlopen("libnl.so", RTLD_NOW)) &&
77 | 	    !(libnl_handle = dlopen(NL_LIB_NAME, RTLD_NOW))) {
78 | 		log_message(LOG_INFO, "Unable to load nl library - %s", dlerror());
79 | 		return false;
81 | 	libnl_genl_handle = libnl_handle;
82 | #endif
83 | #else
84 | 	if (!(libnl_handle = dlopen("libnl-3.so", RTLD_NOW)) &&
85 | 	    !(libnl_handle = dlopen(NL3_LIB_NAME, RTLD_NOW))) {
86 | 		log_message(LOG_INFO, "Unable to load nl-3 library - %s", dlerror());
87 | 		return false;
88 | 	}
89 | #ifdef _WITH_LVS_
90 | 	if (!(libnl_genl_handle = dlopen("libnl-genl-3.so", RTLD_NOW)) &&
91 | 	    !(libnl_genl_handle = dlopen(NL3_GENL_LIB_NAME, RTLD_NOW))) {
92 | 		log_message(LOG_INFO, "Unable to load nl-genl-3 library - %s", dlerror());
93 | 		return false;
{% endraw %}

```