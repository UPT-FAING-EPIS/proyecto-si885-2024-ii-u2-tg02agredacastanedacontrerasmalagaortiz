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

# **Documento de Especidifcaciòn de Requerimientos**

**Plataforma de análisis de datos de matriculados en la carrera de Ingeniería de Sistemas para la Universidad Privada de Tacna - PAMIS**

**Versión 1.0**

## **Control de Versiones**

| Versión | Hecha por | Revisada por | Aprobada por | Fecha      | Motivo           |
| :-----: | --------- | ------------ | ------------ | ---------- | ---------------- |
| 1.0     | JAR       | IME          | XOF          | 27/08/2024 | Versión Original |

<div style="page-break-after: always; visibility: hidden">\pagebreak</div>


## **Índice General**

 [Introducción](#introducción)  

I. [**Generalidades de la Empresa**](#1)  
   1. Nombre de la Empresa
   2. Visión
   3. Misión
   4. Organigrama 

II. [**Visionamiento de la Empresa**](#2)    
   1. Descripción del Problema
   2. Objetivos de Negocios
   3. Objetivos de Diseño
   4. Alcance del Proyecto
   5. Viabilidad del Sistema
      5.1. Viabilidad Técnica
   6. Información obtenida del Levantamiento de Información

III. [**Análisis de Procesos**](#3)

   a) Diagrama del Proceso Actual - Diagrama de Actividades
   
   b) Diagrama del Proceso Propuesto - Diagrama de Actividades Inicial

IV. [**Especificación de Requerimientos de Software**](#4) 

   a) Cuadro de Requerimientos Funcionales Inicial

   b) Cuadro de Requerimientos No Funcionales

   c) Cuadro de Requerimientos Funcionales Final

   d) Reglas de Negocio

V. [**Fases de Desarrollo**](#5)   
   1. Perfiles de Usuario
   2. Modelo Conceptual

      a) Diagrama de Paquetes

      b) Diagrama de Casos de Uso 

      c) Escenarios de Caso de Uso (Narrativa)

   3. Modelo Lógico

      a) Análisis de Objetos

      b) Diagrama de Actividades con Objetos

      c) Diagrama de Secuencia 

      d) Diagrama de Clases

[Conclusiones](#conclusiones)  
[Recomendaciones](#recomendaciones)  


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

## 1. Generalidades de la Empresa <a id="1"></a>
### 1. Nombre de la Empresa
Universidad Privada de Tacna

### 2. Visión
La visión de la UPT con la plataforma PAMIS es fortalecer la calidad educativa mediante una herramienta analítica que permita a los estudiantes tomar decisiones informadas basadas en datos. La plataforma se alinea con el objetivo institucional de proporcionar una educación personalizada y orientada al éxito académico, apoyando el análisis de datos como pilar fundamental para la mejora continua y la toma de decisiones estratégicas”

### 3. Misión
"La misión de la UPT, a través de PAMIS, es ofrecer una herramienta que facilite el acceso a datos académicos detallados y personalizados para los estudiantes de Ingeniería de Sistemas. Esto busca optimizar su experiencia académica y mejorar su rendimiento, brindando una plataforma que centralice la información académica y reduzca la carga administrativa de la consulta y el manejo de datos.

### 4. Organigrama
<center>

![organigrama](../media/organigrama.png)
</center>

Administradores: Nivel superior compuesto por directores de escuela y coordinadores de carrera. Se encargan de optimizar recursos y tomar decisiones estratégicas con base en los datos proporcionados por PAMIS.

Estudiantes: En el nivel base, los usuarios principales de PAMIS, quienes acceden a la plataforma para evaluar su rendimiento, identificar áreas de mejora y tomar decisiones informadas sobre su trayectoria académica.

### 5. Fases de Desarrollo</h2>

#### 1. Perfiles de Usuario

<ul style="text-align: justify;">
    <li><strong>Administradores:</strong><p style="text-align: justify;">
    Es el responsable de supervisar y gestionar toda la información del sistema. Tiene acceso completo para actualizar datos académicos, generar reportes completos y brindar soporte técnico. Además, se encarga del mantenimiento del sistema y de asegurar su correcto funcionamiento. Requiere conocimientos técnicos en herramientas como Power BI y habilidades para manejar datos y resolver problemas del sistema.
    </p>

 </li>
    <li><strong>Estudiantes:</strong><p style="text-align: justify;">
    Es el usuario final que interactúa con la plataforma para consultar datos académicos agregados y segmentados. Puede explorar estadísticas generales de la población estudiantil, como tasas de aprobación o índices de deserción, pero no puede acceder a información específica de otros estudiantes ni visualizar su propio rendimiento. Este perfil está diseñado para analizar tendencias académicas globales y no personalizadas.
    </p>

 </li>
</ul>

#### 2. Modelo Conceptual



### a) Diagrama de Paquetes

**Diagrama de Paquetes de PAMIS**  
![diagrama_de_paquete](../media/diagrama_de_paquete.png)

El diagrama representa la estructura de PAMIS, donde los Dashboards interactúan con los usuarios y son gestionados a través del Power BI Service, que recibe reportes publicados desde los Servicios de Publicación de Power BI. La Base de Datos provee la información que alimenta los gráficos, asegurando un flujo eficiente entre datos, procesamiento y visualización.

---

### b) Diagrama de Casos de Uso

**Diagrama de Casos de Uso de la Plataforma en PowerBi**  
*(diagrama)*

El diagrama muestra cómo el *Estudiante* interactúa con el sistema PAMIS para:

- Consultar estadísticas académicas
- Aplicar filtros
- Exportar reportes

Este modelo destaca las principales funcionalidades disponibles para el usuario.

## c) Escenarios de Caso de Uso (narrativa)

### Narrativa de CU01: “Consultar estadísticas académicas”

| **Caso de Uso**            | Consultar estadísticas académicas (CU01)                                        |
|-----------------------------|---------------------------------------------------------------------------------|
| **Actores**                | Estudiante                                                                      |
| **Descripción**            | Permitir a los estudiantes acceder directamente a la plataforma PAMIS y explorar diferentes secciones de análisis, cada una con gráficos interactivos que muestran información específica, como estadísticas de matrículas, desempeño académico, comparaciones entre cohortes e identificación de áreas críticas. |
| **Precondiciones**         | El estudiante debe tener acceso a un dispositivo con conexión a la plataforma PAMIS. |
| **Flujo Normal**           |                                                                                 |
| **Acción del Actor**       | **Curso del Sistema**                                                           |
| 1. Accede a la plataforma PAMIS desde su navegador. | 2. Muestra la pantalla principal con las secciones disponibles: Análisis de Matrículas, Desempeño Académico, Análisis Comparativo e Identificación de Áreas Críticas. |
| 3. Selecciona una sección, como "Análisis de Matrículas". | 4. Carga y muestra los gráficos relacionados con las estadísticas de matrículas. |
| 5. Navega por los gráficos y observa los datos mostrados. | 6. Permite interactuar con los gráficos, mostrando detalles específicos al pasar el cursor o hacer clic. |

---

### Narrativa de CU02: “Aplicar filtros a los gráficos”

| **Caso de Uso**            | Aplicar filtros a los gráficos (CU02)                                           |
|-----------------------------|---------------------------------------------------------------------------------|
| **Actores**                | Estudiante                                                                      |
| **Descripción**            | Permitir a los estudiantes personalizar los datos mostrados en los gráficos interactivos aplicando filtros específicos, como selección de semestres, cursos o indicadores académicos. |
| **Precondiciones**         | El estudiante debe estar visualizando un gráfico en cualquiera de las secciones disponibles en la plataforma PAMIS. |
| **Flujo Normal**           |                                                                                 |
| **Acción del Actor**       | **Curso del Sistema**                                                           |
| 1. Selecciona un gráfico dentro de una sección de análisis. | 2. Muestra el gráfico con los datos generales y las opciones de filtros disponibles. |
| 3. Elige un filtro, como "Semestre: 2021-I". | 4. Actualiza el gráfico para reflejar los datos correspondientes al semestre seleccionado. |
| 5. Selecciona un segundo filtro, como "Curso: Auditoría de Sistemas". | 6. Combina ambos filtros y actualiza el gráfico de manera interactiva. |

---

### Narrativa de CU03: “Exportar reportes”

| **Caso de Uso**            | Exportar reportes (CU03)                                                        |
|-----------------------------|---------------------------------------------------------------------------------|
| **Actores**                | Estudiante                                                                      |
| **Descripción**            | Permitir a los estudiantes exportar los reportes generados en la plataforma PAMIS en formatos XLSX o CSV, para su análisis y uso externo. |
| **Precondiciones**         | El estudiante debe estar visualizando un gráfico o reporte en cualquier sección de la plataforma PAMIS. |
| **Flujo Normal**           |                                                                                 |
| **Acción del Actor**       | **Curso del Sistema**                                                           |
| 1. Selecciona un gráfico dentro de una sección. | 2. Muestra el gráfico con la opción "Exportar datos". |
| 3. Hace clic en la opción "Exportar datos". | 4. Muestra un cuadro de diálogo con las opciones de exportación: "Datos resumidos" o "Datos con diseño actual" (si aplicable). |
| 5. Selecciona "Datos resumidos". | 6. Habilita los formatos disponibles para exportar: XLSX y CSV. |
| 7. Elige un formato, como "XLSX". | 8. Procesa la exportación y genera el archivo en el formato seleccionado. |
| 9. Hace clic en el botón de descarga. | 10. Descarga el archivo al dispositivo del estudiante. |

## Conclusiones<a id="conclusiones"></a>

+ PAMIS permite centralizar y optimizar el análisis académico mediante herramientas interactivas que mejoran la toma de decisiones de estudiantes, docentes y administradores.
+ La plataforma resuelve la falta de acceso a estadísticas académicas detalladas, proporcionando gráficos dinámicos y opciones de filtrado que facilitan la exploración de datos relevantes.
+ La integración de Power BI garantiza una experiencia de usuario intuitiva y accesible, reduciendo la carga administrativa y aumentando la eficiencia en la planificación académica.

## Recomendaciones<a id="recomendaciones"></a>
+ Ampliar el alcance de PAMIS para incluir otras carreras profesionales, potenciando su utilidad en toda la universidad.
+ Incorporar soporte para dispositivos móviles para aumentar la accesibilidad de la plataforma.
+ Realizar actualizaciones continuas basadas en el feedback de los usuarios para mejorar la experiencia y funcionalidad del sistema.
+ Implementar funcionalidades predictivas basadas en inteligencia artificial para proporcionar recomendaciones personalizadas a los estudiantes.