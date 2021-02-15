---
name: "py-easybuild-framework"
layout: package
next_package: wireshark
previous_package: openbabel
languages: []
---
## 4.0.0
4 / 497 files match

 - [test/framework/easyconfigs/test_ecs/o/OpenMPI/OpenMPI-2.1.2-GCC-4.6.4.eb](#testframeworkeasyconfigstest_ecsoopenmpiopenmpi-212-gcc-464eb)
 - [test/framework/easyconfigs/test_ecs/o/OpenMPI/OpenMPI-2.1.2-GCC-6.4.0-2.28.eb](#testframeworkeasyconfigstest_ecsoopenmpiopenmpi-212-gcc-640-228eb)
 - [test/framework/easyconfigs/test_ecs/o/OpenMPI/OpenMPI-2.1.2-gcccuda-2018a.eb](#testframeworkeasyconfigstest_ecsoopenmpiopenmpi-212-gcccuda-2018aeb)
 - [test/framework/easyconfigs/test_ecs/o/OpenMPI/OpenMPI-3.1.1-GCC-7.3.0-2.30.eb](#testframeworkeasyconfigstest_ecsoopenmpiopenmpi-311-gcc-730-230eb)

### test/framework/easyconfigs/test_ecs/o/OpenMPI/OpenMPI-2.1.2-GCC-4.6.4.eb

```

{% raw %}
18 | configopts += '--disable-dlopen '  # statically link component, don't do dynamic loading
{% endraw %}

```
### test/framework/easyconfigs/test_ecs/o/OpenMPI/OpenMPI-2.1.2-GCC-6.4.0-2.28.eb

```

{% raw %}
18 | configopts += '--disable-dlopen '  # statically link component, don't do dynamic loading
{% endraw %}

```
### test/framework/easyconfigs/test_ecs/o/OpenMPI/OpenMPI-2.1.2-gcccuda-2018a.eb

```

{% raw %}
23 | configopts += '--with-cuda=$CUDA_HOME '             # CUDA-aware build; N.B. --disable-dlopen is incompatible
{% endraw %}

```
### test/framework/easyconfigs/test_ecs/o/OpenMPI/OpenMPI-3.1.1-GCC-7.3.0-2.30.eb

```

{% raw %}
18 | configopts += '--disable-dlopen '  # statically link component, don't do dynamic loading
{% endraw %}

```