---
name: "recorder"
layout: package
next_package: ffmpeg
previous_package: bear
library_name: dlsym
matches: ['dlsym']
languages: ['c']
---
## 2.1.4
2 / 31 files match, 1 filtered matches.

 - [include/recorder.h](#includerecorderh)

### include/recorder.h

```c

{% raw %}
102 |     /* Point __real_func to the real funciton using dlsym() */
103 |     #define MAP_OR_FAIL(func)                                                   \
104 |         if (!(__real_##func)) {                                                 \
105 |             __real_##func = dlsym(RTLD_NEXT, #func);                            \
106 |             if (!(__real_##func)) {                                             \
107 |                 printf("Recorder failed to map symbol: %s\n", #func);           \
{% endraw %}

```