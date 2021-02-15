---
name: "py-ray"
layout: package
next_package: karma
previous_package: octave
languages: ['cpp', 'python']
---
## 0.8.7
3 / 2662 files match

 - [BUILD.bazel](#buildbazel)
 - [src/ray/gcs/redis_module/ray_redis_module.cc](#srcraygcsredis_moduleray_redis_modulecc)
 - [python/ray/services.py](#pythonrayservicespy)

### BUILD.bazel

```

{% raw %}
1766 |     # We need to dlopen this lib with RTLD_GLOBAL to use ABI in this
{% endraw %}

```
### src/ray/gcs/redis_module/ray_redis_module.cc

```cpp

{% raw %}
35 | // libray_redis_module>" (dlopen() under the hood) will a definition of "module"
{% endraw %}

```
### python/ray/services.py

```python

{% raw %}
760 |         # imported from credis dynamically through dlopen when Ray is built
{% endraw %}

```