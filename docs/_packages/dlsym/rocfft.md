---
name: "rocfft"
layout: package
next_package: grass
previous_package: valgrind
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 3.5.0
2 / 182 files match, 1 filtered matches.

 - [library/src/include/ref_cpu.h](#librarysrcincluderef_cpuh)

### library/src/include/ref_cpu.h

```c

{% raw %}
140 |         , typesize(0)
141 |     {
142 |         RefLibHandle& refHandle = RefLibHandle::GetRefLibHandle();
143 |         local_fftwf_malloc      = (ftype_fftwf_malloc)dlsym(refHandle.fftw3f_lib, "fftwf_malloc");
144 |         local_fftwf_free        = (ftype_fftwf_free)dlsym(refHandle.fftw3f_lib, "fftwf_free");
145 |     };
146 |     fftwbuf(const size_t size0, const size_t typesize0)
149 |         , typesize(typesize0)
150 |     {
151 |         RefLibHandle& refHandle = RefLibHandle::GetRefLibHandle();
152 |         local_fftwf_malloc      = (ftype_fftwf_malloc)dlsym(refHandle.fftw3f_lib, "fftwf_malloc");
153 |         local_fftwf_free        = (ftype_fftwf_free)dlsym(refHandle.fftw3f_lib, "fftwf_free");
154 | 
155 |         alloc(size0, typesize0);
435 |     {
436 |         RefLibHandle&             refHandle = RefLibHandle::GetRefLibHandle();
437 |         ftype_fftwf_plan_many_dft local_fftwf_plan_many_dft
438 |             = (ftype_fftwf_plan_many_dft)dlsym(refHandle.fftw3f_lib, "fftwf_plan_many_dft");
439 |         ftype_fftwf_execute local_fftwf_execute
440 |             = (ftype_fftwf_execute)dlsym(refHandle.fftw3f_lib, "fftwf_execute");
441 |         ftype_fftwf_destroy_plan local_fftwf_destroy_plan
442 |             = (ftype_fftwf_destroy_plan)dlsym(refHandle.fftw3f_lib, "fftwf_destroy_plan");
443 | 
444 |         int n[1] = {static_cast<int>(M)};
471 |         {
472 |             RefLibHandle&             refHandle = RefLibHandle::GetRefLibHandle();
473 |             ftype_fftwf_plan_many_dft local_fftwf_plan_many_dft
474 |                 = (ftype_fftwf_plan_many_dft)dlsym(refHandle.fftw3f_lib, "fftwf_plan_many_dft");
475 |             ftype_fftwf_execute local_fftwf_execute
476 |                 = (ftype_fftwf_execute)dlsym(refHandle.fftw3f_lib, "fftwf_execute");
477 |             ftype_fftwf_destroy_plan local_fftwf_destroy_plan
478 |                 = (ftype_fftwf_destroy_plan)dlsym(refHandle.fftw3f_lib, "fftwf_destroy_plan");
479 | 
480 |             int n[1]    = {static_cast<int>(data->node->length[0])};
{% endraw %}

```