import tkinter as tk
from tkinter import filedialog, simpledialog
import json


class DraggableElement:
    def __init__(
        self, canvas, x, y, width, height, id, element_type, **kwargs
    ):
        self.canvas = canvas
        self.element_type = element_type
        self.kwargs = kwargs  # This already stores all passed properties

        if element_type == "text":
            self.item = canvas.create_text(
                x,
                y,
                text=id,
                anchor="nw",
                font=("Arial", kwargs.get("size", 24)),
            )
            # Calculate text bounding box size (simplified for demonstration)
            bbox_width = kwargs.get("size", 24) * len(
                kwargs.get("text", "Sample Text")
            )
            bbox_height = kwargs.get("size", 24) * 1.5
            self.bbox = canvas.create_rectangle(
                x, y, x + bbox_width, y + bbox_height, outline="gray"
            )
        elif element_type == "image":
            self.item = canvas.create_rectangle(
                x, y, x + width, y + height, fill="blue"
            )  # Placeholder for image
            self.bbox = None
        elif element_type == "polygon":
            self.item = canvas.create_polygon(
                x,
                y,
                x + width,
                y,
                x + width,
                y + height,
                x,
                y + height,
                fill="red",
            )
            self.bbox = None

        self.bind_drag()

    def bind_drag(self):
        self.canvas.tag_bind(self.item, "<ButtonPress-1>", self.on_drag_start)
        self.canvas.tag_bind(self.item, "<B1-Motion>", self.on_drag_motion)

    def on_drag_start(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def on_drag_motion(self, event):
        dx = event.x - self.drag_start_x
        dy = event.y - self.drag_start_y
        self.canvas.move(self.item, dx, dy)
        if self.bbox:  # Move the bounding box if it exists
            self.canvas.move(self.bbox, dx, dy)
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def get_position(self):
        coords = self.canvas.coords(self.item)
        if self.element_type in ["text", "polygon"]:
            return coords[0], coords[1]  # x, y
        elif self.element_type == "image":
            return coords[0], coords[1]  # Top-left corner


class CardEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Card Editor")

        self.canvas = tk.Canvas(master, width=1200, height=630)
        self.canvas.pack()

        # 绘制白色背景矩形
        self.canvas.create_rectangle(
            0, 0, 1200, 630, fill="white", outline="white"
        )

        self.load_btn = tk.Button(
            master, text="Load JSON", command=self.load_json
        )
        self.load_btn.pack()

        self.export_btn = tk.Button(
            master, text="Export JSON", command=self.export_json
        )
        self.export_btn.pack()

        self.elements = []
        # Existing initialization code
        self.original_width = 1200  # Default values
        self.original_height = 630

    def load_json(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON Files", "*.json")]
        )
        if file_path:
            with open(file_path, "r") as f:
                data = json.load(f)
                self.canvas.config(
                    width=data["card"]["width"], height=data["card"]["height"]
                )
                for element in data["elements"]:
                    if element["type"] in ["text", "image", "polygon"]:
                        self.add_element(element)
        self.original_width = data["card"]["width"]
        self.original_height = data["card"]["height"]

    def add_element(self, element):
        element_copy = (
            element.copy()
        )  # Make a copy to preserve the original dictionary
        x, y = element_copy.get("position", [0, 0])
        width = element_copy.pop("width", 100)
        height = element_copy.pop("height", 50)
        id = element_copy.pop("id", "EXAMPLEID")
        draggable_element = DraggableElement(
            self.canvas,
            x,
            y,
            width,
            height,
            id,
            element_copy["type"],
            **element_copy
        )
        self.elements.append(draggable_element)

    def export_json(self):
        data = {
            "card": {
                "width": self.original_width,
                "height": self.original_height,
                "bg_color": [255, 255, 255],  # Assuming a white background
            },
            "elements": [],
        }
        for element in self.elements:
            el_data = {
                "type": element.element_type,
                "id": element.kwargs.get("id", ""),
                "position": element.get_position(),
            }
            # Rest of the code to update el_data based on element type...
            data["elements"].append(el_data)

        for element in self.elements:
            el_data = {
                "type": element.element_type,
                "id": element.kwargs.get("id", ""),
                "position": element.get_position(),
            }

            if element.element_type == "text":
                el_data.update(
                    {
                        "font": element.kwargs.get("font"),
                        "text": element.kwargs.get("text", "Sample Text"),
                    }
                )
            elif element.element_type == "image":
                el_data.update(
                    {
                        "path": element.kwargs.get("path", ""),
                        "width": element.kwargs.get("width", 100),
                        "height": element.kwargs.get("height", 50),
                    }
                )
            elif element.element_type == "polygon":
                el_data.update({"points": element.kwargs.get("points", [])})

            data["elements"].append(el_data)

        file_path = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON Files", "*.json")]
        )
        if file_path:
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)


if __name__ == "__main__":
    root = tk.Tk()
    app = CardEditor(root)
    root.mainloop()
