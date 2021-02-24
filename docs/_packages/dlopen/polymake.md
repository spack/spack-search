---
name: "polymake"
layout: package
next_package: fakexrandr
previous_package: gflags
library_name: dlopen
matches: ['dlopen']
languages: ['cpp']
---
## 3.5
1 / 3513 files match, 1 filtered matches.

 - [lib/callable/src/perl/Main.cc](#libcallablesrcperlmaincc)

### lib/callable/src/perl/Main.cc

```cpp

{% raw %}
165 |    void* polyhandle = nullptr;
166 |    int dlreturn;
167 |    if ((dlreturn = dladdr((void*)&destroy_perl, &dli_polymake))) {
168 |       polyhandle = dlopen(dli_polymake.dli_fname, RTLD_LAZY | RTLD_NOLOAD | RTLD_GLOBAL );
169 |    }
170 |    if (!polyhandle) {
171 |       std::cerr << "*** WARNING: Failed to (re-)dlopen libpolymake with RTLD_GLOBAL: " 
172 |                 << (dlreturn ? dlerror() : "dladdr failed to give shared library pathname.") << "***\n"
173 |                    "    Application modules might fail to load." << std::endl;
175 | 
176 |    void* perlhandle = nullptr;
177 |    if ((dlreturn = dladdr((void*)&perl_destruct, &dli_perl))) {
178 |       perlhandle = dlopen(dli_perl.dli_fname, RTLD_LAZY | RTLD_NOLOAD | RTLD_GLOBAL );
179 |    }
180 |    if (!perlhandle) {
181 |       std::cerr << "*** WARNING: Failed to (re-)dlopen libperl with RTLD_GLOBAL: " 
182 |                 << (dlreturn ? dlerror() : "dladdr failed to give shared library pathname.") << "***\n"
183 |                    "    Perl modules might fail to load." << std::endl;
{% endraw %}

```