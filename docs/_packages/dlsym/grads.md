---
name: "grads"
layout: package
next_package: graphicsmagick
previous_package: gpgme
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.2.1
5 / 515 files match, 3 filtered matches.

 - [src/gafunc.c](#srcgafuncc)
 - [src/gxsubs.c](#srcgxsubsc)
 - [src/gradspy.c](#srcgradspyc)

### src/gafunc.c

```c

{% raw %}
7218 |       return (1);
7219 |     }
7220 |     dlerror();
7221 |     pfunc = dlsym(handle,upb->alias);
7222 |     if ((error=dlerror()) != NULL) {
7223 |       snprintf (pout,1255,"Error: dlsym failed to load %s \n%s \n",upb->alias,error);
7224 |       gaprnt (0,pout);
7225 |       return (1);
{% endraw %}

```
### src/gxsubs.c

```c

{% raw %}
196 |   
197 |   /* Get pointers to the printing subroutines */
198 |   dlerror();
199 |   psubs.gxpcfg   = dlsym(phandle,"gxpcfg");
200 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
201 |   psubs.gxpckfont= dlsym(phandle,"gxpckfont");
202 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
203 |   psubs.gxpbgn   = dlsym(phandle,"gxpbgn");   
204 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
205 |   psubs.gxpinit  = dlsym(phandle,"gxpinit");  
206 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
207 |   psubs.gxpend   = dlsym(phandle,"gxpend");   
208 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
209 |   psubs.gxprint  = dlsym(phandle,"gxprint");  
210 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
211 |   psubs.gxpcol   = dlsym(phandle,"gxpcol");   
212 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
213 |   psubs.gxpacol  = dlsym(phandle,"gxpacol");  
214 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
215 |   psubs.gxpwid   = dlsym(phandle,"gxpwid");   
216 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
217 |   psubs.gxprec   = dlsym(phandle,"gxprec");   
218 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
219 |   psubs.gxpbpoly = dlsym(phandle,"gxpbpoly"); 
220 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
221 |   psubs.gxpepoly = dlsym(phandle,"gxpepoly"); 
222 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
223 |   psubs.gxpmov   = dlsym(phandle,"gxpmov");   
224 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
225 |   psubs.gxpdrw   = dlsym(phandle,"gxpdrw");   
226 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
227 |   psubs.gxpflush = dlsym(phandle,"gxpflush"); 
228 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
229 |   psubs.gxpsignal= dlsym(phandle,"gxpsignal");
230 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
231 |   psubs.gxpclip  = dlsym(phandle,"gxpclip");  
232 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
233 |   psubs.gxpch    = dlsym(phandle,"gxpch");    
234 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
235 |   psubs.gxpqchl  = dlsym(phandle,"gxpqchl");  
236 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
237 |   
238 |   /* get pointers to the display (hardware) subroutines, some are needed even in batch mode */
239 |   dsubs.gxdcfg   = dlsym(dhandle,"gxdcfg");
240 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
241 |   dsubs.gxdckfont= dlsym(dhandle,"gxdckfont");
242 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(1);}
243 |   dsubs.gxdbb    = dlsym(dhandle,"gxdbb"); 
244 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
245 |   dsubs.gxdfb    = dlsym(dhandle,"gxdfb"); 
246 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
247 |   dsubs.gxdacol  = dlsym(dhandle,"gxdacol"); 
248 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
249 |   dsubs.gxdbat   = dlsym(dhandle,"gxdbat"); 
250 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
251 |   dsubs.gxdbgn   = dlsym(dhandle,"gxdbgn"); 
252 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
253 |   dsubs.gxdbtn   = dlsym(dhandle,"gxdbtn"); 
254 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
255 |   dsubs.gxdch    = dlsym(dhandle,"gxdch"); 
256 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
257 |   dsubs.gxdclip  = dlsym(dhandle,"gxdclip"); 
258 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
259 |   dsubs.gxdcol   = dlsym(dhandle,"gxdcol"); 
260 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
261 |   dsubs.gxddbl   = dlsym(dhandle,"gxddbl"); 
262 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
263 |   dsubs.gxddrw   = dlsym(dhandle,"gxddrw"); 
264 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
265 |   dsubs.gxdend   = dlsym(dhandle,"gxdend"); 
266 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
267 |   dsubs.gxdfil   = dlsym(dhandle,"gxdfil"); 
268 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
269 |   dsubs.gxdfrm   = dlsym(dhandle,"gxdfrm"); 
270 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
271 |   dsubs.gxdgcoord= dlsym(dhandle,"gxdgcoord"); 
272 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
273 |   dsubs.gxdgeo   = dlsym(dhandle,"gxdgeo"); 
274 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
275 |   dsubs.gxdimg   = dlsym(dhandle,"gxdimg"); 
276 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
277 |   dsubs.gxdlg    = dlsym(dhandle,"gxdlg"); 
278 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
279 |   dsubs.gxdmov   = dlsym(dhandle,"gxdmov"); 
280 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
281 |   dsubs.gxdopt   = dlsym(dhandle,"gxdopt"); 
282 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
283 |   dsubs.gxdpbn   = dlsym(dhandle,"gxdpbn"); 
284 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
285 |   dsubs.gxdptn   = dlsym(dhandle,"gxdptn"); 
286 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
287 |   dsubs.gxdptn   = dlsym(dhandle,"gxdptn"); 
288 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
289 |   dsubs.gxdqchl  = dlsym(dhandle,"gxdqchl"); 
290 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
291 |   dsubs.gxdrbb   = dlsym(dhandle,"gxdrbb"); 
292 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
293 |   dsubs.gxdrec   = dlsym(dhandle,"gxdrec"); 
294 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
295 |   dsubs.gxdrmu   = dlsym(dhandle,"gxdrmu"); 
296 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
297 |   dsubs.gxdsfr   = dlsym(dhandle,"gxdsfr"); 
298 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
299 |   dsubs.gxdsgl   = dlsym(dhandle,"gxdsgl"); 
300 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
301 |   dsubs.gxdsignal= dlsym(dhandle,"gxdsignal"); 
302 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
303 |   dsubs.gxdssh   = dlsym(dhandle,"gxdssh"); 
304 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
305 |   dsubs.gxdssv   = dlsym(dhandle,"gxdssv"); 
306 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
307 |   dsubs.gxdswp   = dlsym(dhandle,"gxdswp"); 
308 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
309 |   dsubs.gxdwid   = dlsym(dhandle,"gxdwid"); 
310 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
311 |   dsubs.gxdXflush= dlsym(dhandle,"gxdXflush"); 
312 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
313 |   dsubs.gxdxsz   = dlsym(dhandle,"gxdxsz"); 
314 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
315 |   dsubs.gxrs1wd  = dlsym(dhandle,"gxrs1wd"); 
316 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
317 |   dsubs.gxsetpatt= dlsym(dhandle,"gxsetpatt"); 
318 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
319 |   dsubs.win_data = dlsym(dhandle,"win_data"); 
320 |   if ((err=dlerror())!=NULL) {printf("Error in gxload: %s\n",err); return(2);}
321 |   return(0);
{% endraw %}

```
### src/gradspy.c

```c

{% raw %}
251 |   } 
252 |   else {
253 | 
254 |     pgainit = dlsym(handle, "gamain");    /* starts GrADS */
255 |     if ((error = dlerror()) != NULL)  {
256 |       fputs(error, stderr);
258 |       gapyerror = 1;
259 |     } 
260 |     
261 |     pdocmd = dlsym(handle, "gagsdo");     /* executes a command */
262 |     if ((error = dlerror()) != NULL)  {
263 |       fputs(error, stderr);
265 |       gapyerror = 1;
266 |     }
267 |     
268 |     pdoexpr = dlsym(handle, "gadoexpr");  /* evaluates an expression */
269 |     if ((error = dlerror()) != NULL)  {
270 |       fputs(error, stderr);
272 |       gapyerror = 1;
273 |     }
274 |     
275 |     pyfre = dlsym(handle, "gapyfre");     /* releases memory after data is copied to Python */
276 |     if ((error = dlerror()) != NULL)  {
277 |       fputs(error, stderr);
{% endraw %}

```