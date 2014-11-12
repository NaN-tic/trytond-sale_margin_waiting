#This file is part sale_margin_waiting module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .sale import *

def register():
    Pool.register(
        Configuration,
        Sale,
        module='sale_margin_waiting', type_='model')
