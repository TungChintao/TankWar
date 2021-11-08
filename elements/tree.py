from elements.SceneElements import SceneElement


class Tree(SceneElement):
    # 树
    def __init__(self, image, position):
        super().__init__(image, position, True)
