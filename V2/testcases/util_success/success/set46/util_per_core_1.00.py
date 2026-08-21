"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199997, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199997, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.884310, 'e_o_k': [0.477579, 0.382063, 0.305651], 'p_i': 10, 'u_i': 2.4451},
        {'id': 1, 'e_m': 1.864502, 'e_o_k': [0.310750, 0.248600], 'p_i': 20, 'u_i': 2.4444},
        {'id': 2, 'e_m': 14.814943, 'e_o_k': [1.821509, 1.457207, 1.165766], 'p_i': 40, 'u_i': 1.8731},
        {'id': 3, 'e_m': 34.869386, 'e_o_k': [2.835463, 2.268370, 1.814696, 1.451757, 1.161406, 0.929124], 'p_i': 80, 'u_i': 3.8016},
        {'id': 4, 'e_m': 5.736317, 'e_o_k': [0.466458, 0.373167, 0.298533, 0.238827, 0.191061, 0.152849], 'p_i': 40, 'u_i': 4.9092},
        {'id': 5, 'e_m': 0.130667, 'e_o_k': [0.016066, 0.012853, 0.010282], 'p_i': 10, 'u_i': 2.2628},
        {'id': 6, 'e_m': 9.949484, 'e_o_k': [1.658247, 1.326598], 'p_i': 20, 'u_i': 3.9298},
        {'id': 7, 'e_m': 4.652330, 'e_o_k': [0.775388, 0.620311], 'p_i': 80, 'u_i': 1.0850},
    ]
    B_BUDGET = 239.199997
    return processors, tasks, B_BUDGET
