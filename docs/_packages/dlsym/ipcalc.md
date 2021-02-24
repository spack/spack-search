---
name: "ipcalc"
layout: package
next_package: nicstat
previous_package: eztrace
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 0.2.3
1 / 30 files match, 1 filtered matches.

 - [ipcalc-geoip.c](#ipcalc-geoipc)

### ipcalc-geoip.c

```c

{% raw %}
80 | 		goto exit;
81 | 	}
82 | 
83 | 	p_GeoIP_setup_dbfilename = dlsym(ld, "_GeoIP_setup_dbfilename");
84 | 
85 | 	pGeoIP_open_type = dlsym(ld, "GeoIP_open_type");
86 | 	pGeoIP_country_name_by_id = dlsym(ld, "GeoIP_country_name_by_id");
87 | 	pGeoIP_delete = dlsym(ld, "GeoIP_delete");
88 | 	pGeoIP_record_by_ipnum = dlsym(ld, "GeoIP_record_by_ipnum");
89 | 	pGeoIP_id_by_ipnum = dlsym(ld, "GeoIP_id_by_ipnum");
90 | 	pGeoIP_id_by_ipnum_v6 = dlsym(ld, "GeoIP_id_by_ipnum_v6");
91 | 	pGeoIP_record_by_ipnum_v6 = dlsym(ld, "GeoIP_record_by_ipnum_v6");
92 | 	pGeoIP_code_by_id = dlsym(ld, "GeoIP_code_by_id");
93 | 
94 | 	if (pGeoIP_open_type == NULL || pGeoIP_country_name_by_id == NULL ||
{% endraw %}

```