#!/usr/bin/env python
#
# Copyright (c) 2014 Kairo Araujo
#
# vvu is vio vhost utility
# This program was created to help in managing vhost devices and its hdisks
# in PowerVM (vios) servers. It was created for personal use. There are no
# guarantees of the author. Use at your own risk.
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# Important:
# IBM, PowerVM (a.k.a. vios) are registered trademarks of IBM Corporation in
# the United States, other countries, or both.
#
# EMC, inq and emcgrab are registered trademarks of EMC Corporation in the
# United States, other countries, or both.

# import modules
###############################################################################################
import os.path
import time

# functions
###############################################################################################

timestr = time.strftime("%d%m%Y-%H%M%S")

# Class to manager files
class OpenFile:
    def __init__(self, filename, f_file):
        self.filename = filename
        self.f_file = f_file

    # method to select file
    def fileselect(self):
        self.filename = input("What´s the %s file (full path): " % (self.filename))

    # method to check and openfile
    def fileopen(self):
        if os.path.isfile(self.filename):
            self.f_file = open(self.filename)
        else:
            print("File %s not exists." % (self.filename))
            exit()

    # method output file read
    def output(self):
        return self.f_file.readlines()

    # method to close file
    def fileclose(self):
        self.f_file.close()


# function to make a vhostX.txt file with hdisks and lun hexa id from the EMC inq.
def mkvhostfile():

    # load files
    lsmap = OpenFile('lsmap', 'f_lsmap')
    lsmap.fileselect()
    lsmap.fileopen()

    inq = OpenFile('inq', 'f_inq')
    inq.fileselect()
    inq.fileopen()

    vhost = input("What´s the vhost you can list devices: ")
    f_vhost = open("%s_%s.txt" % (vhost, timestr) , 'w')
    print ("Creating file %s_%s.txt ..." % (vhost, timestr))

    chklsmap = 0

    # loop to read lsmap file
    for l_lsmap in lsmap.output():
        # loop find the vhost searchs disks and wwns
        while chklsmap == 1:
            # if found another vhost stop
            if l_lsmap.startswith( 'vhost' ):
                chklsmap += 1
            # search disks
            elif l_lsmap.startswith( 'Backing' ):
                hdisk = l_lsmap.split()
                chkinq = 0
                while chkinq == 0:
                    inq.fileopen()
                    # find in inq file wwns and write file
                    for l_inq in inq.output():
                        if l_inq.startswith( '/dev/r%s ' % (hdisk[2].strip()) ):
                            wwn = l_inq.split()
                            f_vhost.write( '%s    \t%s\n' % (hdisk[2].strip(), wwn[5]))
                            print ('Added %s    \t%s' % (hdisk[2].strip(), wwn[5]))
                            chkinq = 1
                    chkinq = 1
                    inq.fileclose() # close inq file looping
                break
            else:
                break
        # find first vhost
        if chklsmap == 0 and l_lsmap.startswith( vhost ):
                f_vhost.write(l_lsmap)
                chklsmap += 1
    # close files
    lsmap.fileclose()
    f_vhost.close()
    print ("File %s_%s.txt created with success!" % (vhost, timestr))


def findhdisk():

    # load files
    wwnlst = OpenFile('wwnlst', 'f_wwnlst')
    wwnlst.fileselect()
    wwnlst.fileopen()

    inq = OpenFile('inq', 'f_inq')
    inq.fileselect()
    inq.fileopen()

    # create file with results
    wwn_hdisk = open("hdisk_wwn_%s" % (timestr), 'w')
    print ("Creating file wwn_hdisk_%s" % (timestr))

    # two simples look to find entry on files
    for l_wwnlst in wwnlst.output():
        inq.fileopen()
        for l_inq in inq.output():
            wwn = l_inq.split()
            if l_inq.startswith("/dev/rhdisk") and l_wwnlst.strip() == wwn[5].strip():
                hdisk = wwn[0].split('/r')
                print ("Added %s   \t %s" % (hdisk[1], wwn[5]))
                wwn_hdisk.write("%s   \t %s.txt" % (hdisk[1], wwn[5]))
        inq.fileclose()
    wwnlst.fileclose()
    wwn_hdisk.close()

# functions with help texts
def helpmkvhostfile():
    print ("1. Make a vhostX.txt file with hdisks and lun hexa id from the EMC inq.\n\n"
           "     . The lsmap file is output of vio command  '$lsmap -all > lsmap.txt'\n"
           "     . The inq file is output of vio command using EMC inq: 'inq -xxx_wwn > inq.txt'\n"
           "       (xxx_wwn = clar_wwn, sym_wwn, etc... check inq -h)\n\n")

def helpfindhdisk():
    print ("2. Find hdisks using a wwn files\n\n"
           "     . The wwn file is a simple file with wwns line by line\n"
           "       Sample:\n"
           "       600601605fd02900b369420ab5cedf11\n"
           "       600601605fd029008a2dbc62b5cedf11\n"
           "       600601605fd029005a4d44a5b4cedf11\n"
           "       600601605fd02900347fb41ab9cedf11\n"
           "       (...)\n"
           "     . The inq file is output of vio command using EMC inq: 'inq -xxx_wwn > inq.txt'\n"
           "       (xxx_wwn = clar_wwn, sym_wwn, etc... check inq -h)\n\n")


# menu options and main
###############################################################################################

vvuoption = input("\n\nVIO VHOST UTILITY\n"
                  "1. Make a vhostX.txt file with hdisks and lun hexa id from the EMC inq.\n"
                  "2. Find hdisks using a wwn files\n"
                  "3. Show README (help and instructons)\n"
                  "4. Quit\n\n"
                  "Please choose an option: ")

if vvuoption == '1':
    print("Fast help:\n")
    helpmkvhostfile()
    mkvhostfile()

elif vvuoption == '2':
    print("Fast help:\n")
    helpfindhdisk()
    findhdisk()

elif vvuoption == '3':
    print ("3. Show README (help and instructons)\n\n")
    helpmkvhostfile()
    helpfindhdisk()

elif vvuoption == '4':
    print ("4. Quit")
    print ("Quiting...")
    exit()
else:
    print ("Invalid option. Quiting")
    exit()
