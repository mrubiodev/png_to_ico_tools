import os
from PIL import Image #pip install Pillow

def png_to_ico(png_file):
    # Verifica si el archivo existe y tiene la extensión .png
    if not os.path.isfile(png_file) or not png_file.endswith('.png'):
        print(f"Error: '{png_file}' no es un archivo PNG válido.")
        return

    # Obtiene el nombre del archivo sin la extensión
    filename = os.path.splitext(os.path.basename(png_file))[0]

    # Crea el archivo ICO
    ico_file = f"{filename}.ico"
    try:
        # Abre la imagen PNG
        image = Image.open(png_file)

        # Crea las diferentes resoluciones de icono
        image.save(ico_file, sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
        print(f"Archivo ICO generado: {ico_file}")
    except Exception as e:
        print(f"Error al generar el archivo ICO: {e}")

if __name__ == "__main__":
    # Permitir pasar el archivo PNG por argumento, abrir un diálogo GUI, o solicitar interactivamente
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Convertir un archivo PNG a ICO (varias resoluciones)')
    parser.add_argument('png_file', nargs='?', help='Ruta al archivo PNG a convertir')
    parser.add_argument('--gui', action='store_true', help='Abrir un diálogo gráfico para seleccionar el archivo PNG')
    parser.add_argument('--sizes', help='Lista separada por comas de tamaños para el ICO, ej: 16,32,48,64', default='16,32,48,64')
    args = parser.parse_args()

    png_file = args.png_file

    # Si no se pasó argumento, por defecto intentar abrir diálogo GUI primero
    if not png_file:
        tried_gui = False
        try:
            tried_gui = True
            import tkinter as tk
            from tkinter import filedialog

            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename(title='Seleccione un archivo PNG', filetypes=[('PNG', '*.png')])
            root.destroy()

            if file_path:
                png_file = file_path
            else:
                # usuario canceló el diálogo; si hay TTY disponible, volver al prompt
                if sys.stdin.isatty():
                    print('No se seleccionó ningún archivo en el diálogo. Volviendo al ingreso por consola.')
                    png_file = input("Ingrese el nombre del archivo PNG: ")
                else:
                    print('No se seleccionó ningún archivo y no hay consola disponible. Operación cancelada.')
                    sys.exit(0)
        except Exception as e:
            # Si no se puede usar GUI (por ejemplo falta tkinter), intentar consola si está disponible
            if sys.stdin.isatty():
                print(f'No se pudo abrir la ventana gráfica (continuando por consola): {e}')
                png_file = input("Ingrese el nombre del archivo PNG: ")
            else:
                print(f'No se pudo abrir la ventana gráfica y no hay consola disponible: {e}')
                sys.exit(1)

    # Parsear tamaños
    def parse_sizes(sizes_str):
        parts = [p.strip() for p in sizes_str.split(',') if p.strip()]
        sizes = []
        for p in parts:
            try:
                n = int(p)
                if n <= 0:
                    raise ValueError('Las dimensiones deben ser positivas')
                sizes.append((n, n))
            except Exception:
                raise ValueError(f"Tamaño inválido en --sizes: '{p}'")
        return sizes

    try:
        sizes = parse_sizes(args.sizes)
    except ValueError as e:
        print(e)
        sys.exit(2)

    # Verificar que el archivo es PNG antes de intentar crear ICO
    def is_png_file(path):
        try:
            with Image.open(path) as im:
                return im.format == 'PNG'
        except Exception:
            # fallback a comprobación por extensión
            return path.lower().endswith('.png')

    # Si --gui fue pasado explícitamente y aún no tenemos archivo, ya se manejó más arriba; de lo contrario png_file puede venir por argumento o prompt
    # Validación final: comprobar que el archivo es PNG
    if not os.path.isfile(png_file):
        print(f"Error: '{png_file}' no es un archivo válido o no existe.")
        sys.exit(1)

    if not is_png_file(png_file):
        print(f"Error: '{png_file}' no parece ser un PNG válido.")
        sys.exit(1)

    # Usar los tamaños solicitados al guardar
    try:
        image = Image.open(png_file)
        filename = os.path.splitext(os.path.basename(png_file))[0]
        ico_file = f"{filename}.ico"
        image.save(ico_file, sizes=sizes)
        print(f"Archivo ICO generado: {ico_file}")
    except Exception as e:
        print(f"Error al generar el archivo ICO: {e}")