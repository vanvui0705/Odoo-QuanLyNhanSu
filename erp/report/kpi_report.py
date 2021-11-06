# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import tools
from odoo import api, fields, models

# from odoo import api, models
#
# class employeereport(models.AbstractModel):
#     _name = 'report.kpi.kpiemployee_report
#
#     @api.model
#     def _get_report_values(self, docids, data=None):
#         docs = self.env[model.model].browse(docids)
#         return {
#               'doc_ids': docids,
#               'doc_model': model.model,
#               'docs': docs,
#               'data': data,
#               'get_something': self.get_something,
#         }
#     def get_something(self):
#         return 5