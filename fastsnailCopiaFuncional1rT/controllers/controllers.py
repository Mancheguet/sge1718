# -*- coding: utf-8 -*-
from odoo import http

# class Fastsnail(http.Controller):
#     @http.route('/fastsnail/fastsnail/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fastsnail/fastsnail/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fastsnail.listing', {
#             'root': '/fastsnail/fastsnail',
#             'objects': http.request.env['fastsnail.fastsnail'].search([]),
#         })

#     @http.route('/fastsnail/fastsnail/objects/<model("fastsnail.fastsnail"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fastsnail.object', {
#             'object': obj
#         })