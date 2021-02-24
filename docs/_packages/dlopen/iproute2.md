---
name: "iproute2"
layout: package
next_package: adiak
previous_package: cpuinfo
library_name: dlopen
matches: ['dlsym', 'dlopen']
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
62 | 			return f;
63 | 
64 | 	snprintf(buf, sizeof(buf), "%s.so", str);
65 | 	dlh = dlopen(buf, RTLD_LAZY);
66 | 	if (dlh == NULL) {
67 | 		dlh = BODY;
68 | 		if (dlh == NULL) {
69 | 			dlh = BODY = dlopen(NULL, RTLD_LAZY);
70 | 			if (dlh == NULL)
71 | 				goto noexist;
{% endraw %}

```
### include/dlfcn.h

```c

{% raw %}
11 | #define RTLD_GLOBAL 1
12 | #define _FAKE_DLFCN_HDL (void *)0xbeefcafe
13 | 
14 | static inline void *dlopen(const char *file, int flag)
15 | {
16 | 	if (file == NULL)
{% endraw %}

```
### ip/iplink.c

```c

{% raw %}
142 | 	return -1;
143 | }
144 | 
145 | static void *BODY;		/* cached dlopen(NULL) handle */
146 | static struct link_util *linkutil_list;
147 | 
156 | 			return l;
157 | 
158 | 	snprintf(buf, sizeof(buf), LIBDIR "/ip/link_%s.so", id);
159 | 	dlh = dlopen(buf, RTLD_LAZY);
160 | 	if (dlh == NULL) {
161 | 		/* look in current binary, only open once */
162 | 		dlh = BODY;
163 | 		if (dlh == NULL) {
164 | 			dlh = BODY = dlopen(NULL, RTLD_LAZY);
165 | 			if (dlh == NULL)
166 | 				return NULL;
{% endraw %}

```
### tc/m_ipt.c

```c

{% raw %}
190 | 
191 | 	/* try libxt_xx first */
192 | 	sprintf(path, "%s/libxt_%s.so", lib_dir, new_name);
193 | 	handle = dlopen(path, RTLD_LAZY);
194 | 	if (!handle) {
195 | 		/* try libipt_xx next */
196 | 		sprintf(path, "%s/libipt_%s.so", lib_dir, new_name);
197 | 		handle = dlopen(path, RTLD_LAZY);
198 | 
199 | 		if (!handle) {
200 | 			sprintf(path, "%s/libxt_%s.so", lib_dir, lname);
201 | 			handle = dlopen(path, RTLD_LAZY);
202 | 		}
203 | 
204 | 		if (!handle) {
205 | 			sprintf(path, "%s/libipt_%s.so", lib_dir, lname);
206 | 			handle = dlopen(path, RTLD_LAZY);
207 | 		}
208 | 		/* ok, lets give up .. */
{% endraw %}

```
### tc/tc.c

```c

{% raw %}
48 | 
49 | struct rtnl_handle rth;
50 | 
51 | static void *BODY;	/* cached handle dlopen(NULL) */
52 | static struct qdisc_util *qdisc_list;
53 | static struct filter_util *filter_list;
117 | 			return q;
118 | 
119 | 	snprintf(buf, sizeof(buf), "%s/q_%s.so", get_tc_lib(), str);
120 | 	dlh = dlopen(buf, RTLD_LAZY);
121 | 	if (!dlh) {
122 | 		/* look in current binary, only open once */
123 | 		dlh = BODY;
124 | 		if (dlh == NULL) {
125 | 			dlh = BODY = dlopen(NULL, RTLD_LAZY);
126 | 			if (dlh == NULL)
127 | 				goto noexist;
161 | 			return q;
162 | 
163 | 	snprintf(buf, sizeof(buf), "%s/f_%s.so", get_tc_lib(), str);
164 | 	dlh = dlopen(buf, RTLD_LAZY);
165 | 	if (dlh == NULL) {
166 | 		dlh = BODY;
167 | 		if (dlh == NULL) {
168 | 			dlh = BODY = dlopen(NULL, RTLD_LAZY);
169 | 			if (dlh == NULL)
170 | 				goto noexist;
{% endraw %}

```
### tc/m_action.c

```c

{% raw %}
101 | 	}
102 | 
103 | 	snprintf(buf, sizeof(buf), "%s/m_%s.so", get_tc_lib(), str);
104 | 	dlh = dlopen(buf, RTLD_LAZY | RTLD_GLOBAL);
105 | 	if (dlh == NULL) {
106 | 		dlh = aBODY;
107 | 		if (dlh == NULL) {
108 | 			dlh = aBODY = dlopen(NULL, RTLD_LAZY);
109 | 			if (dlh == NULL)
110 | 				goto noexist;
{% endraw %}

```
### tc/m_ematch.c

```c

{% raw %}
139 | 	}
140 | 
141 | 	snprintf(buf, sizeof(buf), "em_%s.so", kind);
142 | 	dlh = dlopen(buf, RTLD_LAZY);
143 | 	if (dlh == NULL) {
144 | 		dlh = body;
145 | 		if (dlh == NULL) {
146 | 			dlh = body = dlopen(NULL, RTLD_LAZY);
147 | 			if (dlh == NULL)
148 | 				return NULL;
{% endraw %}

```
### tc/tc_exec.c

```c

{% raw %}
51 | 			return eu;
52 | 
53 | 	snprintf(buf, sizeof(buf), "%s/e_%s.so", get_tc_lib(), name);
54 | 	dlh = dlopen(buf, RTLD_LAZY);
55 | 	if (dlh == NULL) {
56 | 		dlh = BODY;
57 | 		if (dlh == NULL) {
58 | 			dlh = BODY = dlopen(NULL, RTLD_LAZY);
59 | 			if (dlh == NULL)
60 | 				goto noexist;
{% endraw %}

```
### tc/m_pedit.c

```c

{% raw %}
87 | 	}
88 | 
89 | 	snprintf(buf, sizeof(buf), "p_%s.so", str);
90 | 	dlh = dlopen(buf, RTLD_LAZY);
91 | 	if (dlh == NULL) {
92 | 		dlh = pBODY;
93 | 		if (dlh == NULL) {
94 | 			dlh = pBODY = dlopen(NULL, RTLD_LAZY);
95 | 			if (dlh == NULL)
96 | 				goto noexist;
{% endraw %}

```