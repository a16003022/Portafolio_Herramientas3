# Portafolio Herramientas3 - Heisler Narváez Kú
--------------------------------------------------------------------------------------------------------
1) Modelo en Azure ML Studio  
* a) Screenshot del modelo generado:
![Completado](https://github.com/a16003022/Portafolio_Herramientas3/blob/main/Completado.png)
* b) Models:
![Modelos](https://github.com/a16003022/Portafolio_Herramientas3/blob/main/Modelos.png)
* c) Métricas del mejor modelo:
![Metricas](https://github.com/a16003022/Portafolio_Herramientas3/blob/main/Metricas.png)
2) Mongo DB - log de commits
* a) Práctica de conectarse a una base de datos desde Colab:<br>
   <b>IMPORTANTE:</b> Dicha práctica se encuentra al final del documento, ya que además contiene todos los ejercicios realizados en clase.<br>
    Link del archivo colab: https://colab.research.google.com/drive/1nBuKbm_TV0SzAzG9XqcLSQGes_oM2TLd?usp=sharing 
3) Mongo DB - Práctica de Map reduce: <br>
    Aquí como nos funcionó desde la línea de comandos, lo hicimos desde la interfaz gráfica.
* En la colección donde deseamos hacer un aggregation seleccionamos la función que queremos utilizar en el pipeline, en este caso fue $group para agrupar todos los elementos de la colección por la fecha de envío del correo y sumar cuántos elementos agrupó.<br>
![Aggregarion](https://github.com/a16003022/Portafolio_Herramientas3/blob/main/Aggregation.png)
* Una vez verificado el resultado esperado en la vista previa, guardamos este pipeline como una vista, lo cual será de gran ayuda si se insertan nuevos documentos a la colección, esta vista se irá actualizando; contrario al caso de querer crear una nueva colección.<br>

4) 
