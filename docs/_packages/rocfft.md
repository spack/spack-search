---
name: "rocfft"
layout: package
next_package: lhapdf
previous_package: rocm-validation-suite
languages: ['c']
---
## 3.5.0
2 / 182 files match, 1 filtered matches.

 - [library/src/include/ref_cpu.h](#librarysrcincluderef_cpuh)

### library/src/include/ref_cpu.h

```c

{% raw %}
82 |         fftw3f_lib = dlopen(env_value_fftw3f, RTLD_NOW);
85 |             rocfft_cout << "error in fftw3f dlopen" << std::endl;
88 |         fftw3_lib = dlopen(env_value_fftw3, RTLD_NOW);
91 |             rocfft_cout << "error in fftw3 dlopen" << std::endl;
{% endraw %}

```