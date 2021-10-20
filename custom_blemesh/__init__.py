from gym.envs.registration import register

register(
     id='customblemesh-v0',
     entry_point='custom_blemesh.envs:customblemeshEnv'
 )

