# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta, datetime
from dateutil.relativedelta import *

class varietysnail(models.Model):
    _name = 'fastsnail.varietysnail'

    name = fields.Char()
    idvariety = fields.Integer()
    thermalresist = fields.Char()
    description = fields.Text()
    totalsnails = fields.One2many('res.partner','snailclass')#fields.Integer() #total de caracoles que tienen este timpo , tendrá que ser computada  y se dará en kg


class snail(models.Model):
    _name = 'res.partner'
    _inherit ='res.partner'

    name = fields.Char()
    idsnail = fields.Char()
    snailclass = fields.Many2one('fastsnail.varietysnail')#fields.Char() #tendrá que darte a elegir entre las classe creada anteriomente (la parte de arriba)
    totalraces = fields.Many2many('fastsnail.race')
    description = fields.Text()
    photo = fields.Binary() # foto del caracol
    is_snail = fields.Boolean()

    @api.constrains('idsnail')
    def _check_value(self):
    	for r in self:
    		caracolesId = self.search([('idsnail', '=', r.idsnail)])
    		if len(caracolesId) > 1:
    			raise ValidationError("El Id del caracol ya existe.")

class competition(models.Model):
    _name = 'fastsnail.competition'

    name = fields.Char()
    idcompetition = fields.Integer()
    totalSeasons = fields.One2many('fastsnail.season','competition')

    @api.multi
    def copy_competition(self):
        self.env['fastsnail.competition'].create({'name':self.name+"_copia", 'idcompetition':self.idcompetition+1, 'totalSeasons':self.totalSeasons})


class season(models.Model):
    _name = 'fastsnail.season'

    name = fields.Char()
    idseason = fields.Integer()
    startdate = fields.Datetime() #data en la que empieza la temporada
    enddate = fields.Datetime() #data en la que termina la temporada
    description = fields.Text()
    competition = fields.Many2one('fastsnail.competition')
    totalrace = fields.One2many('fastsnail.race','season') #total de carreras con lista , computada de las carreras que esten en esta season

    @api.constrains('idseason')
    def _check_value(self):
    	for r in self:
    		seasonsId = self.search([('idseason', '=', r.idseason)])
    		if len(seasonsId) > 1:
    			raise ValidationError("El Id de la Season ya existe.")

class race(models.Model):
    _name = 'fastsnail.race'

    name = fields.Char()
    idrace = fields.Integer()
    season = fields.Many2one('fastsnail.season')
    startdate = fields.Datetime() #data en la que empieza la temporada
    description = fields.Text()
    totalsnails = fields.Many2many('res.partner') #total de caracoles participan en la temporada computado usando la lista de las carreras
    
    @api.constrains('idrace')
    def _check_value(self):
    	for r in self:
    		idraceId = self.search([('idrace', '=', r.idrace)])
    		if len(idraceId) > 1:
    			raise ValidationError("El Id de la Carrera ya existe.")

    @api.constrains('startdate')
    def _chek_value(self):
        for r in self:
            if r.startdate>r.season.enddate:
                raise ValidationError("La fecha tiene que estar dentro de la Season")
    

class classification(models.Model):
	_name = 'fastsnail.classification'

	name = fields.Char()
	idclassification = fields.Char()
	idrace = fields.Many2one('fastsnail.race') # relación entre la carrera y la classificación ( tendrá que dar a elegir que carrera queremos)
	idfirstsnail = fields.Many2one('res.partner')
	idsecondsnail = fields.Many2one('res.partner')
	idthirdsnail = fields.Many2one('res.partner')

	@api.constrains('idclassification', 'idrace')
	def _check_value(self):
		for x in self:
			idclassificationmomento = self.search([('idclassification', '=', x.idclassification)])
			idraceId = self.search([('idrace', '=', x.idrace.idrace)])
			if len(idclassificationmomento) > 1:
				raise ValidationError("Este id de classificacion ya existe")
			if len(idraceId) > 1:
				raise ValidationError("Esta carrera ya tiene registrada una puntuacion.")
			
class employee(models.Model):
	_name = 'fastsnail.employee'

  	idemployee = fields.Char()
	name = fields.Char()
	surname = fields.Char()
	phone = fields.Integer()

	@api.constrains('idemployee')
	def _check_value(self):
		for r in self:
			idemployeess = self.search([('idemployee', '=', r.idemployee)])
			if len(idemployeess) > 1:
				raise ValidationError("El Id de empleado ya existe")

#CREAR UNA TAULA INTERMIG -> CARERRA-CARAGOL-POSICIÓ


