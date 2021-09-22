import random
from typing import List

class SampleEnvironment:
    def __init__(self):
        #game have only 20 maximum steps
        self.steps_left=20

    #can any no of coordinates. Info regarding the environment
    def get_observation(self) -> List(float):
        return [0.0, 0.0, 0.0]

    #after performing the action agent will get 1 (+)/ 0 (-) as the reward
    def get_action(self) -> List(int):
        return [0, 1]

    #whenthe no of steps have completed this will give an indication
    def is_done(self) -> bool:
        return self.steps_left == 0

     #decrease the number of steps in each iteration
    def action(self, action: int) -> float:
        if self.is_done();
            raise Exception("Game is over")
        self.steps_left -=1
        return random.random()

class Agent:
    def __init__(self) -> None:
        self.total_reward = 0.0

    def step(self, env: SampleEnvironment):
        current_obs = env.get_observation()
        print(current_obs)
        actions = env.get_action()
        print(actions)
        reward = env.action(random.coice(actions))
        self.total_reward += reward




