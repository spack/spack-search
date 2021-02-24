---
name: "gnupg"
layout: package
next_package: legion
previous_package: unifyfs
library_name: dlsym
matches: ['dlsym', 'dlopen']
languages: ['c']
---
## 2.2.15
5 / 1018 files match, 4 filtered matches.

 - [scd/apdu.c](#scdapduc)
 - [common/iobuf.c](#commoniobufc)
 - [common/homedir.c](#commonhomedirc)
 - [common/dynload.h](#commondynloadh)

### scd/apdu.c

```c

{% raw %}
1959 |           return -1;
1960 |         }
1961 | 
1962 |       pcsc_establish_context = dlsym (handle, "SCardEstablishContext");
1963 |       pcsc_release_context   = dlsym (handle, "SCardReleaseContext");
1964 |       pcsc_list_readers      = dlsym (handle, "SCardListReaders");
1965 | #if defined(_WIN32) || defined(__CYGWIN__)
1966 |       if (!pcsc_list_readers)
1967 |         pcsc_list_readers    = dlsym (handle, "SCardListReadersA");
1968 | #endif
1969 |       pcsc_get_status_change = dlsym (handle, "SCardGetStatusChange");
1970 | #if defined(_WIN32) || defined(__CYGWIN__)
1971 |       if (!pcsc_get_status_change)
1972 |         pcsc_get_status_change = dlsym (handle, "SCardGetStatusChangeA");
1973 | #endif
1974 |       pcsc_connect           = dlsym (handle, "SCardConnect");
1975 | #if defined(_WIN32) || defined(__CYGWIN__)
1976 |       if (!pcsc_connect)
1977 |         pcsc_connect         = dlsym (handle, "SCardConnectA");
1978 | #endif
1979 |       pcsc_reconnect         = dlsym (handle, "SCardReconnect");
1980 | #if defined(_WIN32) || defined(__CYGWIN__)
1981 |       if (!pcsc_reconnect)
1982 |         pcsc_reconnect       = dlsym (handle, "SCardReconnectA");
1983 | #endif
1984 |       pcsc_disconnect        = dlsym (handle, "SCardDisconnect");
1985 |       pcsc_status            = dlsym (handle, "SCardStatus");
1986 | #if defined(_WIN32) || defined(__CYGWIN__)
1987 |       if (!pcsc_status)
1988 |         pcsc_status          = dlsym (handle, "SCardStatusA");
1989 | #endif
1990 |       pcsc_begin_transaction = dlsym (handle, "SCardBeginTransaction");
1991 |       pcsc_end_transaction   = dlsym (handle, "SCardEndTransaction");
1992 |       pcsc_transmit          = dlsym (handle, "SCardTransmit");
1993 |       pcsc_set_timeout       = dlsym (handle, "SCardSetTimeout");
1994 |       pcsc_control           = dlsym (handle, "SCardControl");
1995 | 
1996 |       if (!pcsc_establish_context
{% endraw %}

```
### common/iobuf.c

```c

{% raw %}
2304 | 	handle = dlopen ("kernel32.dll", RTLD_LAZY);
2305 | 	if (handle)
2306 | 	  {
2307 | 	    get_file_size_ex = dlsym (handle, "GetFileSizeEx");
2308 | 	    if (!get_file_size_ex)
2309 | 	      dlclose (handle);
{% endraw %}

```
### common/homedir.c

```c

{% raw %}
138 |           handle = dlopen (dllnames[i], RTLD_LAZY);
139 |           if (handle)
140 |             {
141 |               func = dlsym (handle, "SHGetFolderPathA");
142 |               if (!func)
143 |                 {
{% endraw %}

```
### common/dynload.h

```c

{% raw %}
54 | }
55 | 
56 | static inline void *
57 | dlsym (void *hd, const char *sym)
58 | {
59 |   if (hd && sym)
{% endraw %}

```