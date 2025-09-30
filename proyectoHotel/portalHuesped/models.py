from django.db import models
from django.contrib.auth.models import User

"""Modelos adicionales para portal de huésped.

HuespedCuenta vincula un usuario de Django (auth_user) con un registro existente
en la tabla `huespedes` (modelo `trivago.Huespedes`). Los modelos originales del
app `trivago` son unmanaged (managed = False) porque reflejan tablas ya creadas
en la base de datos MySQL. Aquí sí permitimos que Django cree la tabla
`portalHuesped_huespedcuenta` para gestionar la relación.
"""

class HuespedCuenta(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="huesped_cuenta")
	huesped = models.OneToOneField("trivago.Huespedes", on_delete=models.CASCADE, related_name="cuenta")
	creado = models.DateTimeField(auto_now_add=True)
	actualizado = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Cuenta de Huésped"
		verbose_name_plural = "Cuentas de Huéspedes"

	def __str__(self):
		return f"Cuenta {self.user.username} -> Huesped #{self.huesped.id_huesped}"
