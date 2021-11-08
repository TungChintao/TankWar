from sprites.tank import Tank


class EnemyTank(Tank):
    def __init__(self, position, config):
        super().__init__(config)
