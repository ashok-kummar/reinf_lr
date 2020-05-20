import random
from typing import List

class Enviornment:

    def __init__(self):
        self.steps_left = 10

    def get_observation(self) -> List[float]:
        return [0.0, 0.0, 0.0]

    def get_actions(self) -> List[int]:
        return[0, 1]

    def is_done(self) -> bool:
        return self.steps_left == 0

    def actions(self, action:int) -> float:
        if self.is_done():
            raise Exception("Game Over")
        self.steps_left -= 1
        return random.random()

class Agent:

    def __init__(self):
        self.total_reward = 0.0

    def step(self, env:Enviornment):
        current_obs = env.get_observation()
        actions = env.get_actions()
        reward = env.actions(random.choice(actions))
        self.total_reward += reward

if __name__ == "__main__":
    env = Enviornment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)
    print("total reward : %.2f" % agent.total_reward) 