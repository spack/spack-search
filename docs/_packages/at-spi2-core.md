---
name: "at-spi2-core"
layout: package
next_package: damaris
previous_package: cairomm
languages: []
---
## 2.38.0
1 / 238 files match

 - [meson.build](#mesonbuild)

### meson.build

```

{% raw %}
54 | if cc.has_function('dlopen')
56 | elif cc.has_function('dlopen', args: '-ldl')
59 |   error('Could not find a library with the dlopen function')
{% endraw %}

```