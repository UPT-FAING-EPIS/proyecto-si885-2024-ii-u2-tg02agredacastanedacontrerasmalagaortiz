import pandas as pd
import pyodbc

cnxn = pyodbc.connect(
    'Driver={ODBC Driver 18 for SQL Server};'
    'Server=tcp:bi-segunda-unidad.database.windows.net,1433;'
    'Database=CICLO_UNIVERSITARIO;'
    'Uid=adminsql;'
    'Pwd=Upt2024!;'
    'Encrypt=yes;'
    'TrustServerCertificate=no;'
    'Connection Timeout=30;'
)

cursor = cnxn.cursor()

excel_files = [
    './Consolidado/Consolidado_semestre_2020-I.xlsx',
    './Consolidado/Consolidado_semestre_2020-II.xlsx',
    './Consolidado/Consolidado_semestre_2021-I.xlsx',
    './Consolidado/Consolidado_semestre_2021-II.xlsx',
    './Consolidado/Consolidado_semestre_2022-I.xlsx',
    './Consolidado/Consolidado_semestre_2022-II.xlsx',
    './Consolidado/Consolidado_semestre_2023-I.xlsx',
]

for file in excel_files:
    df = pd.read_excel(file, sheet_name='Hoja2')
    
    # Asegurarse de que CODIGO CURSO y ASIGNATURA sean leídos correctamente
    df['CodigoCurso'] = df['CODIGO CURSO'].astype(str)
    df['NombreCurso'] = df['ASIGNATURA'].astype(str)
    df['Matriculados'] = pd.to_numeric(df['MATRICULADOS'], downcast='integer')
    df['Aprobados'] = pd.to_numeric(df['APROBADOS'], downcast='integer')
    df['Desaprobados'] = pd.to_numeric(df['CANTIDAD DESAPROBADOS'], downcast='integer')
    df['Retiros'] = pd.to_numeric(df['CANTIDAD RETIRADOS'], downcast='integer')
    df['Abandonos'] = pd.to_numeric(df['CANTIDAD ABANDONADOS'], downcast='integer')
    df['TotalLlevados'] = pd.to_numeric(df['TOTAL LLEVADOS'], downcast='integer')
    df['CantidadConvalidados'] = pd.to_numeric(df['CANTIDAD CONVALIDADOS'], downcast='integer')
    df['NotaMinima'] = pd.to_numeric(df['NOTA MÍNIMA'].str.replace(',', '.'), errors='coerce').fillna(0.0)
    df['NotaMaxima'] = pd.to_numeric(df['NOTA MÁXIMA'].str.replace(',', '.'), errors='coerce').fillna(0.0)
    df['Promedio'] = pd.to_numeric(df['PROMEDIO'], errors='coerce').fillna(0.0)
    df['DesviacionEstandar'] = pd.to_numeric(df['DESVIACIÓN ESTÁNDAR'].str.replace(',', '.'), errors='coerce').fillna(0.0)
    df['Semestre'] = df['SEMESTRE'].astype(str)

    # Extraer semestre del nombre del archivo
    df['Semestre'] = file.split('_')[2].split('.')[0]
    
    # Insertar en la base de datos
    for index, row in df.iterrows():
        cursor.execute("""
            INSERT INTO Cursos 
            (CodigoCurso, NombreCurso, Matriculados, Aprobados, Desaprobados, Retiros, Abandonos, TotalLlevados, CantidadConvalidados, NotaMinima, NotaMaxima, Promedio, DesviacionEstandar, Semestre) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       row['CodigoCurso'],
                       row['NombreCurso'],
                       row['Matriculados'],
                       row['Aprobados'],
                       row['Desaprobados'],
                       row['Retiros'],
                       row['Abandonos'],
                       row['TotalLlevados'],
                       row['CantidadConvalidados'],
                       row['NotaMinima'],
                       row['NotaMaxima'],
                       row['Promedio'],
                       row['DesviacionEstandar'],
                       row['Semestre']
                       )
    # Guardar los cambios
    cnxn.commit()

# Cerrar conexiones
cursor.close()
cnxn.close()
