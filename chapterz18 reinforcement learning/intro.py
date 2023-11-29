import gym
env = gym.make("CartPole-v1", render_mode="rgb_array")

# returns the initial observation of the environment
# horizontal position, velocity, angle of the pole, angular velocity
# the array is the observation, the dict is the info
# (array([ 0.02049138, -0.00942224, -0.03660891, -0.01586133], dtype=float32), {})

env.reset()

obs, info = env.reset(seed=42)

img = env.render()


