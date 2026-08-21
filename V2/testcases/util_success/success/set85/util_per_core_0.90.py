"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279995, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279995, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.720641, 'e_o_k': [0.421285, 0.337028, 0.269623, 0.215698, 0.172558], 'p_i': 10, 'u_i': 4.3413},
        {'id': 1, 'e_m': 1.416710, 'e_o_k': [0.174186, 0.139348, 0.111479], 'p_i': 20, 'u_i': 1.0636},
        {'id': 2, 'e_m': 12.259749, 'e_o_k': [1.094099, 0.875280, 0.700224, 0.560179, 0.448143], 'p_i': 40, 'u_i': 4.5969},
        {'id': 3, 'e_m': 26.960517, 'e_o_k': [3.314818, 2.651854, 2.121483], 'p_i': 80, 'u_i': 3.6081},
        {'id': 4, 'e_m': 1.172457, 'e_o_k': [0.144155, 0.115324, 0.092259], 'p_i': 20, 'u_i': 2.6638},
        {'id': 5, 'e_m': 1.853540, 'e_o_k': [0.150724, 0.120579, 0.096463, 0.077171, 0.061736, 0.049389], 'p_i': 10, 'u_i': 1.2714},
        {'id': 6, 'e_m': 0.863011, 'e_o_k': [0.077018, 0.061614, 0.049291, 0.039433, 0.031547], 'p_i': 10, 'u_i': 4.5856},
        {'id': 7, 'e_m': 5.666445, 'e_o_k': [0.460776, 0.368621, 0.294897, 0.235918, 0.188734, 0.150987], 'p_i': 20, 'u_i': 3.2593},
    ]
    B_BUDGET = 215.279995
    return processors, tasks, B_BUDGET
