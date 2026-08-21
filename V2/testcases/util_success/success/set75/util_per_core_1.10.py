"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120008, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120008, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.700069, 'e_o_k': [0.450011, 0.360009], 'p_i': 10, 'u_i': 1.8412},
        {'id': 1, 'e_m': 2.124722, 'e_o_k': [0.215927, 0.172742, 0.138193, 0.110555], 'p_i': 20, 'u_i': 1.2830},
        {'id': 2, 'e_m': 19.179733, 'e_o_k': [1.711661, 1.369329, 1.095463, 0.876370, 0.701096], 'p_i': 40, 'u_i': 3.0625},
        {'id': 3, 'e_m': 39.480590, 'e_o_k': [4.854171, 3.883337, 3.106669], 'p_i': 80, 'u_i': 1.6371},
        {'id': 4, 'e_m': 2.020012, 'e_o_k': [0.164261, 0.131409, 0.105127, 0.084101, 0.067281, 0.053825], 'p_i': 20, 'u_i': 3.9678},
        {'id': 5, 'e_m': 1.916233, 'e_o_k': [0.155822, 0.124657, 0.099726, 0.079781, 0.063825, 0.051060], 'p_i': 10, 'u_i': 1.3120},
        {'id': 6, 'e_m': 9.870417, 'e_o_k': [1.213576, 0.970861, 0.776689], 'p_i': 20, 'u_i': 2.6546},
        {'id': 7, 'e_m': 1.292231, 'e_o_k': [0.115323, 0.092258, 0.073807, 0.059045, 0.047236], 'p_i': 20, 'u_i': 1.0495},
    ]
    B_BUDGET = 263.120008
    return processors, tasks, B_BUDGET
