---
name: "keepalived"
layout: package
next_package: gpgme
previous_package: scorep
library_name: dlsym
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
288 | 		return false;
289 | 	}
290 | 
291 | 	if (!(ipset_session_init_addr = dlsym(libipset_handle, "ipset_session_init")) ||
292 | 	    !(ipset_session_fini_addr = dlsym(libipset_handle, "ipset_session_fini")) ||
293 | 	    !(ipset_session_data_addr = dlsym(libipset_handle,"ipset_session_data")) ||
294 | #ifdef LIBIPSET_PRE_V7_COMPAT
295 | 	    !(ipset_envopt_parse_addr = dlsym(libipset_handle,"ipset_envopt_parse")) ||
296 | #else
297 | 	    !(ipset_envopt_set_addr = dlsym(libipset_handle,"ipset_envopt_set")) ||
298 | #endif
299 | 	    !(ipset_type_get_addr = dlsym(libipset_handle,"ipset_type_get")) ||
300 | 	    !(ipset_data_set_addr = dlsym(libipset_handle,"ipset_data_set")) ||
301 | 	    !(ipset_cmd_addr = dlsym(libipset_handle,"ipset_cmd")) ||
302 | 	    !(ipset_load_types_addr = dlsym(libipset_handle,"ipset_load_types"))) {
303 | 		log_message(LOG_INFO, "Failed to dynamic link an ipset function - %s", dlerror());
304 | 		return false;
{% endraw %}

```
### keepalived/vrrp/vrrp_iptables_calls.c

```c

{% raw %}
419 | 		return false;
420 | 	}
421 | 
422 | 	if (!(xtables_insmod_addr = dlsym(libxtables_handle, "xtables_insmod"))) {
423 | 		log_message(LOG_INFO, "Failed to dynamic link xtables_insmod - %s", dlerror());
424 | 		dlclose(libxtables_handle);
890 | 			log_message(LOG_INFO, "Unable to load ip4tc library - %s", dlerror());
891 | 			using_libip4tc = false;
892 | 		}
893 | 		else if (!(iptc_init_addr = dlsym(libip4tc_handle, "iptc_init")) ||
894 | 			 !(iptc_free_addr = dlsym(libip4tc_handle, "iptc_free")) ||
895 | 			 !(iptc_is_chain_addr = dlsym(libip4tc_handle,"iptc_is_chain")) ||
896 | 			 !(iptc_insert_entry_addr = dlsym(libip4tc_handle,"iptc_insert_entry")) ||
897 | 			 !(iptc_append_entry_addr = dlsym(libip4tc_handle,"iptc_append_entry")) ||
898 | 			 !(iptc_delete_entry_addr = dlsym(libip4tc_handle,"iptc_delete_entry")) ||
899 | 			 !(iptc_commit_addr = dlsym(libip4tc_handle,"iptc_commit")) ||
900 | 			 !(iptc_strerror_addr = dlsym(libip4tc_handle,"iptc_strerror"))) {
901 | 			log_message(LOG_INFO, "Failed to dynamic link an iptc function - %s", dlerror());
902 | 			using_libip4tc = false;
912 | 			log_message(LOG_INFO, "Unable to load ip6tc library - %s", dlerror());
913 | 			using_libip6tc = false;
914 | 		}
915 | 		else if (!(ip6tc_init_addr = dlsym(libip6tc_handle, "ip6tc_init")) ||
916 | 			 !(ip6tc_free_addr = dlsym(libip6tc_handle, "ip6tc_free")) ||
917 | 			 !(ip6tc_is_chain_addr = dlsym(libip6tc_handle,"ip6tc_is_chain")) ||
918 | 			 !(ip6tc_insert_entry_addr = dlsym(libip6tc_handle,"ip6tc_insert_entry")) ||
919 | 			 !(ip6tc_append_entry_addr = dlsym(libip6tc_handle,"ip6tc_append_entry")) ||
920 | 			 !(ip6tc_delete_entry_addr = dlsym(libip6tc_handle,"ip6tc_delete_entry")) ||
921 | 			 !(ip6tc_commit_addr = dlsym(libip6tc_handle,"ip6tc_commit")) ||
922 | 			 !(ip6tc_strerror_addr = dlsym(libip6tc_handle,"ip6tc_strerror"))) {
923 | 			log_message(LOG_INFO, "Failed to dynamic link an ip6tc function - %s", dlerror());
924 | 			using_libip6tc = false;
{% endraw %}

```
### keepalived/core/libnl_link.c

```c

{% raw %}
97 | 
98 | 	if (
99 | #ifdef _HAVE_LIBNL1_
100 | 	    !(nl_socket_alloc_addr = dlsym(libnl_handle, "nl_handle_alloc")) ||
101 | 	    !(nl_socket_free_addr = dlsym(libnl_handle, "nl_handle_destroy")) ||
102 | #else
103 | 	    !(nl_socket_alloc_addr = dlsym(libnl_handle, "nl_socket_alloc")) ||
104 | 	    !(nl_socket_free_addr = dlsym(libnl_handle, "nl_socket_free")) ||
105 | #endif
106 | #ifdef _WITH_LVS_
107 | 	    !(genl_connect_addr = dlsym(libnl_genl_handle, "genl_connect")) ||
108 | 	    !(genl_ctrl_resolve_addr = dlsym(libnl_genl_handle, "genl_ctrl_resolve")) ||
109 | 	    !(genlmsg_parse_addr = dlsym(libnl_genl_handle, "genlmsg_parse")) ||
110 | 	    !(genlmsg_put_addr = dlsym(libnl_genl_handle, "genlmsg_put")) ||
111 | 	    !(nla_nest_end_addr = dlsym(libnl_handle, "nla_nest_end")) ||
112 | 	    !(nla_nest_start_addr = dlsym(libnl_handle, "nla_nest_start")) ||
113 | 	    !(nla_put_daddr = dlsym(libnl_handle, "nla_put")) ||
114 | 	    !(nlmsg_alloc_addr = dlsym(libnl_handle, "nlmsg_alloc")) ||
115 | 	    !(nlmsg_free_addr = dlsym(libnl_handle, "nlmsg_free")) ||
116 | 	    !(nlmsg_hdr_addr = dlsym(libnl_handle, "nlmsg_hdr")) ||
117 | 	    !(nl_recvmsgs_default_addr = dlsym(libnl_handle, "nl_recvmsgs_default")) ||
118 | 	    !(nl_send_auto_complete_addr = dlsym(libnl_handle, "nl_send_auto_complete")) ||
119 | 	    !(nl_socket_modify_cb_addr = dlsym(libnl_handle, "nl_socket_modify_cb")) ||
120 | #ifdef _HAVE_LIBNL3_
121 | 	    !(nla_data_addr = dlsym(libnl_handle, "nla_data")) ||
122 | 	    !(nla_get_s32_addr = dlsym(libnl_handle, "nla_get_s32")) ||
123 | 	    !(nla_get_string_addr = dlsym(libnl_handle, "nla_get_string")) ||
124 | 	    !(nla_get_u16_addr = dlsym(libnl_handle, "nla_get_u16")) ||
125 | 	    !(nla_get_u32_addr = dlsym(libnl_handle, "nla_get_u32")) ||
126 | 	    !(nla_get_u64_addr = dlsym(libnl_handle, "nla_get_u64")) ||
127 | 	    !(nla_memcpy_addr = dlsym(libnl_handle, "nla_memcpy")) ||
128 | 	    !(nla_parse_nested_addr = dlsym(libnl_handle, "nla_parse_nested")) ||
129 | #endif
130 | #endif
{% endraw %}

```