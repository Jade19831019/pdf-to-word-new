#!/usr/bin/env python3
"""
PDF to Word Web Tool - Backend MVP
"""

from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
import os
import tempfile

app = Flask(__name__)

# 配置
UPLOAD_FOLDER = tempfile.mkdtemp()
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return jsonify({'error': '没有上传文件'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        
        # TODO: 这里添加真实的 PDF 转 Word 逻辑
        # 现在是 MVP 版本，返回模拟成功
        
        output_filename = filename.rsplit('.', 1)[0] + '.docx'
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        
        # MVP: 创建一个空的 Word 文件作为演示
        with open(output_path, 'w') as f:
            f.write('PDF 转 Word 演示文档\n\n这是一个 MVP 版本，真实转换功能开发中...\n')
        
        return send_file(
            output_path,
            as_attachment=True,
            download_name=output_filename
        )
    
    return jsonify({'error': '文件类型不允许'}), 400

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'message': 'PDF to Word Converter is running!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
