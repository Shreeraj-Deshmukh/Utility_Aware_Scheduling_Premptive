"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400007, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.400007, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.647287, 'e_o_k': [0.137274, 0.137274, 0.137274, 0.137274, 0.137274, 0.137274], 'p_i': 10, 'u_i': 3.9772},
        {'id': 1, 'e_m': 0.034300, 'e_o_k': [0.004288, 0.004288, 0.004288, 0.004288], 'p_i': 20, 'u_i': 1.4627},
        {'id': 2, 'e_m': 2.925892, 'e_o_k': [0.731473, 0.731473], 'p_i': 40, 'u_i': 4.5040},
        {'id': 3, 'e_m': 1.655242, 'e_o_k': [0.275874, 0.275874, 0.275874], 'p_i': 80, 'u_i': 4.7123},
        {'id': 4, 'e_m': 0.978124, 'e_o_k': [0.097812, 0.097812, 0.097812, 0.097812, 0.097812], 'p_i': 20, 'u_i': 4.3702},
        {'id': 5, 'e_m': 1.868312, 'e_o_k': [0.233539, 0.233539, 0.233539, 0.233539], 'p_i': 40, 'u_i': 3.7678},
        {'id': 6, 'e_m': 15.433016, 'e_o_k': [1.929127, 1.929127, 1.929127, 1.929127], 'p_i': 80, 'u_i': 3.2312},
        {'id': 7, 'e_m': 10.047671, 'e_o_k': [1.674612, 1.674612, 1.674612], 'p_i': 40, 'u_i': 3.7207},
    ]
    B_BUDGET = 110.400007
    return processors, tasks, B_BUDGET
