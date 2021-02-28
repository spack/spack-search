---
name: "alsa-lib"
layout: package
next_package: sqlite
previous_package: watch
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.2.3.2
23 / 388 files match, 12 filtered matches.

 - [src/dlmisc.c](#srcdlmiscc)
 - [src/conf.c](#srcconfc)
 - [src/seq/seq.c](#srcseqseqc)
 - [src/hwdep/hwdep.c](#srchwdephwdepc)
 - [src/mixer/simple_abst.c](#srcmixersimple_abstc)
 - [src/pcm/pcm_hooks.c](#srcpcmpcm_hooksc)
 - [src/pcm/pcm_meter.c](#srcpcmpcm_meterc)
 - [src/pcm/pcm_ladspa.c](#srcpcmpcm_ladspac)
 - [src/timer/timer_query.c](#srctimertimer_queryc)
 - [src/timer/timer.c](#srctimertimerc)
 - [include/global.h](#includeglobalh)
 - [modules/mixer/simple/sbasedl.c](#modulesmixersimplesbasedlc)

### src/dlmisc.c

```c

{% raw %}
39 | 
40 | #ifndef DOC_HIDDEN
41 | #ifndef PIC
42 | struct snd_dlsym_link *snd_dlsym_start = NULL;
43 | #endif
44 | #ifdef DL_ORIGIN_AVAILABLE
120 | {
121 | #ifndef PIC
122 | 	if (name == NULL)
123 | 		return &snd_dlsym_start;
124 | #else
125 | #ifdef HAVE_LIBDL
191 | int snd_dlclose(void *handle)
192 | {
193 | #ifndef PIC
194 | 	if (handle == &snd_dlsym_start)
195 | 		return 0;
196 | #endif
211 |  * This function checks that the symbol with the version appended to its name
212 |  * does exist in the library.
213 |  */
214 | static int snd_dlsym_verify(void *handle, const char *name, const char *version)
215 | {
216 | #ifdef HAVE_LIBDL
225 | 	vname[0] = '_';
226 | 	strcpy(vname + 1, name);
227 | 	strcat(vname, version);
228 | 	res = dlsym(handle, vname) == NULL ? -ENOENT : 0;
229 | 	// printf("dlsym verify: %i, vname = '%s'\n", res, vname);
230 | 	if (res < 0)
248 |  * of the symbol. A versioned symbol should be defined using the
249 |  * #SND_DLSYM_BUILD_VERSION macro.
250 |  */
251 | void *snd_dlsym(void *handle, const char *name, const char *version)
252 | {
253 | 	int err;
254 | 
255 | #ifndef PIC
256 | 	if (handle == &snd_dlsym_start) {
257 | 		/* it's the funny part: */
258 | 		/* we are looking for a symbol in a static library */
259 | 		struct snd_dlsym_link *link = snd_dlsym_start;
260 | 		while (link) {
261 | 			if (!strcmp(name, link->dlsym_name))
262 | 				return (void *)link->dlsym_ptr;
263 | 			link = link->next;
264 | 		}
268 | #ifdef HAVE_LIBDL
269 | #ifdef VERSIONED_SYMBOLS
270 | 	if (version) {
271 | 		err = snd_dlsym_verify(handle, name, version);
272 | 		if (err < 0)
273 | 			return NULL;
274 | 	}
275 | #endif
276 | 	return dlsym(handle, name);
277 | #else
278 | 	return NULL;
347 | 		return NULL;
348 | 	}
349 | 
350 | 	func = snd_dlsym(dlobj, name, version);
351 | 	if (func == NULL) {
352 | 		if (verbose)
{% endraw %}

```
### src/conf.c

```c

{% raw %}
3716 | 		func_name = buf;
3717 | 	}
3718 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
3719 | 	func = h ? snd_dlsym(h, func_name, SND_DLSYM_VERSION(SND_CONFIG_DLSYM_VERSION_HOOK)) : NULL;
3720 | 	err = 0;
3721 | 	if (!h) {
4720 | 		}
4721 | 		h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
4722 | 		if (h)
4723 | 			func = snd_dlsym(h, func_name, SND_DLSYM_VERSION(SND_CONFIG_DLSYM_VERSION_EVALUATE));
4724 | 		err = 0;
4725 | 		if (!h) {
{% endraw %}

```
### src/seq/seq.c

```c

{% raw %}
900 | #endif
901 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
902 | 	if (h)
903 | 		open_func = snd_dlsym(h, open_name, SND_DLSYM_VERSION(SND_SEQ_DLSYM_VERSION));
904 | 	err = 0;
905 | 	if (!h) {
{% endraw %}

```
### src/hwdep/hwdep.c

```c

{% raw %}
117 | #endif
118 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
119 | 	if (h)
120 | 		open_func = snd_dlsym(h, open_name, SND_DLSYM_VERSION(SND_HWDEP_DLSYM_VERSION));
121 | 	err = 0;
122 | 	if (!h) {
{% endraw %}

```
### src/mixer/simple_abst.c

```c

{% raw %}
86 | 		return -ENXIO;
87 | 	}
88 | 	priv->dlhandle = h;
89 | 	event_func = snd_dlsym(h, "alsa_mixer_simple_event", NULL);
90 | 	if (event_func == NULL) {
91 | 		SNDERR("Symbol 'alsa_mixer_simple_event' was not found in '%s'", xlib);
92 | 		err = -ENXIO;
93 | 	}
94 | 	if (err == 0) {
95 | 		init_func = snd_dlsym(h, "alsa_mixer_simple_init", NULL);
96 | 		if (init_func == NULL) {
97 | 			SNDERR("Symbol 'alsa_mixer_simple_init' was not found in '%s'", xlib);
133 | 		return -ENXIO;
134 | 	}
135 | 	priv->dlhandle = h;
136 | 	event_func = snd_dlsym(h, "alsa_mixer_simple_event", NULL);
137 | 	if (event_func == NULL) {
138 | 		SNDERR("Symbol 'alsa_mixer_simple_event' was not found in '%s'", xlib);
139 | 		err = -ENXIO;
140 | 	}
141 | 	if (err == 0) {
142 | 		init_func = snd_dlsym(h, "alsa_mixer_simple_finit", NULL);
143 | 		if (init_func == NULL) {
144 | 			SNDERR("Symbol 'alsa_mixer_simple_finit' was not found in '%s'", xlib);
{% endraw %}

```
### src/pcm/pcm_hooks.c

```c

{% raw %}
424 | 		snprintf(buf, sizeof(buf), "_snd_pcm_hook_%s_install", str);
425 | 	}
426 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
427 | 	install_func = h ? snd_dlsym(h, install, SND_DLSYM_VERSION(SND_PCM_DLSYM_VERSION)) : NULL;
428 | 	err = 0;
429 | 	if (!h) {
{% endraw %}

```
### src/pcm/pcm_meter.c

```c

{% raw %}
670 | 		snprintf(buf, sizeof(buf), "_snd_pcm_scope_%s_open", str);
671 | 	}
672 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
673 | 	open_func = h ? dlsym(h, open_name) : NULL;
674 | 	err = 0;
675 | 	if (!h) {
{% endraw %}

```
### src/pcm/pcm_ladspa.c

```c

{% raw %}
1092 | 	assert(filename);
1093 | 	handle = dlopen(filename, RTLD_LAZY);
1094 | 	if (handle) {
1095 | 		LADSPA_Descriptor_Function fcn = (LADSPA_Descriptor_Function)dlsym(handle, "ladspa_descriptor");
1096 | 		if (fcn) {
1097 | 			long idx;
{% endraw %}

```
### src/timer/timer_query.c

```c

{% raw %}
109 | #endif
110 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
111 | 	if (h)
112 | 		open_func = snd_dlsym(h, open_name, SND_DLSYM_VERSION(SND_TIMER_QUERY_DLSYM_VERSION));
113 | 	err = 0;
114 | 	if (!h) {
{% endraw %}

```
### src/timer/timer.c

```c

{% raw %}
151 | #endif
152 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
153 | 	if (h)
154 | 		open_func = snd_dlsym(h, open_name, SND_DLSYM_VERSION(SND_TIMER_DLSYM_VERSION));
155 | 	err = 0;
156 | 	if (!h) {
{% endraw %}

```
### include/global.h

```c

{% raw %}
62 | 
63 | #else /* static build */
64 | 
65 | struct snd_dlsym_link {
66 | 	struct snd_dlsym_link *next;
67 | 	const char *dlsym_name;
68 | 	const void *dlsym_ptr;
69 | };
70 | 
71 | extern struct snd_dlsym_link *snd_dlsym_start;
72 | 
73 | /** \hideinitializer \brief Helper macro for #SND_DLSYM_BUILD_VERSION. */
77 |  * \brief Appends the build version to the name of a versioned dynamic symbol.
78 |  */
79 | #define SND_DLSYM_BUILD_VERSION(name, version) \
80 |   static struct snd_dlsym_link __SND_DLSYM_VERSION(snd_dlsym_, name, version); \
81 |   void __SND_DLSYM_VERSION(snd_dlsym_constructor_, name, version) (void) __attribute__ ((constructor)); \
82 |   void __SND_DLSYM_VERSION(snd_dlsym_constructor_, name, version) (void) { \
83 |     __SND_DLSYM_VERSION(snd_dlsym_, name, version).next = snd_dlsym_start; \
84 |     __SND_DLSYM_VERSION(snd_dlsym_, name, version).dlsym_name = # name; \
85 |     __SND_DLSYM_VERSION(snd_dlsym_, name, version).dlsym_ptr = (void *)&name; \
86 |     snd_dlsym_start = &__SND_DLSYM_VERSION(snd_dlsym_, name, version); \
87 |   }
88 | 
98 | 
99 | int snd_dlpath(char *path, size_t path_len, const char *name);
100 | void *snd_dlopen(const char *file, int mode, char *errbuf, size_t errbuflen);
101 | void *snd_dlsym(void *handle, const char *name, const char *version);
102 | int snd_dlclose(void *handle);
103 | 
{% endraw %}

```
### modules/mixer/simple/sbasedl.c

```c

{% raw %}
67 | 		SNDERR("Unable to open library '%s': %s", xlib, errbuf);
68 | 		goto __error;
69 | 	}
70 | 	initpriv = dlsym(h, "alsa_mixer_sbasic_initpriv");
71 | 	if (initpriv == NULL) {
72 | 		SNDERR("Symbol 'alsa_mixer_sbasic_initpriv' was not found in '%s'", xlib);
73 | 		goto __error;
74 | 	}
75 | 	priv->ops.event = dlsym(h, "alsa_mixer_sbasic_event");
76 | 	if (priv->ops.event == NULL) {
77 | 		SNDERR("Symbol 'alsa_mixer_sbasic_event' was not found in '%s'", xlib);
78 | 		goto __error;
79 | 	}
80 | 	priv->ops.selreg = dlsym(h, "alsa_mixer_sbasic_selreg");
81 | 	if (priv->ops.selreg == NULL) {
82 | 		SNDERR("Symbol 'alsa_mixer_sbasic_selreg' was not found in '%s'", xlib);
83 | 		goto __error;
84 | 	}
85 | 	priv->ops.sidreg = dlsym(h, "alsa_mixer_sbasic_sidreg");
86 | 	if (priv->ops.sidreg == NULL) {
87 | 		SNDERR("Symbol 'alsa_mixer_sbasic_sidreg' was not found in '%s'", xlib);
{% endraw %}

```