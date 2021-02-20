---
name: "simgrid"
layout: package
next_package: slang
previous_package: silo
languages: ['python']
---
## 3.20
12 / 2455 files match, 1 filtered matches.

 - [tools/tesh/tesh.py](#toolsteshteshpy)

### tools/tesh/tesh.py

```python

{% raw %}
470 |            re.compile(r"For details see https://github.com/google/sanitizers/issues/189"),
471 |            re.compile(r"Python runtime initialized with LC_CTYPE=C .*"),
472 |            re.compile(r"cmake: /usr/local/lib/libcurl\.so\.4: no version information available \(required by cmake\)"), # Seen on CircleCI
473 |            re.compile(r".*mmap broken on FreeBSD, but dlopen\+thread broken too. Switching to dlopen\+raw contexts\."),
474 |            re.compile(r".*dlopen\+thread broken on Apple and BSD\. Switching to raw contexts\."),
475 |            ]
476 |         TeshState().jenkins = True # This is a Jenkins build
{% endraw %}

```