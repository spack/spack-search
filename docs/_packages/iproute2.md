---
name: "iproute2"
layout: package
next_package: isc-dhcp
previous_package: ipopt
languages: ['c']
---
## 5.8.0
9 / 597 files match, 9 filtered matches.

 - [genl/genl.c](#genlgenlc)
 - [include/dlfcn.h](#includedlfcnh)
 - [ip/iplink.c](#ipiplinkc)
 - [tc/m_ipt.c](#tcm_iptc)
 - [tc/tc.c](#tctcc)
 - [tc/m_action.c](#tcm_actionc)
 - [tc/m_ematch.c](#tcm_ematchc)
 - [tc/tc_exec.c](#tctc_execc)
 - [tc/m_pedit.c](#tcm_peditc)

### genl/genl.c

```c

{% raw %}
65 | 	dlh = dlopen(buf, RTLD_LAZY);
69 | 			dlh = BODY = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### include/dlfcn.h

```c

{% raw %}
14 | static inline void *dlopen(const char *file, int flag)
{% endraw %}

```
### ip/iplink.c

```c

{% raw %}
145 | static void *BODY;		/* cached dlopen(NULL) handle */
159 | 	dlh = dlopen(buf, RTLD_LAZY);
164 | 			dlh = BODY = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### tc/m_ipt.c

```c

{% raw %}
193 | 	handle = dlopen(path, RTLD_LAZY);
197 | 		handle = dlopen(path, RTLD_LAZY);
201 | 			handle = dlopen(path, RTLD_LAZY);
206 | 			handle = dlopen(path, RTLD_LAZY);
{% endraw %}

```
### tc/tc.c

```c

{% raw %}
51 | static void *BODY;	/* cached handle dlopen(NULL) */
120 | 	dlh = dlopen(buf, RTLD_LAZY);
125 | 			dlh = BODY = dlopen(NULL, RTLD_LAZY);
164 | 	dlh = dlopen(buf, RTLD_LAZY);
168 | 			dlh = BODY = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### tc/m_action.c

```c

{% raw %}
104 | 	dlh = dlopen(buf, RTLD_LAZY | RTLD_GLOBAL);
108 | 			dlh = aBODY = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### tc/m_ematch.c

```c

{% raw %}
142 | 	dlh = dlopen(buf, RTLD_LAZY);
146 | 			dlh = body = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### tc/tc_exec.c

```c

{% raw %}
54 | 	dlh = dlopen(buf, RTLD_LAZY);
58 | 			dlh = BODY = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### tc/m_pedit.c

```c

{% raw %}
90 | 	dlh = dlopen(buf, RTLD_LAZY);
94 | 			dlh = pBODY = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```