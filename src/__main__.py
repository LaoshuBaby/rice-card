import json
from PIL import Image, ImageDraw, ImageFont

def create_open_graph_card(text_content, image_path, output_path):
    # 从 repo.json 文件加载配置信息
    with open("repo.json", "r") as f:
        config = json.load(f)

    card_width = 1200
    card_height = 630
    bg_color = (255, 255, 255)
    card_image = Image.new("RGB", (card_width, card_height), bg_color)

    draw = ImageDraw.Draw(card_image)
    current_top_margin = 0

    for text_box_key in text_content.keys():
        text_box_config = config["text_boxes"][text_box_key]

        # 加载字体
        font = ImageFont.truetype(
            text_box_config["font_name"], text_box_config["font_size"]
        )

        # 计算文本框位置
        text_bbox = draw.textbbox((0, 0), text_content[text_box_key], font=font)
        text_width, text_height = text_bbox[2], text_bbox[3]
        text_pos = (
            (card_width - text_width) // 2,
            current_top_margin + text_box_config["top_margin"],
        )
        current_top_margin += text_height + text_box_config["top_margin"]

        # 绘制文本
        draw.text(text_pos, text_content[text_box_key], fill=(0, 0, 0), font=font)

    # 保存生成的卡片到指定路径
    card_image.save(output_path)

# 使用示例
text_content = {
    "title": "肉骨茶——新加坡特色美食",
    "desc": "在台灣也可能被寫作肉骨茶"
}
create_open_graph_card(
    text_content=text_content,
    image_path="background_bak-kut-teh.jpg",
    output_path="preview_card_ZH.png",
)