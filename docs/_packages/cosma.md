---
name: "cosma"
layout: package
next_package: dtcmp
previous_package: fuse-overlayfs
languages: []
---
## master
2 / 407 files match

 - [docker/gpu/deploy.Dockerfile](#dockergpudeploydockerfile)
 - [docker/cpu-release/deploy.Dockerfile](#dockercpu-releasedeploydockerfile)

### docker/gpu/deploy.Dockerfile

```

{% raw %}
21 | # Run linuxdeploy, and add a bunch of libs that are dlopen'ed by mkl
{% endraw %}

```
### docker/cpu-release/deploy.Dockerfile

```

{% raw %}
22 | # Run linuxdeploy, and add a bunch of libs that are dlopen'ed by mkl
30 |       # MKL dlopen's some of their libs, so we have to explicitly copy them over
{% endraw %}

```