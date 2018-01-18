# -*- coding: utf-8 -*-
from odoo import http

# class Primermodulo(http.Controller):
#     @http.route('/primermodulo/primermodulo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/primermodulo/primermodulo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('primermodulo.listing', {
#             'root': '/primermodulo/primermodulo',
#             'objects': http.request.env['primermodulo.primermodulo'].search([]),
#         })

#     @http.route('/primermodulo/primermodulo/objects/<model("primermodulo.primermodulo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('primermodulo.object', {
#             'object': obj
#         })