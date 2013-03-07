=======================================
Peligro en ganancias de pedido de venta
=======================================

Este módulo añade un nuevo estado en los pedidos de venta,
**Esperando aprobación de riesgo**, que evita que se venda algo por debajo del
precio de coste hasta que un usuario con permisos de aprobación decida si
procesar la venta o no. En el caso que el pedido de venta esté pendiente de
aprobación, el usuario siempre puede rectificarlo, pasarlo a borrador y volver
hacer una nueva propuesta.

Módulos que dependen
====================

Instalados
----------

.. toctree::
   :maxdepth: 1

   /sale/index
   /sale_margin/index
   /sale_waiting/index

Dependencias
------------

* Ventas_
* `Margen pedido de ventas`_
* `Venta en espera`_

.. _Ventas: ../sale/index.html
.. _Margen pedido de ventas: ../sale_margin/index.html
.. _Venta en espera: ../sale_waiting/index.html
 