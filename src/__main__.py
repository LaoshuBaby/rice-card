from PIL import Image, ImageDraw, ImageFont

def create_open_graph_card(title, description, image_path, output_path):
    # 设置背景颜色和尺寸，符合Open Graph标准
    card_width = 1200
    card_height = 630
    bg_color = (255, 255, 255)
    
    # 创建新图像并设置纯白色背景（原背景图片加载已注释）
    card_image = Image.new('RGB', (card_width, card_height), bg_color)
    
    # 加载字体并设置字号
    title_font = ImageFont.truetype('arial.ttf', 48)
    desc_font = ImageFont.truetype('arial.ttf', 24)

    draw = ImageDraw.Draw(card_image)

    # 使用textbbox获取文本尺寸
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_text_width, title_text_height = title_bbox[2], title_bbox[3]

    desc_bbox = draw.textbbox((0, 0), description, font=desc_font)
    desc_text_width, desc_text_height = desc_bbox[2], desc_bbox[3]

    # 计算文字位置以居中显示
    title_pos = ((card_width - title_text_width) // 2, 50)
    desc_pos = ((card_width - desc_text_width) // 2, 100 + title_text_height)

    # 绘制标题和描述（此部分保持不变）
    draw.text(title_pos, title, fill=(0, 0, 0), font=title_font)
    draw.text(desc_pos, description, fill=(0, 0, 0), font=desc_font)

    # 注释掉加载并粘贴背景图片的代码（若需保持纯白背景）
    # background_image = Image.open(image_path)
    # card_image.paste(background_image, (0, 0), background_image)

    # 保存生成的卡片到指定路径
    card_image.save(output_path)

# 使用函数创建卡片
title = "Rice Card Preview"
description = "A Python-based Open Graph preview card generator"
image_path = "background.jpg"  # 背景图片路径（若使用纯白背景则可忽略此变量）
output_path = "preview_card.png"

create_open_graph_card(title, description, image_path, output_path)