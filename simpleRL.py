#https://www.youtube.com/watch?v=g_8gw2POOYE

import random
from typing import List

class SampleEnvironment:
    def __init__(self):
        #game have only 20 maximum steps
        self.steps_left=20

    #can any no of coordinates. Info regarding the environment
    def get_observation(self) -> List[float]:
        return [0.0, 0.0, 0.0]

    #after performing the action agent will get 1 (+)/ 0 (-) as the reward
    def get_action(self) -> List[int]:
        return [0, 1]

    #whenthe no of steps have completed this will give an indication
    def is_done(self) -> bool:
        return self.steps_left == 0

     #decrease the number of steps in each iteration
    def action(self, action: int) -> float:
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -=1
        return random.random()

class Agent:
    def __init__(self) -> None:
        self.total_reward = 0.0

    #consider the sample environment
    def step(self, env: SampleEnvironment):
        #here obs is hardcoded
        current_obs = env.get_observation()
        print("Observation {}".format(current_obs))
        #getting random value form 1/0. no logic has iplemented
        actions = env.get_action()
        print(actions)
        reward = env.action(random.coice(actions)) #random action selection
        #add rewards together
        self.total_reward += reward
        print("Total Rewards: {}".format(self.total_reward))

if __name__ == "_main_":
    #calling the env
    env = SampleEnvironment()
    #calling the agent
    agent = Agent()
    i=0

    while not env.is_done():
        i+=1
        print("Steps {}".format(i))
        agent.step(env)

    print("Total reward got: %.4f" % agent.total_reward)

