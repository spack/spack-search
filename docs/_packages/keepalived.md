---
name: "keepalived"
layout: package
next_package: kitty
previous_package: kaldi
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
285 | 	if (!(libipset_handle = dlopen("libipset.so", RTLD_NOW)) &&
286 | 	    !(libipset_handle = dlopen(IPSET_LIB_NAME, RTLD_NOW))) {
{% endraw %}

```
### keepalived/vrrp/vrrp_iptables_calls.c

```c

{% raw %}
416 | 	if (!(libxtables_handle = dlopen("libxtables.so", RTLD_NOW)) &&
417 | 	    !(libxtables_handle = dlopen(XTABLES_LIB_NAME, RTLD_NOW))) {
888 | 		if (!(libip4tc_handle = dlopen("libip4tc.so", RTLD_NOW)) &&
889 | 		    !(libip4tc_handle = dlopen(IP4TC_LIB_NAME, RTLD_NOW))) {
910 | 		if (!(libip6tc_handle = dlopen("libip6tc.so", RTLD_NOW)) &&
911 | 		    !(libip6tc_handle = dlopen(IP6TC_LIB_NAME, RTLD_NOW))) {
{% endraw %}

```
### keepalived/core/libnl_link.c

```c

{% raw %}
76 | 	if (!(libnl_handle = dlopen("libnl.so", RTLD_NOW)) &&
77 | 	    !(libnl_handle = dlopen(NL_LIB_NAME, RTLD_NOW))) {
84 | 	if (!(libnl_handle = dlopen("libnl-3.so", RTLD_NOW)) &&
85 | 	    !(libnl_handle = dlopen(NL3_LIB_NAME, RTLD_NOW))) {
90 | 	if (!(libnl_genl_handle = dlopen("libnl-genl-3.so", RTLD_NOW)) &&
91 | 	    !(libnl_genl_handle = dlopen(NL3_GENL_LIB_NAME, RTLD_NOW))) {
{% endraw %}

```