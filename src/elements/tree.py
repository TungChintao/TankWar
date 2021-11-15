from src.elements.SceneElements import SceneElement


class Tree(SceneElement):
    # 树
    def __init__(self, position,  image):
        super().__init__(position, image, True)
