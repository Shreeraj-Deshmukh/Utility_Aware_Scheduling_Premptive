"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680009, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680009, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.145211, 'e_o_k': [0.116383, 0.093107, 0.074485, 0.059588], 'p_i': 10, 'u_i': 1.6225},
        {'id': 1, 'e_m': 1.131105, 'e_o_k': [0.091978, 0.073582, 0.058866, 0.047093, 0.037674, 0.030139], 'p_i': 20, 'u_i': 1.5082},
        {'id': 2, 'e_m': 1.635759, 'e_o_k': [0.166236, 0.132989, 0.106391, 0.085113], 'p_i': 40, 'u_i': 1.8233},
        {'id': 3, 'e_m': 10.249639, 'e_o_k': [1.041630, 0.833304, 0.666643, 0.533315], 'p_i': 80, 'u_i': 1.9473},
        {'id': 4, 'e_m': 4.233912, 'e_o_k': [0.344288, 0.275430, 0.220344, 0.176275, 0.141020, 0.112816], 'p_i': 20, 'u_i': 2.1026},
        {'id': 5, 'e_m': 0.437464, 'e_o_k': [0.035573, 0.028459, 0.022767, 0.018213, 0.014571, 0.011657], 'p_i': 10, 'u_i': 4.2691},
        {'id': 6, 'e_m': 2.093940, 'e_o_k': [0.170272, 0.136218, 0.108974, 0.087179, 0.069743, 0.055795], 'p_i': 20, 'u_i': 3.6679},
        {'id': 7, 'e_m': 7.981619, 'e_o_k': [1.330270, 1.064216], 'p_i': 80, 'u_i': 2.7165},
    ]
    B_BUDGET = 95.680009
    return processors, tasks, B_BUDGET
