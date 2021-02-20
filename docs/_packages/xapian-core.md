---
name: "xapian-core"
layout: package
next_package: xdm
previous_package: wt
languages: ['cpp']
---
## 1.4.3
5 / 1244 files match, 2 filtered matches.

 - [tests/api_termgen.cc](#testsapi_termgencc)
 - [tests/api_queryparser.cc](#testsapi_queryparsercc)

### tests/api_termgen.cc

```cpp

{% raw %}
281 |     { "/var/run/mysqld/mysqld.sock", "(var:(pos=1) PHRASE 5 run:(pos=2) PHRASE 5 mysqld:(pos=3) PHRASE 5 mysqld:(pos=4) PHRASE 5 sock:(pos=5))" },
282 |     { "\"QSI-161 drivers\"", "(qsi:(pos=1) PHRASE 3 161:(pos=2) PHRASE 3 drivers:(pos=3))" },
283 |     { "\"e-cube\" barebone", "((e:(pos=1) PHRASE 2 cube:(pos=2)) OR Zbarebon:(pos=3))" },
284 |     { "\"./httpd: symbol not found: dlopen\"", "(httpd:(pos=1) PHRASE 5 symbol:(pos=2) PHRASE 5 not:(pos=3) PHRASE 5 found:(pos=4) PHRASE 5 dlopen:(pos=5))" },
285 |     { "ERROR 2003: Can't connect to MySQL server on 'localhost' (10061)", "(error:(pos=1) OR 2003:(pos=2) OR can't:(pos=3) OR Zconnect:(pos=4) OR Zto:(pos=5) OR mysql:(pos=6) OR Zserver:(pos=7) OR Zon:(pos=8) OR Zlocalhost:(pos=9) OR 10061:(pos=10))" },
286 |     { "location.href = \"\"", "(location:(pos=1) PHRASE 2 href:(pos=2))" },
{% endraw %}

```
### tests/api_queryparser.cc

```cpp

{% raw %}
251 |     { "/var/run/mysqld/mysqld.sock", "(var@1 PHRASE 5 run@2 PHRASE 5 mysqld@3 PHRASE 5 mysqld@4 PHRASE 5 sock@5)" },
252 |     { "\"QSI-161 drivers\"", "(qsi@1 PHRASE 3 161@2 PHRASE 3 drivers@3)" },
253 |     { "\"e-cube\" barebone", "((e@1 PHRASE 2 cube@2) OR Zbarebon@3)" },
254 |     { "\"./httpd: symbol not found: dlopen\"", "(httpd@1 PHRASE 5 symbol@2 PHRASE 5 not@3 PHRASE 5 found@4 PHRASE 5 dlopen@5)" },
255 |     { "ERROR 2003: Can't connect to MySQL server on 'localhost' (10061)", "(((error@1 OR 2003@2 OR can't@3 OR Zconnect@4 OR Zto@5 OR mysql@6 OR Zserver@7 OR Zon@8) OR Zlocalhost@9) OR 10061@10)" },
256 |     { "location.href = \"\"", "(location@1 PHRASE 2 href@2)" },
{% endraw %}

```