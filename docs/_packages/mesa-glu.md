---
name: "mesa-glu"
layout: package
next_package: meson
previous_package: mesa
languages: ['c']
---
## 9.0.1
3 / 200 files match, 1 filtered matches.

 - [src/libutil/mipmap.c](#srclibutilmipmapc)

### src/libutil/mipmap.c

```c

{% raw %}
6648 |       if (!pTexImage3D)
6649 | 	 pTexImage3D = (TexImage3Dproc) wglGetProcAddress("glTexImage3DEXT");
6650 | #else
6651 |       void *libHandle = dlopen("libgl.so", RTLD_LAZY);
6652 |       pTexImage3D = (TexImage3Dproc) dlsym(libHandle, "glTexImage3D" );
6653 |       if (!pTexImage3D)
{% endraw %}

```