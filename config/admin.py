from django.contrib import admin
from models import Usuario, Libro, Prestamo

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('idUsuario', 'nombre', 'numeroDocumento', 'correo', 'celular')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('idLibro', 'nombreLibro', 'autor', 'ISBN', 'numeroCopias') if hasattr(Libro, 'idLibro') else ('nombreLibro', 'autor', 'ISBN', 'numeroCopias')

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    pass