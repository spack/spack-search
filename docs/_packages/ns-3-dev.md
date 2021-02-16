---
name: "ns-3-dev"
layout: package
next_package: rose
previous_package: soci
languages: ['cpp', 'c']
---
## 3.30.1
3 / 3342 files match

 - [src/internet/model/nsc-tcp-l4-protocol.cc](#srcinternetmodelnsc-tcp-l4-protocolcc)
 - [src/internet/model/nsc-tcp-l4-protocol.h](#srcinternetmodelnsc-tcp-l4-protocolh)

### src/internet/model/nsc-tcp-l4-protocol.cc

```cpp

{% raw %}
162 |   m_dlopenHandle = NULL;
169 |   dlclose (m_dlopenHandle);
178 |       NS_ASSERT (!m_dlopenHandle);
179 |       m_dlopenHandle = dlopen (soname.c_str (), RTLD_NOW);
180 |       if (m_dlopenHandle == NULL)
200 |   NS_ASSERT (m_dlopenHandle);
202 |   FCreateStack create = (FCreateStack)dlsym (m_dlopenHandle, "nsc_create_stack");
{% endraw %}

```
### src/internet/model/nsc-tcp-l4-protocol.h

```c

{% raw %}
222 |   void *m_dlopenHandle; //!< dynamic library handle.
{% endraw %}

```