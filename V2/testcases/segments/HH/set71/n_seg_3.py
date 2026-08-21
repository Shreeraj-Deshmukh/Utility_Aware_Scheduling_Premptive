"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.149966, 'e_o_k': [1.233587, 0.986870, 0.789496], 'p_i': 10, 'u_i': 1.0606},
        {'id': 1, 'e_m': 0.415795, 'e_o_k': [0.238571, 0.190857, 0.152685], 'p_i': 20, 'u_i': 3.4010},
        {'id': 2, 'e_m': 1.011654, 'e_o_k': [0.580457, 0.464366, 0.371493], 'p_i': 40, 'u_i': 1.6455},
        {'id': 3, 'e_m': 23.962531, 'e_o_k': [13.748993, 10.999195, 8.799356], 'p_i': 80, 'u_i': 1.3745},
        {'id': 4, 'e_m': 1.255643, 'e_o_k': [0.720451, 0.576361, 0.461088], 'p_i': 40, 'u_i': 1.5038},
        {'id': 5, 'e_m': 6.392981, 'e_o_k': [3.668104, 2.934483, 2.347586], 'p_i': 40, 'u_i': 4.4242},
        {'id': 6, 'e_m': 1.712311, 'e_o_k': [0.982474, 0.785979, 0.628783], 'p_i': 40, 'u_i': 1.3856},
        {'id': 7, 'e_m': 0.107345, 'e_o_k': [0.061592, 0.049273, 0.039419], 'p_i': 20, 'u_i': 2.4453},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
