import json
from PIL import Image, ImageDraw, ImageFont

def create_open_graph_card(text_content, config_path, output_path):
    with open(config_path, "r") as f:
        config = json.load(f)

    card_width = config["card"]["width"]
    card_height = config["card"]["height"]
    bg_color = tuple(config["card"]["bg_color"])
    python_color = "#66CCFF"  # 定义python颜色
    card_image = Image.new("RGB", (card_width, card_height), bg_color)
    draw = ImageDraw.Draw(card_image)

    for element in config["elements"]:
        if element["type"] == "text_box":
            text_content_key = element["content_key"]
            font = ImageFont.truetype(
                element["font"]["name"], element["font"]["size"]
            )
            text = text_content[text_content_key]
            text_pos = element["position"]
            draw.text(text_pos, text, fill=tuple(element["font"]["color"]), font=font)
        elif element["type"] == "image":
            img = Image.open(element["path"])
            img = img.resize((element["width"], element["height"]))
            img_pos = element["position"]
            card_image.paste(img, img_pos)
        elif element["type"] == "polygon":
            points = element["points"]
            fill_color = python_color if element["fill"] == "python" else element["fill"]
            draw.polygon(points, fill=fill_color)

    card_image.save(output_path)

# 使用示例
text_content = {
    "title": "肉骨茶——新加坡特色美食",
    "desc": "在台灣也可能被寫作肉骨茶",
    "extra_info": "享受美味的同时，不要忘记文化的意义。"
}
create_open_graph_card(
    text_content=text_content,
    config_path="config.json",
    output_path="preview_card.png",
)