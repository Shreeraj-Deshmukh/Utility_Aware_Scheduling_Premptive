"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.12002, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.12002, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.048497, 'e_o_k': [0.272058, 0.217646, 0.174117, 0.139294, 0.111435], 'p_i': 10, 'u_i': 1.5170},
        {'id': 1, 'e_m': 6.135860, 'e_o_k': [0.754409, 0.603527, 0.482822], 'p_i': 20, 'u_i': 1.1074},
        {'id': 2, 'e_m': 18.881644, 'e_o_k': [1.685059, 1.348047, 1.078438, 0.862750, 0.690200], 'p_i': 40, 'u_i': 1.6550},
        {'id': 3, 'e_m': 0.340016, 'e_o_k': [0.041805, 0.033444, 0.026755], 'p_i': 80, 'u_i': 1.4707},
        {'id': 4, 'e_m': 4.568211, 'e_o_k': [0.371472, 0.297177, 0.237742, 0.190194, 0.152155, 0.121724], 'p_i': 40, 'u_i': 3.8998},
        {'id': 5, 'e_m': 10.182581, 'e_o_k': [1.697097, 1.357677], 'p_i': 80, 'u_i': 3.2713},
        {'id': 6, 'e_m': 8.415850, 'e_o_k': [1.034736, 0.827789, 0.662231], 'p_i': 20, 'u_i': 1.8462},
        {'id': 7, 'e_m': 17.991440, 'e_o_k': [1.828398, 1.462719, 1.170175, 0.936140], 'p_i': 40, 'u_i': 2.0665},
    ]
    B_BUDGET = 263.120020
    return processors, tasks, B_BUDGET
