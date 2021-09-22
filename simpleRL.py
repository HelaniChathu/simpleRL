import random
from typing import List

class SampleEnvironment:
    def __init__(self):
        self.steps_left=20

    def get_observation(self) -> List(float):
        return [0.0, 0.0, 0.0]

        def get_action(self) -> List(int):
            return [0, 1]