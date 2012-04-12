#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import fapws._evwsgi as evwsgi
from fapws import base
import ming

import settings
from cookie_encoder import encode_cookie

as_code = ''

def application(environ, start_response):
    if environ.get('HTTP_TESTCOOKIE_VALID', 'no') == "yes":
        response_headers = [('Content-type', 'application/x-shockwave-flash')]
        start_response('304 Not Modified', response_headers)
        return []
    response_headers = [('Content-type', 'application/x-shockwave-flash')]
    start_response('200 OK', response_headers)
    m = ming.SWFMovie()
    ac = ming.SWFAction(as_code.replace('#TESTCOOKIE_VALUE#', encode_cookie(environ.get(settings.HTTP_TESTCOOKIE_VALUE, '')
                                    )).replace('#TESTCOOKIE_NAME#', environ.get(settings.HTTP_TESTCOOKIE_NAME, '')))
    m.add(ac)
    return [m.as_buffer()]

if __name__=="__main__":
    as_code = open(settings.AS_FILE).read()
    if not as_code:
        sys.exit('Check your ActionScript code')
    evwsgi.start(settings.LISTEN, settings.PORT)
    evwsgi.set_base_module(base)
    evwsgi.wsgi_cb(("/", application))
#    evwsgi.set_debug(0)
    evwsgi.run()
