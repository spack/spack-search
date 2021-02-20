---
name: "slurm"
layout: package
next_package: sollya
previous_package: slang
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
44 |  *  Common function to dlopen() the appropriate Lua libraries, and
45 |  *   ensure the lua version matches what we compiled against.
46 |  */
47 | int xlua_dlopen(void)
48 | {
49 | 	/*
53 | 	 */
54 | 	if (!LUA_VERSION_NUM) {
55 | 		fatal("Slurm wasn't configured against any LUA lib but you are trying to use it like it was.  Please check config.log and reconfigure against liblua.  Make sure you have lua devel installed.");
56 | 	} else if (!dlopen("liblua.so",       RTLD_NOW | RTLD_GLOBAL) &&
57 | #if LUA_VERSION_NUM == 503
58 | 		   !dlopen("liblua-5.3.so",   RTLD_NOW | RTLD_GLOBAL) &&
59 | 		   !dlopen("liblua5.3.so",    RTLD_NOW | RTLD_GLOBAL) &&
60 | 		   !dlopen("liblua5.3.so.0",  RTLD_NOW | RTLD_GLOBAL) &&
61 | 		   !dlopen("liblua.so.5.3",   RTLD_NOW | RTLD_GLOBAL)
62 | #elif LUA_VERSION_NUM == 502
63 | 		   !dlopen("liblua-5.2.so",   RTLD_NOW | RTLD_GLOBAL) &&
64 | 		   !dlopen("liblua5.2.so",    RTLD_NOW | RTLD_GLOBAL) &&
65 | 		   !dlopen("liblua5.2.so.0",  RTLD_NOW | RTLD_GLOBAL) &&
66 | 		   !dlopen("liblua.so.5.2",   RTLD_NOW | RTLD_GLOBAL)
67 | #else
68 | 		   !dlopen("liblua-5.1.so",   RTLD_NOW | RTLD_GLOBAL) &&
69 | 		   !dlopen("liblua5.1.so",    RTLD_NOW | RTLD_GLOBAL) &&
70 | 		   !dlopen("liblua5.1.so.0",  RTLD_NOW | RTLD_GLOBAL) &&
71 | 		   !dlopen("liblua.so.5.1",   RTLD_NOW | RTLD_GLOBAL)
72 | #endif
73 | 		) {
{% endraw %}

```
### src/common/xlua.h

```c

{% raw %}
43 | #include "slurm/slurm_errno.h"
44 | #include "src/common/log.h"
45 | 
46 | int xlua_dlopen();
47 | 
48 | #endif
{% endraw %}

```
### src/common/plugin.c

```c

{% raw %}
108 | 	char *type;
109 | 	uint32_t *version;
110 | 
111 | 	plug = dlopen( fq_path, RTLD_LAZY );
112 | 	if ( plug == NULL ) {
113 | 		debug3( "plugin_peek: dlopen(%s): %s", fq_path, _dlerror() );
114 | 		return SLURM_ERROR;
115 | 	}
173 | 	 * used in the context of srun, not slurmd.)
174 | 	 *
175 | 	 */
176 | 	plug = dlopen(fq_path, RTLD_LAZY);
177 | 	if (plug == NULL) {
178 | 		error("plugin_load_from_file: dlopen(%s): %s",
179 | 		      fq_path,
180 | 		      _dlerror());
{% endraw %}

```
### src/common/plugstack.c

```c

{% raw %}
2312 |  */
2313 | const char *dyn_spank_get_job_env(const char *name)
2314 | {
2315 | 	void *h = dlopen(NULL, 0);
2316 | 	char * (*fn)(const char *n);
2317 | 	char *rc;
2329 | 
2330 | int dyn_spank_set_job_env(const char *n, const char *v, int overwrite)
2331 | {
2332 | 	void *h = dlopen(NULL, 0);
2333 | 	int (*fn)(const char *n, const char *v, int overwrite);
2334 | 	int rc;
2346 | 
2347 | extern int dyn_spank_unset_job_env(const char *n)
2348 | {
2349 | 	void *h = dlopen(NULL, 0);
2350 | 	int (*fn)(const char *n);
2351 | 	int rc;
{% endraw %}

```
### src/plugins/job_submit/lua/job_submit_lua.c

```c

{% raw %}
1743 | 	 * Need to dlopen() the Lua library to ensure plugins see
1744 | 	 * appropriate symptoms
1745 | 	 */
1746 | 	if ((rc = xlua_dlopen()) != SLURM_SUCCESS)
1747 | 		return rc;
1748 | 
{% endraw %}

```
### src/plugins/switch/nrt/nrt.c

```c

{% raw %}
88 | 	if (!nrt_handle) {
89 | 		void **api_pptr = (void **) &nrt_api;
90 | #ifdef LIBNRT_SO
91 | 		nrt_handle = dlopen(LIBNRT_SO, RTLD_LAZY);
92 | #endif
93 | 		if (!nrt_handle)
{% endraw %}

```
### src/plugins/switch/nrt/libpermapi/shr_64.c

```c

{% raw %}
1506 | 	   we just open ourself again with those options and bada bing
1507 | 	   bada boom we are good to go with the symbols we need.
1508 | 	*/
1509 | 	my_handle = dlopen(MYSELF_SO, RTLD_LAZY | RTLD_GLOBAL | RTLD_DEEPBIND);
1510 | 	if (!my_handle) {
1511 | 		debug("%s", dlerror());
{% endraw %}

```
### src/plugins/mpi/pmi2/setup.c

```c

{% raw %}
616 | 
617 | 	/* hjcao: this is really dirty.
618 | 	   But writing a new launcher is not desirable. */
619 | 	handle = dlopen(NULL, RTLD_LAZY);
620 | 	if (handle == NULL) {
621 | 		error("mpi/pmi2: failed to dlopen()");
622 | 		return SLURM_ERROR;
623 | 	}
{% endraw %}

```
### src/plugins/mpi/pmix/mpi_pmix.c

```c

{% raw %}
105 | 	xstrfmtcat(full_path, "%s/", PMIXP_V2_LIBPATH);
106 | #endif
107 | 	xstrfmtcat(full_path, "libpmix.so");
108 | 	lib_plug = dlopen(full_path, RTLD_LAZY | RTLD_GLOBAL);
109 | 	xfree(full_path);
110 | 
{% endraw %}

```
### src/plugins/mpi/pmix/pmixp_dconn_ucx.c

```c

{% raw %}
167 | 	 */
168 | 	char *full_path = NULL;
169 | 	xstrfmtcat(full_path, "%s/libucp.so", PMIXP_UCX_LIBPATH);
170 | 	_ucx_lib_handler = dlopen(full_path, RTLD_LAZY | RTLD_GLOBAL);
171 | 	xfree(full_path);
172 | 	if (_ucx_lib_handler) {
177 | 	 * known by dynamic linker.
178 | 	 */
179 | #endif
180 | 	_ucx_lib_handler = dlopen("libucp.so", RTLD_LAZY | RTLD_GLOBAL);
181 | 	if (!_ucx_lib_handler) {
182 | 		char *err = dlerror();
{% endraw %}

```
### src/plugins/proctrack/sgi_job/proctrack_sgi_job.c

```c

{% raw %}
99 | 	 *   conflict with symbols in slurmd. dlopening the library
100 | 	 *   prevents these symbols from going into the global namespace.
101 | 	 */
102 | 	if ((libjob_handle = dlopen ("libjob.so", RTLD_LAZY)) == NULL) {
103 | 		error ("Unable to open libjob.so: %m");
104 | 		return SLURM_ERROR;
{% endraw %}

```
### src/plugins/proctrack/lua/proctrack_lua.c

```c

{% raw %}
254 | 	 * Need to dlopen() the Lua library to ensure plugins see
255 | 	 * appropriate symptoms
256 | 	 */
257 | 	if ((rc = xlua_dlopen()) != SLURM_SUCCESS)
258 | 		return rc;
259 | 
{% endraw %}

```
### contribs/pam_slurm_adopt/helper.c

```c

{% raw %}
164 | 			SLURM_API_REVISION, SLURM_API_AGE) >=
165 | 			(signed) sizeof(libslurmname) ) {
166 | 		_log_msg (LOG_ERR, "Unable to write libslurmname\n");
167 | 	} else if ((slurm_h = dlopen(libslurmname, RTLD_NOW|RTLD_GLOBAL))) {
168 | 		return;
169 | 	} else {
170 | 		_log_msg (LOG_INFO, "Unable to dlopen %s: %s\n",
171 | 			libslurmname, dlerror ());
172 | 	}
174 | 	if (snprintf(libslurmname, sizeof(libslurmname), "libslurm.so.%d",
175 | 			SLURM_API_CURRENT) >= (signed) sizeof(libslurmname) ) {
176 | 		_log_msg (LOG_ERR, "Unable to write libslurmname\n");
177 | 	} else if ((slurm_h = dlopen(libslurmname, RTLD_NOW|RTLD_GLOBAL))) {
178 | 		return;
179 | 	} else {
180 | 		_log_msg (LOG_INFO, "Unable to dlopen %s: %s\n",
181 | 			libslurmname, dlerror ());
182 | 	}
183 | 
184 | 	if (!(slurm_h = dlopen("libslurm.so", RTLD_NOW|RTLD_GLOBAL))) {
185 | 		_log_msg (LOG_ERR, "Unable to dlopen libslurm.so: %s\n",
186 | 			  dlerror ());
187 | 	}
{% endraw %}

```
### contribs/pam/pam_slurm.c

```c

{% raw %}
435 | 			SLURM_API_REVISION, SLURM_API_AGE) >=
436 | 			sizeof(libslurmname) ) {
437 | 		_log_msg (LOG_ERR, "Unable to write libslurmname\n");
438 | 	} else if ((slurm_h = dlopen(libslurmname, RTLD_NOW|RTLD_GLOBAL))) {
439 | 		return;
440 | 	} else {
441 | 		_log_msg (LOG_INFO, "Unable to dlopen %s: %s\n",
442 | 			libslurmname, dlerror ());
443 | 	}
445 | 	if (snprintf(libslurmname, sizeof(libslurmname), "libslurm.so.%d",
446 | 			SLURM_API_CURRENT) >= sizeof(libslurmname) ) {
447 | 		_log_msg (LOG_ERR, "Unable to write libslurmname\n");
448 | 	} else if ((slurm_h = dlopen(libslurmname, RTLD_NOW|RTLD_GLOBAL))) {
449 | 		return;
450 | 	} else {
451 | 		_log_msg (LOG_INFO, "Unable to dlopen %s: %s\n",
452 | 			libslurmname, dlerror ());
453 | 	}
454 | 
455 | 	if (!(slurm_h = dlopen("libslurm.so", RTLD_NOW|RTLD_GLOBAL))) {
456 | 		_log_msg (LOG_ERR, "Unable to dlopen libslurm.so: %s\n",
457 |  			  dlerror ());
458 | 	}
{% endraw %}

```