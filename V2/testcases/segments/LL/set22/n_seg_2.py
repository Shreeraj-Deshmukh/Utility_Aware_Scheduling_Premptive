"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200008, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200008, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.003420, 'e_o_k': [0.278728, 0.222982], 'p_i': 10, 'u_i': 2.9329},
        {'id': 1, 'e_m': 0.071930, 'e_o_k': [0.019981, 0.015984], 'p_i': 20, 'u_i': 4.3550},
        {'id': 2, 'e_m': 2.182642, 'e_o_k': [0.606289, 0.485032], 'p_i': 40, 'u_i': 2.2741},
        {'id': 3, 'e_m': 0.960574, 'e_o_k': [0.266826, 0.213461], 'p_i': 80, 'u_i': 2.5808},
        {'id': 4, 'e_m': 1.684688, 'e_o_k': [0.467969, 0.374375], 'p_i': 40, 'u_i': 4.5356},
        {'id': 5, 'e_m': 0.701210, 'e_o_k': [0.194781, 0.155824], 'p_i': 20, 'u_i': 4.4130},
        {'id': 6, 'e_m': 3.408563, 'e_o_k': [0.946823, 0.757458], 'p_i': 80, 'u_i': 1.1305},
        {'id': 7, 'e_m': 1.097036, 'e_o_k': [0.304732, 0.243786], 'p_i': 10, 'u_i': 4.7707},
    ]
    B_BUDGET = 55.200008
    return processors, tasks, B_BUDGET
