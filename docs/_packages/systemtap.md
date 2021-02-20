---
name: "systemtap"
layout: package
next_package: talloc
previous_package: sysbench
languages: ['c']
---
## 4.2
7 / 4791 files match, 1 filtered matches.

 - [stapdyn/mutator.h](#stapdynmutatorh)

### stapdyn/mutator.h

```c

{% raw %}
30 |   private:
31 |     BPatch patch;
32 | 
33 |     void* module; // the locally dlopened probe module
34 |     std::string module_name; // the filename of the probe module
35 |     std::vector<std::string> modoptions; // custom globals from -G option
{% endraw %}

```