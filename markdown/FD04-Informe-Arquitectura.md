<center>

![logo-upt](../media/logo-upt.png)

# UNIVERSIDAD PRIVADA DE TACNA  
## FACULTAD DE INGENIERÍA  
### Escuela Profesional de Ingeniería de Sistemas

**Plataforma de análisis de datos de matriculados en la carrera de Ingeniería de Sistemas para la Universidad Privada de Tacna - PAMIS**

Curso: *Inteligencia de Negocios*  
Docente: *Mag. Patrick Cuadros Quiroga*

**Integrantes:**

<p style="font-size: 13px;">Agreda Ramirez, Jesus Eduardo  &emsp;&emsp;&emsp;&emsp;- &emsp;  (2021069823)
<br>Castañeda Centurion, Jorge Enrique &emsp; - &emsp; (2021069822)
<br>Contreras Lipa Alvaro Javier &emsp;&emsp;&emsp;&emsp;&emsp;&ensp; - &emsp;  (2021070020)
<br>Malaga Espinoza, Ivan Francisco &emsp;&emsp;&ensp; - &emsp; (2021071086)
<br>Ortiz Fernandez, Ximena Andrea &emsp;&emsp;&ensp; - &emsp;  (2021071080)</p>

**Tacna – Perú**  
***2024***

</center>

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# **Documento de Arquitectura**

**Plataforma de análisis de datos de matriculados en la carrera de Ingeniería de Sistemas para la Universidad Privada de Tacna - PAMIS**

**Versión 1.0**

## **Control de Versiones**

| Versión | Hecha por | Revisada por | Aprobada por | Fecha      | Motivo           |
| :-----: | --------- | ------------ | ------------ | ---------- | ---------------- |
| 1.0     | JAR       | IME          | XOF          | 27/08/2024 | Versión Original |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>


## **Índice General**

1. [Introducción](#1)  
   1.1. Propósito  
   1.2. Alcance  
   1.3. Definiciones, Siglas y Abreviaturas  
   1.4. Visión General  

2. [Representación Arquitectónica](#2)  
   2.1. Escenarios  
   2.2. Vista Lógica  
   2.3. Vista del Proceso  
   2.4. Vista de Desarrollo  
   2.5. Vista Física  

3. [Objetivos y Limitaciones Arquitectónicas](#3)  
   3.1. Disponibilidad  
   3.2. Seguridad  
   3.3. Adaptabilidad  
   3.4. Rendimiento  

4. [Análisis de Requerimientos](#4)  
   4.1. Requerimientos Funcionales  
   4.2. Requerimientos No Funcionales  

5. [Vistas de Caso de Uso](#5)  

6. [Vista Lógica](#6)  
   6.1. Diagrama Contextual  

7. [Vista de Procesos](#7)  
   7.1. Diagrama de Proceso Actual  
   7.2. Diagrama de Proceso Propuesto  

8. [Vista de Despliegue](#8)  
   8.1. Diagrama de Contenedor  

9. [Vista de Implementación](#9)  
   9.1. Diagrama de Componentes  

10. [Vista de Datos](#10)  
    10.1. Diagrama Entidad Relación  

11. [Calidad](#11)  
    11.1. Escenario de Seguridad  
    11.2. Escenario de Usabilidad  
    11.3. Escenario de Adaptabilidad  
    11.4. Escenario de Disponibilidad  
    11.5. Otro Escenario  

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>


