---
name: "darshan-util"
layout: package
next_package: dcap
previous_package: darshan-runtime
languages: ['python']
---
## develop
2 / 409 files match, 1 filtered matches.

 - [darshan-util/pydarshan/darshan/discover_darshan.py](#darshan-utilpydarshandarshandiscover_darshanpy)

### darshan-util/pydarshan/darshan/discover_darshan.py

```python

{% raw %}
135 |     Try different methods to discover darshan-util:
136 | 
137 |     Precedence:
138 |     1) Try if the current environment allows dlopen to load libdarshan-util
139 |     2) Try if darshan-parser is exposed via PATH, and attempt loading relative to it.
140 |     3) Try if darshan is exposed via pkgconfig
147 |     """
148 |     if libdutil is None:
149 |         try:
150 |             libdutil = ffi.dlopen("libdarshan-util.so")
151 |         except:
152 |             libdutil = None
155 |         try:
156 |             library_path = discover_darshan_shutil()
157 |             logger.debug(f"Attempting library_path={library_path} via shutil discovery.")
158 |             libdutil = ffi.dlopen(library_path + "/lib/libdarshan-util.so")
159 |         except:
160 |             libdutil = None
163 |         try:
164 |             library_path = discover_darshan_pkgconfig()
165 |             logger.debug(f"Attempting library_path={library_path} via pkgconfig discovery.")
166 |             libdutil = ffi.dlopen(library_path + "/lib/libdarshan-util.so")
167 |         except:
168 |             libdutil = None
175 |             logger.debug(f"Attempting library_path={library_path} in case of binary wheel.")
176 |             save = os.getcwd()
177 |             os.chdir(darshan_path)
178 |             libdutil = ffi.dlopen(library_path)
179 |             os.chdir(save)
180 |         except:
188 |             logger.debug(f"Attempting library_path={library_path} for pyinstaller bundles.")
189 |             save = os.getcwd()
190 |             os.chdir(darshan_path)
191 |             libdutil = ffi.dlopen(library_path)
192 |             os.chdir(save)
193 |         except:
{% endraw %}

```