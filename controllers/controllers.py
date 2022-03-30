# -*- coding: utf-8 -*-
# from odoo import http


# class Onthebite(http.Controller):
#     @http.route('/onthebite/onthebite/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/onthebite/onthebite/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('onthebite.listing', {
#             'root': '/onthebite/onthebite',
#             'objects': http.request.env['onthebite.onthebite'].search([]),
#         })

#     @http.route('/onthebite/onthebite/objects/<model("onthebite.onthebite"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('onthebite.object', {
#             'object': obj
#         })
