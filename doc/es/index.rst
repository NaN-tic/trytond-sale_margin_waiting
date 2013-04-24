=======================================
Peligro en ganancias de pedido de venta
=======================================

Este módulo añade un nuevo estado en los pedidos de venta,
**Esperando aprobación de riesgo**, que evita que se venda algo por debajo del
precio de coste hasta que un usuario con permisos de aprobación decida si
procesar la venta o no. En el caso que el pedido de venta esté pendiente de
aprobación, el usuario siempre puede rectificarlo, pasarlo a borrador y volver
hacer una nueva propuesta.
