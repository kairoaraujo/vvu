vvu
===

vvu - vio vhost utility

License
=======
Copyright (c) 2014 Kairo Araujo

vvu is vio vhost utility
This program was created to help in managing vhost devices and its hdisks
in PowerVM (vios) servers. It was created for personal use. There are no
guarantees of the author. Use at your own risk.

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

Important:
IBM, PowerVM (a.k.a. vios) are registered trademarks of IBM Corporation in
the United States, other countries, or both.

EMC, inq and emcgrab are registered trademarks of EMC Corporation in the
United States, other countries, or both.

Requirements
============

Python 3.2

System Operation supported: Mac OS X, Linux, Windows and AIX

Utilization
===========

## Menu Options 

VIO VHOST UTILITY

1. Make a vhostX.txt file with hdisks and lun hexa id from the EMC inq.\n
2. Find hdisks using a wwn files
3. Show README (help and instructons)
4. Quit

## Options details 

1.  Make a vhostX.txt file with hdisks and lun hexa id from the EMC inq.

. The lsmap file is output of vio command  '$lsmap -all > lsmap.txt'
. The inq file is output of vio command using EMC inq: 'inq -xxx_wwn > inq.txt'
  (xxx_wwn = clar_wwn, sym_wwn, etc... check inq -h)


2. Find hdisks using a wwn files

. The wwn file is a simple file with wwns line by line

       Sample:
       600601605fd02900b369420ab5cedf11
       600601605fd029008a2dbc62b5cedf11
       600601605fd029005a4d44a5b4cedf11
       600601605fd02900347fb41ab9cedf11
       (...)

. The inq file is output of vio command using EMC inq: 'inq -xxx_wwn > inq.txt'
  (xxx_wwn = clar_wwn, sym_wwn, etc... check inq -h)
  
3. Show README (help and instructions)
 
 . Show that output
 
4. Quit

 . Exit of program
       
Screenshots
===========

https://github.com/kairoaraujo/vvu/wiki

