from django import forms

class formUsuario(forms.Form):
    nombres = forms.CharField(
        label = "Nombres"
    )

    apellidos = forms.CharField(
        label = "Apellidos"
    )

    documento = forms.CharField(
        label = "Documento"
    )

    fechanacimiento = forms.DateTimeField(
        label = "Fecha De Nacimiento"
    )

    email = forms.CharField(
        label = "email",
        widget=forms.EmailInput
    )

    telefono = forms.CharField(
        label = "Telefono"
    )

    usuario = forms.CharField(
        label = "Usuario"
    )

    tipodoc_options=[
        (0, 'Seleccione'),
        (1, 'Cedula de Ciudadanía'),
        (2, 'Cedula de Extranjería'),
        (3, 'Tarjeta de Identidad')
    ]
    tipodoc =  forms.TypedChoiceField(
        label =  "Tipo de documento",
        choices = tipodoc_options
    )