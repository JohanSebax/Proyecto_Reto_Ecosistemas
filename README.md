# Proyecto Reto Ecosistemas

# Descripción del proyecto

En este proyecto, me proporcionaron una base de datos **"database.sqlite"**, con la base de datos se desarrollaron unos scripts de Python para calcular comisiones y enviar un correo electrónico de acuerdo a los requerimientos.

Los requerimientos, las necesidades del proyecto y la bases de datos proporcionada los pueden descargar en el siguiente link: [requerimientos y base de datos proporcionada](https://github.com/jupjaramilloca/Prueba_vacante_ecosistemas/tree/main).

# INSTRUCCIONES Y EXPLICACIÓN DE EJECUCIONES DE LOS SCRIPTS

# Pasos para ejecutar los scripts

**Paso 1. Instalar todas las dependencias o librerías**

Antes de instalar las dependencias se debe tener **Python** ya instalado en el computador o ordenador donde se vayan a ejecutar los scripts. También se recomienda instalar las extensiones **Python**, **SQLite** y **Jupyter** en Visual Studio Code(VS Code). Asegúrate de haber instalado al menos los siguientes paquetes en el entorno: **pandas**, **sqlite** y **openpyxl**. En el directorio del proyecto hay un archivo **"requirements.txt"** con todas las dependencias necesarias para ejecutar los scripts.

**Ejecuta el siguiente código en la terminal desde VS Code para instalar todas las dependencias o librerías requeridas:**

```bash
pip install -r requirements.txt
```

**Paso 2. Descargar la base de datos e ingresarla en el directorio**

Se coloca la base de datos en el directorio del proyecto y asegurarse de que el archivo sea nombrado como **database.sqlite**. Si al momento de clonar o hacer fork y guardar el repositorio localmente se encuentra el archivo con el mismo nombre, se debe descargar nuevamente la base de datos y reemplazarlo usando el mismo nombre.

**Paso 3. Ejecutar script "create_table.py"**

Este scripts agrega **2 nuevas tablas** a la base de datos proporcionada con el objetivo de calcular las comisiones para cada comercio de acuerdo a las condiciones de cobro de los contratos tanto fijos como variables y también se tienen en cuenta las condiciones de descuento para el cálculo del **Valor_Total** final para cada comercio o compañía.

**NOTA**: Se debe tener en cuenta que las condiciones de los contratos, los descuentos y el valor del IVA pueden cambiar por lo tanto si alguno de estos valores o condiciones cambia este es el script donde se pueden hacer las modificaciones pertinentes.

Para ejecutar el script **create_table.py** puedes usar el siguiente código en la terminal de comando en VS Code:

```bash
python create_table.py
```
Una vez ejecutado este script se deberían agregar 2 tablas más a la base de datos proporcionada que serían las tablas **"contracts"** y **"discount_rules"**. Deberían haber **4 tablas** en total almacenadas en la base de datos despues de ejecutar este script:

La tabla **"apicall"** y la tabla **"commerce"**, estas son las tablas que contiene la base de datos de origen ya proporcionada.

La tabla **"contract"** almacena y agrega las condiciones de los contratos de los comercios esto con la idea de que se pueden agregar más comercios o condiciones en un futuro y se pueden ir almacenando en esta tabla.

La tabla **"discount_rules"** almacena y agrega las condiciones de descuentos establecidas para los diferentes comercios o compañías de acuerdo a los requerimientos estipulados para aplicar los descuentos.

**IMPORTANTE**: En caso de que se requieran modificar las condiciones de los contratos, descuentos o valor del IVA, este es el script donde se deberían hacer los cambios.

**Paso 4. Ejecutar script "generate_report.py"**

Este Script es el script principal y más importante del repositorio, **"generate_report.py"** contiene la automatización que calcula las comisiones o valores totales a cobrar a cada empresa o comercio con status activo (**"Active"**) para el mes de **Julio** y **Agosto** de 2024, **el cálculo de los valores totales de las comisiones contiene los descuentos en caso de que cumplan con las condiciones de descuento**.  En caso de que se requiera cambiar los meses de los valores a cobrar se pueden realizar los ajustes en este mismo script.

**Cambio de Meses para el cálculo de las comisiones(Opcional):**

El script **"generate_report.py"** contiene por defecto los meses de **Julio** y **Agosto**, en caso de que se requieran cambiar se puede hacer de la siguiente manera:

En este mismo script se encuentra la variable **"selected_year_months"**, para cambiar los meses se debe ajustar el formato de las fechas de la siguiente forma:

- **selected_year_months = ['yyyy-mm']** Ingresa el primer dato de año y mes en el formato  
- **selected_year_months = ['yyyy-mm']** Ingresa el segundo dato de año y mes en el formato 

Por ejemplo, **"2024-03"** y **"2024-04"** realizaria los cálculos de las comisiones para los meses de **Marzo** y **Abril** respectivamente. 

Al ejecutar este script debería aparecer una tabla como output con columnas **"Fecha-Mes"**, **"Nombre"**, **"Nit"**, **"Valor_comision"**, **"Valor_iva"**, **"Valor_Total"**, **"Correo"** en la terminal mostrando todos los resultados para cada comercio o compañía.

**Generación del reporte de comisiones en formato excel(xlsx)**

Este Script también genera un reporte de comisiones en el formato requerido en un documento excel **xlsx**, el formato de excel se carga automáticamente dentro del mismo repositorio donde se ejecute el script, el documento excel queda automáticamente guardado en la carpeta del repositorio con el nombre de **"reporte_comisiones.xlsx"**. El reporte generado se puede abrir localmente en la carpeta donde esté localizado el repositorio.

**NOTA**: El repositorio ya contiene el archivo generado por el script, para poderlo probar se debe eliminar el documento y ejecutar el script para que se genere nuevamente una vez que se tenga el repositorio localmente.

Lo otra parte importante es que este script también manda un correo con los resultados de las facturas resumidas en la tablas en formato excel **xlsx**.

Para ejecutar el script **generate_report.py** puedes usar el siguiente código en la terminal de comando en VS Code:

```bash
python generate_report.py
```

**IMPORTANTE: POSIBLE ERROR DESPUÉS DE EJECUTAR EL SCRIPT**

Si al momento de ejecutar el script aparece un mesaje de error parecido a este: **SMTP error occurred: (535, b'5.7.3 Authentication unsuccessful [BN9PR03CA0779.namprd03.prod.outlook.com 2024-12-26T05:07:15.145Z 08DD2543506A083A]')** significa que se deben ingresar el **Username** y el **Password** del remitente para poder enviar el correo exitosamente al destinatario. 

**NOTA**: El script se ejecuta independientemente si se ingresa o no las credenciales para el envío del correo. **Si se requiere enviar un correo sigue el paso siguiente**.

**Paso 5 (Envío de correo). Ingresa Username y Password del SMTP Server para Office 365 o cualquier otro servicio**

En el script **"send.email.py"** se encuentra la automatización para el envío de correos por SMTP Server para Office 365, en esta parte es importante ingresar el **Username** y el **Password** del **"sender"** que es la persona que envía el correo. 

**Pasos para Ingresar Username y Password**

En el script **"send.email.py"** se encuentran las variables **"smtp_username"** y **"smtp_password"**, ingresa tu **Username** en la variable **smtp_username** y el **Password** en la variable **smtp_password** ambos datos deberían ingresarse en formato (str) de python.

Si ya se tiene una cuenta de **Microsoft Office 365** se pueden obtener el Username y el Password siguiendo los pasos de esta guía:

[Office 365 SMTP Settings Parameters](https://smartreach.io/blog/masterclass/smtp/office-365-smtp-settings/)

Los parámetros de configuración son los siguientes, leer la guía para tener claridad sobre los datos a ingresar:

- **SMTP Server Address: smtp.office365.com**
- **Port: 587 (TLS)**
- Encryption: STARTTLS (if using port 587) 
- Authentication: Yes, requires authentication.
- **Username: Your Office 365 email address (e.g., example@domain.com)**
- **Password: Your Office 365 email account password**

**NOTA:** No compartir estos datos con otras personas, esta información es sensible y solo de uso personal de la persona que quiera mandar el correo.

**Pasos para configurar el envío de correo**

En el script **"generate_report.py"** se encuentran las opciones para configurar el envío del correo, se pueden agregar los siguientes datos al correo si así lo desean, para hacerlo buscar las variables en el script y agregar la información en formato string (str) de Python de la siguiente manera:

- **recipient**= Ingresar correo del destinatario
- **sender**= Ingresar correo de la persona que lo envia 
- **subject**= Ingresa asunto del correo
- **body**= Ingresar cuerpo del correo 

El resto de variables no deberían sufrir cambios o no es necesario ingresarle datos.

**NOTA**: Una vez se hayan ingresado las configuraciones, se deben guardar los cambios y ejecutar el script "**"generate_report.py"** nuevamente para comprobar si el envio del correo fue exitoso. Debería aparecer un mensage de envio de correo exitoso (**"Email sent successfully to {recipient_email}"**) en la terminal después de ejecutado el script. 

## Documentación

[Base de datos proporcionada y lineamientos del proyecto](https://github.com/jupjaramilloca/Prueba_vacante_ecosistemas/tree/main)

[Accessing SQLite Databases Using Python and Pandas](https://datacarpentry.github.io/python-ecology-lesson/instructor/09-working-with-sql.html)

[SQL References](https://www.w3schools.com/sql/default.asp)

[Python SQLite tutorial using sqlite3](https://pynative.com/python-sqlite/#h-python-sqlite-database-connection)

[Python SQLite – Connecting to Database](https://www.geeksforgeeks.org/python-sqlite-connecting-to-database/)

[Sending Emails with Python Using the ‘smtplib’ Library](https://medium.com/@thakuravnish2313/sending-emails-with-python-using-the-smtplib-library-e5db3a8ce69a)

[smtplib — SMTP protocol client](https://docs.python.org/3/library/smtplib.html)

[Office 365 SMTP Settings | The Complete Guide](https://smartreach.io/blog/masterclass/smtp/office-365-smtp-settings/)



