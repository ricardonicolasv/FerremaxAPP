from django.contrib import admin
from .models import (
    TipoPromocion, Especialidad, CategoriaProducto, Usuario, Cliente, 
    Vendedor, Sucursal, Producto, Inventario, EstadoPedido, Pedido, 
    DetallePedido, Promocion, Mensaje
)

admin.site.register(TipoPromocion)
admin.site.register(Especialidad)
admin.site.register(CategoriaProducto)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Sucursal)
admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(EstadoPedido)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Promocion)
admin.site.register(Mensaje)