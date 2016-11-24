#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4:et

import pycurl
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://pal2-sap-cvmatcher.cfapps.sap.hana.ondemand.com/cvr/sso')
c.setopt(c.COOKIEFILE, 'cookie.txt')
c.setopt(c.COOKIEJAR, 'cookie.txt')
c.setopt(c.FOLLOWLOCATION, True)
c.setopt(c.SSL_VERIFYPEER, False)
c.setopt(c.SSL_VERIFYHOST, False)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
body = buffer.getvalue()
print(body.decode('iso-8859-1'))

#c.setopt(c.URL, 'https://pal2-sap-cvmatcher.cfapps.sap.hana.ondemand.com/cvr/cvfile/5834d464e04ed2001daafed1')
