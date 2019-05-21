###################################################################################
# 
#    Copyright (C) 2017 MuK IT GmbH
#
#    Odoo Proprietary License v1.0
#    
#    This software and associated files (the 'Software') may only be used 
#    (executed, modified, executed after modifications) if you have
#    purchased a valid license from the authors, typically via Odoo Apps,
#    or if you have received a written agreement from the authors of the
#    Software (see the COPYRIGHT file).
#    
#    You may develop Odoo modules that use the Software as a library 
#    (typically by depending on it, importing it and using its resources),
#    but without copying any source code or material from the Software.
#    You may distribute those modules under the license of your choice,
#    provided that this license is compatible with the terms of the Odoo
#    Proprietary License (For example: LGPL, MIT, or proprietary licenses
#    similar to this one).
#    
#    It is forbidden to publish, distribute, sublicense, or sell copies of
#    the Software or modified copies of the Software.
#    
#    The above copyright notice and this permission notice must be included
#    in all copies or substantial portions of the Software.
#    
#    THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS
#    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
###################################################################################
 
{
    'name': 'MuK REST API for Odoo',
    'summary': 'A customizable Restful API for Odoo',
    'version': '12.0.3.2.3',
    'category': 'Extra Tools',
    'license': 'OPL-1',
    'price': 95.00,
    'currency': 'EUR',
    'author': 'MuK IT',
    'live_test_url': 'https://mukit.at/r/SgN',
    'website': 'http://www.mukit.at',
    'contributors': [
        'Mathias Markl <mathias.markl@mukit.at>',
    ],
    'depends': [
        'muk_autovacuum',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/menu.xml',
        'views/oauth.xml',
        'views/oauth1.xml',
        'views/oauth2.xml',
        'views/access.xml',
        'views/callback.xml',
        'views/request.xml',
        'views/endpoint.xml',
        'views/request_token.xml',
        'views/access_token.xml',
        'views/bearer_token.xml',
        'views/authorization_code.xml',
        'views/res_users.xml',
        'views/documentation.xml',
        'template/assets.xml',
        'template/authorize.xml',
        'data/autovacuum.xml',
    ],
    'demo': [
        'demo/oauth.xml',
        'demo/endpoints.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'images': [
        'static/description/banner.png'
    ],
    'external_dependencies': {
        'python': [
            'oauthlib',
        ],
        'bin': [],
    },
    'application': False,
    'installable': True,
    'auto_install': False,
}