"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200008, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200008, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.572605, 'e_o_k': [0.117337, 0.093870, 0.075096], 'p_i': 10, 'u_i': 1.6225},
        {'id': 1, 'e_m': 0.565553, 'e_o_k': [0.115892, 0.092714, 0.074171], 'p_i': 20, 'u_i': 4.7220},
        {'id': 2, 'e_m': 0.817880, 'e_o_k': [0.167598, 0.134079, 0.107263], 'p_i': 40, 'u_i': 1.8233},
        {'id': 3, 'e_m': 5.124820, 'e_o_k': [1.050168, 0.840134, 0.672107], 'p_i': 80, 'u_i': 1.9473},
        {'id': 4, 'e_m': 2.116956, 'e_o_k': [0.433802, 0.347042, 0.277634], 'p_i': 20, 'u_i': 3.9894},
        {'id': 5, 'e_m': 0.218732, 'e_o_k': [0.044822, 0.035858, 0.028686], 'p_i': 10, 'u_i': 1.1602},
        {'id': 6, 'e_m': 1.046970, 'e_o_k': [0.214543, 0.171634, 0.137308], 'p_i': 20, 'u_i': 4.5224},
        {'id': 7, 'e_m': 3.990809, 'e_o_k': [0.817789, 0.654231, 0.523385], 'p_i': 80, 'u_i': 3.6370},
    ]
    B_BUDGET = 55.200008
    return processors, tasks, B_BUDGET
