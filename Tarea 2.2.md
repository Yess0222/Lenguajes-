# Tarea 2.2 Bot Yess

## Creación del bot 
  - Primero tenemos que revisar si tenemos instalado python y si no lo tenemos instalarlo
  - Después tenemos que instalar la biblioteca para interactuar con telegram: `pip install python-telegram-bot`
  - Finalmente escribimos el codigo del bot utilizando expresiones regulares

## Expresión regular para saludar 

  `expresion_regular = re.compile(r"hello|hi|hey|hola", re.IGNORECASE)` Esta expresión busca saludos genéricos en los mensajes de los usuarios, incluyendo palabras como "hello", "hi", "hey" y "hola", sin importar si están escritas en mayúsculas o minúsculas y como respuesta nos contesta ¡Hola! ¿Cómo estás?.
  
  ![Imagen de WhatsApp 2024-04-16 a las 20 40 37_43059c39](https://github.com/Yess0222/Lenguajes-/assets/161245314/d19f2cf3-5969-4637-8c16-3a2e78571d45)

## Expresión regular helado

  `expresion_helado = re.compile(r"helado|sabor de helado|favorito", re.IGNORECASE)` Esta expresión busca menciones relacionadas con el helado en los mensajes de los usuarios, incluyendo palabras como "helado", "sabor de helado" y "favorito", sin importar si están escritas en mayúsculas o minúsculas como resultado el bot nos pregunta cual es nuestro sabor favorito.

  ![Imagen de WhatsApp 2024-04-16 a las 20 51 14_3c594d2f](https://github.com/Yess0222/Lenguajes-/assets/161245314/914730c1-0c28-4e90-b071-475d062eae92)

## Expresión regular sabor

  `expresion_sabor = re.compile(r"fresa|limon|chocolate", re.IGNORECASE)` Esta expresión busca los sabores de helado "fresa", "limon" y "chocolate" en los mensajes de los usuarios, sin importar si están escritos en mayúsculas o minúsculas y como respuesta nos regresa la frase uyyy que rico.

![Imagen de WhatsApp 2024-04-16 a las 20 51 14_ab45796f](https://github.com/Yess0222/Lenguajes-/assets/161245314/3b42b964-1d13-412f-a50d-82210467b689)

## Expresión regular correo1

  `expresion_correo1 = re.compile(r"puedes|correo|promociones", re.IGNORECASE)`

![Imagen de WhatsApp 2024-04-16 a las 20 51 14_7ffbeceb](https://github.com/Yess0222/Lenguajes-/assets/161245314/6604660d-5502-405b-a3cd-e1e75d9b2e20)
  
## Expresión regular correo

  `expresion_correo = re.compile(r"^[a-zA-Z0-9_.+-]*@[hotmail|outlook|gmail]*\.(com)$")`

  ![Imagen de WhatsApp 2024-04-16 a las 20 51 15_0e30d31c](https://github.com/Yess0222/Lenguajes-/assets/161245314/f37499cb-2d64-4ec2-8806-7075518d875e)

## Expresión regular adiós

  `expresion_adios = re.compile(r"adiós|bye|no", re.IGNORECASE)`

  ![Imagen de WhatsApp 2024-04-16 a las 20 51 15_eec81993](https://github.com/Yess0222/Lenguajes-/assets/161245314/b5cbaa77-44c7-4eb6-a381-b564ac1921e8)

## Resultado final

![Imagen de WhatsApp 2024-04-16 a las 20 40 37_63e17a58](https://github.com/Yess0222/Lenguajes-/assets/161245314/ddd4eee2-578c-4489-9b81-46f88e3dbae3)
