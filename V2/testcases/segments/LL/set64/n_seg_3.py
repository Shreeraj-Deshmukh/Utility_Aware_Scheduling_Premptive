"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199993, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199993, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.721674, 'e_o_k': [0.147884, 0.118307, 0.094646], 'p_i': 10, 'u_i': 4.7302},
        {'id': 1, 'e_m': 2.496139, 'e_o_k': [0.511504, 0.409203, 0.327362], 'p_i': 20, 'u_i': 1.8342},
        {'id': 2, 'e_m': 0.886501, 'e_o_k': [0.181660, 0.145328, 0.116262], 'p_i': 40, 'u_i': 2.1428},
        {'id': 3, 'e_m': 2.410461, 'e_o_k': [0.493947, 0.395158, 0.316126], 'p_i': 80, 'u_i': 3.7337},
        {'id': 4, 'e_m': 2.948362, 'e_o_k': [0.604173, 0.483338, 0.386670], 'p_i': 40, 'u_i': 3.4112},
        {'id': 5, 'e_m': 4.596887, 'e_o_k': [0.941985, 0.753588, 0.602870], 'p_i': 80, 'u_i': 2.7179},
        {'id': 6, 'e_m': 0.004759, 'e_o_k': [0.000975, 0.000780, 0.000624], 'p_i': 40, 'u_i': 2.6898},
        {'id': 7, 'e_m': 0.388865, 'e_o_k': [0.079685, 0.063748, 0.050999], 'p_i': 20, 'u_i': 4.5690},
    ]
    B_BUDGET = 55.199993
    return processors, tasks, B_BUDGET
