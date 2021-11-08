from elements.SceneElements import SceneElement


class River(SceneElement):
    # 河流
    def __init__(self, image, position):
        super().__init__(image, position, True)