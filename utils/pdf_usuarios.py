# pip install reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_pdf_usuarios(usuarios, nombre_archivo="usuarios.pdf"):
    """
    Recibe una lista de dicts (usuarios) y genera un PDF con el listado.
    """
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    width, height = letter

    # Título
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Listado de usuarios")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 65, "Generado por el sistema de gestion de personas")

    # Encabezados
    y = height - 100
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50,  y, "RUT")
    c.drawString(120, y, "Nombre")
    c.drawString(280, y, "Usuario")
    c.drawString(380, y, "Direccion")
    c.drawString(520, y, "Sueldo")

    y -= 15
    c.line(50, y, 560, y)
    y -= 15

    c.setFont("Helvetica", 9)

    for u in usuarios:
        if y < 50:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 9)

        c.drawString(50,  y, str(u["rut"]))
        c.drawString(120, y, str(u["nombre"])[:25])
        c.drawString(280, y, str(u["usuario"])[:15])
        c.drawString(380, y, str(u["direccion"])[:25])
        c.drawRightString(560, y, str(u["sueldo"]))

        y -= 15

    c.save()
    print(f"PDF generado correctamente: {nombre_archivo}")
