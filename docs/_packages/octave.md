---
name: "octave"
layout: package
next_package: onednn
previous_package: ocl-icd
languages: ['cpp', 'c']
---
## 4.0.0
15 / 6223 files match, 2 filtered matches.

 - [liboctave/util/oct-shlib.cc](#liboctaveutiloct-shlibcc)
 - [liboctave/cruft/misc/blaswrap.c](#liboctavecruftmiscblaswrapc)

### liboctave/util/oct-shlib.cc

```cpp

{% raw %}
44 | extern void *dlopen (const char *, int);
156 | octave_dlopen_shlib : public octave_shlib::shlib_rep
160 |   octave_dlopen_shlib (const std::string& f);
162 |   ~octave_dlopen_shlib (void);
177 |   octave_dlopen_shlib (const octave_dlopen_shlib&);
179 |   octave_dlopen_shlib& operator = (const octave_dlopen_shlib&);
184 | octave_dlopen_shlib::octave_dlopen_shlib (const std::string& f)
197 |   library = dlopen (file.c_str (), flags);
212 | octave_dlopen_shlib::~octave_dlopen_shlib (void)
219 | octave_dlopen_shlib::search (const std::string& name,
512 |   return new octave_dlopen_shlib (f);
{% endraw %}

```
### liboctave/cruft/misc/blaswrap.c

```c

{% raw %}
273 |   apple_vecLib = dlopen (VECLIB_FILE, RTLD_LOCAL | RTLD_NOLOAD | RTLD_FIRST);
{% endraw %}

```