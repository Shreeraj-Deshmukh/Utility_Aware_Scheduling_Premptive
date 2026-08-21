"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399982, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399982, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.755444, 'e_o_k': [0.359722, 0.287778, 0.230222], 'p_i': 10, 'u_i': 2.2749},
        {'id': 1, 'e_m': 1.252161, 'e_o_k': [0.256590, 0.205272, 0.164218], 'p_i': 20, 'u_i': 4.9536},
        {'id': 2, 'e_m': 4.766658, 'e_o_k': [0.976774, 0.781419, 0.625135], 'p_i': 40, 'u_i': 2.9112},
        {'id': 3, 'e_m': 0.196999, 'e_o_k': [0.040369, 0.032295, 0.025836], 'p_i': 80, 'u_i': 2.1467},
        {'id': 4, 'e_m': 0.073294, 'e_o_k': [0.015019, 0.012015, 0.009612], 'p_i': 10, 'u_i': 3.3563},
        {'id': 5, 'e_m': 11.978121, 'e_o_k': [2.454533, 1.963626, 1.570901], 'p_i': 80, 'u_i': 2.2972},
        {'id': 6, 'e_m': 0.516364, 'e_o_k': [0.105812, 0.084650, 0.067720], 'p_i': 10, 'u_i': 3.3121},
        {'id': 7, 'e_m': 9.261051, 'e_o_k': [1.897756, 1.518205, 1.214564], 'p_i': 40, 'u_i': 4.6359},
    ]
    B_BUDGET = 110.399982
    return processors, tasks, B_BUDGET
