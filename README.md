
# Análisis de Ventas y Rentabilidad en CompuConnect 💻📊

![Power BI](https://shields.io) ![Excel](https://shields.io) ![Python](https://shields.io)


Este repositorio contiene el proyecto final desarrollado para la asignatura de **Seminario en Analítica y Big Data** en Bogotá D.C. El objetivo principal es transformar datos brutos de ventas en información estratégica para optimizar la toma de decisiones comerciales en la empresa ficticia **CompuConnect**, dedicada a la comercialización de accesorios para computadores.

## 📋 Descripción del Proyecto
CompuConnect enfrentaba el reto de comprender el comportamiento de sus ventas en tiendas físicas en cuatro departamentos de Colombia, evaluar el desempeño de su equipo de ventas e identificar a sus clientes potenciales. Para resolverlo, se diseñó e implementó una solución integral de Inteligencia de Negocios utilizando un modelo de datos en estrella y un dashboard interactivo en Power BI.

## 📊 Arquitectura de Datos y Modelo ETL
1. **Extracción y Origen:** Dataset simulado mediante Python en formato Excel con 100 registros detallados de transacciones del año 2024.
2. **Transformación (ETL en Power Query):** Se realizaron labores de depuración (remoción de duplicados y nulos), conversión de tipos de datos, normalización de campos de texto y creación de columnas calculadas mediante lenguaje DAX (Monto Total, Utilidad, Margen % y Ticket Promedio).
3. **Modelado (Star Schema):** Implementación de un modelo analítico en estrella compuesto por una tabla de hechos (`FactVentas`) y cuatro tablas de dimensiones (`DimProducto`, `DimCliente`, `DimVendedor` y `DimFecha`), optimizando el rendimiento de las consultas multidimensionales.

## 💡 Indicadores y Hallazgos Clave (Insights)
De acuerdo con el análisis de los 100 registros del periodo 2024, se identificaron los siguientes resultados comerciales:
* **Rendimiento Global:** Se consolidó un volumen de **Total Ventas de 35 millones** (exactamente \$34,210,000.00), una **Ganancia/Utilidad de 12 millones** y un **Ticket Promedio de \$65 mil** por cada una de las 530 unidades vendidas.
* **Concentración Geográfica y Categorías:** El departamento del **Tolima (Ibagué)** lidera ampliamente los ingresos regionales. A nivel de inventario, la categoría de **Almacenamiento** es la más demandada.
* **Fuerza de Ventas:** Los vendedores **Luisa Arias** (Medellín) y **Carlos Ramírez** (Cali) se posicionaron como los de mayor rendimiento comercial.
* **Producto Estrella:** El dispositivo **Multipuerto USB Hub P-1601** se consolidó como el producto más vendido, generando un volumen de facturación de **\$1.259 millones**.

## 🛠️ Estructura del Repositorio
* `/data`: Archivo original `Base de Datos.xlsx` generado de forma simulada.
* `/dashboards`: Archivo fuente de Power BI `Proyectofinal.pbix`.
* `/reports`: Documento metodológico e informe final en PDF (`Entregable técnico.pdf`).

## 📈 Vistas del Dashboard Interactivo
El reporte de Power BI se estructuró en tres vistas clave para la toma de decisiones:

### 1. Resumen General de Ventas 
Presenta la salud financiera del negocio, Kpis globales y distribución de ingresos por categorías y ciudades.
<img width="1105" height="620" alt="image" src="https://github.com/user-attachments/assets/5739e074-9c56-448e-bb72-196897fdb1dc" />


### 2. Rendimiento por Vendedor y Cliente
Permite evaluar de forma dinámica el Top de clientes acumulados y el promedio de ventas por asesor comercial.
<img width="998" height="561" alt="image" src="https://github.com/user-attachments/assets/29c1a5f2-a79f-4374-8a09-dc065f306ef7" />


### 3. Análisis de Productos y Rentabilidad
Explora la relación entre el precio promedio y el volumen de salida, contrastando el margen de utilidad real contra el ingreso bruto por producto.
<img width="680" height="395" alt="image" src="https://github.com/user-attachments/assets/3fe84a80-e357-40a6-8fe0-17f0e4e491fe" />


## 🎓 Conclusiones del Proyecto
* La estructuración de datos bajo un **modelo en estrella** simplifica la creación de relaciones eficientes 1:* hacia la tabla de hechos.
* El uso de **fórmulas DAX** es indispensable en entornos corporativos para estructurar métricas de rentabilidad escalables en tiempo real.
* Las herramientas analíticas reducen la incertidumbre, transformando registros planos de Excel en visualizaciones accionables para planeación comercial futura.

---
**Autor:** Wilson Fernando Pinzon Guacaneme  
**Asignatura:** Seminario en Analítica y Big Data (2025)  

