---
name: "node-js"
layout: package
next_package: sed
previous_package: wget
languages: ['json', 'html', 'cpp', 'python', 'js']
---
## 13.5.0
46 / 16565 files match

 - [src/node_process_methods.cc](#srcnode_process_methodscc)
 - [src/node_constants.cc](#srcnode_constantscc)
 - [src/node_binding.cc](#srcnode_bindingcc)
 - [lib/constants.js](#libconstantsjs)
 - [lib/internal/bootstrap/node.js](#libinternalbootstrapnodejs)
 - [lib/internal/modules/cjs/loader.js](#libinternalmodulescjsloaderjs)
 - [test/parallel/test-binding-constants.js](#testparalleltest-binding-constantsjs)
 - [test/parallel/test-process-dlopen-undefined-exports.js](#testparalleltest-process-dlopen-undefined-exportsjs)
 - [test/addons/dlopen-ping-pong/test-worker.js](#testaddonsdlopen-ping-pongtest-workerjs)
 - [test/addons/dlopen-ping-pong/binding.cc](#testaddonsdlopen-ping-pongbindingcc)
 - [test/addons/dlopen-ping-pong/test.js](#testaddonsdlopen-ping-pongtestjs)
 - [test/addons/dlopen-ping-pong/ping.c](#testaddonsdlopen-ping-pongpingc)
 - [deps/openssl/openssl/crypto/dso/dso_locl.h](#depsopensslopensslcryptodsodso_loclh)
 - [deps/openssl/openssl/crypto/dso/dso_dlfcn.c](#depsopensslopensslcryptodsodso_dlfcnc)
 - [deps/v8/src/third_party/vtune/jitprofiling.cc](#depsv8srcthird_partyvtunejitprofilingcc)
 - [deps/v8/src/third_party/vtune/ittnotify_config.h](#depsv8srcthird_partyvtuneittnotify_configh)
 - [deps/v8/src/base/debug/stack_trace_posix.cc](#depsv8srcbasedebugstack_trace_posixcc)
 - [deps/uv/configure.ac](#depsuvconfigureac)
 - [deps/uv/src/win/dl.c](#depsuvsrcwindlc)
 - [deps/uv/src/unix/darwin-proctitle.c](#depsuvsrcunixdarwin-proctitlec)
 - [deps/uv/src/unix/fsevents.c](#depsuvsrcunixfseventsc)
 - [deps/uv/src/unix/dl.c](#depsuvsrcunixdlc)
 - [deps/uv/include/uv.h](#depsuvincludeuvh)
 - [deps/uv/include/uv/win.h](#depsuvincludeuvwinh)
 - [deps/uv/include/uv/unix.h](#depsuvincludeuvunixh)
 - [deps/icu-small/source/common/putil.cpp](#depsicu-smallsourcecommonputilcpp)
 - [deps/npm/node_modules/node-gyp/gyp/pylib/gyp/generator/make.py](#depsnpmnode_modulesnode-gypgyppylibgypgeneratormakepy)
 - [tools/gyp/pylib/gyp/generator/make.py](#toolsgyppylibgypgeneratormakepy)
 - [tools/icu/patches/64/source/common/putil.cpp](#toolsicupatches64sourcecommonputilcpp)
 - [tools/doc/type-parser.js](#toolsdoctype-parserjs)
 - [doc/changelogs/CHANGELOG_V10.md](#docchangelogschangelog_v10md)
 - [doc/changelogs/CHANGELOG_V12.md](#docchangelogschangelog_v12md)
 - [doc/changelogs/CHANGELOG_V9.md](#docchangelogschangelog_v9md)
 - [doc/changelogs/CHANGELOG_V010.md](#docchangelogschangelog_v010md)
 - [doc/changelogs/CHANGELOG_ARCHIVE.md](#docchangelogschangelog_archivemd)
 - [doc/api/all.html](#docapiallhtml)
 - [doc/api/os.json](#docapiosjson)
 - [doc/api/process.json](#docapiprocessjson)
 - [doc/api/modules.md](#docapimodulesmd)
 - [doc/api/process.html](#docapiprocesshtml)
 - [doc/api/modules.html](#docapimoduleshtml)
 - [doc/api/process.md](#docapiprocessmd)
 - [doc/api/os.md](#docapiosmd)
 - [doc/api/all.json](#docapialljson)
 - [doc/api/modules.json](#docapimodulesjson)
 - [doc/api/os.html](#docapioshtml)

### src/node_process_methods.cc

```cpp

{% raw %}
471 |   env->SetMethod(target, "dlopen", binding::DLOpen);
{% endraw %}

```
### src/node_constants.cc

```cpp

{% raw %}
1266 | void DefineDLOpenConstants(Local<Object> target) {
1350 |   Local<Object> dlopen_constants = Object::New(isolate);
1351 |   CHECK(dlopen_constants->SetPrototype(env->context(),
1365 |   DefineDLOpenConstants(dlopen_constants);
1372 |                     OneByteString(isolate, "dlopen"),
1373 |                     dlopen_constants).Check();
{% endraw %}

```
### src/node_binding.cc

```cpp

{% raw %}
110 | // On AIX, dlopen() behaves differently from other operating systems, in that
113 | // We try to work around that by providing wrappers for the dlopen() family of
150 | void* wrapped_dlopen(const char* filename, int flags) {
151 |   CHECK_NOT_NULL(filename);  // This deviates from the 'real' dlopen().
175 |   void* real_handle = dlopen(filename, flags);
210 | #define dlopen node::dlwrapper::wrapped_dlopen
327 |   handle_ = dlopen(filename_.c_str(), flags_);
358 |   int ret = uv_dlopen(filename_.c_str(), &lib_);
409 | // DLOpen is process.dlopen(module, filename, flags).
415 | void DLOpen(const FunctionCallbackInfo<Value>& args) {
422 |     env->ThrowError("process.dlopen needs at least 2 arguments.");
{% endraw %}

```
### lib/constants.js

```js

{% raw %}
34 |              constants.os.dlopen,
{% endraw %}

```
### lib/internal/bootstrap/node.js

```js

{% raw %}
101 |   process.dlopen = rawMethods.dlopen;
{% endraw %}

```
### lib/internal/modules/cjs/loader.js

```js

{% raw %}
1188 |   return process.dlopen(module, path.toNamespacedPath(filename));
{% endraw %}

```
### test/parallel/test-binding-constants.js

```js

{% raw %}
13 |   Object.keys(constants.os).sort(), ['UV_UDP_REUSEADDR', 'dlopen', 'errno',
31 |   constants.zlib, constants.os.dlopen, constants.os.errno, constants.os.signals
{% endraw %}

```
### test/parallel/test-process-dlopen-undefined-exports.js

```js

{% raw %}
8 |   process.dlopen({ exports: undefined }, someBindingPath);
{% endraw %}

```
### test/addons/dlopen-ping-pong/test-worker.js

```js

{% raw %}
4 |   common.skip('dlopen global symbol loading is not supported on this os.');
{% endraw %}

```
### test/addons/dlopen-ping-pong/binding.cc

```cpp

{% raw %}
7 | extern "C" const char* dlopen_pong(void) {
27 |   void* handle = dlopen(*filename, RTLD_LAZY);
30 |   ping_func = reinterpret_cast<ping>(dlsym(handle, "dlopen_ping"));
{% endraw %}

```
### test/addons/dlopen-ping-pong/test.js

```js

{% raw %}
4 |   common.skip('dlopen global symbol loading is not supported on this os.');
11 | console.log('process.dlopen:', bindingPath);
12 | process.dlopen(module, bindingPath,
13 |                os.constants.dlopen.RTLD_NOW | os.constants.dlopen.RTLD_GLOBAL);
19 | // process.dlopen() a require() call fails.
{% endraw %}

```
### test/addons/dlopen-ping-pong/ping.c

```cpp

{% raw %}
2 | const char* dlopen_pong(void);
4 | const char* dlopen_ping(void) {
5 |   return dlopen_pong();
{% endraw %}

```
### deps/openssl/openssl/crypto/dso/dso_locl.h

```cpp

{% raw %}
21 |      * Standard dlopen uses a (void *). Win32 uses a HANDLE. VMS doesn't use
{% endraw %}

```
### deps/openssl/openssl/crypto/dso/dso_dlfcn.c

```cpp

{% raw %}
69 |  * Prior to using the dlopen() function, we should decide on the flag we
78 | #   define DLOPEN_FLAG DL_LAZY
81 | #    define DLOPEN_FLAG RTLD_NOW
83 | #    define DLOPEN_FLAG 0
87 | #  define DLOPEN_FLAG RTLD_NOW  /* Hope this works everywhere else */
92 |  * (void*) returned from dlopen().
100 |     int flags = DLOPEN_FLAG;
115 |     ptr = dlopen(filename, flags);
122 |      * Some dlopen() implementations (e.g. solaris) do no preserve errno, even
385 |                      * sys/ldr.h, loadquery() and dlopen()/RTLD_MEMBER.
446 |     void *ret = NULL, *handle = dlopen(NULL, RTLD_LAZY);
{% endraw %}

```
### deps/v8/src/third_party/vtune/jitprofiling.cc

```cpp

{% raw %}
368 |         m_libHandle = dlopen(dllName, RTLD_LAZY);
377 |         m_libHandle = dlopen(DEFAULT_DLLNAME, RTLD_LAZY);
{% endraw %}

```
### deps/v8/src/third_party/vtune/ittnotify_config.h

```cpp

{% raw %}
275 | #define __itt_load_lib(name)      dlopen(name, RTLD_LAZY)
{% endraw %}

```
### deps/v8/src/base/debug/stack_trace_posix.cc

```cpp

{% raw %}
306 |   // #13 0x00007ffff6215602 in do_dlopen at dl-libc.c:89
309 |   // #16 __GI___libc_dlopen_mode at dl-libc.c:165
{% endraw %}

```
### deps/uv/configure.ac

```

{% raw %}
44 | AC_CHECK_LIB([dl], [dlopen])
{% endraw %}

```
### deps/uv/src/win/dl.c

```cpp

{% raw %}
27 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
{% endraw %}

```
### deps/uv/src/unix/darwin-proctitle.c

```cpp

{% raw %}
82 |   application_services_handle = dlopen("/System/Library/Frameworks/"
86 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### deps/uv/src/unix/fsevents.c

```cpp

{% raw %}
536 |   core_foundation_handle = dlopen("/System/Library/Frameworks/"
543 |   core_services_handle = dlopen("/System/Library/Frameworks/"
{% endraw %}

```
### deps/uv/src/unix/dl.c

```cpp

{% raw %}
32 | int uv_dlopen(const char* filename, uv_lib_t* lib) {
35 |   lib->handle = dlopen(filename, RTLD_LAZY);
{% endraw %}

```
### deps/uv/include/uv.h

```cpp

{% raw %}
1652 | UV_EXTERN int uv_dlopen(const char* filename, uv_lib_t* lib);
{% endraw %}

```
### deps/uv/include/uv/win.h

```cpp

{% raw %}
317 | /* Platform-specific definitions for uv_dlopen support. */
{% endraw %}

```
### deps/uv/include/uv/unix.h

```cpp

{% raw %}
212 | /* Platform-specific definitions for uv_dlopen support. */
{% endraw %}

```
### deps/icu-small/source/common/putil.cpp

```

{% raw %}
142 | #    define HAVE_DLOPEN 0
147 | #   ifndef HAVE_DLOPEN
148 | #    define HAVE_DLOPEN 1
156 | #   define HAVE_DLOPEN 0
2278 | #if U_ENABLE_DYLOAD && HAVE_DLOPEN && !U_PLATFORM_USES_ONLY_WIN32_API
2293 |   ret =  dlopen(libName, RTLD_NOW|RTLD_GLOBAL);
2296 |     printf("dlerror on dlopen(%s): %s\n", libName, dlerror());
{% endraw %}

```
### deps/npm/node_modules/node-gyp/gyp/pylib/gyp/generator/make.py

```python

{% raw %}
156 | # 2) loadable_module, which is generating a module intended for dlopen().
{% endraw %}

```
### tools/gyp/pylib/gyp/generator/make.py

```python

{% raw %}
156 | # 2) loadable_module, which is generating a module intended for dlopen().
{% endraw %}

```
### tools/icu/patches/64/source/common/putil.cpp

```

{% raw %}
142 | #    define HAVE_DLOPEN 0
147 | #   ifndef HAVE_DLOPEN
148 | #    define HAVE_DLOPEN 1
156 | #   define HAVE_DLOPEN 0
2275 | #if U_ENABLE_DYLOAD && HAVE_DLOPEN && !U_PLATFORM_USES_ONLY_WIN32_API
2290 |   ret =  dlopen(libName, RTLD_NOW|RTLD_GLOBAL);
2293 |     printf("dlerror on dlopen(%s): %s\n", libName, dlerror());
{% endraw %}

```
### tools/doc/type-parser.js

```js

{% raw %}
109 |   'os.constants.dlopen': 'os.html#os_dlopen_constants',
{% endraw %}

```
### doc/changelogs/CHANGELOG_V10.md

```

{% raw %}
4376 | * [[`65bd225f13`](https://github.com/nodejs/node/commit/65bd225f13)] - **test**: fix warning in dlopen-ping-pong/binding.cc (Daniel Bevenius) [#19966](https://github.com/nodejs/node/pull/19966)
{% endraw %}

```
### doc/changelogs/CHANGELOG_V12.md

```

{% raw %}
120 | * [[`adee99883a`](https://github.com/nodejs/node/commit/adee99883a)] - **test**: debug output for dlopen-ping-pong test (Sam Roberts) [#29818](https://github.com/nodejs/node/pull/29818)
{% endraw %}

```
### doc/changelogs/CHANGELOG_V9.md

```

{% raw %}
488 |   * make process.dlopen() load well-known symbol (Ben Noordhuis) [#18934](https://github.com/nodejs/node/pull/18934)
549 | * [[`4fae6e3904`](https://github.com/nodejs/node/commit/4fae6e3904)] - **(SEMVER-MINOR)** **src**: make process.dlopen() load well-known symbol (Ben Noordhuis) [#18934](https://github.com/nodejs/node/pull/18934)
550 | * [[`89edbae7ab`](https://github.com/nodejs/node/commit/89edbae7ab)] - **(SEMVER-MINOR)** **src**: clean up process.dlopen() (Ben Noordhuis) [#18934](https://github.com/nodejs/node/pull/18934)
1663 | * [[`8336e4f88e`](https://github.com/nodejs/node/commit/8336e4f88e)] - **test**: add test case for process.dlopen with undefined (Leko) [#17343](https://github.com/nodejs/node/pull/17343)
2248 | * [[`5f22375922`](https://github.com/nodejs/node/commit/5f22375922)] - **(SEMVER-MAJOR)** **src**: add support to pass flags to dlopen (Ezequiel Garcia) [#12794](https://github.com/nodejs/node/pull/12794)
2361 | * [[`16ed116203`](https://github.com/nodejs/node/commit/16ed116203)] - **test**: clean up string concat in dlopen-ping-pong (agilbert) [#15820](https://github.com/nodejs/node/pull/15820)
{% endraw %}

```
### doc/changelogs/CHANGELOG_V010.md

```

{% raw %}
850 | * core: Append filename properly in dlopen on windows (isaacs)
{% endraw %}

```
### doc/changelogs/CHANGELOG_ARCHIVE.md

```

{% raw %}
1297 | * unix: assume that dlopen() may clobber dlerror() (Ben Noordhuis)
{% endraw %}

```
### doc/api/all.html

```html

{% raw %}
2873 | <li><a href="#os_dlopen_constants">dlopen Constants</a></li>
3042 | <li><a href="#process_process_dlopen_module_filename_flags">process.dlopen(module, filename[, flags])</a></li>
40998 | modules loaded with <code>process.dlopen()</code>.</p>
43721 | <h3>dlopen Constants<span><a class="mark" href="#os_dlopen_constants" id="os_dlopen_constants">#</a></span></h3>
43723 | are exported in <code>os.constants.dlopen</code>. See <a href="http://man7.org/linux/man-pages/man3/dlopen.3.html"><code>dlopen(3)</code></a> for detailed
43736 |     <td>Resolve all undefined symbols in the library before dlopen(3)
45660 | <h2>process.dlopen(module, filename[, flags])<span><a class="mark" href="#process_process_dlopen_module_filename_flags" id="process_process_dlopen_module_filename_flags">#</a></span></h2>
45675 | <li><code>flags</code> <a href="#os_dlopen_constants" class="type">&#x3C;os.constants.dlopen></a> <strong>Default:</strong> <code>os.constants.dlopen.RTLD_LAZY</code></li>
45677 | <p>The <code>process.dlopen()</code> method allows to dynamically load shared
45681 | <code>process.dlopen()</code>, unless there are specific reasons.</p>
45682 | <p>The <code>flags</code> argument is an integer that allows to specify dlopen
45683 | behavior. See the <a href="#os_dlopen_constants"><code>os.constants.dlopen</code></a> documentation for details.</p>
45684 | <p>If there are specific reasons to use <code>process.dlopen()</code> (for instance,
45685 | to specify dlopen flags), it's often useful to use <a href="#modules_require_resolve_request_options"><code>require.resolve()</code></a>
45687 | <p>An important drawback when calling <code>process.dlopen()</code> is that the <code>module</code>
45695 | process.dlopen(module, require.resolve('binding'),
45696 |                os.constants.dlopen.RTLD_NOW);
{% endraw %}

```
### doc/api/os.json

```json

{% raw %}
504 |               "textRaw": "dlopen Constants",
505 |               "name": "dlopen_constants",
506 |               "desc": "<p>If available on the operating system, the following constants\nare exported in <code>os.constants.dlopen</code>. See <a href=\"http://man7.org/linux/man-pages/man3/dlopen.3.html\"><code>dlopen(3)</code></a> for detailed\ninformation.</p>\n<table>\n  <tr>\n    <th>Constant</th>\n    <th>Description</th>\n  </tr>\n  <tr>\n    <td><code>RTLD_LAZY</code></td>\n    <td>Perform lazy binding. Node.js sets this flag by default.</td>\n  </tr>\n  <tr>\n    <td><code>RTLD_NOW</code></td>\n    <td>Resolve all undefined symbols in the library before dlopen(3)\n    returns.</td>\n  </tr>\n  <tr>\n    <td><code>RTLD_GLOBAL</code></td>\n    <td>Symbols defined by the library will be made available for symbol\n    resolution of subsequently loaded libraries.</td>\n  </tr>\n  <tr>\n    <td><code>RTLD_LOCAL</code></td>\n    <td>The converse of <code>RTLD_GLOBAL</code>. This is the default behavior\n    if neither flag is specified.</td>\n  </tr>\n  <tr>\n    <td><code>RTLD_DEEPBIND</code></td>\n    <td>Make a self-contained library use its own symbols in preference to\n    symbols from previously loaded libraries.</td>\n  </tr>\n</table>",
508 |               "displayName": "dlopen Constants"
{% endraw %}

```
### doc/api/process.json

```json

{% raw %}
409 |           "textRaw": "process.dlopen(module, filename[, flags])",
411 |           "name": "dlopen",
438 |                   "textRaw": "`flags` {os.constants.dlopen} **Default:** `os.constants.dlopen.RTLD_LAZY`",
440 |                   "type": "os.constants.dlopen",
441 |                   "default": "`os.constants.dlopen.RTLD_LAZY`",
447 |           "desc": "<p>The <code>process.dlopen()</code> method allows to dynamically load shared\nobjects. It is primarily used by <code>require()</code> to load\nC++ Addons, and should not be used directly, except in special\ncases. In other words, <a href=\"globals.html#globals_require\"><code>require()</code></a> should be preferred over\n<code>process.dlopen()</code>, unless there are specific reasons.</p>\n<p>The <code>flags</code> argument is an integer that allows to specify dlopen\nbehavior. See the <a href=\"os.html#os_dlopen_constants\"><code>os.constants.dlopen</code></a> documentation for details.</p>\n<p>If there are specific reasons to use <code>process.dlopen()</code> (for instance,\nto specify dlopen flags), it's often useful to use <a href=\"modules.html#modules_require_resolve_request_options\"><code>require.resolve()</code></a>\nto look up the module's path.</p>\n<p>An important drawback when calling <code>process.dlopen()</code> is that the <code>module</code>\ninstance must be passed. Functions exported by the C++ Addon will be accessible\nvia <code>module.exports</code>.</p>\n<p>The example below shows how to load a C++ Addon, named as <code>binding</code>,\nthat exports a <code>foo</code> function. All the symbols will be loaded before\nthe call returns, by passing the <code>RTLD_NOW</code> constant. In this example\nthe constant is assumed to be available.</p>\n<pre><code class=\"language-js\">const os = require('os');\nprocess.dlopen(module, require.resolve('binding'),\n               os.constants.dlopen.RTLD_NOW);\nmodule.exports.foo();\n</code></pre>"
{% endraw %}

```
### doc/api/modules.md

```

{% raw %}
372 | modules loaded with `process.dlopen()`.
{% endraw %}

```
### doc/api/process.html

```html

{% raw %}
163 | <li><a href="#process_process_dlopen_module_filename_flags">process.dlopen(module, filename[, flags])</a></li>
916 | <h2>process.dlopen(module, filename[, flags])<span><a class="mark" href="#process_process_dlopen_module_filename_flags" id="process_process_dlopen_module_filename_flags">#</a></span></h2>
931 | <li><code>flags</code> <a href="os.html#os_dlopen_constants" class="type">&#x3C;os.constants.dlopen></a> <strong>Default:</strong> <code>os.constants.dlopen.RTLD_LAZY</code></li>
933 | <p>The <code>process.dlopen()</code> method allows to dynamically load shared
937 | <code>process.dlopen()</code>, unless there are specific reasons.</p>
938 | <p>The <code>flags</code> argument is an integer that allows to specify dlopen
939 | behavior. See the <a href="os.html#os_dlopen_constants"><code>os.constants.dlopen</code></a> documentation for details.</p>
940 | <p>If there are specific reasons to use <code>process.dlopen()</code> (for instance,
941 | to specify dlopen flags), it's often useful to use <a href="modules.html#modules_require_resolve_request_options"><code>require.resolve()</code></a>
943 | <p>An important drawback when calling <code>process.dlopen()</code> is that the <code>module</code>
951 | process.dlopen(module, require.resolve('binding'),
952 |                os.constants.dlopen.RTLD_NOW);
{% endraw %}

```
### doc/api/modules.html

```html

{% raw %}
486 | modules loaded with <code>process.dlopen()</code>.</p>
{% endraw %}

```
### doc/api/process.md

```

{% raw %}
795 | ## process.dlopen(module, filename\[, flags\])
806 | * `flags` {os.constants.dlopen} **Default:** `os.constants.dlopen.RTLD_LAZY`
808 | The `process.dlopen()` method allows to dynamically load shared
812 | `process.dlopen()`, unless there are specific reasons.
814 | The `flags` argument is an integer that allows to specify dlopen
815 | behavior. See the [`os.constants.dlopen`][] documentation for details.
817 | If there are specific reasons to use `process.dlopen()` (for instance,
818 | to specify dlopen flags), it's often useful to use [`require.resolve()`][]
821 | An important drawback when calling `process.dlopen()` is that the `module`
832 | process.dlopen(module, require.resolve('binding'),
833 |                os.constants.dlopen.RTLD_NOW);
2446 | [`os.constants.dlopen`]: os.html#os_dlopen_constants
{% endraw %}

```
### doc/api/os.md

```

{% raw %}
1149 | ### dlopen Constants
1152 | are exported in `os.constants.dlopen`. See dlopen(3) for detailed
1166 |     <td>Resolve all undefined symbols in the library before dlopen(3)
{% endraw %}

```
### doc/api/all.json

```json

{% raw %}
39373 |           "desc": "<p>If the exact filename is not found, then Node.js will attempt to load the\nrequired filename with the added extensions: <code>.js</code>, <code>.json</code>, and finally\n<code>.node</code>.</p>\n<p><code>.js</code> files are interpreted as JavaScript text files, and <code>.json</code> files are\nparsed as JSON text files. <code>.node</code> files are interpreted as compiled addon\nmodules loaded with <code>process.dlopen()</code>.</p>\n<p>A required module prefixed with <code>'/'</code> is an absolute path to the file. For\nexample, <code>require('/home/marco/foo.js')</code> will load the file at\n<code>/home/marco/foo.js</code>.</p>\n<p>A required module prefixed with <code>'./'</code> is relative to the file calling\n<code>require()</code>. That is, <code>circle.js</code> must be in the same directory as <code>foo.js</code> for\n<code>require('./circle')</code> to find it.</p>\n<p>Without a leading <code>'/'</code>, <code>'./'</code>, or <code>'../'</code> to indicate a file, the module must\neither be a core module or is loaded from a <code>node_modules</code> folder.</p>\n<p>If the given path does not exist, <code>require()</code> will throw an <a href=\"errors.html#errors_class_error\"><code>Error</code></a> with its\n<code>code</code> property set to <code>'MODULE_NOT_FOUND'</code>.</p>"
42119 |               "textRaw": "dlopen Constants",
42120 |               "name": "dlopen_constants",
42121 |               "desc": "<p>If available on the operating system, the following constants\nare exported in <code>os.constants.dlopen</code>. See <a href=\"http://man7.org/linux/man-pages/man3/dlopen.3.html\"><code>dlopen(3)</code></a> for detailed\ninformation.</p>\n<table>\n  <tr>\n    <th>Constant</th>\n    <th>Description</th>\n  </tr>\n  <tr>\n    <td><code>RTLD_LAZY</code></td>\n    <td>Perform lazy binding. Node.js sets this flag by default.</td>\n  </tr>\n  <tr>\n    <td><code>RTLD_NOW</code></td>\n    <td>Resolve all undefined symbols in the library before dlopen(3)\n    returns.</td>\n  </tr>\n  <tr>\n    <td><code>RTLD_GLOBAL</code></td>\n    <td>Symbols defined by the library will be made available for symbol\n    resolution of subsequently loaded libraries.</td>\n  </tr>\n  <tr>\n    <td><code>RTLD_LOCAL</code></td>\n    <td>The converse of <code>RTLD_GLOBAL</code>. This is the default behavior\n    if neither flag is specified.</td>\n  </tr>\n  <tr>\n    <td><code>RTLD_DEEPBIND</code></td>\n    <td>Make a self-contained library use its own symbols in preference to\n    symbols from previously loaded libraries.</td>\n  </tr>\n</table>",
42123 |               "displayName": "dlopen Constants"
60535 |           "textRaw": "process.dlopen(module, filename[, flags])",
60537 |           "name": "dlopen",
60564 |                   "textRaw": "`flags` {os.constants.dlopen} **Default:** `os.constants.dlopen.RTLD_LAZY`",
60566 |                   "type": "os.constants.dlopen",
60567 |                   "default": "`os.constants.dlopen.RTLD_LAZY`",
60573 |           "desc": "<p>The <code>process.dlopen()</code> method allows to dynamically load shared\nobjects. It is primarily used by <code>require()</code> to load\nC++ Addons, and should not be used directly, except in special\ncases. In other words, <a href=\"globals.html#globals_require\"><code>require()</code></a> should be preferred over\n<code>process.dlopen()</code>, unless there are specific reasons.</p>\n<p>The <code>flags</code> argument is an integer that allows to specify dlopen\nbehavior. See the <a href=\"os.html#os_dlopen_constants\"><code>os.constants.dlopen</code></a> documentation for details.</p>\n<p>If there are specific reasons to use <code>process.dlopen()</code> (for instance,\nto specify dlopen flags), it's often useful to use <a href=\"modules.html#modules_require_resolve_request_options\"><code>require.resolve()</code></a>\nto look up the module's path.</p>\n<p>An important drawback when calling <code>process.dlopen()</code> is that the <code>module</code>\ninstance must be passed. Functions exported by the C++ Addon will be accessible\nvia <code>module.exports</code>.</p>\n<p>The example below shows how to load a C++ Addon, named as <code>binding</code>,\nthat exports a <code>foo</code> function. All the symbols will be loaded before\nthe call returns, by passing the <code>RTLD_NOW</code> constant. In this example\nthe constant is assumed to be available.</p>\n<pre><code class=\"language-js\">const os = require('os');\nprocess.dlopen(module, require.resolve('binding'),\n               os.constants.dlopen.RTLD_NOW);\nmodule.exports.foo();\n</code></pre>"
{% endraw %}

```
### doc/api/modules.json

```json

{% raw %}
60 |           "desc": "<p>If the exact filename is not found, then Node.js will attempt to load the\nrequired filename with the added extensions: <code>.js</code>, <code>.json</code>, and finally\n<code>.node</code>.</p>\n<p><code>.js</code> files are interpreted as JavaScript text files, and <code>.json</code> files are\nparsed as JSON text files. <code>.node</code> files are interpreted as compiled addon\nmodules loaded with <code>process.dlopen()</code>.</p>\n<p>A required module prefixed with <code>'/'</code> is an absolute path to the file. For\nexample, <code>require('/home/marco/foo.js')</code> will load the file at\n<code>/home/marco/foo.js</code>.</p>\n<p>A required module prefixed with <code>'./'</code> is relative to the file calling\n<code>require()</code>. That is, <code>circle.js</code> must be in the same directory as <code>foo.js</code> for\n<code>require('./circle')</code> to find it.</p>\n<p>Without a leading <code>'/'</code>, <code>'./'</code>, or <code>'../'</code> to indicate a file, the module must\neither be a core module or is loaded from a <code>node_modules</code> folder.</p>\n<p>If the given path does not exist, <code>require()</code> will throw an <a href=\"errors.html#errors_class_error\"><code>Error</code></a> with its\n<code>code</code> property set to <code>'MODULE_NOT_FOUND'</code>.</p>"
{% endraw %}

```
### doc/api/os.html

```html

{% raw %}
155 | <li><a href="#os_dlopen_constants">dlopen Constants</a></li>
1275 | <h3>dlopen Constants<span><a class="mark" href="#os_dlopen_constants" id="os_dlopen_constants">#</a></span></h3>
1277 | are exported in <code>os.constants.dlopen</code>. See <a href="http://man7.org/linux/man-pages/man3/dlopen.3.html"><code>dlopen(3)</code></a> for detailed
1290 |     <td>Resolve all undefined symbols in the library before dlopen(3)
{% endraw %}

```