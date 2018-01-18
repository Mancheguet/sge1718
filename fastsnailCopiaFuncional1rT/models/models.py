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
    totalsnails = fields.One2many('fastsnail.snail','snailclass')#fields.Integer() #total de caracoles que tienen este timpo , tendrá que ser computada  y se dará en kg


class snail(models.Model):
    _name = 'fastsnail.snail'

    name = fields.Char()
    idsnail = fields.Char()
    snailclass = fields.Many2one('fastsnail.varietysnail')#fields.Char() #tendrá que darte a elegir entre las classe creada anteriomente (la parte de arriba)
    totalraces = fields.Many2many('fastsnail.race', 'totalsnails')
    description = fields.Text()
    photo = fields.Binary() # foto del caracol

    # @api.constrains('idsnail')
    # def _check_value(self):
    #      for r in self.search([]):
    #         for x in self.search([]):
    #             if r.id != x.id: 
    #                 if r.idsnail == x.idsnail:
    #                     raise ValidationError("El ids de caracol ya esxiste.")

            #snailsexistentes = self.search_count([('idsnail', '=', r.idsnail)])
            # if len(snailsexistentes) > 0:
            #     raise ValidationError("El ID de caracol ya esxiste.")

class competition(models.Model):
    _name = 'fastsnail.competition'

    name = fields.Char()
    idcompetition = fields.Integer()
    totalSeasons = fields.One2many('fastsnail.season','competition')

class season(models.Model):
    _name = 'fastsnail.season'

    name = fields.Char()
    idseason = fields.Integer()
    startdate = fields.Datetime() #data en la que empieza la temporada
    enddate = fields.Datetime() #data en la que termina la temporada
    description = fields.Text()
    competition = fields.Many2one('fastsnail.competition')
    totalrace = fields.One2many('fastsnail.race','season') #total de carreras con lista , computada de las carreras que esten en esta season

class race(models.Model):
    _name = 'fastsnail.race'

    name = fields.Char()
    idrace = fields.Integer()
    startdate = fields.Datetime() #data en la que empieza la temporada
    description = fields.Text()
    season = fields.Many2one('fastsnail.season')
    totalsnails = fields.Many2many('fastsnail.snail','totalraces') #total de caracoles participan en la temporada computado usando la lista de las carreras

class classification(models.Model):
	_name = 'fastsnail.classification'

	name = fields.Char()
	idclassification = fields.Integer()
	idrace = fields.Integer() # relación entre la carrera y la classificación ( tendrá que dar a elegir que carrera queremos)
	idfirstsnail = fields.Many2one('fastsnail.snail')
	idsecondsnail = fields.Many2one('fastsnail.snail')
	idthirdsnail = fields.Many2one('fastsnail.snail')


class employee(models.Model):
	_name = 'fastsnail.employee'

  	idemployee = fields.Integer()
	name = fields.Char()
	surname = fields.Char()
	phone = fields.Integer()

#CREAR UNA TAULA INTERMIG -> CARERRA-CARAGOL-POSICIÓ
