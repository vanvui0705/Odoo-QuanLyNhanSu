# -*- coding: utf-8 -*-
# from odoo import http


# class Erp(http.Controller):
#     @http.route('/erp/erp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/erp/erp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('erp.listing', {
#             'root': '/erp/erp',
#             'objects': http.request.env['erp.erp'].search([]),
#         })

#     @http.route('/erp/erp/objects/<model("erp.erp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('erp.object', {
#             'object': obj
#         })
