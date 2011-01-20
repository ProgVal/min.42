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

import copy
from common import user

head = u"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr">
<head>
<title>%(title)s</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" media="screen" type="text/css" href="/static/design.css" />
</head>
<body>
<div id="header">
<img src="/static/logo.png" alt="logo" />
</div>
<table id="menu">
<tr>
<td>%(username)s</td>
%(menu)s
</tr>
</table>
<div id="body">
"""
menuTemplate = [('tinyfy', '/', 'URLs raccourcies'),
        ('about', '/about/', u'À propos')]
def getHead(**kwargs):
    global menuTemplate
    menu = copy.deepcopy(menuTemplate)
    if kwargs.has_key('menu'):
        menu += kwargs['menu']
    params = kwargs
    if not params.has_key('title'):
        params.update({'title': 'min.42'})
    else:
        params['title'] += ' - min.42'
    if user.currentUser.name == 'anonyme':
        menu += [('connect', '/connect/', 'Connexion')]
        menu += [('register', '/register/', 'Inscription')]
    else:
        menu += [('disconnect', '/disconnect/', u'Déconnexion')]
    strMenu = ''
    for image, link, name in menu:
        strMenu += u"""
<td>
<a href="%s">
<img src="/static/%s.png" alt="%s" title="%s" />
<br />
%s
</a>
</td>""" % (link, image, image, name, name)
    params.update({'menu': strMenu,
                   'username': unicode(user.currentUser.name),
                   'connection': ''})
    return head % params


foot = u"""
</div>
<p id="footer">
Site conçu par <a href="mailto:progval@gmail.com">ProgVal</a> et
disponible sous licence BSD.
</p>
</body>
</html>
"""
def getFoot(**kwargs):
    global foot
    return foot
