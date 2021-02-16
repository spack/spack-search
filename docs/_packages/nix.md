---
name: "nix"
layout: package
next_package: nmap
previous_package: nim
languages: ['cpp']
---
## 2.2.1
4 / 700 files match, 2 filtered matches.

 - [src/libexpr/primops.cc](#srclibexprprimopscc)
 - [src/libstore/globals.cc](#srclibstoreglobalscc)

### src/libexpr/primops.cc

```cpp

{% raw %}
173 |     void *handle = dlopen(path.c_str(), RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```
### src/libstore/globals.cc

```cpp

{% raw %}
174 |                 dlopen(file.c_str(), RTLD_LAZY | RTLD_LOCAL);
{% endraw %}

```