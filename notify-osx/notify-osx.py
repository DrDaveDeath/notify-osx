#!/usr/bin/env python
#
# OSX Notification script for NZBGet
#
# Copyright (C) 2014 David Ambler
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
##############################################################################
### NZBGET QUEUE/POST-PROCESSING SCRIPT                                    ###

# Sends a OSX Notification via Notification Center.
#
# NOTE: This script requires Python to be installed on your system.

##############################################################################
### OPTIONS																                                 ###

# Notify on success (yes, no).
#
#Success=yes

# Notify on failure (yes, no).
#
#Failure=yes

# Notify upon adding a new NZB file (yes, no).
#
#New=yes

### NZBGET QUEUE/POST-PROCESSING SCRIPT										                 ###
##############################################################################

import os
import sys

on_success = os.environ.get('NZBPO_SUCCESS')
on_failure = os.environ.get('NZBPO_FAILURE')
on_new = os.environ.get('NZBPO_NEW')

SCRIPT_SUCCESS = 93

# Function to send OSX notification
def notify(title, message):
    t = '-title {!r}'.format(title)
    m = '-message {!r}'.format(message)
    s = '-sender {!r}'.format('net.sourceforge.nzbget')
    directory = str(os.path.dirname(os.path.realpath(__file__))).replace('\\', '\\\\')
    os.system(directory + '/terminal-notifier.app/Contents/MacOS/terminal-notifier {}'.format(' '.join([m, t, s])))

# If download is a success
if os.environ.get('NZBPP_TOTALSTATUS') == 'SUCCESS' and on_success == 'yes':
  file_name = os.environ.get('NZBPP_NZBNAME').replace('.',' ')
  notify(title = 'Download Complete', message  = file_name)

# If download has failed
if os.environ.get('NZBPP_TOTALSTATUS') == 'FAILURE' and on_failure == 'yes':
  file_name = os.environ.get('NZBPP_NZBNAME').replace('.',' ')
  notify(title = 'Download Failed', message  = file_name)

# When NZB added to Queue
if os.environ.get('NZBNA_EVENT') == 'NZB_ADDED' and on_new == 'yes':
  file_name = os.environ.get('NZBNA_FILENAME').replace('.',' ').rstrip('nzb')
  notify(title = 'NZB added to Queue', message = file_name)

sys.exit(SCRIPT_SUCCESS)
