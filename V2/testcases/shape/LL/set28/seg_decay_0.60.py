"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199993, "H": 80, "J": 43, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199993, "H": 80, "J": 43, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.417118, 'e_o_k': [0.130349, 0.078210], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 1.031475, 'e_o_k': [0.263131, 0.157879, 0.094727], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 1.084639, 'e_o_k': [0.338950, 0.203370], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 6.513493, 'e_o_k': [1.496667, 0.898000, 0.538800, 0.323280], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.140753, 'e_o_k': [0.043985, 0.026391], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 0.605859, 'e_o_k': [0.139214, 0.083528, 0.050117, 0.030070], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 0.592474, 'e_o_k': [0.151141, 0.090685, 0.054411], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 0.713089, 'e_o_k': [0.181910, 0.109146, 0.065488], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 55.199993
    return processors, tasks, B_BUDGET
