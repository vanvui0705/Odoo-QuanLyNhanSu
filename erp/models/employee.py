from odoo import api, fields, models, tools, _


class employee(models.Model):
    _inherit = 'hr.employee'
    _description = "nhan vien"

    code_health = fields.Char('ID Health insurance', required=True)
    code_BHXH = fields.Char('ID Social insurance', required=True)
    id = fields.Char(string='ID', required=True, copy=False, readonly=True,
                     default=lambda seft: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('classlist.id') or _('New')
        res = super(employee, self).create(vals)
        return res


# id = fields.Char(string='Mã Khóa Học', required=True, copy=False, readonly=True,
#                      default=lambda seft: _('New'))
#
#
# @api.model
#     def create(self, vals):
#         if vals.get('id', ('New')) == ('New'):
#             vals['id'] = self.env['ir.sequence'].next_by_code('classlist.id') or _('New')
#         res = super(classlist, self).create(vals)
#          return res
#
#
# <?xml version="1.0" encoding="utf-8"?>
# <odoo>
#     <data noupdate ="1">
#         <record id="educate_id" model="ir.sequence">
#             <field name="name">ma khoa hoc </field>
#             <field name="code">classlist.id</field>
#             <field name="prefix">MDT</field>
#             <field name="padding">4</field>
#             <field name="company_id" eval="False"/>
#         </record>
#
#     </data>
# </odoo>