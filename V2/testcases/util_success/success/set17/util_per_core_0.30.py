"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759997, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759997, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.595144, 'e_o_k': [0.048395, 0.038716, 0.030973, 0.024778, 0.019823, 0.015858], 'p_i': 10, 'u_i': 2.9192},
        {'id': 1, 'e_m': 0.787446, 'e_o_k': [0.080025, 0.064020, 0.051216, 0.040973], 'p_i': 20, 'u_i': 2.0454},
        {'id': 2, 'e_m': 5.653189, 'e_o_k': [0.459699, 0.367759, 0.294207, 0.235366, 0.188293, 0.150634], 'p_i': 40, 'u_i': 2.8602},
        {'id': 3, 'e_m': 12.841594, 'e_o_k': [2.140266, 1.712213], 'p_i': 80, 'u_i': 2.9521},
        {'id': 4, 'e_m': 0.640553, 'e_o_k': [0.106759, 0.085407], 'p_i': 10, 'u_i': 3.5497},
        {'id': 5, 'e_m': 2.484475, 'e_o_k': [0.252487, 0.201990, 0.161592, 0.129274], 'p_i': 40, 'u_i': 2.7971},
        {'id': 6, 'e_m': 1.379090, 'e_o_k': [0.112143, 0.089714, 0.071772, 0.057417, 0.045934, 0.036747], 'p_i': 80, 'u_i': 4.6429},
        {'id': 7, 'e_m': 4.468623, 'e_o_k': [0.744770, 0.595816], 'p_i': 80, 'u_i': 1.6248},
    ]
    B_BUDGET = 71.759997
    return processors, tasks, B_BUDGET
