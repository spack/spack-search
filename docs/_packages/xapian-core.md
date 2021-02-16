---
name: "xapian-core"
layout: package
next_package: xrootd
previous_package: wxwidgets
languages: ['cpp']
---
## 1.4.3
5 / 1244 files match, 2 filtered matches.

 - [tests/api_termgen.cc](#testsapi_termgencc)
 - [tests/api_queryparser.cc](#testsapi_queryparsercc)

### tests/api_termgen.cc

```cpp

{% raw %}
284 |     { "\"./httpd: symbol not found: dlopen\"", "(httpd:(pos=1) PHRASE 5 symbol:(pos=2) PHRASE 5 not:(pos=3) PHRASE 5 found:(pos=4) PHRASE 5 dlopen:(pos=5))" },
{% endraw %}

```
### tests/api_queryparser.cc

```cpp

{% raw %}
254 |     { "\"./httpd: symbol not found: dlopen\"", "(httpd@1 PHRASE 5 symbol@2 PHRASE 5 not@3 PHRASE 5 found@4 PHRASE 5 dlopen@5)" },
{% endraw %}

```