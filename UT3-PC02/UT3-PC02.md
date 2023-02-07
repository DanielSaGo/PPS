# UT3. - Prueba calificable 02

# **Control de versiones seguro**

Puesta en Producción Segura

Para esta práctica primeramente crearemos un repositorio en la organización para poder conectarlo posteriormente remotamente al repositorio que crearemos a continuación.

Para comenzar la práctica crearemos un repositorio local donde habrá un documento para poder identificar el nombre del grupo y de la práctica. Antes de nada añadiremos el repositorio a git.

 ![0](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled.png)

Cuando añadamos el documento en la carpeta explicada antes, haremos un git add para añadirlo.

Después de añadir el documento ‘.md’, añadimos el archivo .log, el cual haremos que se impida que se añada al repositorio gracias a .gitignore.
Ahora añadimos el .gitignore a la carpeta local y haremos un git add para añadirlo y después un git status para ver el contenido que se añadió. Como podemos ver, el archivo ‘.log’ no se añadió, gracias a que dentro del archivo ‘.gitignore’ hemos especificado que no añada los archivos con extensión ‘.log’.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%201.png)

---

Despues de añadir el documento ‘.md’, añadimos el archivo .log, el cual haremos que se impida que se añada al repositorio gracias a .gitignore.

Ahora añadimos el .gitignore a la carpeta local y haremos un git add para añadirlo y despues un git status para ver el contenido que se añadio. Como podemos ver, el archivo ‘.log’ no se añadio, gracias a que dentro del archivo ‘.gitignore’ hemos especificado que no añada los archivos con extension ‘.log’.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%202.png)

Haremos un commit del contenido del repositorio local.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%203.png)

---

Conectaremos ahora el repositorio local que hemos creado anteriormente al repositorio creado en la organización.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%204.png)

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%205.png)

---

Crearemos una nueva rama en el repositorio y nos cambiaremos a ella.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%206.png)

Después de estar en la rama que hemos creado, haremos un git push para subir al repositorio de la organización, los archivos.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%207.png)

---

Después de haber hecho el push a la rama creada, nos pondremos a configurar git para tener una firma GPG y verificar los commits que se hagan.

Antes de ponernos a escribir comandos, nos iremos al siguiente enlace y descargaremos lo siguiente: [https://www.gpg4win.org/](https://www.gpg4win.org/)

Después de haber descargado GPG y empezaremos a configurarlo:

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%208.png)

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%209.png)

Después de poner nuestro datos en la configuración nos pedirá que escribamos una frase para que sea nuestra contraseña al efectuar los commits.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2010.png)

De la lista de claves GPG, se copiará el ID de la clave GPG que usaremos.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2011.png)

El ID que escogimos antes lo pondremos en el comando de a continuación:

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2012.png)

Ya hasta aquí habremos configurado la firma GPG, únicamente nos quedaría añadirla a nuestro git. Para ello cogeremos la clave de GPG que se nos generó anteriormente.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2013.png)

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2014.png)

Después de añadir la clave GPG a nuestro github, tendremos que asignar la clave usada al repositorio en cuestión. Para terminar con la comprobación de la clave GPG, haremos un git add, git commit como vemos en el comando, para que nos pida verificación y por último el git push.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2015.png)

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2016.png)

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2017.png)

Como podemos ver al hacer el push e irnos a github podremos ver que el commit esta verificado.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2018.png)

---

Después de haber realizado la configuración e implementación de las claves GPG, instalamos gitleasks para **detectar y prevenir** secretos codificados como contraseñas, claves u otros.

Después de haberlo instalado, probaremos que no tengamos leaks en los commits realizados.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2019.png)

Ahora para comprobar que todo esté correcto, crearemos un archivo llamado ‘.env’ en el que añadiremos una KEY, para que gitleaks nos detecte un leak.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2020.png)

Una vez creado el archivo, haremos un git add y un commit

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2021.png)

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2022.png)

Cuando hagamos el commit, probaremos si hay algún leak en el commit y como vemos hay un leak, que es el archivo que creamos antes.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2023.png)

Finalmente incluimos la variable de entorno del archivo a gitignore para evitar que se añada al repositorio.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2024.png)

---

Ahora automatizamos que cuando gitleaks detecte un error, el commit no se haga , para ello usaremos hooks.

Primeramente nos iremos a la ruta que vemos y crearemos un archivo donde estará el script que se ejecute.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2025.png)

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2026.png)

Ahora haremos la configuración de git, para ello daremos permisos al archivo creado y también ponemos true para habilitar esta opción, en este caso habilitamos bool.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2027.png)

Para probar que todo fue correcto creará nuevamente un archivo con claves.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2028.png)

Hacemos un git add.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2029.png)

Por ultimo haremos el commit y como vemos nos indica que hay un leak.

![Untitled](https://github.com/DanielSaGo/PPS/blob/main/UT3-PC02/img-UT3-PC02/Untitled%2030.png)
