---
name: "openfoam"
layout: package
next_package: valgrind
previous_package: nbdkit
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 1806
1 / 11471 files match, 1 filtered matches.

 - [src/OSspecific/POSIX/POSIX.C](#srcosspecificposixposixc)

### src/OSspecific/POSIX/POSIX.C

```c

{% raw %}
1547 |     {
1548 |         std::cout
1549 |             << "dlSym(void*, const std::string&)"
1550 |             << " : dlsym of " << symbol << std::endl;
1551 |     }
1552 |     // clear any old errors - see manpage dlopen
1553 |     (void) ::dlerror();
1554 | 
1555 |     // get address of symbol
1556 |     void* fun = ::dlsym(handle, symbol.c_str());
1557 | 
1558 |     // find error (if any)
1577 |         {
1578 |             std::cout
1579 |                 << "dlSymFound(void*, const std::string&)"
1580 |                 << " : dlsym of " << symbol << std::endl;
1581 |         }
1582 | 
1584 |         (void) ::dlerror();
1585 | 
1586 |         // get address of symbol
1587 |         (void) ::dlsym(handle, symbol.c_str());
1588 | 
1589 |         // symbol can be found if there was no error
{% endraw %}

```