---
name: "alsa-lib"
layout: package
next_package: amgx
previous_package: ace
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.2.3.2
22 / 388 files match, 17 filtered matches.

 - [src/dlmisc.c](#srcdlmiscc)
 - [src/conf.c](#srcconfc)
 - [src/seq/seq.c](#srcseqseqc)
 - [src/hwdep/hwdep.c](#srchwdephwdepc)
 - [src/mixer/simple_abst.c](#srcmixersimple_abstc)
 - [src/pcm/pcm_hooks.c](#srcpcmpcm_hooksc)
 - [src/pcm/pcm_meter.c](#srcpcmpcm_meterc)
 - [src/pcm/pcm_ladspa.c](#srcpcmpcm_ladspac)
 - [src/pcm/ladspa.h](#srcpcmladspah)
 - [src/timer/timer_query.c](#srctimertimer_queryc)
 - [src/timer/timer.c](#srctimertimerc)
 - [include/global.h](#includeglobalh)
 - [include/local.h](#includelocalh)
 - [modules/mixer/simple/sbase.h](#modulesmixersimplesbaseh)
 - [modules/mixer/simple/ac97.c](#modulesmixersimpleac97c)
 - [modules/mixer/simple/hda.c](#modulesmixersimplehdac)
 - [modules/mixer/simple/sbasedl.c](#modulesmixersimplesbasedlc)

### src/dlmisc.c

```c

{% raw %}
113 |  * the alsa-lib library. In that case, \p name is set to \c NULL.
114 |  */
115 | #ifndef DOXYGEN
116 | EXPORT_SYMBOL void *INTERNAL(snd_dlopen)(const char *name, int mode, char *errbuf, size_t errbuflen)
117 | #else
118 | void *snd_dlopen(const char *name, int mode, char *errbuf, size_t errbuflen)
119 | #endif
120 | {
127 | 		static const char * self = NULL;
128 | 		if (self == NULL) {
129 | 			Dl_info dlinfo;
130 | 			if (dladdr(snd_dlopen, &dlinfo) > 0)
131 | 				self = dlinfo.dli_fname;
132 | 		}
147 | 	if (name && name[0] != '/') {
148 | 		if (snd_dlpath(path, sizeof(path), name) == 0) {
149 | 			filename = path;
150 | 			handle = dlopen(filename, mode);
151 | 			if (!handle) {
152 | 				/* if the filename exists and cannot be opened */
158 | 	}
159 | 	if (!handle) {
160 | 		filename = name;
161 | 		handle = dlopen(name, mode);
162 | 		if (!handle)
163 | 			goto errpath;
171 | }
172 | 
173 | #ifndef DOXYGEN
174 | void *INTERNAL(snd_dlopen_old)(const char *name, int mode)
175 | {
176 |   return INTERNAL(snd_dlopen)(name, mode, NULL, 0);
177 | }
178 | #endif
179 | 
180 | use_symbol_version(__snd_dlopen_old, snd_dlopen, ALSA_0.9);
181 | use_default_symbol_version(__snd_dlopen, snd_dlopen, ALSA_1.1.6);
182 | 
183 | /**
336 | 	}
337 | 
338 | 	errbuf[0] = '\0';
339 | 	dlobj = INTERNAL(snd_dlopen)(lib, RTLD_NOW,
340 | 	                   verbose ? errbuf : 0,
341 | 	                   verbose ? sizeof(errbuf) : 0);
{% endraw %}

```
### src/conf.c

```c

{% raw %}
3715 | 		buf[len-1] = '\0';
3716 | 		func_name = buf;
3717 | 	}
3718 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
3719 | 	func = h ? snd_dlsym(h, func_name, SND_DLSYM_VERSION(SND_CONFIG_DLSYM_VERSION_HOOK)) : NULL;
3720 | 	err = 0;
4718 | 			buf[len-1] = '\0';
4719 | 			func_name = buf;
4720 | 		}
4721 | 		h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
4722 | 		if (h)
4723 | 			func = snd_dlsym(h, func_name, SND_DLSYM_VERSION(SND_CONFIG_DLSYM_VERSION_EVALUATE));
{% endraw %}

```
### src/seq/seq.c

```c

{% raw %}
898 | #ifndef PIC
899 | 	snd_seq_open_symbols();
900 | #endif
901 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
902 | 	if (h)
903 | 		open_func = snd_dlsym(h, open_name, SND_DLSYM_VERSION(SND_SEQ_DLSYM_VERSION));
{% endraw %}

```
### src/hwdep/hwdep.c

```c

{% raw %}
115 | #ifndef PIC
116 | 	snd_hwdep_open_symbols();
117 | #endif
118 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
119 | 	if (h)
120 | 		open_func = snd_dlsym(h, open_name, SND_DLSYM_VERSION(SND_HWDEP_DLSYM_VERSION));
{% endraw %}

```
### src/mixer/simple_abst.c

```c

{% raw %}
79 | 	strcpy(xlib, path);
80 | 	strcat(xlib, "/");
81 | 	strcat(xlib, lib);
82 | 	h = INTERNAL(snd_dlopen)(xlib, RTLD_NOW, errbuf, sizeof(errbuf));
83 | 	if (h == NULL) {
84 | 		SNDERR("Unable to open library '%s' (%s)", xlib, errbuf);
126 | 	strcat(xlib, "/");
127 | 	strcat(xlib, lib);
128 | 	/* note python modules requires RTLD_GLOBAL */
129 | 	h = INTERNAL(snd_dlopen)(xlib, RTLD_NOW|RTLD_GLOBAL, errbuf, sizeof(errbuf));
130 | 	if (h == NULL) {
131 | 		SNDERR("Unable to open library '%s'", xlib);
{% endraw %}

```
### src/pcm/pcm_hooks.c

```c

{% raw %}
423 | 		install = buf;
424 | 		snprintf(buf, sizeof(buf), "_snd_pcm_hook_%s_install", str);
425 | 	}
426 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
427 | 	install_func = h ? snd_dlsym(h, install, SND_DLSYM_VERSION(SND_PCM_DLSYM_VERSION)) : NULL;
428 | 	err = 0;
{% endraw %}

```
### src/pcm/pcm_meter.c

```c

{% raw %}
669 | 		open_name = buf;
670 | 		snprintf(buf, sizeof(buf), "_snd_pcm_scope_%s_open", str);
671 | 	}
672 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
673 | 	open_func = h ? dlsym(h, open_name) : NULL;
674 | 	err = 0;
{% endraw %}

```
### src/pcm/pcm_ladspa.c

```c

{% raw %}
1090 | 	void *handle;
1091 | 
1092 | 	assert(filename);
1093 | 	handle = dlopen(filename, RTLD_LAZY);
1094 | 	if (handle) {
1095 | 		LADSPA_Descriptor_Function fcn = (LADSPA_Descriptor_Function)dlsym(handle, "ladspa_descriptor");
{% endraw %}

```
### src/pcm/ladspa.h

```c

{% raw %}
63 |    `connect_port()' function below) before it is asked to run.
64 | 
65 |    Plugins will reside in shared object files suitable for dynamic
66 |    linking by dlopen() and family. The file will provide a number of
67 |    `plugin types' that can be used to instantiate actual plugins
68 |    (sometimes known as `plugin instances') that can be connected
{% endraw %}

```
### src/timer/timer_query.c

```c

{% raw %}
107 | #ifndef PIC
108 | 	snd_timer_query_open_symbols();
109 | #endif
110 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
111 | 	if (h)
112 | 		open_func = snd_dlsym(h, open_name, SND_DLSYM_VERSION(SND_TIMER_QUERY_DLSYM_VERSION));
{% endraw %}

```
### src/timer/timer.c

```c

{% raw %}
149 | #ifndef PIC
150 | 	snd_timer_open_symbols();
151 | #endif
152 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
153 | 	if (h)
154 | 		open_func = snd_dlsym(h, open_name, SND_DLSYM_VERSION(SND_TIMER_DLSYM_VERSION));
{% endraw %}

```
### include/global.h

```c

{% raw %}
97 | #define SND_DLSYM_VERSION(version) __STRING(version)
98 | 
99 | int snd_dlpath(char *path, size_t path_len, const char *name);
100 | void *snd_dlopen(const char *file, int mode, char *errbuf, size_t errbuflen);
101 | void *snd_dlsym(void *handle, const char *name, const char *version);
102 | int snd_dlclose(void *handle);
{% endraw %}

```
### include/local.h

```c

{% raw %}
370 | 	(type *)( (char *)__mptr - offsetof(type,member) );})
371 | 
372 | #ifdef INTERNAL
373 | void *INTERNAL(snd_dlopen)(const char *name, int mode, char *errbuf, size_t errbuflen);
374 | #endif
375 | 
{% endraw %}

```
### modules/mixer/simple/sbase.h

```c

{% raw %}
104 | 	bclass_base_ops_t ops;
105 | };
106 | 
107 | int mixer_simple_basic_dlopen(snd_mixer_class_t *class,
108 | 			      bclass_base_ops_t **ops);
109 | 
{% endraw %}

```
### modules/mixer/simple/ac97.c

```c

{% raw %}
75 | 	struct bclass_base_ops *ops;
76 | 	int err;
77 | 	
78 | 	err = mixer_simple_basic_dlopen(class, &ops);
79 | 	if (err < 0)
80 | 		return 0;
{% endraw %}

```
### modules/mixer/simple/hda.c

```c

{% raw %}
76 | 	struct bclass_base_ops *ops;
77 | 	int err;
78 | 	
79 | 	err = mixer_simple_basic_dlopen(class, &ops);
80 | 	if (err < 0)
81 | 		return 0;
{% endraw %}

```
### modules/mixer/simple/sbasedl.c

```c

{% raw %}
34 | 
35 | #define SO_PATH "smixer"
36 | 
37 | int mixer_simple_basic_dlopen(snd_mixer_class_t *class,
38 | 			      bclass_base_ops_t **ops)
39 | {
62 | 	strcpy(xlib, path);
63 | 	strcat(xlib, "/");
64 | 	strcat(xlib, lib);
65 | 	h = snd_dlopen(xlib, RTLD_NOW, errbuf, sizeof(errbuf));
66 | 	if (h == NULL) {
67 | 		SNDERR("Unable to open library '%s': %s", xlib, errbuf);
{% endraw %}

```