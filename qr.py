import streamlit as st
import qrcode
from PIL import Image
import io

# Título de la aplicación
st.title("Generador de Código QR")

# Entrada del texto para generar el QR
qr_text = st.text_input("Introduce el texto o enlace para generar el código QR")

if qr_text:
    # Crear código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_text)
    qr.make(fit=True)

    # Convertir el código QR en imagen
    img = qr.make_image(fill='black', back_color='white')

    # Mostrar la imagen en Streamlit
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    st.image(buffer, caption="Código QR generado", use_column_width=True)
