---
name: "rocfft"
layout: package
next_package: zabbix
previous_package: aspell
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.5.0
2 / 182 files match, 1 filtered matches.

 - [library/src/include/ref_cpu.h](#librarysrcincluderef_cpuh)

### library/src/include/ref_cpu.h

```c

{% raw %}
79 |                         << std::endl;
80 |         }
81 | 
82 |         fftw3f_lib = dlopen(env_value_fftw3f, RTLD_NOW);
83 |         if(!fftw3f_lib)
84 |         {
85 |             rocfft_cout << "error in fftw3f dlopen" << std::endl;
86 |         }
87 | 
88 |         fftw3_lib = dlopen(env_value_fftw3, RTLD_NOW);
89 |         if(!fftw3_lib)
90 |         {
91 |             rocfft_cout << "error in fftw3 dlopen" << std::endl;
92 |         }
93 |     }
{% endraw %}

```