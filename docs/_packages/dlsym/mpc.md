---
name: "mpc"
layout: package
next_package: postgresql
previous_package: extrae
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1.0.2
5 / 222 files match, 1 filtered matches.

 - [src/logging.c](#srcloggingc)

### src/logging.c

```c

{% raw %}
64 | { \
65 |    static c_c_func_ptr func = NULL; \
66 |    if (func == NULL) \
67 |       func = (c_c_func_ptr) (intptr_t) dlsym (NULL, "mpc_"#funcname); \
68 |    MPC_LOGGING_FUNC_TYPE (funcname, c_c); \
69 |    MPC_LOGGING_OUT_PREC (rop); \
77 | { \
78 |    static c_cc_func_ptr func = NULL; \
79 |    if (func == NULL) \
80 |       func = (c_cc_func_ptr) (intptr_t) dlsym (NULL, "mpc_"#funcname); \
81 |    MPC_LOGGING_FUNC_TYPE (funcname, c_cc); \
82 |    MPC_LOGGING_OUT_PREC (rop); \
91 | { \
92 |    static c_ccc_func_ptr func = NULL; \
93 |    if (func == NULL) \
94 |       func = (c_ccc_func_ptr) (intptr_t) dlsym (NULL, "mpc_"#funcname); \
95 |    MPC_LOGGING_FUNC_TYPE (funcname, c_ccc); \
96 |    MPC_LOGGING_OUT_PREC (rop); \
106 | { \
107 |    static cc_c_func_ptr func = NULL; \
108 |    if (func == NULL) \
109 |       func = (cc_c_func_ptr) (intptr_t) dlsym (NULL, "mpc_"#funcname); \
110 |    MPC_LOGGING_FUNC_TYPE (funcname, cc_c); \
111 |    MPC_LOGGING_OUT_PREC (rop1); \
{% endraw %}

```