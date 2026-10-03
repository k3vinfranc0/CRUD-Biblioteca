from django.db import models

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    tipoDocumento = models.CharField(max_length=20)
    numeroDocumento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    celular = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.numeroDocumento})"

class Libro(models.Model):
    codigoLibro = models.AutoField(primary_key=True)
    nombreLibro = models.CharField(max_length=150)
    autor = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20, unique=True)
    tematica = models.CharField(max_length=100)
    resumen = models.TextField()
    numeroCopias = models.IntegerField(default=1)

    def __str__(self):
        return self.nombreLibro

class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='idUsuario')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, db_column='codigoLibro')
    fechaPrestamo = models.DateField(auto_now_add=True)
    fechaEntrega = models.DateField()

    def __str__(self):
        return f"Prestamo: {self.libro.nombreLibro} a {self.usuario.nombre}"              