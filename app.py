from flask import Flask, request, jsonify
import os
import uuid
import requests

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

API_URL = 'https://api.collov.ai/flair/enterpriseApi/collovAi/generateImage'
API_KEY = 'Bearer ck_F1CCB7229737B54EE4D8AF201D033B76'

@app.route('/generate', methods=['POST'])
def generate_image():
    if 'image' not in request.files:
        return jsonify({"error": "Nessuna immagine inviata"}), 400

    image = request.files['image']
    style = request.form.get('style')
    room_type = request.form.get('roomType')

    if not style or not room_type:
        return jsonify({"error": "Style o roomType mancanti"}), 400

    # Salva immagine
    image_name = f"{uuid.uuid4().hex}_{image.filename}"
    image_path = os.path.join(UPLOAD_FOLDER, image_name)
    image.save(image_path)

    # URL pubblico (modifica con il tuo dominio/server se necessario)
    upload_url = f"https://alexmedia.it/public/arreda/uploads/{image_name}"

    payload = {
        "style": style,
        "roomType": room_type,
        "uploadUrl": upload_url,
        "mode": "WELL",
        "requestId": str(uuid.uuid4())
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": API_KEY
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
