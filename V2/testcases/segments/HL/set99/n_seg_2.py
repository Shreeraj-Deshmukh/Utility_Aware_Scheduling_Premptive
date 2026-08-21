"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.970629, 'e_o_k': [0.269619, 0.215695], 'p_i': 10, 'u_i': 1.8657},
        {'id': 1, 'e_m': 2.923011, 'e_o_k': [0.811947, 0.649558], 'p_i': 20, 'u_i': 1.6547},
        {'id': 2, 'e_m': 1.109904, 'e_o_k': [0.308307, 0.246645], 'p_i': 40, 'u_i': 3.2690},
        {'id': 3, 'e_m': 3.648613, 'e_o_k': [1.013503, 0.810803], 'p_i': 80, 'u_i': 2.0883},
        {'id': 4, 'e_m': 1.035116, 'e_o_k': [0.287532, 0.230026], 'p_i': 10, 'u_i': 2.4453},
        {'id': 5, 'e_m': 10.125219, 'e_o_k': [2.812561, 2.250049], 'p_i': 40, 'u_i': 4.4841},
        {'id': 6, 'e_m': 4.891882, 'e_o_k': [1.358856, 1.087085], 'p_i': 40, 'u_i': 2.2759},
        {'id': 7, 'e_m': 0.359380, 'e_o_k': [0.099828, 0.079862], 'p_i': 80, 'u_i': 4.2544},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
