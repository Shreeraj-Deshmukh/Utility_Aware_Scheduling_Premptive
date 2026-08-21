"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519997, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519997, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.395949, 'e_o_k': [0.232658, 0.186127], 'p_i': 10, 'u_i': 3.1458},
        {'id': 1, 'e_m': 4.896418, 'e_o_k': [0.497603, 0.398083, 0.318466, 0.254773], 'p_i': 20, 'u_i': 4.9683},
        {'id': 2, 'e_m': 4.165694, 'e_o_k': [0.694282, 0.555426], 'p_i': 40, 'u_i': 2.4718},
        {'id': 3, 'e_m': 12.396422, 'e_o_k': [1.008036, 0.806429, 0.645143, 0.516114, 0.412891, 0.330313], 'p_i': 80, 'u_i': 4.0774},
        {'id': 4, 'e_m': 4.498310, 'e_o_k': [0.365788, 0.292630, 0.234104, 0.187283, 0.149827, 0.119861], 'p_i': 80, 'u_i': 2.9703},
        {'id': 5, 'e_m': 0.593047, 'e_o_k': [0.052925, 0.042340, 0.033872, 0.027098, 0.021678], 'p_i': 40, 'u_i': 3.9269},
        {'id': 6, 'e_m': 3.818629, 'e_o_k': [0.636438, 0.509151], 'p_i': 10, 'u_i': 3.4836},
        {'id': 7, 'e_m': 4.142744, 'e_o_k': [0.369712, 0.295769, 0.236616, 0.189292, 0.151434], 'p_i': 40, 'u_i': 2.8974},
    ]
    B_BUDGET = 143.519997
    return processors, tasks, B_BUDGET
