---
name: "hdf5"
layout: package
next_package: r
previous_package: tfel
library_name: dlopen
matches: ['dlsym', 'dlopen']
languages: ['java']
---
## 1.10.2
8 / 2976 files match, 1 filtered matches.

 - [java/test/TestH5PL.java](#javatesttesth5pljava)

### java/test/TestH5PL.java

```java

{% raw %}
27 | 
28 | public class TestH5PL {
29 |     @Rule public TestName testname = new TestName();
30 |     private static String FILENAME = "h5_dlopenChunk.h5";
31 |     private static String DATASETNAME = "DS1";
32 |     private static final int DIM_X = 6;
145 |     }
146 | 
147 |     @Ignore
148 |     public void TestH5PLdlopen() {
149 |         long file_id = -1;
150 |         long filespace_id = -1;
174 |             }
175 |             catch (Exception e) {
176 |                 e.printStackTrace();
177 |                 fail("TestH5PLdlopen H5Fcreate:" + e);
178 |             }
179 | 
184 |             }
185 |             catch (Exception e) {
186 |                 e.printStackTrace();
187 |                 fail("TestH5PLdlopen H5Screate_simple:" + e);
188 |             }
189 | 
193 |             }
194 |             catch (Exception e) {
195 |                 e.printStackTrace();
196 |                 fail("TestH5PLdlopen H5Pcreate:" + e);
197 |             }
198 | 
203 |             }
204 |             catch (Exception e) {
205 |                 e.printStackTrace();
206 |                 fail("TestH5PLdlopen H5Pset_chunk:" + e);
207 |             }
208 | 
216 |             }
217 |             catch (Exception e) {
218 |                 e.printStackTrace();
219 |                 fail("TestH5PLdlopen H5Pset_filter:" + e);
220 |             }
221 | 
227 |             }
228 |             catch (Exception e) {
229 |                 e.printStackTrace();
230 |                 fail("TestH5PLdlopen H5Dcreate:" + e);
231 |             }
232 | 
237 |             }
238 |             catch (Exception e) {
239 |                 e.printStackTrace();
240 |                 fail("TestH5PLdlopen H5Dwrite:" + e);
241 |             }
242 |         }
243 |         catch (Throwable err) {
244 |             err.printStackTrace();
245 |             fail("TestH5PLdlopen " + err);
246 |         }
247 |         finally {
{% endraw %}

```