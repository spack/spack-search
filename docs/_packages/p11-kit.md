---
name: "p11-kit"
layout: package
next_package: pandaseq
previous_package: osqp
languages: ['c']
---
## 0.23.20
9 / 446 files match, 3 filtered matches.

 - [common/compat.h](#commoncompath)
 - [p11-kit/modules.c](#p11-kitmodulesc)
 - [trust/frob-multi-init.c](#trustfrob-multi-initc)

### common/compat.h

```c

{% raw %}
236 | 	(dlopen ((f), RTLD_LOCAL | RTLD_NOW))
{% endraw %}

```
### p11-kit/modules.c

```c

{% raw %}
349 | dlopen_and_get_function_list (Module *mod,
428 | 	rv = dlopen_and_get_function_list (mod, path, &funcs);
{% endraw %}

```
### trust/frob-multi-init.c

```c

{% raw %}
26 | 	dl = dlopen (TRUST_SO, RTLD_LOCAL | RTLD_NOW);
{% endraw %}

```