#This file is part sale_margin_waiting module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from decimal import Decimal
from trytond.pool import PoolMeta

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    'Sale'
    __name__ = 'sale.sale'
    
    def check_for_quotation(self):
        super(Sale, self).check_for_quotation()
        if self.margin <= Decimal(0.0):
            self.write([self], {
                'state': 'waiting',
            })
