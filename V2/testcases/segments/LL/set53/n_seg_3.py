"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.159031, 'e_o_k': [0.032588, 0.026071, 0.020856], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 1.218826, 'e_o_k': [0.249759, 0.199807, 0.159846], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 0.995792, 'e_o_k': [0.204056, 0.163245, 0.130596], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 5.369863, 'e_o_k': [1.100382, 0.880305, 0.704244], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 0.918489, 'e_o_k': [0.188215, 0.150572, 0.120458], 'p_i': 40, 'u_i': 4.0720},
        {'id': 5, 'e_m': 0.851463, 'e_o_k': [0.174480, 0.139584, 0.111667], 'p_i': 10, 'u_i': 3.0767},
        {'id': 6, 'e_m': 1.430219, 'e_o_k': [0.293078, 0.234462, 0.187570], 'p_i': 20, 'u_i': 2.4479},
        {'id': 7, 'e_m': 4.121451, 'e_o_k': [0.844560, 0.675648, 0.540518], 'p_i': 80, 'u_i': 3.0328},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
