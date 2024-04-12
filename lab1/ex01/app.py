from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

# Router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form.get('inputPlainText', '')  # Lấy giá trị của trường 'inputPlainText' từ form
    key = request.form.get('inputKey')  # Lấy giá trị của trường 'inputKey' từ form
    if key is None:
        return "Key is missing"  # Trả về thông báo nếu key không được gửi
    key = int(key)  # Chuyển đổi key thành số nguyên
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form.get('inputCipherText', '')  # Lấy giá trị của trường 'inputCipherText' từ form
    key = request.form.get('inputKeyCipher')  # Lấy giá trị của trường 'inputKeyCipher' từ form
    if key is None:
        return "Key is missing"  # Trả về thông báo nếu key không được gửi
    key = int(key)  # Chuyển đổi key thành số nguyên
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
    
