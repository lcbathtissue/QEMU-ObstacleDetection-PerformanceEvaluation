from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file:
        file_path = os.path.join('uploads', uploaded_file.filename)
        uploaded_file.save(file_path)
        return jsonify({'message': 'File uploaded successfully'})
    else:
        return jsonify({'error': 'No file provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
