# Proyecto Reto Ecosistemas

# Descripción del proyecto

En este proyecto, me proporcionaron una base de datos **"database.sqlite"**, con la base de datos se desarrollaron unos scripts de Python para calcular comisiones y enviar un correo electronico de acuerdo a los requerimientos.

# INSTRUCCIONES Y EXPLICACIÓN DE EJECUCIONES DE LOS SCRIPTS

# Pasos para ejecutar los scripts

**Paso 1. Installar todas las depencias o librerias**

Asegúrate de haber instalado al menos los siguientes paquetes en el entorno: **pandas**, **sqlite** y **openpyxl**. En el directorio del proyecto hay un archivo **"requirements.txt"** con todas las dependencias necesarias para ejecutar los scripts.

**Ejecuta el siguiente codigo en la terminal desde VS Code para instalar todas las dependencias o librerias requeridas:**

```bash
pip install -r requirements.txt
```

**Paso 2. Descargar la base de datos e ingresarla en el directorio**

Se coloca la base de datos en el directorio del proyecto y asegurarse de que el archivo sea nombrado como **database.sqlite**. Si al momento de bifurcar y guardar el repositorio localmente se encuentra el archivo con el mismo nombre, se debe descargar nuevamente la base de datos y reemplazarlo usando el mismo nombre.

**Paso 3. Ejecutar script "create_table.py"**

Este scripts agrega 2 nuevas tablas a la base de datos proporcionada con el objetivo de calcular las comisiones para cada comercio de acuerdo a las condiciones de cobro de los contratos tanto fijos como variables y también se tienen en cuenta las condiciones de descuento para el calculo del Valor_Total final para cada comercio.

**NOTA**: Se debe tener en cuenta que las condiciones de los contratos, los descuentos y el valor del IVA pueden cambiar por lo tanto si alguno de estos valores o condiciones cambia este es el script donde se pueden hacer las modificaciones pertinentes.

Para ejecutar el script **create_table.py** puedes usar el siguiente codigo en la terminal de comando en VS Code:

```bash
python create_table.py
```
Una vez ejecutado este script se deberian agregar 2 tablas más a la base de datos proporcionada que serían las tablas **"contracts"** y **"discount_rules"**. Deberian haber 4 tablas en total almacenadas en la base de datos.

La tabla **"contract"** agrega las condiciones de los contratos de los comercios esto con la idea de que se pueden agregar más comercios o condiciones en un futuro y se pueden ir almacenando en esta tabla.

La tabla **"discount_rules"** almacena las condiciones de descuentos establecidas para los diferentes comercios o compañias de acuerdo a los requerimientos estipulados para aplicar los descuentos.

En caso de que se requieran modificar las condiciones de los contratos, descuentos o valor del IVA, este es el script donde se deberian hacer los cambios.

**Paso 4. Ejecutar script "generate_report.py"**

Este Script es el script principal y más importante del repositorio, **"generate_report.py"** contiene la automatización que calcula las comisiones o valores totales a cobrar a cada empresa o comercio con status activo (**"Active"**) para el mes de Julio y Agosto de 2024, el calculo de los valores totales contiene los descuentos en caso de que cumplan con las condiciones de descuento. 

Al ejecutar este script deberia aparecer una tabla como output con columnas **Fecha-Mes**, **Nombre**, **Nit**, **Valor_comision**, **Valor_iva**, **Valor_Total**, **Correo** en la terminal mostrando todos los resultados para cada comercio o compañia.

Este Script también genera un reporte de comisiones en el formato requerido en un documento excel **xlsx**, el formato de excel se carga automaticamente dentro del mismo repositorio donde se ejecute el script, el documento excel queda automaticamente guardado en la carpeta del repositorio. 

**Nota**: El repositorio ya contiene el archivo generado por el script, para poderlo probar se debe eliminar el documento y ejecutar el script para que se genere nuevamente una vez que se tenga el repositorio localmente.

Lo otra parte importante es que este script también manda un correo con los resultados de las facturas resumidas en la tablas en formato excel **xlsx**.

**Posible Error**

Si al momento de ejecutar el script aparece un mesaje de error parecido a este: **SMTP error occurred: (535, b'5.7.3 Authentication unsuccessful [BN9PR03CA0779.namprd03.prod.outlook.com 2024-12-26T05:07:15.145Z 08DD2543506A083A]')** siginifica que se deben ingresar el **Username** y el **Password** del remitente para poder enviar el correo exitosamente al destinatario.

**Paso 5 (Envio de correo). Ingresa Username y Password del SMTP Server para Office 365 o cualquier otro servicio**

En el script **"send.email.py"** se encuentra la automatización para el envio de correos por SMTP Server para Office 365, en esta parte es importante ingresar el **Username** y el **Password** del sender que es la persona que envia el correo. 

**Pasos para Ingresar Username y Password**

En el script **"send.email.py"** se encuentran las variables **smtp_username** y **smtp_password**, ingresa tu Username en la variable smtp_username y el Password en la variable smtp_password ambos datos deberian ingresarse en formato (str) de python.

**Pasos para configurar el envio de correo**

En el script **"generate_report.py"** se encuentran las opciones para configurar el envio del correo, se pueden agregar los siguientes datos al correo si asi lo desean, para hacerlo buscar las variables en el script y agregar la información en formato (str) de Python de la siguiente manera:

- **recipient**= Ingresar correo del destinatario
- **sender**= Ingresar correo de la persona que lo envia 
- **subject**= Ingresa asunto del correo
- **body**= Ingresar cuerpo del correo 

El resto de variables no deberian sufrir cambios o no es necesario ingresarle datos.

**NOTA**: Una vez se hayan ingresado las configuraciones, se deben guardar los cambios y ejecutar el script "**"generate_report.py"** nuevamente para comprobar si el envio del correo fue exitoso. Deberia aparecer un mensage de envio de correo exitoso en la terminal despues de ejecutado el script. 
