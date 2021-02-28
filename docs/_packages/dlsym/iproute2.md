---
name: "iproute2"
layout: package
next_package: xrootd
previous_package: bmi
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 5.8.0
12 / 597 files match, 12 filtered matches.

 - [genl/static-syms.c](#genlstatic-symsc)
 - [genl/genl.c](#genlgenlc)
 - [include/dlfcn.h](#includedlfcnh)
 - [ip/iplink.c](#ipiplinkc)
 - [ip/static-syms.c](#ipstatic-symsc)
 - [tc/m_ipt.c](#tcm_iptc)
 - [tc/tc.c](#tctcc)
 - [tc/m_action.c](#tcm_actionc)
 - [tc/m_ematch.c](#tcm_ematchc)
 - [tc/static-syms.c](#tcstatic-symsc)
 - [tc/tc_exec.c](#tctc_execc)
 - [tc/m_pedit.c](#tcm_peditc)

### genl/static-syms.c

```c

{% raw %}
7 | #include <string.h>
8 | #include "dlfcn.h"
9 | 
10 | void *_dlsym(const char *sym)
11 | {
12 | #include "static-syms.h"
{% endraw %}

```
### genl/genl.c

```c

{% raw %}
74 | 
75 | 	snprintf(buf, sizeof(buf), "%s_genl_util", str);
76 | 
77 | 	f = dlsym(dlh, buf);
78 | 	if (f == NULL)
79 | 		goto noexist;
{% endraw %}

```
### include/dlfcn.h

```c

{% raw %}
19 | 		return NULL;
20 | }
21 | 
22 | void *_dlsym(const char *sym);
23 | static inline void *dlsym(void *handle, const char *sym)
24 | {
25 | 	if (handle != _FAKE_DLFCN_HDL)
26 | 		return NULL;
27 | 	return _dlsym(sym);
28 | }
29 | 
{% endraw %}

```
### ip/iplink.c

```c

{% raw %}
168 | 	}
169 | 
170 | 	snprintf(buf, sizeof(buf), "%s_link_util", id);
171 | 	l = dlsym(dlh, buf);
172 | 	if (l == NULL)
173 | 		return NULL;
{% endraw %}

```
### ip/static-syms.c

```c

{% raw %}
7 | #include <string.h>
8 | #include "dlfcn.h"
9 | 
10 | void *_dlsym(const char *sym)
11 | {
12 | #include "static-syms.h"
{% endraw %}

```
### tc/m_ipt.c

```c

{% raw %}
215 | 		}
216 | 	}
217 | 
218 | 	m = dlsym(handle, new_name);
219 | 	if ((error = dlerror()) != NULL) {
220 | 		m = (struct xtables_target *) dlsym(handle, lname);
221 | 		if ((error = dlerror()) != NULL) {
222 | 			m = find_t(new_name);
{% endraw %}

```
### tc/tc.c

```c

{% raw %}
129 | 	}
130 | 
131 | 	snprintf(buf, sizeof(buf), "%s_qdisc_util", str);
132 | 	q = dlsym(dlh, buf);
133 | 	if (q == NULL)
134 | 		goto noexist;
172 | 	}
173 | 
174 | 	snprintf(buf, sizeof(buf), "%s_filter_util", str);
175 | 	q = dlsym(dlh, buf);
176 | 	if (q == NULL)
177 | 		goto noexist;
{% endraw %}

```
### tc/m_action.c

```c

{% raw %}
112 | 	}
113 | 
114 | 	snprintf(buf, sizeof(buf), "%s_action_util", str);
115 | 	a = dlsym(dlh, buf);
116 | 	if (a == NULL)
117 | 		goto noexist;
{% endraw %}

```
### tc/m_ematch.c

```c

{% raw %}
150 | 	}
151 | 
152 | 	snprintf(buf, sizeof(buf), "%s_ematch_util", kind);
153 | 	e = dlsym(dlh, buf);
154 | 	if (e == NULL)
155 | 		return NULL;
{% endraw %}

```
### tc/static-syms.c

```c

{% raw %}
7 | #include <string.h>
8 | #include "dlfcn.h"
9 | 
10 | void *_dlsym(const char *sym)
11 | {
12 | #include "static-syms.h"
{% endraw %}

```
### tc/tc_exec.c

```c

{% raw %}
62 | 	}
63 | 
64 | 	snprintf(buf, sizeof(buf), "%s_exec_util", name);
65 | 	eu = dlsym(dlh, buf);
66 | 	if (eu == NULL)
67 | 		goto noexist;
{% endraw %}

```
### tc/m_pedit.c

```c

{% raw %}
98 | 	}
99 | 
100 | 	snprintf(buf, sizeof(buf), "p_pedit_%s", str);
101 | 	p = dlsym(dlh, buf);
102 | 	if (p == NULL)
103 | 		goto noexist;
{% endraw %}

```