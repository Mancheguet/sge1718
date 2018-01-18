# -*- coding: utf-8 -*-

from odoo import models, fields, api
from openerp.exceptions import ValidationError

class net(models.Model):
     _name = 'tots.net'

     name = fields.Char()
     net_ip = fields.Char()
     mask = fields.Integer()
     net_map = fields.Binary()
     net_class = fields.Selection([('a','A'),('b','B'),('c','C')])
     pcs = fields.One2many('tots.pc','net')
     servers = fields.Many2many('tots.pc',relation='net_servers')

class pc(models.Model):
     _name = 'tots.pc'
        
     name = fields.Char(default="PC")
     number = fields.Integer()
     ip = fields.Char(compute='_get_ip')
     ping = fields.Float()

     def _get_date(self):
       print self
       return fields.Date.today()

     def _get_datetime(self):
        print self
        return fields.Datetime.now()
#default=_get_datetime esto va dins de on volem , en este cas, uptime i registered

     registered = fields.Date(default=_get_date)
     uptime = fields.Datetime(default=_get_datetime)
     net = fields.Many2one('tots.net')
     servers = fields.Many2many('tots.net',relation='net_servers')
     
     #api_depends depende de number y de net , se ejecutara entonces, cuando cambien
     @api.depends('number', 'net')
     def _get_ip(self):
       print self
       for pc in self:
         print pc
         pc.ip = str(pc.net.net_ip)+str(pc.number)

     @api.constrains('number')
     def _check_number(self):
       for pc in self:
           if pc.number > 254:
             raise ValidationError("The IP must be under 254: %s" % pc.number)

