---
name: "binutils"
layout: package
next_package: podio
previous_package: ucx
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c', 'cpp']
---
## 2.32
17 / 22031 files match, 13 filtered matches.

 - [bfd/plugin.c](#bfdpluginc)
 - [gold/plugin.cc](#goldplugincc)
 - [gold/testsuite/ifuncmain3.c](#goldtestsuiteifuncmain3c)
 - [ld/plugin.c](#ldpluginc)
 - [ld/testsuite/ld-elf/dl1main.c](#ldtestsuiteld-elfdl1mainc)
 - [ld/testsuite/ld-elf/dl6dmain.c](#ldtestsuiteld-elfdl6dmainc)
 - [ld/testsuite/ld-elf/pr21964-5.c](#ldtestsuiteld-elfpr21964-5c)
 - [ld/testsuite/ld-elf/dl6bmain.c](#ldtestsuiteld-elfdl6bmainc)
 - [ld/testsuite/ld-elf/dl6amain.c](#ldtestsuiteld-elfdl6amainc)
 - [ld/testsuite/ld-elf/dl6cmain.c](#ldtestsuiteld-elfdl6cmainc)
 - [ld/testsuite/ld-elf/pr21964-2c.c](#ldtestsuiteld-elfpr21964-2cc)
 - [ld/testsuite/ld-elf/pr21964-4.c](#ldtestsuiteld-elfpr21964-4c)
 - [ld/testsuite/ld-pe/vers-script-dll.c](#ldtestsuiteld-pevers-script-dllc)

### bfd/plugin.c

```c

{% raw %}
48 | }
49 | 
50 | static void *
51 | dlsym (void *handle, const char *name)
52 | {
53 |   return GetProcAddress (handle, name);
267 |   plugin_list_iter->next = plugin_list;
268 |   plugin_list = plugin_list_iter;
269 | 
270 |   onload = dlsym (plugin_handle, "onload");
271 |   if (!onload)
272 |     return 0;
{% endraw %}

```
### gold/plugin.cc

```cpp

{% raw %}
50 | }
51 | 
52 | static void *
53 | dlsym(void *handle, const char *name)
54 | {
55 |   return reinterpret_cast<void *>(
204 |     }
205 | 
206 |   // Find the plugin's onload entry point.
207 |   void* ptr = dlsym(this->handle_, "onload");
208 |   if (ptr == NULL)
209 |     {
{% endraw %}

```
### gold/testsuite/ifuncmain3.c

```c

{% raw %}
49 |       return 1;
50 |     }
51 | 
52 |   p = dlsym (h, "foo");
53 |   if (p == NULL)
54 |     {
58 |   if ((*p) () != -1)
59 |     abort ();
60 | 
61 |   f = dlsym (h, "get_foo_p");
62 |   if (f == NULL)
63 |     {
65 |       return 1;
66 |     }
67 | 
68 |   ret = dlsym (h, "ret_foo");
69 |   if (ret == NULL)
70 |     {
80 |   if (*ret != -30 || (*p) () != *ret)
81 |     abort ();
82 | 
83 |   f = dlsym (h, "get_foo_hidden_p");
84 |   if (f == NULL)
85 |     {
87 |       return 1;
88 |     }
89 | 
90 |   ret = dlsym (h, "ret_foo_hidden");
91 |   if (ret == NULL)
92 |     {
100 |   if (*ret != 1 || (*p) () != *ret)
101 |     abort ();
102 | 
103 |   f = dlsym (h, "get_foo_protected_p");
104 |   if (f == NULL)
105 |     {
107 |       return 1;
108 |     }
109 | 
110 |   ret = dlsym (h, "ret_foo_protected");
111 |   if (ret == NULL)
112 |     {
{% endraw %}

```
### ld/plugin.c

```c

{% raw %}
186 | }
187 | 
188 | static void *
189 | dlsym (void *handle, const char *name)
190 | {
191 |   return GetProcAddress (handle, name);
1002 |       enum ld_plugin_status rv;
1003 |       ld_plugin_onload onloadfn;
1004 | 
1005 |       onloadfn = (ld_plugin_onload) dlsym (curplug->dlhandle, "onload");
1006 |       if (!onloadfn)
1007 | 	onloadfn = (ld_plugin_onload) dlsym (curplug->dlhandle, "_onload");
1008 |       if (!onloadfn)
1009 | 	einfo (_("%F%P: %s: error loading plugin: %s\n"),
{% endraw %}

```
### ld/testsuite/ld-elf/dl1main.c

```c

{% raw %}
16 |       return 1;
17 |     }
18 | 
19 |   fcn = (void (*)(void)) dlsym(handle, "foo");
20 |   if (!fcn)
21 |     {
22 |       printf("dlsym foo: %s\n", dlerror ());
23 |       ret += 1;
24 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/dl6dmain.c

```c

{% raw %}
16 |       return 1;
17 |     }
18 | 
19 |   fcn = (void (*)(void)) dlsym(handle, "foo");
20 |   if (!fcn)
21 |     {
22 |       printf("dlsym foo: %s\n", dlerror ());
23 |       ret += 1;
24 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/pr21964-5.c

```c

{% raw %}
10 | {
11 |   static int my_var __attribute__((section("__verbose"), used)) = 6;
12 |   int *ptr;
13 |   ptr = (int*) dlsym(RTLD_DEFAULT, "__start___verbose");
14 |   if (!ptr || *ptr != 6)
15 |     return -1;
{% endraw %}

```
### ld/testsuite/ld-elf/dl6bmain.c

```c

{% raw %}
16 |       return 1;
17 |     }
18 | 
19 |   fcn = (void (*)(void)) dlsym(handle, "foo");
20 |   if (!fcn)
21 |     {
22 |       printf("dlsym foo: %s\n", dlerror ());
23 |       ret += 1;
24 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/dl6amain.c

```c

{% raw %}
16 |       return 1;
17 |     }
18 | 
19 |   fcn = (void (*)(void)) dlsym(handle, "foo");
20 |   if (!fcn)
21 |     {
22 |       printf("dlsym foo: %s\n", dlerror ());
23 |       ret += 1;
24 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/dl6cmain.c

```c

{% raw %}
16 |       return 1;
17 |     }
18 | 
19 |   fcn = (void (*)(void)) dlsym(handle, "foo");
20 |   if (!fcn)
21 |     {
22 |       printf("dlsym foo: %s\n", dlerror ());
23 |       ret += 1;
24 |     }
{% endraw %}

```
### ld/testsuite/ld-elf/pr21964-2c.c

```c

{% raw %}
15 |   if (!dl)
16 |     return 2;
17 | 
18 |   sym = dlsym(dl, "__start___verbose");
19 |   if (!sym)
20 |     return 3;
21 | 
22 |   func = dlsym(dl, "foo2");
23 |   if (!func)
24 |     return 4;
{% endraw %}

```
### ld/testsuite/ld-elf/pr21964-4.c

```c

{% raw %}
6 | {
7 |   static int my_var __attribute__ ((section("__verbose"), used)) = 6;
8 |   int *ptr;
9 |   ptr = (int*) dlsym (RTLD_DEFAULT, "__start___verbose");
10 |   if (ptr != NULL || __start___verbose[0] != 6)
11 |     return -1;
{% endraw %}

```
### ld/testsuite/ld-pe/vers-script-dll.c

```c

{% raw %}
74 | FUNC(lt_dladderror)
75 | FUNC(lt_dladdsearchdir)
76 | FUNC(lt_dlsetsearchpath)
77 | FUNC(lt_dlsym)
78 | FUNC(lt_preloaded_symbols)
79 | FUNC(print)
{% endraw %}

```