---
name: "isc-dhcp"
layout: package
next_package: jags
previous_package: iproute2
languages: ['c']
---
## 4.4.0
1 / 244 files match, 1 filtered matches.

 - [server/ldap_casa.c](#serverldap_casac)

### server/ldap_casa.c

```c

{% raw %}
62 | int
63 | load_casa (void)
64 | {
65 |        if( !(casaIDK = dlopen(MICASA_LIB,RTLD_LAZY)))
66 |        	  return 0;
67 |        p_miCASAGetCredential = (CASA_GetCredential_T) dlsym(casaIDK, "miCASAGetCredential");
{% endraw %}

```