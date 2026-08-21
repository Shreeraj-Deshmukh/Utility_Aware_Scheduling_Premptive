"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 58.879997, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.2, "seed": 1030, "set": 30, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.20"}
"""

_SPEC = '{"B": 58.879997, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.2, "seed": 1030, "set": 30, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.20"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.024511, 'e_o_k': [0.005023, 0.004018, 0.003215], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 1.054701, 'e_o_k': [0.142941, 0.114353, 0.091482, 0.073186, 0.058549, 0.046839], 'p_i': 20, 'u_i': 1.5905},
        {'id': 2, 'e_m': 1.348573, 'e_o_k': [0.374604, 0.299683], 'p_i': 40, 'u_i': 4.0467},
        {'id': 3, 'e_m': 2.496489, 'e_o_k': [0.422847, 0.338278, 0.270622, 0.216498], 'p_i': 80, 'u_i': 4.3793},
        {'id': 4, 'e_m': 9.549774, 'e_o_k': [1.617509, 1.294007, 1.035206, 0.828165], 'p_i': 80, 'u_i': 2.7000},
        {'id': 5, 'e_m': 0.041493, 'e_o_k': [0.007028, 0.005622, 0.004498, 0.003598], 'p_i': 10, 'u_i': 2.7208},
        {'id': 6, 'e_m': 0.729370, 'e_o_k': [0.123538, 0.098831, 0.079064, 0.063252], 'p_i': 80, 'u_i': 2.5904},
        {'id': 7, 'e_m': 2.945096, 'e_o_k': [0.603503, 0.482803, 0.386242], 'p_i': 20, 'u_i': 1.1735},
    ]
    B_BUDGET = 58.879997
    return processors, tasks, B_BUDGET
