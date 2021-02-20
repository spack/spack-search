---
name: "ns-3-dev"
layout: package
next_package: nspr
previous_package: node-js
languages: ['cpp', 'c']
---
## 3.30.1
3 / 3342 files match, 2 filtered matches.

 - [src/internet/model/nsc-tcp-l4-protocol.cc](#srcinternetmodelnsc-tcp-l4-protocolcc)
 - [src/internet/model/nsc-tcp-l4-protocol.h](#srcinternetmodelnsc-tcp-l4-protocolh)

### src/internet/model/nsc-tcp-l4-protocol.cc

```cpp

{% raw %}
159 |     m_nscInterface (new NscInterfaceImpl (this)),
160 |     m_softTimer (Timer::CANCEL_ON_DESTROY)
161 | {
162 |   m_dlopenHandle = NULL;
163 |   NS_LOG_LOGIC ("Made a NscTcpL4Protocol "<<this);
164 | }
166 | NscTcpL4Protocol::~NscTcpL4Protocol ()
167 | {
168 |   NS_LOG_FUNCTION (this);
169 |   dlclose (m_dlopenHandle);
170 | }
171 | 
175 |   if (soname!="")
176 |     {
177 |       m_nscLibrary = soname;
178 |       NS_ASSERT (!m_dlopenHandle);
179 |       m_dlopenHandle = dlopen (soname.c_str (), RTLD_NOW);
180 |       if (m_dlopenHandle == NULL)
181 |         NS_FATAL_ERROR (dlerror ());
182 |     }
197 |       return;
198 |     }
199 | 
200 |   NS_ASSERT (m_dlopenHandle);
201 | 
202 |   FCreateStack create = (FCreateStack)dlsym (m_dlopenHandle, "nsc_create_stack");
203 |   NS_ASSERT (create);
204 |   m_nscStack = create (m_nscInterface, m_nscInterface, external_rand);
{% endraw %}

```
### src/internet/model/nsc-tcp-l4-protocol.h

```c

{% raw %}
219 |   Ipv4EndPointDemux *m_endPoints; //!< A list of IPv4 end points.
220 |   INetStack* m_nscStack; //!< the NSC stack.
221 |   NscInterfaceImpl *m_nscInterface; //!< the NSC Interface.
222 |   void *m_dlopenHandle; //!< dynamic library handle.
223 |   std::string m_nscLibrary; //!< path to the NSC library.
224 |   Timer m_softTimer; //!< Soft interrupt timer
{% endraw %}

```