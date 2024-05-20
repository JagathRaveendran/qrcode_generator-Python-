# from flask import Flask, render_template, request
# import qrcode

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')



# @app.route('/generate_qr_code', methods=['POST'])
# def generate_qr_code():
#     data = request.form['data']

#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )

#     qr.add_data(data)
#     qr.make(fit=True)

#     img = qr.make_image(fill_color="black", back_color="white")

#     # Convert image to bytes and encode as base64
#     buffered = BytesIO()
#     img.save(buffered, format="PNG")
#     img_str = base64.b64encode(buffered.getvalue()).decode()

#     # Create data URI for the image
#     data_uri = f"data:image/png;base64,{img_str}"

#     return render_template('qrcode.html', data_uri=data_uri)



# @app.route('/generate_qr_code', methods=['POST'])
# def generate_qr_code():
#     data = request.form['data']

#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )

#     qr.add_data(data)
#     qr.make(fit=True)

#     img = qr.make_image(fill_color="black", back_color="white")
#     img.save("static/qrcode.png")

#     return render_template('qrcode.html')

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
from flask import send_from_directory
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_qr_code')
def download_qr_code():
    return send_from_directory('static', 'qrcode.png', as_attachment=True)

@app.route('/generate_qr_code', methods=['POST'])
def generate_qr_code():
    data = request.form['data']

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("static/qrcode.png")

    # Render the template with the generated QR code image path
    return render_template('qrcode.html', qr_image="qrcode.png")

if __name__ == '__main__':
    app.run(debug=True)


