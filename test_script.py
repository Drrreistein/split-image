#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本 - 创建示例长图并测试切分功能
"""

from PIL import Image
import os
import sys

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from split_image import split_image


def create_test_image(width=800, height=2400, output_path="test_long_image.png"):
    """
    创建测试用的长图
    
    Args:
        width: 图片宽度
        height: 图片高度
        output_path: 输出路径
    """
    # 创建渐变色长图
    img = Image.new('RGB', (width, height), color='white')
    pixels = img.load()
    
    # 创建渐变效果
    for y in range(height):
        # 从蓝色渐变到红色
        r = int(255 * y / height)
        g = 100
        b = int(255 * (1 - y / height))
        for x in range(width):
            pixels[x, y] = (r, g, b)
    
    # 添加分段标记
    from PIL import ImageDraw, ImageFont
    draw = ImageDraw.Draw(img)
    
    # 每800像素标记一段
    num_sections = height // 800
    for i in range(num_sections):
        y_pos = i * 800 + 400
        text = f"Section {i+1}"
        # 使用默认字体
        draw.text((width//2 - 50, y_pos), text, fill='white')
    
    img.save(output_path)
    print(f"✓ 测试图片已创建: {output_path}")
    print(f"  尺寸: {width} x {height}")
    print(f"  分段数: {num_sections}")
    
    return output_path


def test_split():
    """测试切分功能"""
    print("=" * 50)
    print("长图切分工具测试")
    print("=" * 50)
    
    # 1. 创建测试图片
    print("\n步骤1: 创建测试长图...")
    test_image = create_test_image(800, 2400, "test_long_image.png")
    
    # 2. 测试切分
    print("\n步骤2: 测试切分功能（切分成3份）...")
    try:
        output_dir = split_image(test_image, 3)
        print(f"\n✓ 切分成功!")
        print(f"  输出目录: {output_dir}")
        
        # 3. 验证输出
        print("\n步骤3: 验证输出文件...")
        if os.path.exists(output_dir):
            files = sorted(os.listdir(output_dir))
            print(f"  生成文件数: {len(files)}")
            for f in files:
                file_path = os.path.join(output_dir, f)
                with Image.open(file_path) as img:
                    print(f"  - {f}: {img.size[0]}x{img.size[1]}")
        
        print("\n" + "=" * 50)
        print("✓ 测试完成!")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_split()
