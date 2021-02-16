---
name: "openldap"
layout: package
next_package: openmc
previous_package: openfoam-org
languages: ['c']
---
## 2.4.48
9 / 1488 files match, 2 filtered matches.

 - [servers/slapd/module.c](#serversslapdmodulec)
 - [servers/slapd/overlays/ppolicy.c](#serversslapdoverlaysppolicyc)

### servers/slapd/module.c

```c

{% raw %}
182 | 	if ((module->lib = lt_dlopenext(file)) == NULL) {
189 | 		Debug(LDAP_DEBUG_ANY, "lt_dlopenext failed: (%s) %s\n", file_name,
{% endraw %}

```
### servers/slapd/overlays/ppolicy.c

```c

{% raw %}
684 | 		if ((mod = lt_dlopen( pp->pwdCheckModule )) == NULL) {
688 | 			"check_password_quality: lt_dlopen failed: (%s) %s.\n",
{% endraw %}

```