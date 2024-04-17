# Tarea 2.2 Bot Yess

## Creación del bot 
**Paso 1**
  - Abre la aplicación de Telegram y busca el bot llamado @BotFather.
  - Inicia una conversación con @BotFather y usa el comando /newbot para crear un nuevo bot.
  - Sigue las instrucciones de @BotFather, proporciona un nombre para tu bot en este caso "Yess" y luego un nombre de usuario único que termine en "bot" para este ejemplo es "mi_primer241_bot". Recibirás un mensaje con el token de acceso del bot.

**Paso 2**
  - Tenemos que verificar si tenemos instalado Python y si no descargarlo
  - Instala la biblioteca `python-telegram-bot`que te ayudará a interactuar con la API de Telegram. Puedes instalarla utilizando pip:
    `pip install python-telegram-bot`

 **Paso 3**
  - Finalmente escribimos el codigo del Bot y lo ejecutamos

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

  `expresion_correo1 = re.compile(r"puedes|correo|promociones", re.IGNORECASE)` Esta expresión busca menciones relacionadas con el correo electrónico y las promociones en los mensajes de los usuarios, incluyendo palabras como "puedes", "correo" y "promociones", sin importar si están escritas en mayúsculas o minúsculas después nos manda un mensaje donde nos pide un correo electronico.

![Imagen de WhatsApp 2024-04-16 a las 20 51 14_7ffbeceb](https://github.com/Yess0222/Lenguajes-/assets/161245314/6604660d-5502-405b-a3cd-e1e75d9b2e20)
  
## Expresión regular correo

  `expresion_correo = re.compile(r"^[a-zA-Z0-9_.+-]*@[hotmail|outlook|gmail]*\.(com)$")` Esta expresión valida direcciones de correo electrónico con dominios específicos (hotmail, outlook, gmail) y la extensión ".com", si el correo electronico es correcto nos manda el siguiente mensaje "Tu correo es correcto, en un momento te enviaremos nuestras promociones. Algo más en lo que pueda ayudarte??" de lo contrario manda el mensaje "No entendí tu mensaje.".

  ![Imagen de WhatsApp 2024-04-16 a las 21 45 05_01bd266b](https://github.com/Yess0222/Lenguajes-/assets/161245314/76a01dfa-1d5f-4953-b934-a5970e4de4e7)

## Expresión regular adiós

  `expresion_adios = re.compile(r"adiós|bye|no", re.IGNORECASE)` Esta expresión busca palabras relacionadas con despedidas en los mensajes de los usuarios, incluyendo palabras como "adiós", "bye" y "no", sin importar si están escritas en mayúsculas o minúsculas y como resultado nos manda el mensaje "Fue un gusto ayudarte".

  ![Imagen de WhatsApp 2024-04-16 a las 20 51 15_eec81993](https://github.com/Yess0222/Lenguajes-/assets/161245314/b5cbaa77-44c7-4eb6-a381-b564ac1921e8)

## Resultado final

![Imagen de WhatsApp 2024-04-16 a las 21 45 32_0c0fdd76](https://github.com/Yess0222/Lenguajes-/assets/161245314/83d6dc50-e528-4e2d-82c0-bb794851d316)

![Imagen de WhatsApp 2024-04-16 a las 21 45 32_be9346df](https://github.com/Yess0222/Lenguajes-/assets/161245314/cc35e768-c4da-476f-98f2-e4915843a5e6)

## Conclusión 
Las expresiones regulares son una herramienta poderosa para la creación de bots, ya que permiten buscar patrones específicos en los mensajes de los usuarios de manera eficiente. Su uso facilita la detección y respuesta a diferentes tipos de solicitudes o interacciones, lo que contribuye a mejorar la experiencia del usuario y la funcionalidad del bot en general.
