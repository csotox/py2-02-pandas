from pathlib import Path

import pandas as pd

#-- - --------------------------------------
# Convensión de nombres
# Clases se escriben en PascalCase
# Funciones se escriben en snake_case
#-- - --------------------------------------

DATA_DIR = Path( "data" )

def get_ruta():
    return DATA_DIR

def cargar_csv(nombre_archivo: str) -> pd.DataFrame:

    ruta = DATA_DIR / nombre_archivo

    if not ruta.exists():
        raise FileNotFoundError(
            f"Archvio no existe [{ruta}]"
        )

    return pd.read_csv( ruta )

