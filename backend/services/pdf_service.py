from reportlab.pdfgen import canvas
import os

OUTPUT_FOLDER = "generated_pdfs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def create_pdf(file_name, agreement):

    pdf_path = os.path.join(
        OUTPUT_FOLDER,
        file_name
    )

    c = canvas.Canvas(pdf_path)

    y = 800

    for line in agreement.split("\n"):

        c.drawString(50, y, line)

        y -= 20

        if y < 50:

            c.showPage()

            y = 800

    c.save()

    return pdf_path