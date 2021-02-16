---
name: "slurm"
layout: package
next_package: libestr
previous_package: libsamplerate
languages: ['c']
---
## 18-08-9-1
52 / 2484 files match, 14 filtered matches.

 - [src/common/xlua.c](#srccommonxluac)
 - [src/common/xlua.h](#srccommonxluah)
 - [src/common/plugin.c](#srccommonpluginc)
 - [src/common/plugstack.c](#srccommonplugstackc)
 - [src/plugins/job_submit/lua/job_submit_lua.c](#srcpluginsjob_submitluajob_submit_luac)
 - [src/plugins/switch/nrt/nrt.c](#srcpluginsswitchnrtnrtc)
 - [src/plugins/switch/nrt/libpermapi/shr_64.c](#srcpluginsswitchnrtlibpermapishr_64c)
 - [src/plugins/mpi/pmi2/setup.c](#srcpluginsmpipmi2setupc)
 - [src/plugins/mpi/pmix/mpi_pmix.c](#srcpluginsmpipmixmpi_pmixc)
 - [src/plugins/mpi/pmix/pmixp_dconn_ucx.c](#srcpluginsmpipmixpmixp_dconn_ucxc)
 - [src/plugins/proctrack/sgi_job/proctrack_sgi_job.c](#srcpluginsproctracksgi_jobproctrack_sgi_jobc)
 - [src/plugins/proctrack/lua/proctrack_lua.c](#srcpluginsproctrackluaproctrack_luac)
 - [contribs/pam_slurm_adopt/helper.c](#contribspam_slurm_adopthelperc)
 - [contribs/pam/pam_slurm.c](#contribspampam_slurmc)

### src/common/xlua.c

```c

{% raw %}
47 | int xlua_dlopen(void)
56 | 	} else if (!dlopen("liblua.so",       RTLD_NOW | RTLD_GLOBAL) &&
58 | 		   !dlopen("liblua-5.3.so",   RTLD_NOW | RTLD_GLOBAL) &&
59 | 		   !dlopen("liblua5.3.so",    RTLD_NOW | RTLD_GLOBAL) &&
60 | 		   !dlopen("liblua5.3.so.0",  RTLD_NOW | RTLD_GLOBAL) &&
61 | 		   !dlopen("liblua.so.5.3",   RTLD_NOW | RTLD_GLOBAL)
63 | 		   !dlopen("liblua-5.2.so",   RTLD_NOW | RTLD_GLOBAL) &&
64 | 		   !dlopen("liblua5.2.so",    RTLD_NOW | RTLD_GLOBAL) &&
65 | 		   !dlopen("liblua5.2.so.0",  RTLD_NOW | RTLD_GLOBAL) &&
66 | 		   !dlopen("liblua.so.5.2",   RTLD_NOW | RTLD_GLOBAL)
68 | 		   !dlopen("liblua-5.1.so",   RTLD_NOW | RTLD_GLOBAL) &&
69 | 		   !dlopen("liblua5.1.so",    RTLD_NOW | RTLD_GLOBAL) &&
70 | 		   !dlopen("liblua5.1.so.0",  RTLD_NOW | RTLD_GLOBAL) &&
71 | 		   !dlopen("liblua.so.5.1",   RTLD_NOW | RTLD_GLOBAL)
{% endraw %}

```
### src/common/xlua.h

```c

{% raw %}
46 | int xlua_dlopen();
{% endraw %}

```
### src/common/plugin.c

```c

{% raw %}
111 | 	plug = dlopen( fq_path, RTLD_LAZY );
113 | 		debug3( "plugin_peek: dlopen(%s): %s", fq_path, _dlerror() );
176 | 	plug = dlopen(fq_path, RTLD_LAZY);
178 | 		error("plugin_load_from_file: dlopen(%s): %s",
{% endraw %}

```
### src/common/plugstack.c

```c

{% raw %}
2315 | 	void *h = dlopen(NULL, 0);
2332 | 	void *h = dlopen(NULL, 0);
2349 | 	void *h = dlopen(NULL, 0);
{% endraw %}

```
### src/plugins/job_submit/lua/job_submit_lua.c

```c

{% raw %}
1746 | 	if ((rc = xlua_dlopen()) != SLURM_SUCCESS)
{% endraw %}

```
### src/plugins/switch/nrt/nrt.c

```c

{% raw %}
91 | 		nrt_handle = dlopen(LIBNRT_SO, RTLD_LAZY);
{% endraw %}

```
### src/plugins/switch/nrt/libpermapi/shr_64.c

```c

{% raw %}
1509 | 	my_handle = dlopen(MYSELF_SO, RTLD_LAZY | RTLD_GLOBAL | RTLD_DEEPBIND);
{% endraw %}

```
### src/plugins/mpi/pmi2/setup.c

```c

{% raw %}
619 | 	handle = dlopen(NULL, RTLD_LAZY);
621 | 		error("mpi/pmi2: failed to dlopen()");
{% endraw %}

```
### src/plugins/mpi/pmix/mpi_pmix.c

```c

{% raw %}
108 | 	lib_plug = dlopen(full_path, RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### src/plugins/mpi/pmix/pmixp_dconn_ucx.c

```c

{% raw %}
170 | 	_ucx_lib_handler = dlopen(full_path, RTLD_LAZY | RTLD_GLOBAL);
180 | 	_ucx_lib_handler = dlopen("libucp.so", RTLD_LAZY | RTLD_GLOBAL);
{% endraw %}

```
### src/plugins/proctrack/sgi_job/proctrack_sgi_job.c

```c

{% raw %}
102 | 	if ((libjob_handle = dlopen ("libjob.so", RTLD_LAZY)) == NULL) {
{% endraw %}

```
### src/plugins/proctrack/lua/proctrack_lua.c

```c

{% raw %}
257 | 	if ((rc = xlua_dlopen()) != SLURM_SUCCESS)
{% endraw %}

```
### contribs/pam_slurm_adopt/helper.c

```c

{% raw %}
167 | 	} else if ((slurm_h = dlopen(libslurmname, RTLD_NOW|RTLD_GLOBAL))) {
170 | 		_log_msg (LOG_INFO, "Unable to dlopen %s: %s\n",
177 | 	} else if ((slurm_h = dlopen(libslurmname, RTLD_NOW|RTLD_GLOBAL))) {
180 | 		_log_msg (LOG_INFO, "Unable to dlopen %s: %s\n",
184 | 	if (!(slurm_h = dlopen("libslurm.so", RTLD_NOW|RTLD_GLOBAL))) {
185 | 		_log_msg (LOG_ERR, "Unable to dlopen libslurm.so: %s\n",
{% endraw %}

```
### contribs/pam/pam_slurm.c

```c

{% raw %}
438 | 	} else if ((slurm_h = dlopen(libslurmname, RTLD_NOW|RTLD_GLOBAL))) {
441 | 		_log_msg (LOG_INFO, "Unable to dlopen %s: %s\n",
448 | 	} else if ((slurm_h = dlopen(libslurmname, RTLD_NOW|RTLD_GLOBAL))) {
451 | 		_log_msg (LOG_INFO, "Unable to dlopen %s: %s\n",
455 | 	if (!(slurm_h = dlopen("libslurm.so", RTLD_NOW|RTLD_GLOBAL))) {
456 | 		_log_msg (LOG_ERR, "Unable to dlopen libslurm.so: %s\n",
{% endraw %}

```