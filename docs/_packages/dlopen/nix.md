---
name: "nix"
layout: package
next_package: pnmpi
previous_package: fakechroot
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 2.2.1
4 / 700 files match, 2 filtered matches.

 - [src/libexpr/primops.cc](#srclibexprprimopscc)
 - [src/libstore/globals.cc](#srclibstoreglobalscc)

### src/libexpr/primops.cc

```cpp

{% raw %}
170 | 
171 |     string sym = state.forceStringNoCtx(*args[1], pos);
172 | 
173 |     void *handle = dlopen(path.c_str(), RTLD_LAZY | RTLD_LOCAL);
174 |     if (!handle)
175 |         throw EvalError(format("could not open '%1%': %2%") % path % dlerror());
{% endraw %}

```
### src/libstore/globals.cc

```cpp

{% raw %}
171 |             /* handle is purposefully leaked as there may be state in the
172 |                DSO needed by the action of the plugin. */
173 |             void *handle =
174 |                 dlopen(file.c_str(), RTLD_LAZY | RTLD_LOCAL);
175 |             if (!handle)
176 |                 throw Error("could not dynamically open plugin file '%s': %s", file, dlerror());
{% endraw %}

```