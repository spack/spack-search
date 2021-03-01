---
name: "perfstubs"
layout: package
next_package: perl
previous_package: pdsh
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## master
2 / 48 files match, 1 filtered matches.

 - [perfstubs_api/timer.c](#perfstubs_apitimerc)

### perfstubs_api/timer.c

```c

{% raw %}
135 |     free_metadata_functions[0] = &ps_tool_free_metadata;
136 | #else
137 |     initialize_functions[0] =
138 |         (ps_initialize_t)dlsym(RTLD_DEFAULT, "ps_tool_initialize");
139 |     if (initialize_functions[0] == NULL) {
140 |         perfstubs_initialized = PERFSTUBS_FAILURE;
142 |     }
143 |     printf("Found ps_tool_initialize(), registering tool\n");
144 |     finalize_functions[0] =
145 |         (ps_finalize_t)dlsym(RTLD_DEFAULT, "ps_tool_finalize");
146 |     pause_measurement_functions[0] =
147 |         (ps_pause_measurement_t)dlsym(RTLD_DEFAULT, "ps_tool_pause_measurement");
148 |     resume_measurement_functions[0] =
149 |         (ps_resume_measurement_t)dlsym(RTLD_DEFAULT, "ps_tool_resume_measurement");
150 |     register_thread_functions[0] =
151 |         (ps_register_thread_t)dlsym(RTLD_DEFAULT, "ps_tool_register_thread");
152 |     dump_data_functions[0] =
153 |         (ps_dump_data_t)dlsym(RTLD_DEFAULT, "ps_tool_dump_data");
154 |     timer_create_functions[0] =
155 |         (ps_timer_create_t)dlsym(RTLD_DEFAULT,
156 |         "ps_tool_timer_create");
157 |     timer_start_functions[0] =
158 |         (ps_timer_start_t)dlsym(RTLD_DEFAULT, "ps_tool_timer_start");
159 |     timer_stop_functions[0] =
160 |         (ps_timer_stop_t)dlsym(RTLD_DEFAULT, "ps_tool_timer_stop");
161 |     start_string_functions[0] =
162 |         (ps_start_string_t)dlsym(RTLD_DEFAULT, "ps_tool_start_string");
163 |     stop_string_functions[0] =
164 |         (ps_stop_string_t)dlsym(RTLD_DEFAULT, "ps_tool_stop_string");
165 |     stop_current_functions[0] =
166 |         (ps_stop_current_t)dlsym(RTLD_DEFAULT, "ps_tool_stop_current");
167 |     set_parameter_functions[0] =
168 |         (ps_set_parameter_t)dlsym(RTLD_DEFAULT, "ps_tool_set_parameter");
169 |     dynamic_phase_start_functions[0] = (ps_dynamic_phase_start_t)dlsym(
170 |         RTLD_DEFAULT, "ps_tool_dynamic_phase_start");
171 |     dynamic_phase_stop_functions[0] = (ps_dynamic_phase_stop_t)dlsym(
172 |         RTLD_DEFAULT, "ps_tool_dynamic_phase_stop");
173 |     create_counter_functions[0] = (ps_create_counter_t)dlsym(
174 |         RTLD_DEFAULT, "ps_tool_create_counter");
175 |     sample_counter_functions[0] = (ps_sample_counter_t)dlsym(
176 |         RTLD_DEFAULT, "ps_tool_sample_counter");
177 |     set_metadata_functions[0] =
178 |         (ps_set_metadata_t)dlsym(RTLD_DEFAULT, "ps_tool_set_metadata");
179 |     get_timer_data_functions[0] = (ps_get_timer_data_t)dlsym(
180 |         RTLD_DEFAULT, "ps_tool_get_timer_data");
181 |     get_counter_data_functions[0] = (ps_get_counter_data_t)dlsym(
182 |         RTLD_DEFAULT, "ps_tool_get_counter_data");
183 |     get_metadata_functions[0] = (ps_get_metadata_t)dlsym(
184 |         RTLD_DEFAULT, "ps_tool_get_metadata");
185 |     free_timer_data_functions[0] = (ps_free_timer_data_t)dlsym(
186 |         RTLD_DEFAULT, "ps_tool_free_timer_data");
187 |     free_counter_data_functions[0] = (ps_free_counter_data_t)dlsym(
188 |         RTLD_DEFAULT, "ps_tool_free_counter_data");
189 |     free_metadata_functions[0] = (ps_free_metadata_t)dlsym(
190 |         RTLD_DEFAULT, "ps_tool_free_metadata");
191 | #endif
{% endraw %}

```