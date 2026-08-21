"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.127543, 'e_o_k': [0.077446, 0.046468, 0.027881, 0.016728, 0.010037], 'p_i': 10, 'u_i': 1.4092},
        {'id': 1, 'e_m': 0.883465, 'e_o_k': [0.631046, 0.378628, 0.227177], 'p_i': 20, 'u_i': 2.7448},
        {'id': 2, 'e_m': 2.358898, 'e_o_k': [1.432363, 0.859418, 0.515651, 0.309391, 0.185634], 'p_i': 40, 'u_i': 3.9391},
        {'id': 3, 'e_m': 1.038301, 'e_o_k': [0.668025, 0.400815, 0.240489, 0.144293], 'p_i': 80, 'u_i': 3.4662},
        {'id': 4, 'e_m': 0.490201, 'e_o_k': [0.287947, 0.172768, 0.103661, 0.062196, 0.037318, 0.022391], 'p_i': 40, 'u_i': 1.3531},
        {'id': 5, 'e_m': 14.146212, 'e_o_k': [12.377936, 7.426761], 'p_i': 80, 'u_i': 3.5457},
        {'id': 6, 'e_m': 0.399627, 'e_o_k': [0.349674, 0.209804], 'p_i': 10, 'u_i': 1.4096},
        {'id': 7, 'e_m': 0.841518, 'e_o_k': [0.541418, 0.324851, 0.194910, 0.116946], 'p_i': 20, 'u_i': 4.8654},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
