# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class training_employee(models.Model):
    _name = "training_employee"
    _description = ""

    employee_id = fields.Many2one('res.partner', string='Employee')
    department_id = fields.Many2one('res.partner', string='Department')
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', default='1')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='male')
    skill = fields.Char(string='Skill' , required=True)
    workexperience = fields.Char(string='WorkExperience')
    email = fields.Text(string='Email')
    address = fields.Text(string='Address')
    note = fields.Text(string='Description')
