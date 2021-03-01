---
name: "lftp"
layout: package
next_package: libcanberra
previous_package: legion
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['cpp']
---
## 4.8.1
5 / 797 files match, 2 filtered matches.

 - [src/commands.cc](#srccommandscc)
 - [src/module.cc](#srcmodulecc)

### src/commands.cc

```cpp

{% raw %}
2820 | 
2821 | #if defined(HAVE_DLOPEN) && defined(RTLD_DEFAULT)
2822 |    /* Show some of loaded libraries. Modules can load those libraries on
2823 |       demand so use dlsym to avoid linking with them just for showing version. */
2824 |    printf("\n");
2825 |    const char *msg=_("Libraries used: ");
2838 |       const char *query() const
2839 | 	 {
2840 | 	    int v;
2841 | 	    void *sym_ptr=dlsym(RTLD_DEFAULT,symbol);
2842 | 	    if(!sym_ptr)
2843 | 	       return 0;
{% endraw %}

```
### src/module.cc

```cpp

{% raw %}
177 |       return 0;
178 |    (void)new lftp_module_info(fullpath,map);
179 | #if 0 // for some reason this does not work even with LAZY (because of _init?).
180 |    const char*const*depend=(const char*const*)dlsym(map,"module_depend");
181 |    if(depend)
182 |    {
192 |       }
193 |    }
194 | #endif //0
195 |    init=(init_t)dlsym(map,"module_init");
196 |    if(init)
197 |       (*init)(argc,argv);
220 |       if(*scan=='-')
221 | 	 *scan='_';
222 |    strcat(init_fn,"_module_init");
223 |    init_t init=(init_t)dlsym(RTLD_DEFAULT,init_fn);
224 |    if(init) {
225 |       (*init)(0,0);
{% endraw %}

```