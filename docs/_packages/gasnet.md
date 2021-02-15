---
name: "gasnet"
layout: package
next_package: netperf
previous_package: sst-elements
languages: []
---
## 2019.9.0
2 / 372 files match

 - [tests/upcr-harness/external-upcxx/harness.conf](#testsupcr-harnessexternal-upcxxharnessconf)
 - [tests/upcr-harness/external-legion/harness.conf](#testsupcr-harnessexternal-legionharnessconf)

### tests/upcr-harness/external-upcxx/harness.conf

```

{% raw %}
312 | WarningFilter:   all ; '.*?warning: Using .dlopen. in statically linked applications.*?'
369 | WarningFilter:   all ; '.*?warning: Using .dlopen. in statically linked applications.*?'
376 | WarningFilter:   all ; '.*?warning: Using .dlopen. in statically linked applications.*?'
{% endraw %}

```
### tests/upcr-harness/external-legion/harness.conf

```

{% raw %}
25 | WarningFilter:  os_cnl ; .*?warning: Using .dlopen. in statically linked applications.*?
{% endraw %}

```