Expresión regular que valida una Contraseña fuerte
  - 1 minúscula
  - 1 mayúscula
  - 1 número
  - 1 carácter especial
  - 8 caracteres de longitud

`^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8}$`

Expresión Regular que valida un Nombre de usuario
  - Longitud de 3 a 16 caracteres
  - Letra o número o guion medio o bajo

`^[A-Za-z0-9_-]{3,16}$`

