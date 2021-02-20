---
name: "libibumad"
layout: package
next_package: libical
previous_package: libiberty
languages: ['c']
---
## 25.0
5 / 960 files match, 2 filtered matches.

 - [libibverbs/dynamic_driver.c](#libibverbsdynamic_driverc)
 - [ibacm/src/acm.c](#ibacmsrcacmc)

### libibverbs/dynamic_driver.c

```c

{% raw %}
169 | 	if (name[0] == '/') {
170 | 		if (asprintf(&so_name, "%s" VERBS_PROVIDER_SUFFIX, name) < 0)
171 | 			goto out_asprintf;
172 | 		dlhandle = dlopen(so_name, RTLD_NOW);
173 | 		if (!dlhandle)
174 | 			goto out_dlopen;
175 | 		free(so_name);
176 | 		return;
182 | 			     VERBS_PROVIDER_DIR "/lib%s" VERBS_PROVIDER_SUFFIX,
183 | 			     name) < 0)
184 | 			goto out_asprintf;
185 | 		dlhandle = dlopen(so_name, RTLD_NOW);
186 | 		free(so_name);
187 | 		if (dlhandle)
193 | 	 */
194 | 	if (asprintf(&so_name, "lib%s" VERBS_PROVIDER_SUFFIX, name) < 0)
195 | 		goto out_asprintf;
196 | 	dlhandle = dlopen(so_name, RTLD_NOW);
197 | 	if (!dlhandle)
198 | 		goto out_dlopen;
199 | 	free(so_name);
200 | 	return;
202 | out_asprintf:
203 | 	fprintf(stderr, PFX "Warning: couldn't load driver '%s'.\n", name);
204 | 	return;
205 | out_dlopen:
206 | 	fprintf(stderr, PFX "Warning: couldn't load driver '%s': %s\n", so_name,
207 | 		dlerror());
{% endraw %}

```
### ibacm/src/acm.c

```c

{% raw %}
2788 | 			continue;
2789 | 
2790 | 		acm_log(2, "Loading provider %s...\n", file_name);
2791 | 		if (!(handle = dlopen(file_name, RTLD_LAZY))) {
2792 | 			acm_log(0, "Error - could not load provider %s (%s)\n",
2793 | 				file_name, dlerror());
{% endraw %}

```