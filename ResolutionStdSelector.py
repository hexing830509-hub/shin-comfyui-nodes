class ResolutionStdSelector:
    def __init__(self):
        pass

    @staticmethod
    def INPUT_TYPES():
        return {
            "required": {
                "分辨率规格": (
                    [
                        "720×1280 竖屏",
                        "1280×720 横屏",
                        "1080×1920 竖屏",
                        "1920×1080 横屏",
                        "1200×900 横屏",
                        "900×1200 竖屏",
                    ],
                ),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("宽度", "高度")
    FUNCTION = "run"
    CATEGORY = "自定义/工具"

    def run(self, 分辨率规格):
        res_map = {
            "720×1280 竖屏": (720, 1280),
            "1280×720 横屏": (1280, 720),
            "1080×1920 竖屏": (1080, 1920),
            "1920×1080 横屏": (1920, 1080),
            "1200×900 横屏": (1200, 900),
            "900×1200 竖屏": (900, 1200),
        }
        return res_map.get(分辨率规格, (1024, 1024))

NODE_CLASS_MAPPINGS = {
    "ResolutionStdSelector": ResolutionStdSelector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionStdSelector": "常用规格分辨率选择器"
}
