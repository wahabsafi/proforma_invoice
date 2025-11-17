from odoo import models, fields,api

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    our_ref=fields.Char("Our Ref")
    your_ref=fields.Char("Your Ref")
    shipment_method = fields.Char("Shipment Method")
    shipment_ref = fields.Char("Shipment Ref")
    payment_condition = fields.Char("Payment Conditon")
    country_of_origin = fields.Char("Country Of Origin")
    destination_of_goods =fields.Char("Destination Of Goods")
    total_pallet = fields.Integer("Total Pallet Number")
    net_weight = fields.Float("Total Net Weight (Kg)")
    gross_weight = fields.Float("Total Gross Weight (Kg)")
    hs_code = fields.Char("Customs Code")
    transporter = fields.Char("Transporter")
    customer_national_id = fields.Char("Customer National ID")
    customer_code = fields.Char("Customer Code")
    packing_charges=fields.Monetary("Paking Charges")
    transport_cost=fields.Monetary("Transport Cost")
    final_amount = fields.Float(compute="_compute_final_amount",store=True)
    
    @api.depends("amount_total","packing_charges","transport_cost")
    def _compute_final_amount(self):
        for order in self:
            order.final_amount=order.amount_total+order.packing_charges+order.transport_cost
    