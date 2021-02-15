---
name: "transrate"
layout: package
next_package: tinker
previous_package: rocm-debug-agent
languages: []
---
## 1.0.3
3 / 1488 files match

 - [lib/app/ruby/lib/ruby/gems/2.2.0/gems/bundler-1.7.12/lib/bundler/runtime.rb](#libapprubylibrubygems220gemsbundler-1712libbundlerruntimerb)
 - [lib/app/ruby/lib/ruby/2.2.0/fiddle.rb](#libapprubylibruby220fiddlerb)
 - [lib/app/ruby/lib/ruby/2.2.0/fiddle/import.rb](#libapprubylibruby220fiddleimportrb)

### lib/app/ruby/lib/ruby/gems/2.2.0/gems/bundler-1.7.12/lib/bundler/runtime.rb

```

{% raw %}
53 |       /^dlopen\([^)]*\): Library not loaded: (.+)$/i,
{% endraw %}

```
### lib/app/ruby/lib/ruby/2.2.0/fiddle.rb

```

{% raw %}
29 |   # call-seq: dlopen(library) => Fiddle::Handle
35 |   # is the equivalent to RTLD_DEFAULT. See <code>man 3 dlopen</code> for more.
37 |   #   lib = Fiddle.dlopen(nil)
44 |   def dlopen library
47 |   module_function :dlopen
{% endraw %}

```
### lib/app/ruby/lib/ruby/2.2.0/fiddle/import.rb

```

{% raw %}
66 |     # Fiddle::Handle using Fiddle.dlopen
70 |     # See Fiddle.dlopen
82 |             Fiddle.dlopen(lib)
{% endraw %}

```