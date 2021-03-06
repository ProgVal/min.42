# -*- coding: utf8 -*-

# Copyright (c) 2010, Valentin Lorentz
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# * Neither the name of the University of California, Berkeley nor the
# names of its contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE REGENTS AND CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os

################################
# Configuration
FILE = 'database.sqlite'
################################

if not os.path.isfile(FILE):
    populateDb = True
else:
    populateDb = False

import sqlite3
conn = sqlite3.connect(FILE, check_same_thread = False)

cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS `tiny2full` (
                      `tiny` varchar(10),
                      `u_id` int(10),
                      `full` varchar(65536),
                      `submit_time` int(10),
                      `expiry` int(10),
                      PRIMARY KEY(`tiny`)
                  );""")
cursor.execute("""CREATE TABLE IF NOT EXISTS `users` (
                      `u_id` int(10),
                      `name` varchar(40),
                      `passwdhash` varchar(100),
                      `email` varchar(200),
                      PRIMARY KEY(`u_id`)
                  );""")
cursor.execute("""CREATE TABLE IF NOT EXISTS `clicks` (
                    `tiny` varchar(10),
                    `u_id` int(10),
                    `time` int(10)
                 );""")
