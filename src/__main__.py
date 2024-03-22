import json
from PIL import Image, ImageDraw, ImageFont

MAGIC_SYMBOL = {"REPO_URL": "get_repo_metadata"}


def get_repo_metadata(repo_owner=None, repo_name=None, repo_url=None):
    # 如果repo_owner和repo_name均不为空，则构建repo_url
    if repo_owner and repo_name:
        repo_url = "https://github.com/" + f"{repo_owner}/{repo_name}"
    else:
        repo_url = repo_url
    return repo_url


def get_colour(colour_name: str) -> str:
    palette = {"python": "#66CCFF", "html": "#114514"}
    return palette[colour_name]


def create_open_graph_card(text_content, config_path, output_path):
    with open(config_path, "r") as f:
        config = json.load(f)

    card_width = config["card"]["width"]
    card_height = config["card"]["height"]
    bg_color = tuple(config["card"]["bg_color"])
    card_image = Image.new("RGB", (card_width, card_height), bg_color)
    draw = ImageDraw.Draw(card_image)

    for element in config["elements"]:
        if element["type"] == "text_box":
            text_pos = element["position"]
            text_content_key = element["content_key"]
            font = ImageFont.truetype(
                element["font"]["name"], element["font"]["size"]
            )
            text = text_content[text_content_key]
            for magic_word in MAGIC_SYMBOL:
                magic_word_key = "{{" + magic_word + "}}"
                if magic_word_key in text:
                    text = text.replace(
                        magic_word_key,
                        get_repo_metadata(
                            repo_owner="laoshubaby", repo_name="rice-card"
                        ),
                    )
            draw.text(
                text_pos, text, fill=tuple(element["font"]["color"]), font=font
            )
        elif element["type"] == "image":
            img = Image.open(element["path"]).convert("RGBA")
            img = img.resize(
                (element["width"], element["height"]), Image.Resampling.LANCZOS
            )
            img_pos = element["position"]
            # 假设background是您要将图片合并到的背景Image对象
            # 确保背景图片也是RGBA模式，以支持透明度
            card_image.paste(img, img_pos, img)
        elif element["type"] == "polygon":
            points = element["points"]
            fill_color = (
                get_colour("python")
                if element["fill"] == "python"
                else element["fill"]
            )
            draw.polygon(points, fill=fill_color)

    card_image.save(output_path)


# 使用示例
text_content = {
    "title": "肉骨茶——新加坡特色美食",
    "desc": "在台灣也可能被寫作肉骨茶\n享受美味的同时，不要忘记文化的意义。",
    "meta_link": "{{REPO_URL}}",
}
create_open_graph_card(
    text_content=text_content,
    config_path="../template/github_repo.json",
    output_path="preview_card.png",
)
