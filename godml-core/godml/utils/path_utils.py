import os
from pathlib import Path

def normalize_path(path: str) -> str:
    """
    Convierte rutas con formato Windows a rutas absolutas compatibles con Linux/macOS.
    También convierte rutas relativas a absolutas.
    """
    # Manejo de /C:/ o C:/ usado en Windows
    if path.startswith("/C:/") or path.startswith("C:/"):
        path = path.replace("/C:/", "").replace("C:/", "")
        return os.path.abspath(f"/mnt/c/{path}")

    # Manejo de rutas como C:\Users\... (estilo Windows puro)
    if ":" in path and "\\" in path:
        drive, subpath = path.split(":", 1)
        subpath_clean = subpath.replace("\\", "/")
        return os.path.abspath(f"/mnt/{drive.lower()}/{subpath_clean}")
    
    return str(Path(path).expanduser().resolve())
