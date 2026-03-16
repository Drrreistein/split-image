#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
长图切分 Web 应用
Flask 后端服务
"""

import os
import io
import zipfile
from datetime import datetime
from pathlib import Path
from flask import Flask, request, render_template, send_file, jsonify, url_for
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)

# 配置
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 最大50MB
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'webp', 'bmp'}

# 确保目录存在
Path(app.config['UPLOAD_FOLDER']).mkdir(exist_ok=True)
Path(app.config['OUTPUT_FOLDER']).mkdir(exist_ok=True)


def allowed_file(filename):
    """检查文件类型是否允许"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def split_image_to_folder(image_path, num_parts, output_dir):
    """
    将长图均匀切分成指定数量的图片
    
    Args:
        image_path: 输入图片路径
        num_parts: 切分数量
        output_dir: 输出目录路径
    
    Returns:
        生成的图片文件列表
    """
    # 打开图片
    img = Image.open(image_path)
    width, height = img.size
    
    # 计算每段高度
    part_height = height // num_parts
    
    # 创建输出目录
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    generated_files = []
    
    # 切分图片
    y_offset = 0
    for i in range(num_parts):
        # 最后一张包含剩余像素
        if i == num_parts - 1:
            box_height = height - y_offset
        else:
            box_height = part_height
        
        # 计算切分区域
        box = (0, y_offset, width, y_offset + box_height)
        cropped = img.crop(box)
        
        # 生成输出文件名
        output_file = output_path / f"part_{i+1:02d}.png"
        cropped.save(output_file)
        
        generated_files.append({
            'filename': f"part_{i+1:02d}.png",
            'path': str(output_file),
            'width': width,
            'height': box_height
        })
        
        y_offset += box_height
    
    return generated_files


@app.route('/')
def index():
    """主页"""
    return render_template('index.html')


@app.route('/api/split', methods=['POST'])
def split_image():
    """处理图片切分请求"""
    # 检查文件是否存在
    if 'file' not in request.files:
        return jsonify({'error': '没有上传文件'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': '没有选择文件'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': '不支持的文件类型，请上传 PNG、JPG、JPEG、WEBP 或 BMP 格式的图片'}), 400
    
    # 获取切分数量
    try:
        num_parts = int(request.form.get('num_parts', 2))
        if num_parts < 1 or num_parts > 100:
            return jsonify({'error': '切分数量必须在 1-100 之间'}), 400
    except ValueError:
        return jsonify({'error': '切分数量必须是数字'}), 400
    
    try:
        # 生成唯一文件名
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = secure_filename(file.filename)
        base_name = Path(filename).stem
        
        # 保存上传的文件
        upload_dir = Path(app.config['UPLOAD_FOLDER']) / f"{timestamp}_{base_name}"
        upload_dir.mkdir(parents=True, exist_ok=True)
        upload_path = upload_dir / filename
        file.save(upload_path)
        
        # 获取图片信息
        with Image.open(upload_path) as img:
            width, height = img.size
            file_size = os.path.getsize(upload_path)
        
        # 创建输出目录
        output_dir = Path(app.config['OUTPUT_FOLDER']) / f"{timestamp}_{base_name}"
        
        # 执行切分
        generated_files = split_image_to_folder(upload_path, num_parts, output_dir)
        
        # 返回结果
        return jsonify({
            'success': True,
            'original': {
                'filename': filename,
                'width': width,
                'height': height,
                'size': file_size
            },
            'split': {
                'num_parts': num_parts,
                'part_height': height // num_parts
            },
            'files': generated_files,
            'download_url': url_for('download_result', folder=f"{timestamp}_{base_name}")
        })
        
    except Exception as e:
        return jsonify({'error': f'处理失败: {str(e)}'}), 500


@app.route('/api/download/<folder>')
def download_result(folder):
    """下载切分结果（ZIP压缩包）"""
    output_dir = Path(app.config['OUTPUT_FOLDER']) / folder
    
    if not output_dir.exists():
        return jsonify({'error': '文件不存在'}), 404
    
    # 创建ZIP文件
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for file_path in sorted(output_dir.glob('*.png')):
            zip_file.write(file_path, file_path.name)
    
    zip_buffer.seek(0)
    
    return send_file(
        zip_buffer,
        mimetype='application/zip',
        as_attachment=True,
        download_name=f'{folder}_切分结果.zip'
    )


@app.route('/api/download/<folder>/<filename>')
def download_single_file(folder, filename):
    """下载单个切分后的图片"""
    file_path = Path(app.config['OUTPUT_FOLDER']) / folder / filename
    
    if not file_path.exists():
        return jsonify({'error': '文件不存在'}), 404
    
    return send_file(file_path, mimetype='image/png', as_attachment=True)


@app.route('/api/preview/<folder>/<filename>')
def preview_file(folder, filename):
    """预览切分后的图片"""
    file_path = Path(app.config['OUTPUT_FOLDER']) / folder / filename
    
    if not file_path.exists():
        return jsonify({'error': '文件不存在'}), 404
    
    return send_file(file_path, mimetype='image/png')


# 清理旧文件（可选，定期运行）
def cleanup_old_files():
    """清理超过24小时的文件"""
    import time
    current_time = time.time()
    
    for folder in [app.config['UPLOAD_FOLDER'], app.config['OUTPUT_FOLDER']]:
        for path in Path(folder).iterdir():
            if path.is_dir() and path.stat().st_mtime < current_time - 86400:
                import shutil
                shutil.rmtree(path)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
