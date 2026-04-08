# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Comisiones(models.Model):
    inmueble = models.ForeignKey('Inmuebles', models.DO_NOTHING, blank=True, null=True)
    monto_pagado = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    tipo_pago = models.CharField(max_length=50, blank=True, null=True)
    fecha_pago = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'comisiones'
    def __str__(self):
            return self.tipo_pago


class Inmuebles(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    tipo_negocio = models.CharField(max_length=8)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    ubicacion_especifica = models.CharField(max_length=255, blank=True, null=True)
    propietario = models.ForeignKey('Usuarios', models.DO_NOTHING, blank=True, null=True)
    estado = models.CharField(max_length=10, blank=True, null=True)
    imagen = models.ImageField(upload_to='propiedades/fotos/', null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'inmuebles'

    # DEBE IR AQUÍ (Alineado con el class Meta anterior)
    def __str__(self):
        return self.titulo


class Roles(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'roles'
    def __str__(self):
            return self.nombre


class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    rol = models.ForeignKey(Roles, models.DO_NOTHING, blank=True, null=True)
    fecha_registro = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'usuarios'
    
    def __str__(self):
        return self.nombre

    
