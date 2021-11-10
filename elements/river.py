from elements.SceneElements import SceneElement


class River(SceneElement):
    # 河流
    def __init__(self, position, image):
        super().__init__(position, image, True)