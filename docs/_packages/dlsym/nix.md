---
name: "nix"
layout: package
next_package: nspr
previous_package: nicstat
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 2.2.1
1 / 700 files match, 1 filtered matches.

 - [src/libexpr/primops.cc](#srclibexprprimopscc)

### src/libexpr/primops.cc

```cpp

{% raw %}
175 |         throw EvalError(format("could not open '%1%': %2%") % path % dlerror());
176 | 
177 |     dlerror();
178 |     ValueInitializer func = (ValueInitializer) dlsym(handle, sym.c_str());
179 |     if(!func) {
180 |         char *message = dlerror();
{% endraw %}

```