import json
from PIL import Image, ImageDraw, ImageFont


def create_open_graph_card(title, description, image_path, output_path):
    # 从 repo.json 文件加载配置信息
    with open("repo.json", "r") as f:
        config = json.load(f)

    # 设置背景颜色和尺寸，符合Open Graph标准
    card_width = 1200
    card_height = 630
    bg_color = (255, 255, 255)

    # 创建新图像并设置纯白色背景（原背景图片加载已注释）
    card_image = Image.new("RGB", (card_width, card_height), bg_color)
    # 注释掉加载并粘贴背景图片的代码（若需保持纯白背景）
    # background_image = Image.open(image_path) # 背景图片路径（若使用纯白背景则可忽略此变量）
    # card_image.paste(background_image, (0, 0), background_image)

    title_CJK_varient = config["title_CJK_varient"]
    desc_CJK_varient = config["desc_CJK_varient"]

    # 加载简繁中文标题和描述的字体
    title_font_sc = ImageFont.truetype(
        config["title_font_sc_fontname"], config["title_font_size"]
    )
    desc_font_tc = ImageFont.truetype(
        config["desc_font_tc_fontname"], config["desc_font_size"]
    )

    draw = ImageDraw.Draw(card_image)

    # 使用textbbox获取文本尺寸
    title_bbox = draw.textbbox((0, 0), title, font=title_font_sc)
    title_text_width, title_text_height = title_bbox[2], title_bbox[3]

    desc_bbox = draw.textbbox((0, 0), description, font=desc_font_tc)
    desc_text_width, desc_text_height = desc_bbox[2], desc_bbox[3]

    # 从配置文件中获取文字居中位置坐标
    title_pos = (
        (card_width - title_text_width) // 2,
        config["title_top_margin"],
    )
    desc_pos = (
        (card_width - desc_text_width) // 2,
        config["desc_top_margin"] + title_text_height,
    )

    # 使用简繁中文标题和描述进行绘制
    draw.text(title_pos, title, fill=(0, 0, 0), font=title_font_sc)
    draw.text(desc_pos, description, fill=(0, 0, 0), font=desc_font_tc)

    # 保存生成的卡片到指定路径
    card_image.save(output_path)


# create_open_graph_card(
#     title="Rice Card Preview",
#     description="A Python-based Open Graph preview card generator",
#     image_path="",
#     output_path="preview_card_EN.png",
# )
create_open_graph_card(
    title="肉骨茶——新加坡特色美食",
    description="在台灣也可能被寫作肉骨茶",
    image_path="background_bak-kut-teh.jpg",
    output_path="preview_card_ZH.png",
)
