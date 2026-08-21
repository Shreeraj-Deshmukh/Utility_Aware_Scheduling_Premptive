"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320031, "H": 80, "J": 43, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.320031, "H": 80, "J": 43, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.417118, 'e_o_k': [0.291983, 0.291983], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 1.031475, 'e_o_k': [0.481355, 0.481355, 0.481355], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 1.084639, 'e_o_k': [0.759247, 0.759247], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 6.513493, 'e_o_k': [2.279722, 2.279722, 2.279722, 2.279722], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.140753, 'e_o_k': [0.098527, 0.098527], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 0.605859, 'e_o_k': [0.212051, 0.212051, 0.212051, 0.212051], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 0.592474, 'e_o_k': [0.276488, 0.276488, 0.276488], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 0.713089, 'e_o_k': [0.332775, 0.332775, 0.332775], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 88.320031
    return processors, tasks, B_BUDGET
