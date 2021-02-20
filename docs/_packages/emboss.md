---
name: "emboss"
layout: package
next_package: energyplus
previous_package: emacs
languages: ['c']
---
## 6.6.0
5 / 6463 files match, 1 filtered matches.

 - [plplot/plcore.c](#plplotplcorec)

### plplot/plcore.c

```c

{% raw %}
2523 | 	pldebug("plLoadDriver", "Trying to load %s on %s\n",
2524 | 		driver->drvnam, drvspec );
2525 | 
2526 |         driver->dlhand = lt_dlopenext( drvspec);
2527 |     }
2528 | 
2529 | /* If it still isn't loaded, then we're doomed. */
2530 |     if (!driver->dlhand)
2531 |     {
2532 |         pldebug("plLoadDriver", "lt_dlopenext failed because of "
2533 | 		 "the following reason:\n%s\n", lt_dlerror ());
2534 |         fprintf( stderr, "Unable to load driver: %s.\n", driver->drvnam );
{% endraw %}

```