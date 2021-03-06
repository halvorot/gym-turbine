from gym.envs.registration import register
import numpy as np

DEFAULT_CONFIG = {
    "step_size": 0.01,
    "min_reward": -1500,
    "max_t_steps": 30000,
    "crash_angle_condition": 7*(np.pi/180),
    "max_init_angle": 5*(np.pi/180),
    "reward_crash": -2000,
    "wind_dir": 0,
    "gamma_p": 250,                              # Exponential coefficient for pitch angle reward
    "gamma_r": 250,                              # Exponential coefficient for roll angle reward
}


register(
    id='TurbineStab-v0',
    entry_point='gym_turbine.envs:TurbineEnv',
    kwargs={'env_config': DEFAULT_CONFIG}
)
