---
name: "nix"
layout: package
next_package: libvdwxc
previous_package: moab
languages: ['cpp']
---
## 2.2.1
4 / 700 files match

 - [src/libexpr/primops.cc](#srclibexprprimopscc)
 - [src/libstore/globals.cc](#srclibstoreglobalscc)
 - [doc/manual/expressions/language-values.xml](#docmanualexpressionslanguage-valuesxml)
 - [doc/manual/command-ref/conf-file.xml](#docmanualcommand-refconf-filexml)

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
### doc/manual/expressions/language-values.xml

```

{% raw %}
54 |   ${if openglSupport then "-dlopen-opengl
{% endraw %}

```
### doc/manual/command-ref/conf-file.xml

```

{% raw %}
530 |         files will be dlopened by Nix, allowing them to affect
{% endraw %}

```