"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 77.279995, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.1, "seed": 1030, "set": 30, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.10"}
"""

_SPEC = '{"B": 77.279995, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.1, "seed": 1030, "set": 30, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.049022, 'e_o_k': [0.010046, 0.008036, 0.006429], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 2.109402, 'e_o_k': [0.285883, 0.228706, 0.182965, 0.146372, 0.117098, 0.093678], 'p_i': 20, 'u_i': 1.5905},
        {'id': 2, 'e_m': 2.697147, 'e_o_k': [0.749207, 0.599366], 'p_i': 40, 'u_i': 4.0467},
        {'id': 3, 'e_m': 4.992978, 'e_o_k': [0.845694, 0.676555, 0.541244, 0.432995], 'p_i': 80, 'u_i': 4.3793},
        {'id': 4, 'e_m': 19.099547, 'e_o_k': [3.235018, 2.588015, 2.070412, 1.656329], 'p_i': 80, 'u_i': 2.7000},
        {'id': 5, 'e_m': 0.082986, 'e_o_k': [0.014056, 0.011245, 0.008996, 0.007197], 'p_i': 10, 'u_i': 2.7208},
        {'id': 6, 'e_m': 1.458740, 'e_o_k': [0.247077, 0.197661, 0.158129, 0.126503], 'p_i': 80, 'u_i': 2.5904},
        {'id': 7, 'e_m': 5.890191, 'e_o_k': [1.207006, 0.965605, 0.772484], 'p_i': 20, 'u_i': 1.1735},
    ]
    B_BUDGET = 77.279995
    return processors, tasks, B_BUDGET
