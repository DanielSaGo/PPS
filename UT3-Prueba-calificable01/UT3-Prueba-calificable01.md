# UT3 - Prueba calificable 01

# Seguridad y desplegado de aplicaciones con Docker

Puesta en Producción Segura

**Primera parte: Dockerfile y Docker-compose**

La primera parte de este trabajo era realizar las actividades propuesta por la Moodle, sobre la creariacion de dockerfiles y docker-composes

Dichas actividades realizadas fueron las siguientes:

**Dockerfile**

- *[UT3.AP00a - Afianzando el uso de Dockerfile.](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/assign/view.php?id=454669)*
- *[UT3.AP00b - Creación de imágenes a partir de ficheros Dockerfile](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/assign/view.php?id=121456)*

**Docker-compose**

- *[UT3.AP01 - Docker-compose para desarrollo](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/assign/view.php?id=121458)*
- *[UT3.AP02 - Prueba de aplicaciones con docker-compose](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/assign/view.php?id=121459)*
- *[UT3.AP03 - Docker-compose Wordpress](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/assign/view.php?id=454668)*
- *[UT3.AP04 - Habilitar protección para imágenes sin firmar.](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/assign/view.php?id=121460)*

**Segunda parte: Docker Brench** 

En este apartado veremos cómo se analiza el entorno, depués de hacer las actividades anteriores.

1. **Docker bench y análisis de Docker.**
    
    Instalamos y ejecutamos las pruebas iniciales. Como veremos, nos enseñará los WARN y PASS, de los ficheros creados.
    
    ```bash
    git clone https://github.com/docker/docker-bench-security.git
    ```
    
    ![0](https://github.com/DanielSaGo/PPS/blob/main/UT3-Prueba-calificable01/img/0image.png)
    
    ```bash
    cd docker-bench-security/
    
    ./docker-bench-security.sh
    ```
    
    ![1](https://github.com/DanielSaGo/PPS/blob/main/UT3-Prueba-calificable01/img/1image.png)
    
    ![2](https://github.com/DanielSaGo/PPS/blob/main/UT3-Prueba-calificable01/img/2image.png)
    
    <img src="https://github.com/DanielSaGo/PPS/blob/main/UT3-Prueba-calificable01/img/3image.png" width="250"/>

2. **Utilizando AuditD para analizar las pruebas de la Sección A, referente al host.**

A continuación instalaremos AuditD para análaizar las pruebas de las Sección A del host.

```bash
apt-get install [auditd](https://rubensa.wordpress.com/2018/07/23/auditando-sistemas-linux-con-el-demonio-audit/)
```

![4](https://github.com/DanielSaGo/PPS/blob/main/UT3-Prueba-calificable01/img/4image.png)

Entraremos en el siguiente fichero para configurara las reglas de audit y escribiremos en dicho fichero lo siguiente:

```bash
nano /etc/audit/rules.d/audit.rules
```

```bash
- w /usr/bin/docker -p wa
- w /var/lib/docker -p wa
- w /etc/docker -p wa
- w /lib/systemd/system/docker.service -p wa
- w /lib/systemd/system/docker.socket -p wa
- w /etc/default/docker -p wa
- w /etc/docker/daemon.json -p wa
- w /usr/bin/docker-containerd -p wa
- w /usr/bin/docker-runc -p wa
```

![5](https://github.com/DanielSaGo/PPS/blob/main/UT3-Prueba-calificable01/img/5image.png)

Reiniciaremo AuditD

```bash
systemctl restart auditd
```

Ahora entraremos en el fichero de daemon.json y ajustaremos la seguridad.

```bash
cd /etc/docker/

nano daemon.json
```

```bash
{

"icc": false,

"userns-remap": "default",

"log-driver": "syslog",

"disable-legacy-registry": true,

"live-restore": true,

"userland-proxy": false,

"no-new-privileges": true

}
```

![6](https://github.com/DanielSaGo/PPS/blob/main/UT3-Prueba-calificable01/img/6image.png)

Al ejecutar el docker-brench-security, se arreglan algunos errores con lo hecho anteriormente y veremos la diferencia con el primer análaisis de la sección A del host.

![7](https://github.com/DanielSaGo/PPS/blob/main/UT3-Prueba-calificable01/img/7image.png)

![8](https://github.com/DanielSaGo/PPS/blob/main/UT3-Prueba-calificable01/img/8image.png)

<img src="https://github.com/DanielSaGo/PPS/blob/main/UT3-Prueba-calificable01/img/9image.png" width="250"/>

1. **Explicación de dos errores**
    
    En este apartado veremos, explicaremos y solucionaremos dos ejemplos de los WARN que hemos **visto anteriormente en el análisis.**
    
    El primer WARN que veremos es: 
    
    ```bash
    **[WARN]** 2.13 - Ensure centralized and remote logging is configured (Scored)
    tee: log/docker-bench-security.log: Permission denied
    ```
    
    Este error, cuenta que hay que as**egurarse de que el registro centralizado y remoto esté configurado.**
    
    El registro **rem**oto centralizado garantiza que todos los registros de registro críticos estén protegidos incluso en el caso de problemas graves de disponibilidad de datos. Docker admite varios métodos de registro, por lo que debe utilizar el método que mejor se adapte a su política de seguridad de TI.
    
    La solución que podemos realizar, es usar este controlador de registro:
    
    ```bash
    dockerd --log-driver=syslog --log-opt dirección-syslog=tcp://192.xxx.xxx.xxx
    ```
    
    El segundo WARN que veremos es: 
    
    ```bash
    **[WARN]** 2.15 - Ensure live restore is enabled (Scored)
    tee: log/docker-bench-security.log: Permission denied
    ```
    
    Una de las **principales** tríadas de seguridad es la **usabilidad.** Establecer el indicador --live-restore **en el** demonio **de** Docker **evita** que la ejecución del contenedor se **suspenda** cuando no está disponible. **También** facilita la actualización y el parche del demonio Docker sin **bloquear** la aplicación.
    
    La solución que podemos realizar, en ejecutar docker en daemon y ejecutar el siguiente comando:
    
    ```bash
    dockerd --live-restore
    ```
    

**Tercera parte: Análisis de archivo dockerfile**

**Para el análisis de archivos de dockerfile, instalaremos y configuraremos la herramienta Trivy. Para ello seguiremos los comandos que veremos a continuación:**

```bash
sudo apt-get install wget apt-transport-https gnupg lsb-release

wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | sudo tee /usr/share/keyrings/trivy.gpg > /dev/null

echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | sudo tee -a /etc/apt/sources.list.d/trivy.list

sudo apt-get update

sudo apt-get install trivy

sudo trivy config Dockerfile
```

**Con el siguiente comando podremos hacer el análisis del archivo Dockerfile creado en la actividades:**

```bash
trivy config Dockerfile
```

![10](https://github.com/DanielSaGo/PPS/blob/main/UT3-Prueba-calificable01/img/10image.png)

**El resultado que vemos, al hacer el análisis del dockerfile que creamos en la primera actividad es el siguiente: Al ser un dockerfile con poco contenido, nos mostrará menos información de análisis del dockerfile, en nuestro caso nos especifica dos errores, uno HIGH y otro MEDIUM. La alerta HIGH nos cuenta como podemos leer, nos recomienda que especifiquemos al menos un usuario en el dockerfile. La alerta MEDIUM que nos especifica, es que deberíamos de cambiar en el comando RUN cd /var/www/html por WORKDIR cd /var/www/html.**

**Cuarta parte: Análisis de imágenes y comparación**

**A continuación usaremos la herramienta Trivy instalada anteriormente para poder analizar dos imágenes de docker. Una de las imágenes, será la imagen que se creó en la actividad de wordpress y la otra será la versión 4.6 de wordpress. Una vez descargadas y analizadas, las dos imágenes, haremos una pequeña comparación del estado de las dos imágenes.**

Con el siguiente comando se iniciara el análisis de la imagen de wordpress:

```bash
**trivy image wordpress:latest**
```

![11](https://github.com/DanielSaGo/PPS/blob/main/UT3-Prueba-calificable01/img/11image.png)

Con el siguiente comando se iniciara el analisi de la imagen de wordpress:4.6: 

```bash
**trivy image wordpress:4.6**
```

![12](https://https://github.com/DanielSaGo/PPS/UT3-Prueba-calificable01/img/12image.png)

**Comparación de las dos imágenes de wordpress**

**Con respecto a las dos imágenes analizadas de Wordpress podemos ver que la versión de la actividad de Wordpress, tiene soporte de versiones y detección de vulnerabilidades. También podemos ver que dicha imagen tiene una vulnerabilidad sin una versión para arreglarla.**

**Por otro lado la segunda imagen analizada es la de Wordpress:4.6, esta no tiene soporte de versiones y tiene una vulnerabilidad con el CVE que se ve en la captura, pero tiene una versión para arreglarlo. Otro dato que nos da es que la detección de vulnerabilidades al hacer el análisis, puede ser insuficiente.**
