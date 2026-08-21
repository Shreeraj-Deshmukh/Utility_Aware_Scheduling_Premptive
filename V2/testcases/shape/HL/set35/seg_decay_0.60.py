"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.306627, 'e_o_k': [0.070456, 0.042274, 0.025364, 0.015219], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.296738, 'e_o_k': [0.062252, 0.037351, 0.022411, 0.013446, 0.008068, 0.004841], 'p_i': 20, 'u_i': 2.3478},
        {'id': 2, 'e_m': 4.540447, 'e_o_k': [1.158277, 0.694966, 0.416980], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 14.551355, 'e_o_k': [3.155655, 1.893393, 1.136036, 0.681621, 0.408973], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 5.361003, 'e_o_k': [1.675313, 1.005188], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 2.936211, 'e_o_k': [0.615982, 0.369589, 0.221753, 0.133052, 0.079831, 0.047899], 'p_i': 40, 'u_i': 2.1935},
        {'id': 6, 'e_m': 1.139762, 'e_o_k': [0.290756, 0.174453, 0.104672], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 0.606538, 'e_o_k': [0.189543, 0.113726], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
