---
name: "rocm-debug-agent"
layout: package
next_package: transrate
previous_package: flux-core
languages: []
---
## 3.5.0
1 / 40 files match

 - [src/AgentUtils.cpp](#srcagentutilscpp)

### src/AgentUtils.cpp

```

{% raw %}
158 |     hModule = dlopen(ipFilename.c_str(), RTLD_LAZY );
244 |     hModule = dlopen(dllName.c_str(), RTLD_LAZY | RTLD_NOLOAD);
{% endraw %}

```