---
name: "rocfft"
layout: package
next_package: lhapdf
previous_package: rocm-validation-suite
languages: ['cpp']
---
## 3.5.0
2 / 182 files match

 - [library/src/include/ref_cpu.h](#librarysrcincluderef_cpuh)
 - [clients/rider/dyna-rider.cpp](#clientsriderdyna-ridercpp)

### library/src/include/ref_cpu.h

```cpp

{% raw %}
82 |         fftw3f_lib = dlopen(env_value_fftw3f, RTLD_NOW);
85 |             rocfft_cout << "error in fftw3f dlopen" << std::endl;
88 |         fftw3_lib = dlopen(env_value_fftw3, RTLD_NOW);
91 |             rocfft_cout << "error in fftw3 dlopen" << std::endl;
{% endraw %}

```
### clients/rider/dyna-rider.cpp

```

{% raw %}
412 |         void* libhandle = dlopen((libdir[idx] + "/librocfft.so").c_str(), RTLD_LAZY);
{% endraw %}

```