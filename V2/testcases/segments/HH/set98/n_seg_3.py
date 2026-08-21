"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.755444, 'e_o_k': [1.007222, 0.805778, 0.644622], 'p_i': 10, 'u_i': 2.2749},
        {'id': 1, 'e_m': 1.252161, 'e_o_k': [0.718453, 0.574762, 0.459810], 'p_i': 20, 'u_i': 4.9536},
        {'id': 2, 'e_m': 4.766658, 'e_o_k': [2.734968, 2.187974, 1.750379], 'p_i': 40, 'u_i': 2.9112},
        {'id': 3, 'e_m': 0.196999, 'e_o_k': [0.113032, 0.090426, 0.072341], 'p_i': 80, 'u_i': 2.1467},
        {'id': 4, 'e_m': 0.073294, 'e_o_k': [0.042054, 0.033643, 0.026915], 'p_i': 10, 'u_i': 3.3563},
        {'id': 5, 'e_m': 11.978121, 'e_o_k': [6.872692, 5.498154, 4.398523], 'p_i': 80, 'u_i': 2.2972},
        {'id': 6, 'e_m': 0.516364, 'e_o_k': [0.296274, 0.237019, 0.189616], 'p_i': 10, 'u_i': 3.3121},
        {'id': 7, 'e_m': 9.261051, 'e_o_k': [5.313718, 4.250974, 3.400779], 'p_i': 40, 'u_i': 4.6359},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET
