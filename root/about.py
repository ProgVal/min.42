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

from common import exceptions
from common import errors
from common import html

body = u"""<h1>Min.42</h1>
<p>min.42 a pour but de vous laisser autant que possible la liberté de choisir
le rapport durée de vie/taille que vous souhaitez (les raccourcisseurs
classiques vous proposent une taille de 7 ou 8 caractères pour une durée
infinie ; pour min.42, une durée de vie infinie correspond à 7 caractères).
<br />
Même si l'inscription est préférée, pour profiter d'un maximum de
fonctionnalités, elle est <strong>totalement</strong> gratuite, et ne demande
pas d'autre information que l'essentiel. Votre mot de passe est hashé
dans notre base de données.
Tout est mis en œuvre pour que votre choix de ne pas vous inscrire soit le
moins pénalisant possible.
<br />
Enfin, Min.42 est sous licence libre. Vous pouvez lire le code sur
<a href="http://github.com/ProgVal/Min.42/">GitHub</a>, vous en servir pour
créer votre propre raccourcisseur d'URLs, le modifier, et le redistribuer,
en respectant les termes de la licence BSD.<br />
Les images utilisées proviennent de la Open Icon Library et sont disponibles
sous licence libre.</p>

<h1>Contenus et liens</h1>
<p>En utilisant ce service, vous acceptez implicitement de ne pas impliquer
ce site et ce service dans une quelconque activité illégale, ce qui inclue
(liste non exhaustive) :
<ul>
    <li>Liens vers des contenus illégaux (warez, pédopornographie, ...)</li>
    <li>Utilisation des liens à des fins répréhensibles (spam, flood,
        piratage, ...)</li>
</ul>
Les liens longs (ceux vers lesquels les liens courts redirigent) sont
sous l'entière responsabilité de l'utilisateur les soumettant, et ne sont en
aucun cas sous la responsabilité de l'auteur du site. Les liens ne sont pas
modérés, rien ne peut donc garantir leur sanité.
</p>

<h1>Contact</h1>
<p>progval+min42(arobase)progval[point]net</p>"""

def run(environ):
    return '200 OK', [], html.getHead(title=u'À propos')+body+html.getFoot()
