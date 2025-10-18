#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
橙猫猫导航页面生成器
扫描同目录下的txt文件，生成导航页面
"""

import os
import re
import shutil
from pathlib import Path

def scan_txt_files():
    """扫描同目录下的txt文件"""
    current_dir = Path('.')
    txt_files = list(current_dir.glob('*.txt'))
    
    entries = []
    for txt_file in txt_files:
        try:
            with open(txt_file, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            
            if content:
                # 解析文件内容：文件名=入口名，第一行=链接，第二行=简介
                lines = content.split('\n')
                name = txt_file.stem  # 文件名作为项目名
                url = lines[0].strip() if lines else "#"  # 第一行是链接
                description = lines[1].strip() if len(lines) > 1 else "暂无描述"  # 第二行是简介
                
                # 查找对应的图片文件
                image_file = find_image_file(txt_file.stem)
                
                entries.append({
                    'name': name,
                    'description': description,
                    'url': url,
                    'image': image_file,
                    'is_blog': '博客' in name or 'blog' in name.lower()
                })
                
        except Exception as e:
            print(f"⚠️ 读取文件 {txt_file} 时出错: {e}")
    
    # 排序：橙猫猫博客预览页排在第一个
    def sort_key(entry):
        if '橙猫猫博客' in entry['name']:
            return 0  # 橙猫猫博客排在最前面
        return 1  # 其他项目按原顺序
    
    entries.sort(key=sort_key)
    return entries

def find_image_file(base_name):
    """查找对应的图片文件"""
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
    
    for ext in image_extensions:
        # 尝试直接匹配
        image_file = f"{base_name}{ext}"
        if os.path.exists(image_file):
            return image_file
        
        # 尝试带 copy 后缀的
        image_file_copy = f"{base_name} copy{ext}"
        if os.path.exists(image_file_copy):
            return image_file_copy
    
    return None

def generate_html_content(entries):
    """生成HTML内容"""
    if not entries:
        return '<div class="no-projects">暂无项目</div>'
    
    html_parts = []
    
    for entry in entries:
        # 确定样式类
        info_class = "blog-style" if entry['is_blog'] else ""
        
        # 确定背景图片
        if entry['image']:
            bg_style = f"background-image: url('{entry['image']}')"
        else:
            bg_style = ""
        
        # 生成HTML
        html = f'''        <div class="project-card" onclick="openProject('{entry['url']}')">
            <div class="project-bg" style="{bg_style}">
            </div>
            <div class="project-info {info_class}">
                <div class="project-name">{entry['name']}</div>
                <div class="project-description">{entry['description']}</div>
            </div>
        </div>
        '''
        html_parts.append(html)
    
    return '\n'.join(html_parts)

def update_navigation():
    """更新导航页面"""
    print("🔍 开始扫描入口文件...")
    
    # 扫描txt文件
    entries = scan_txt_files()
    
    if not entries:
        print("❌ 未找到任何txt文件")
        return
    
    print(f"找到 {len(entries)} 个入口文件:")
    for entry in entries:
        print(f"  - {entry['name']}: {entry['description']}")
    
    # 生成HTML内容
    new_content = generate_html_content(entries)
    
    # 读取模板文件
    template_file = '12345.html'
    if not os.path.exists(template_file):
        print(f"❌ 模板文件 {template_file} 不存在")
        return
    
    with open(template_file, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # 替换项目容器中的内容
    pattern = r'<div id="projects-container" class="projects-grid">\s*<!-- 项目内容将由Python脚本生成 -->\s*</div>'
    replacement = f'<div id="projects-container" class="projects-grid">\n{new_content}\n        </div>'
    
    updated_content = re.sub(pattern, replacement, template_content, flags=re.DOTALL)
    
    # 写入到index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print("✅ 成功更新 index.html")
    print(f"📊 生成了 {len(entries)} 个项目卡片")
    print("\n🎉 导航页面生成完成！")
    print("💡 提示：现在可以直接打开 index.html 查看结果")

if __name__ == "__main__":
    update_navigation()