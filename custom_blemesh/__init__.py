from gym.envs.registration import register

register(
     id='customblemesh-v1',
     entry_point='custom_blemesh.envs:customblemeshEnv'
 )

