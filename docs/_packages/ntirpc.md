---
name: "ntirpc"
layout: package
next_package: eztrace
previous_package: py-pygpu
languages: ['cpp']
---
## 3.0
2 / 199 files match

 - [ntirpc/misc/winpthreads.h](#ntirpcmiscwinpthreadsh)
 - [src/lttng/main.c](#srclttngmainc)

### ntirpc/misc/winpthreads.h

```cpp

{% raw %}
1531 | #define dlopen(...) (pthread_testcancel(), dlopen(__VA_ARGS__))
{% endraw %}

```
### src/lttng/main.c

```cpp

{% raw %}
55 | struct lttng_ust_tracepoint_dlopen tracepoint_dlopen
{% endraw %}

```