---
name: "veclibfort"
layout: package
next_package: verrou
previous_package: varnish-cache
languages: ['c']
---
## develop
2 / 17 files match, 1 filtered matches.

 - [vecLibFort.c](#veclibfortc)

### vecLibFort.c

```c

{% raw %}
201 | {
202 |   static const char* veclib_loc = VECLIB_FILE;
203 |   DEBUG( "Loading library: %s\n", veclib_loc )
204 |   veclib = dlopen (veclib_loc, RTLD_LOCAL | RTLD_FIRST);
205 |   if ( veclib == 0 ) {
206 |     fprintf( stderr, "Failed to open vecLib library; aborting.\n   Location: %s\n", veclib );
{% endraw %}

```