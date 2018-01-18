# -*- coding: utf-8 -*-

from odoo import models, fields, api

class primermodulo(models.Model):
     _name = 'primermodulo.primermodulo'

     name = fields.Char()
     date = fields.Datetime()
     complete = fields.Boolean()

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
