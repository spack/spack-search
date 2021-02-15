---
name: "nim"
layout: package
next_package: opari2
previous_package: biobloom
languages: ['html', 'cpp']
---
## 0.19.6
9 / 7503 files match

 - [lib/posix/posix.nim](#libposixposixnim)
 - [lib/system/dyncalls.nim](#libsystemdyncallsnim)
 - [lib/pure/dynlib.nim](#libpuredynlibnim)
 - [tests/realtimeGC/cmain.c](#testsrealtimegccmainc)
 - [doc/nimc.rst](#docnimcrst)
 - [doc/backends.rst](#docbackendsrst)
 - [doc/html/backends.html](#dochtmlbackendshtml)
 - [doc/html/posix.html](#dochtmlposixhtml)
 - [doc/html/nimc.html](#dochtmlnimchtml)

### lib/posix/posix.nim

```

{% raw %}
170 | proc dlopen*(a1: cstring, a2: cint): pointer {.importc, header: "<dlfcn.h>".}
{% endraw %}

```
### lib/system/dyncalls.nim

```

{% raw %}
24 |   when not defined(nimDebugDlOpen) and not defined(windows):
25 |     stderr.rawWrite("compile with -d:nimDebugDlOpen for more information\n")
66 |   proc dlopen(path: cstring, mode: cint): LibHandle {.
77 |     result = dlopen(path, RTLD_NOW)
78 |     when defined(nimDebugDlOpen):
{% endraw %}

```
### lib/pure/dynlib.nim

```

{% raw %}
125 |   proc dlopen(path: cstring, mode: int): LibHandle {.
133 |     return dlopen(path, flags)
134 |   proc loadLib(): LibHandle = return dlopen(nil, RTLD_NOW)
148 |   proc dlopen(path: cstring, mode: int): LibHandle =
149 |     raise newException(OSError, "dlopen not implemented on Nintendo Switch!")
{% endraw %}

```
### tests/realtimeGC/cmain.c

```cpp

{% raw %}
31 |     hndl = (void*) dlopen((char const*)"./tests/realtimeGC/libshared.so", RTLD_LAZY);
{% endraw %}

```
### doc/nimc.rst

```

{% raw %}
313 | 2. Dynamic calls. DevkitPro libraries have no dlopen/dlclose functions.
{% endraw %}

```
### doc/backends.rst

```

{% raw %}
290 | use ``-ldl`` too to link in required dlopen functionality.
{% endraw %}

```
### doc/html/backends.html

```html

{% raw %}
1359 | <p>The Nim compiler will handle linking the source files generated in the <tt class="docutils literal"><span class="pre">nimcache</span></tt> directory into the <tt class="docutils literal"><span class="pre">libfib.nim.a</span></tt> static library, which you can then link into your C program.  Note that these commands are generic and will vary for each system. For instance, on Linux systems you will likely need to use <tt class="docutils literal"><span class="pre">-ldl</span></tt> too to link in required dlopen functionality.</p>
{% endraw %}

```
### doc/html/posix.html

```html

{% raw %}
3180 |   <li><a class="reference" href="#dlopen%2Ccstring%2Ccint"
3181 |     title="dlopen(a1: cstring; a2: cint): pointer"><wbr />dlopen<span class="attachedType" style="visibility:hidden"></span></a></li>
12681 | <a id="dlopen,cstring,cint"></a>
12682 | <dt><pre><span class="Keyword">proc</span> <span class="Identifier">dlopen</span><span class="Other">(</span><span class="Identifier">a1</span><span class="Other">:</span> <a href="system.html#cstring"><span class="Identifier">cstring</span></a><span class="Other">;</span> <span class="Identifier">a2</span><span class="Other">:</span> <a href="system.html#cint"><span class="Identifier">cint</span></a><span class="Other">)</span><span class="Other">:</span> <a href="system.html#pointer"><span class="Identifier">pointer</span></a> <span><span class="Other">{</span><span class="Other pragmadots">...</span><span class="Other">}</span></span><span class="pragmawrap"><span class="Other">{.</span><span class="pragma"><span class="Identifier">importc</span><span class="Other">,</span> <span class="Identifier">header</span><span class="Other">:</span> <span class="StringLit">&quot;&lt;dlfcn.h&gt;&quot;</span></span><span class="Other">.}</span></span></pre></dt>
{% endraw %}

```
### doc/html/nimc.html

```html

{% raw %}
1621 | <li>Dynamic calls. DevkitPro libraries have no dlopen/dlclose functions.</li>
{% endraw %}

```