---
name: "grpc"
layout: package
next_package: abi-compliance-checker
previous_package: p11-kit
languages: []
---
## 1.28.1
1 / 5251 files match

 - [src/csharp/Grpc.Core/Internal/UnmanagedLibrary.cs](#srccsharpgrpccoreinternalunmanagedlibrarycs)

### src/csharp/Grpc.Core/Internal/UnmanagedLibrary.cs

```

{% raw %}
31 |     /// First, the native library is loaded using dlopen (on Unix systems) or using LoadLibrary (on Windows).
40 |         // flags for dlopen
144 |                     return LoadLibraryPosix(Mono.dlopen, Mono.dlerror, libraryPath, out errorMsg);
148 |                     return LoadLibraryPosix(CoreCLR.dlopen, CoreCLR.dlerror, libraryPath, out errorMsg);
150 |                 return LoadLibraryPosix(Linux.dlopen, Linux.dlerror, libraryPath, out errorMsg);
154 |                 return LoadLibraryPosix(MacOSX.dlopen, MacOSX.dlerror, libraryPath, out errorMsg);
159 |         private static IntPtr LoadLibraryPosix(Func<string, int, IntPtr> dlopenFunc, Func<IntPtr> dlerrorFunc, string libraryPath, out string errorMsg)
162 |             IntPtr ret = dlopenFunc(libraryPath, RTLD_GLOBAL + RTLD_LAZY);
197 |             internal static extern IntPtr dlopen(string filename, int flags);
209 |             internal static extern IntPtr dlopen(string filename, int flags);
219 |         /// On Linux systems, using using dlopen and dlsym results in
222 |         /// dlopen and dlsym from the current process as on Linux
228 |             internal static extern IntPtr dlopen(string filename, int flags);
239 |         /// dlopen and dlsym from the "libcoreclr.so",
245 |             internal static extern IntPtr dlopen(string filename, int flags);
{% endraw %}

```