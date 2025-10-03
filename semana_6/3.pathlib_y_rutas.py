from pathlib import Path

root = Path("inventario_app_colab")        # carpeta del proyecto dentro de /content
carp_data = root / "data"
carp_logs = root / "logs"
carp_reports = root / "reports"

# 1) Crear estructura
for d in (carp_data, carp_logs, carp_reports):
    d.mkdir(parents=True, exist_ok=True)

# 2) Escribir log (append)
log = carp_logs / "app.log"
with log.open("a", encoding="utf-8") as f:
    f.write("Inicio de la aplicación\n")

# 3) Guardar un dataset simple y leerlo
datos = carp_data / "productos.txt"
datos.write_text("SKU-001,Teclado,500.0,3\nSKU-002,Mouse,300.0,5\n", encoding="utf-8")
print("Contenido de productos:\n", datos.read_text(encoding="utf-8"))

# 4) Buscar todos los .txt recursivamente
print("Archivos .txt en el proyecto:")
for txt in root.rglob("*.txt"):
    print("  -", txt)