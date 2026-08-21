"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.877722, 'e_o_k': [0.503611, 0.402889, 0.322311], 'p_i': 10, 'u_i': 2.2749},
        {'id': 1, 'e_m': 0.626081, 'e_o_k': [0.359227, 0.287381, 0.229905], 'p_i': 20, 'u_i': 4.9536},
        {'id': 2, 'e_m': 2.383329, 'e_o_k': [1.367484, 1.093987, 0.875190], 'p_i': 40, 'u_i': 2.9112},
        {'id': 3, 'e_m': 0.098499, 'e_o_k': [0.056516, 0.045213, 0.036170], 'p_i': 80, 'u_i': 2.1467},
        {'id': 4, 'e_m': 0.036647, 'e_o_k': [0.021027, 0.016822, 0.013457], 'p_i': 10, 'u_i': 3.3563},
        {'id': 5, 'e_m': 5.989060, 'e_o_k': [3.436346, 2.749077, 2.199261], 'p_i': 80, 'u_i': 2.2972},
        {'id': 6, 'e_m': 0.258182, 'e_o_k': [0.148137, 0.118510, 0.094808], 'p_i': 10, 'u_i': 3.3121},
        {'id': 7, 'e_m': 4.630526, 'e_o_k': [2.656859, 2.125487, 1.700390], 'p_i': 40, 'u_i': 4.6359},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
