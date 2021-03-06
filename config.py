#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    CERTitude: the seeker of IOC
    Copyright (c) 2016 CERT-W
    
    Contact: cert@wavestone.com
    Contributors: @iansus, @nervous, @fschwebel
    
    CERTitude is under licence GPL-2.0:
    This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation; either version 2
    of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''

# Global
# ======
## passage en mode debug : log plus d'infos sur le déroulement
DEBUG = True
DOSSIER_LOG = '_log/'
FORMAT_LOGS = '%(asctime)s %(name)-14s %(levelname)-8s %(message)s'

# SSL configuration
USE_SSL = False
SSL_KEY_FILE = 'ssl\\server.pem.key'
SSL_CERT_FILE = 'ssl\\server.pem.cer'


INTERFACE_HASH_SALT = '' # nocommit
SECONDES_POUR_RESCAN = 300 # secondes mini entre un résultat et une nouvelle demande

SLEEP = 5 # nombre de secondes entre les interrogations de la base
SECONDES_ENTRE_TENTATIVES = 300 # secondes entre les essais sur une même IP
BASE_DE_DONNEES_QUEUE = "sqlite:///data.db"

# IOC Scanner
# ===========

IOC_MODE = 'flat'           # flat | logic ## DO NOT USE "logic" for now !!!
IOC_KEEPFILES = False       # True | False
IOC_CONFIDENTIAL_DIRECTORY = 'DR_PLUS' # \components\iocscan\DR_PLUS
IOC_COMPONENT_ROOT = 'components\\scanner'
IOC_TEMP_DIR = 'components\\scanner\\tmp'