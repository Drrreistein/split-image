#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
长图均匀切分工具
功能：将一张长图按照指定个数均匀切分成多张图片
"""

import os
import sys
from pathlib import Path
from PIL import Image


def split_image(image_path: str, num_parts: int, output_dir: str = None) -> str:
    """
    将长图均匀切分成指定数量的图片
    
    Args:
        image_path: 输入图片路径
        num_parts: 切分数量
        output_dir: 输出目录路径，默认为图片所在目录下的切分文件夹
    
    Returns:
        输出目录路径
    """
    # 验证输入
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"图片文件不存在: {image_path}")
    
    if num_parts < 1:
        raise ValueError("切分数量必须大于0")
    
    # 打开图片
    img = Image.open(image_path)
    width, height = img.size
    
    print(f"图片尺寸: {width} x {height}")
    print(f"切分数量: {num_parts}")
    
    # 计算每段高度
    part_height = height // num_parts
    remainder = height % num_parts
    
    # 准备输出目录
    if output_dir is None:
        image_name = Path(image_path).stem
        parent_dir = Path(image_path).parent
        output_dir = parent_dir / f"{image_name}_切分"
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
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
        output_path = output_dir / f"part_{i+1:02d}.png"
        cropped.save(output_path)
        
        print(f"已保存: {output_path} (高度: {box_height}px)")
        y_offset += box_height
    
    print(f"\n切分完成！共生成 {num_parts} 张图片")
    print(f"输出目录: {output_dir}")
    
    return str(output_dir)


def main():
    """命令行入口"""
    if len(sys.argv) < 3:
        print("用法: python split_image.py <图片路径> <切分数量> [输出目录]")
        print("示例: python split_image.py long_image.png 5")
        print("      python split_image.py long_image.png 5 ./output")
        sys.exit(1)
    
    image_path = sys.argv[1]
    num_parts = int(sys.argv[2])
    output_dir = sys.argv[3] if len(sys.argv) > 3 else None
    
    try:
        split_image(image_path, num_parts, output_dir)
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
