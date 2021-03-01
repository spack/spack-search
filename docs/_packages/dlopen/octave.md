---
name: "octave"
layout: package
next_package: openfoam
previous_package: ocaml
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['cpp', 'c']
---
## 4.0.0
15 / 6223 files match, 2 filtered matches.

 - [liboctave/util/oct-shlib.cc](#liboctaveutiloct-shlibcc)
 - [liboctave/cruft/misc/blaswrap.c](#liboctavecruftmiscblaswrapc)

### liboctave/util/oct-shlib.cc

```cpp

{% raw %}
41 | #if defined (HAVE_DLFCN_H)
42 | #include <dlfcn.h>
43 | #else
44 | extern void *dlopen (const char *, int);
45 | extern const char *dlerror (void);
46 | extern void *dlsym (void *, const char *);
153 | #if defined (HAVE_DLOPEN_API)
154 | 
155 | class
156 | octave_dlopen_shlib : public octave_shlib::shlib_rep
157 | {
158 | public:
159 | 
160 |   octave_dlopen_shlib (const std::string& f);
161 | 
162 |   ~octave_dlopen_shlib (void);
163 | 
164 |   void *search (const std::string& name,
174 | 
175 |   // No copying!
176 | 
177 |   octave_dlopen_shlib (const octave_dlopen_shlib&);
178 | 
179 |   octave_dlopen_shlib& operator = (const octave_dlopen_shlib&);
180 | 
181 |   void *library;
182 | };
183 | 
184 | octave_dlopen_shlib::octave_dlopen_shlib (const std::string& f)
185 |   : octave_shlib::shlib_rep (f), library (0)
186 | {
194 |   flags |= RTLD_NOW;
195 | #endif
196 | 
197 |   library = dlopen (file.c_str (), flags);
198 | 
199 |   if (! library)
209 |     }
210 | }
211 | 
212 | octave_dlopen_shlib::~octave_dlopen_shlib (void)
213 | {
214 |   if (library)
216 | }
217 | 
218 | void *
219 | octave_dlopen_shlib::search (const std::string& name,
220 |                              octave_shlib::name_mangler mangler)
221 | {
509 | octave_shlib::shlib_rep::new_instance (const std::string& f)
510 | {
511 | #if defined (HAVE_DLOPEN_API)
512 |   return new octave_dlopen_shlib (f);
513 | #elif defined (HAVE_SHL_LOAD_API)
514 |   return new octave_shl_load_shlib (f);
{% endraw %}

```
### liboctave/cruft/misc/blaswrap.c

```c

{% raw %}
270 | __attribute__((constructor))
271 | static void initVecLibWrappers (void)
272 | {
273 |   apple_vecLib = dlopen (VECLIB_FILE, RTLD_LOCAL | RTLD_NOLOAD | RTLD_FIRST);
274 |   if (0 == apple_vecLib)
275 |     abort ();
{% endraw %}

```