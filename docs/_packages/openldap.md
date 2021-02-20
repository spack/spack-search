---
name: "openldap"
layout: package
next_package: openloops
previous_package: openfst
languages: ['c']
---
## 2.4.48
9 / 1488 files match, 2 filtered matches.

 - [servers/slapd/module.c](#serversslapdmodulec)
 - [servers/slapd/overlays/ppolicy.c](#serversslapdoverlaysppolicyc)

### servers/slapd/module.c

```c

{% raw %}
179 | 	 * to calling Debug. This is because Debug is a macro that expands
180 | 	 * into multiple function calls.
181 | 	 */
182 | 	if ((module->lib = lt_dlopenext(file)) == NULL) {
183 | 		error = lt_dlerror();
184 | #ifdef HAVE_EBCDIC
186 | 		__etoa( ebuf );
187 | 		error = ebuf;
188 | #endif
189 | 		Debug(LDAP_DEBUG_ANY, "lt_dlopenext failed: (%s) %s\n", file_name,
190 | 			error, 0);
191 | 
{% endraw %}

```
### servers/slapd/overlays/ppolicy.c

```c

{% raw %}
681 | 		lt_dlhandle mod;
682 | 		const char *err;
683 | 		
684 | 		if ((mod = lt_dlopen( pp->pwdCheckModule )) == NULL) {
685 | 			err = lt_dlerror();
686 | 
687 | 			Debug(LDAP_DEBUG_ANY,
688 | 			"check_password_quality: lt_dlopen failed: (%s) %s.\n",
689 | 				pp->pwdCheckModule, err, 0 );
690 | 			ok = LDAP_OTHER; /* internal error */
{% endraw %}

```