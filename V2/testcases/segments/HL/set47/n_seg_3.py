"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.433436, 'e_o_k': [0.498655, 0.398924, 0.319139], 'p_i': 10, 'u_i': 3.4259},
        {'id': 1, 'e_m': 1.678664, 'e_o_k': [0.343989, 0.275191, 0.220153], 'p_i': 20, 'u_i': 1.3819},
        {'id': 2, 'e_m': 2.697717, 'e_o_k': [0.552811, 0.442249, 0.353799], 'p_i': 40, 'u_i': 1.7445},
        {'id': 3, 'e_m': 5.583418, 'e_o_k': [1.144143, 0.915314, 0.732252], 'p_i': 80, 'u_i': 2.0127},
        {'id': 4, 'e_m': 0.959967, 'e_o_k': [0.196714, 0.157372, 0.125897], 'p_i': 10, 'u_i': 4.7864},
        {'id': 5, 'e_m': 1.200367, 'e_o_k': [0.245977, 0.196781, 0.157425], 'p_i': 10, 'u_i': 1.7550},
        {'id': 6, 'e_m': 0.195327, 'e_o_k': [0.040026, 0.032021, 0.025617], 'p_i': 10, 'u_i': 2.9364},
        {'id': 7, 'e_m': 3.996858, 'e_o_k': [0.819028, 0.655223, 0.524178], 'p_i': 40, 'u_i': 1.0429},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
