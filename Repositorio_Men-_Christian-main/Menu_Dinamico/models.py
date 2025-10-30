from django.db import models

# Create your models here.
class Trabajador(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    cedula = models.CharField(max_length=10, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    f_nacimiento = models.DateField(null=False)
    direccion = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    estado = models.IntegerField(9, null=False)
    class Meta:
        db_table = 'Trabajador'

class Rol(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    descripcion = models.CharField(max_length=100)
    fecha : models.DateField(null=False)
    estado = models.IntegerField(9, null=False)
    class Meta:
        db_table = 'Rol'

class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    usuario = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    estado = models.IntegerField(9, null=False)
    id_Trabajador = models.ForeignKey(Trabajador, null=False, blank=False, on_delete=models.CASCADE)
    id_Rol = models.ForeignKey(Rol, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Usuarios'

class Historial_Login(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    id_Usuarios = models.ForeignKey(Usuarios, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField(null=False)
    class Meta:
        db_table = 'Historial_Login'

class Empresa(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    comercial = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    ruc = models.CharField(max_length=13)
    O_contabilidad = models.BooleanField()
    estado = models.IntegerField(9, null=False)
    class Meta:
        db_table = 'Empresa'


class Sucursal(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    sucursal = models.CharField(max_length=3)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    estado = models.IntegerField(null=False)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=100)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Sucursal'


class Permisos(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)
    estado = models.IntegerField(9, null=False)
    class Meta:
        db_table = 'Permisos'

class Surcursal_Permisos(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    id_permiso = models.ForeignKey(Permisos, on_delete=models.CASCADE)
    historico = models.CharField(max_length=100)
    estado = models.IntegerField(9, null=False)
    class Meta:
        db_table = 'Surcursal_Permisos'

class Menu(models.Model):
    id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    menu = models.CharField(max_length=50)
    ruta = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    estado = models.IntegerField(9, null=False)
    class Meta:
        db_table = 'Menu'