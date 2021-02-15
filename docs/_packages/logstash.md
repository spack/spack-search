---
name: "logstash"
layout: package
next_package: hsa-rocr-dev
previous_package: kripke
languages: []
---
## 6.6.0
3 / 12042 files match

 - [vendor/jruby/lib/ruby/stdlib/fiddle.rb](#vendorjrubylibrubystdlibfiddlerb)
 - [vendor/jruby/lib/ruby/stdlib/fiddle/import.rb](#vendorjrubylibrubystdlibfiddleimportrb)
 - [vendor/bundle/jruby/2.3.0/gems/bundler-1.9.10/lib/bundler/runtime.rb](#vendorbundlejruby230gemsbundler-1910libbundlerruntimerb)

### vendor/jruby/lib/ruby/stdlib/fiddle.rb

```

{% raw %}
50 |   # call-seq: dlopen(library) => Fiddle::Handle
56 |   # is the equivalent to RTLD_DEFAULT. See <code>man 3 dlopen</code> for more.
58 |   #   lib = Fiddle.dlopen(nil)
65 |   def dlopen library
68 |   module_function :dlopen
{% endraw %}

```
### vendor/jruby/lib/ruby/stdlib/fiddle/import.rb

```

{% raw %}
67 |     # Fiddle::Handle using Fiddle.dlopen
71 |     # See Fiddle.dlopen
83 |             Fiddle.dlopen(lib)
{% endraw %}

```
### vendor/bundle/jruby/2.3.0/gems/bundler-1.9.10/lib/bundler/runtime.rb

```

{% raw %}
53 |       /^dlopen\([^)]*\): Library not loaded: (.+)$/i,
{% endraw %}

```