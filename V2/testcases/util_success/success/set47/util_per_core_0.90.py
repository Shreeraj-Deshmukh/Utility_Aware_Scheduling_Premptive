"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279984, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279984, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.810243, 'e_o_k': [0.065886, 0.052709, 0.042167, 0.033734, 0.026987, 0.021590], 'p_i': 10, 'u_i': 2.3485},
        {'id': 1, 'e_m': 8.401813, 'e_o_k': [0.683208, 0.546566, 0.437253, 0.349802, 0.279842, 0.223873], 'p_i': 20, 'u_i': 4.6143},
        {'id': 2, 'e_m': 6.000480, 'e_o_k': [1.000080, 0.800064], 'p_i': 40, 'u_i': 3.6010},
        {'id': 3, 'e_m': 25.406318, 'e_o_k': [4.234386, 3.387509], 'p_i': 80, 'u_i': 3.9719},
        {'id': 4, 'e_m': 2.165745, 'e_o_k': [0.220096, 0.176077, 0.140861, 0.112689], 'p_i': 10, 'u_i': 1.7124},
        {'id': 5, 'e_m': 0.665521, 'e_o_k': [0.067634, 0.054107, 0.043286, 0.034629], 'p_i': 40, 'u_i': 2.0839},
        {'id': 6, 'e_m': 31.992378, 'e_o_k': [3.251258, 2.601006, 2.080805, 1.664644], 'p_i': 80, 'u_i': 3.4011},
        {'id': 7, 'e_m': 3.963535, 'e_o_k': [0.660589, 0.528471], 'p_i': 20, 'u_i': 4.0659},
    ]
    B_BUDGET = 215.279984
    return processors, tasks, B_BUDGET
