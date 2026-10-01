# -*- coding: utf-8 -*-
"""
Script para la generación de la Base de Datos simulada de CompuConnect.
Asignatura: Seminario en Analítica y Big Data
Autor: Wilson Fernando Pinzon Guacaneme
Año: 2025
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# ==========================================
# 1. CONFIGURACIÓN DE PARÁMETROS INICIALES
# ==========================================
# Fijamos una semilla (seed) para garantizar que los datos siempre sean los mismos al ejecutarlo
np.random.seed(42)
random.seed(42)
num_registros = 100  # Total de transacciones del año 2024

# ==========================================
# 2. DEFINICIÓN DE ENTIDADES DEL NEGOCIO
# ==========================================
# Mapeo exacto de asesores comerciales y sus zonas asignadas
vendedores_regiones = [
    {"vendedor": "Carlos Ramirez", "ciudad": "Cali", "departamento": "Valle Del Cauca"},
    {"vendedor": "Juan Montoya", "ciudad": "Bogota", "departamento": "Bogota"},
    {"vendedor": "Natalia Jimenez", "ciudad": "Ibague", "departamento": "Tolima"},
    {"vendedor": "Luisa Arias", "ciudad": "Medellín", "departamento": "Antioquia"},
    {"vendedor": "Ana Cordoba", "ciudad": "Bogota", "departamento": "Bogota"}
]

# Catálogo maestro de productos con precios reales y costos base (para cálculo de DAX)
productos_detalle = [
    {"producto": "Base Refrigerante Para Computador Dos Ventiladores Jetech KL330", "categoria": "Accesorios", "precio": 54900, "costo": 35000},
    {"producto": "Parlantes Para Computador ATI", "categoria": "Audio", "precio": 88900, "costo": 55000},
    {"producto": "Combo Teclado Y Mouse Inalambrico 2.4GHZ GKM520", "categoria": "Periféricos", "precio": 53900, "costo": 33900},
    {"producto": "Memoria USB Sandisk SDC2410 32GB", "categoria": "Almacenamiento", "precio": 39900, "costo": 25000},
    {"producto": "Multipuerto USB Hub P-1601", "categoria": "Almacenamiento", "precio": 45900, "costo": 29000},
    {"producto": "Pad Mouse Gamer GMS-X3", "categoria": "Periféricos", "precio": 29900, "costo": 18000},
    {"producto": "Mousepad Jetech MP44", "categoria": "Periféricos", "precio": 19900, "costo": 12000},
    {"producto": "Microfono Omega De Mesa 6620268K", "categoria": "Otros", "precio": 63900, "costo": 41000},
    {"producto": "Soporte Para Computador Portatil Plegable Metalico Graduable AED01", "categoria": "Otros", "precio": 44900, "costo": 28000}
]

# Variables categóricas complementarias para segmentación en Power BI
clientes = ["Yuli Gomez", "Hernando Jaramillo", "Jose Lopez", "Lady Pulido", "Laura Martinez", "Solange Jimenez", "Sebastian Gomez", "Diana Suarez"]
medios_pago = ["Transferencia", "Tarjeta", "Efectivo"]
estados = ["Entregado", "Pendiente", "Devuelto"]
tipos_cliente = ["Particular", "Corporativo"]

# ==========================================
# 3. SIMULACIÓN TEMPORAL (AÑO 2024)
# ==========================================
# Creamos fechas distribuidas aleatoriamente a lo largo de las 24 horas de los 365 días del 2024
fecha_inicio = datetime(2024, 1, 1)
fechas = [fecha_inicio + timedelta(days=random.randint(0, 364), hours=random.randint(0, 23)) for _ in range(num_registros)]
fechas.sort()  # Se ordenan cronológicamente para simular una secuencia real de auditoría

# ==========================================
# 4. CONSTRUCCIÓN LOGÍSTICA DEL DATASET
# ==========================================
data = []
for i in range(num_registros):
    fecha_str = fechas[i].strftime("%Y-%m-%d %H:%M:%S")
    
    # Extracción de variables aleatorias desde nuestros maestros estructurados
    vr = random.choice(vendedores_regiones)
    prod = random.choice(productos_detalle)
    cliente = random.choice(clientes)
    medio = random.choice(medios_pago)
    estado = random.choice(estados)
    tipo = random.choice(tipos_cliente)
    
    # Asignación de cantidades de compra lógicas por transacción
    cantidad = random.randint(1, 10)
    precio_unitario = prod["precio"]
    costo_unitario = prod["costo"]
    
    # Métricas financieras calculadas idénticas a los requerimientos del reporte
    monto_total = cantidad * precio_unitario
    utilidad = monto_total - (cantidad * costo_unitario)
    margen_porcentaje = round((utilidad / monto_total) * 100, 2) if monto_total > 0 else 0
    
    # Agrupamos la fila correspondiente
    data.append([
        fecha_str, vr["vendedor"], vr["ciudad"], vr["departamento"], 
        prod["producto"], cantidad, precio_unitario, costo_unitario,
        monto_total, utilidad, margen_porcentaje, cliente, 
        prod["categoria"], medio, estado, tipo
    ])

# ==========================================
# 5. ESTRUCTURACIÓN EN PANDAS Y EXPORTACIÓN
# ==========================================
columnas = [
    "Fecha", "Vendedor", "Ciudad", "Departamento", 
    "Producto", "Cantidad", "Precio Unitario", "Costo Unitario",
    "Monto Total", "Utilidad", "Margen (%)", "Cliente", 
    "Categoría", "Medio de Pago", "Estado", "Tipo Cliente"
]
df = pd.DataFrame(data, columns=columnas)

# Guardamos el archivo final estructurado listo para conectar directamente a tu Power BI
output_file = "Base de Datos.xlsx"
df.to_excel(output_file, index=False, sheet_name="FactVentas")

print(f"¡Base de datos generada exitosamente con {len(df)} registros en el archivo '{output_file}'!")
