"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639987, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639987, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.755444, 'e_o_k': [1.365345, 1.092276], 'p_i': 10, 'u_i': 2.2749},
        {'id': 1, 'e_m': 1.252161, 'e_o_k': [0.973903, 0.779122], 'p_i': 20, 'u_i': 4.9536},
        {'id': 2, 'e_m': 4.766658, 'e_o_k': [3.707401, 2.965921], 'p_i': 40, 'u_i': 2.9112},
        {'id': 3, 'e_m': 0.196999, 'e_o_k': [0.153221, 0.122577], 'p_i': 80, 'u_i': 2.1467},
        {'id': 4, 'e_m': 0.073294, 'e_o_k': [0.057007, 0.045605], 'p_i': 10, 'u_i': 3.3563},
        {'id': 5, 'e_m': 11.978121, 'e_o_k': [9.316316, 7.453053], 'p_i': 80, 'u_i': 2.2972},
        {'id': 6, 'e_m': 0.516364, 'e_o_k': [0.401616, 0.321293], 'p_i': 10, 'u_i': 3.3121},
        {'id': 7, 'e_m': 9.261051, 'e_o_k': [7.203040, 5.762432], 'p_i': 40, 'u_i': 4.6359},
    ]
    B_BUDGET = 176.639987
    return processors, tasks, B_BUDGET
