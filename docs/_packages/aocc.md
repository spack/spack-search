---
name: "aocc"
layout: package
next_package: aomp
previous_package: alsa-lib
languages: ['python', 'c']
---
## 2.3.0
10 / 3125 files match, 2 filtered matches.

 - [include/ompt-multiplex.h](#includeompt-multiplexh)
 - [lib-debug/ompd/ompd.py](#lib-debugompdompdpy)

### include/ompt-multiplex.h

```c

{% raw %}
1054 |         tmp_progress++;
1055 |       if (tmp_progress < strlen(tool_libs))
1056 |         tool_libs_buffer[tmp_progress] = 0;
1057 |       void *h = dlopen(tool_libs_buffer + progress, RTLD_LAZY);
1058 |       if (h) {
1059 |         client_start_tool =
{% endraw %}

```
### lib-debug/ompd/ompd.py

```python

{% raw %}
55 | 					raise ValueError("Handle of OMPD library is not a valid string!")
56 | 				if ret == -2:
57 | 					print("ret == -2")
58 | 					pass # It's ok to fail on dlopen
59 | 				if ret == -3:
60 | 					print("ret == -3")
{% endraw %}

```