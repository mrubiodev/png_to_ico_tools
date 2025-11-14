# pngtoico

Pequeña utilidad en Python para convertir imágenes PNG a archivos ICO (varias resoluciones).

Basado en una plantilla de proyecto mayor, este repositorio contiene una herramienta simple y portátil que permite:

- Convertir un PNG a un ICO con múltiples tamaños (16, 32, 48, 64 por defecto).
- Pasar la ruta del PNG por argumento de línea de comandos.
- Abrir un diálogo gráfico (Tkinter) para seleccionar el PNG cuando se ejecuta sin argumentos.
- Alternar explícitamente al diálogo gráfico con `--gui`.

## Requisitos

- Python 3.8+ (probado con Python 3.13 en Windows)
- Pillow (biblioteca de imágenes)

Instalar dependencias:

```powershell
# Crear/activar entorno virtual (opcional)
python -m venv .venv; .\.venv\Scripts\Activate.ps1
# Instalar dependencias
python -m pip install -r requirements.txt
```

Si no usas el entorno virtual, puedes instalar Pillow directamente:

```powershell
python -m pip install Pillow
```

## Uso

Desde PowerShell o terminal:

- Usar pasando el archivo como argumento:

```powershell
python "m:\mrubiodev\TipsandUtils\MiniTools\pngtoico\main.py" imagen.png
```

- Ejecutar sin argumentos: por defecto intentará abrir un diálogo gráfico para seleccionar el PNG; si cancelas, volverá a pedir la ruta por consola (si hay TTY):

```powershell
python "m:\mrubiodev\TipsandUtils\MiniTools\pngtoico\main.py"
```

- Forzar el diálogo gráfico con `--gui`:

```powershell
python "m:\mrubiodev\TipsandUtils\MiniTools\pngtoico\main.py" --gui
```

- Mostrar ayuda:

```powershell
python "m:\mrubiodev\TipsandUtils\MiniTools\pngtoico\main.py" --help
```

## Salida

El fichero ICO resultante se guarda junto al PNG (o en el directorio de trabajo) con el mismo nombre base y extensión `.ico`. Por ejemplo `imagen.png` → `imagen.ico`.

## Notas técnicas

- El script usa Pillow para abrir y guardar imágenes. Se generan varios tamaños para que el ICO soporte diferentes resoluciones.
- Si deseas tamaños adicionales (ej. 128, 256) o parámetros personalizables, puedo añadir una opción CLI `--sizes` que acepte una lista separada por comas.

## Ejemplos

- Convertir `logo.png` a `logo.ico` (diálogo o prompt si se ejecuta sin argumento):

```powershell
python main.py logo.png
```

- Abrir selector gráfico y convertir:

```powershell
python main.py --gui
```
