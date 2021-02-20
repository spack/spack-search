---
name: "libpulsar"
layout: package
next_package: libquo
previous_package: libpam
languages: ['cpp']
---
## 2.7.0
1 / 5061 files match, 1 filtered matches.

 - [pulsar-client-cpp/lib/Authentication.cc](#pulsar-client-cpplibauthenticationcc)

### pulsar-client-cpp/lib/Authentication.cc

```cpp

{% raw %}
166 |     }
167 | 
168 |     Authentication* auth = NULL;
169 |     void* handle = dlopen(pluginNameOrDynamicLibPath.c_str(), RTLD_LAZY);
170 |     if (handle != NULL) {
171 |         {
202 |     }
203 | 
204 |     Authentication* auth = NULL;
205 |     void* handle = dlopen(pluginNameOrDynamicLibPath.c_str(), RTLD_LAZY);
206 |     if (handle != NULL) {
207 |         std::lock_guard<std::mutex> lock(mutex);
{% endraw %}

```