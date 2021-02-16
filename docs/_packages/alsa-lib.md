---
name: "alsa-lib"
layout: package
next_package: libpulsar
previous_package: samrai
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
116 | EXPORT_SYMBOL void *INTERNAL(snd_dlopen)(const char *name, int mode, char *errbuf, size_t errbuflen)
118 | void *snd_dlopen(const char *name, int mode, char *errbuf, size_t errbuflen)
130 | 			if (dladdr(snd_dlopen, &dlinfo) > 0)
150 | 			handle = dlopen(filename, mode);
161 | 		handle = dlopen(name, mode);
174 | void *INTERNAL(snd_dlopen_old)(const char *name, int mode)
176 |   return INTERNAL(snd_dlopen)(name, mode, NULL, 0);
180 | use_symbol_version(__snd_dlopen_old, snd_dlopen, ALSA_0.9);
181 | use_default_symbol_version(__snd_dlopen, snd_dlopen, ALSA_1.1.6);
339 | 	dlobj = INTERNAL(snd_dlopen)(lib, RTLD_NOW,
{% endraw %}

```
### src/conf.c

```c

{% raw %}
3718 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
4721 | 		h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```
### src/seq/seq.c

```c

{% raw %}
901 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```
### src/hwdep/hwdep.c

```c

{% raw %}
118 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```
### src/mixer/simple_abst.c

```c

{% raw %}
82 | 	h = INTERNAL(snd_dlopen)(xlib, RTLD_NOW, errbuf, sizeof(errbuf));
129 | 	h = INTERNAL(snd_dlopen)(xlib, RTLD_NOW|RTLD_GLOBAL, errbuf, sizeof(errbuf));
{% endraw %}

```
### src/pcm/pcm_hooks.c

```c

{% raw %}
426 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```
### src/pcm/pcm_meter.c

```c

{% raw %}
672 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```
### src/pcm/pcm_ladspa.c

```c

{% raw %}
1093 | 	handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### src/pcm/ladspa.h

```c

{% raw %}
66 |    linking by dlopen() and family. The file will provide a number of
{% endraw %}

```
### src/timer/timer_query.c

```c

{% raw %}
110 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```
### src/timer/timer.c

```c

{% raw %}
152 | 	h = INTERNAL(snd_dlopen)(lib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```
### include/global.h

```c

{% raw %}
100 | void *snd_dlopen(const char *file, int mode, char *errbuf, size_t errbuflen);
{% endraw %}

```
### include/local.h

```c

{% raw %}
373 | void *INTERNAL(snd_dlopen)(const char *name, int mode, char *errbuf, size_t errbuflen);
{% endraw %}

```
### modules/mixer/simple/sbase.h

```c

{% raw %}
107 | int mixer_simple_basic_dlopen(snd_mixer_class_t *class,
{% endraw %}

```
### modules/mixer/simple/ac97.c

```c

{% raw %}
78 | 	err = mixer_simple_basic_dlopen(class, &ops);
{% endraw %}

```
### modules/mixer/simple/hda.c

```c

{% raw %}
79 | 	err = mixer_simple_basic_dlopen(class, &ops);
{% endraw %}

```
### modules/mixer/simple/sbasedl.c

```c

{% raw %}
37 | int mixer_simple_basic_dlopen(snd_mixer_class_t *class,
65 | 	h = snd_dlopen(xlib, RTLD_NOW, errbuf, sizeof(errbuf));
{% endraw %}

```