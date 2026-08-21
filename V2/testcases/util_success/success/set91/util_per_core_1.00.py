"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200007, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200007, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.366379, 'e_o_k': [0.167997, 0.134398, 0.107518], 'p_i': 10, 'u_i': 1.0994},
        {'id': 1, 'e_m': 2.187722, 'e_o_k': [0.177898, 0.142319, 0.113855, 0.091084, 0.072867, 0.058294], 'p_i': 20, 'u_i': 4.8716},
        {'id': 2, 'e_m': 19.758518, 'e_o_k': [1.606697, 1.285358, 1.028286, 0.822629, 0.658103, 0.526483], 'p_i': 40, 'u_i': 3.1304},
        {'id': 3, 'e_m': 4.896297, 'e_o_k': [0.497591, 0.398073, 0.318458, 0.254767], 'p_i': 80, 'u_i': 4.2274},
        {'id': 4, 'e_m': 18.874459, 'e_o_k': [1.534808, 1.227847, 0.982277, 0.785822, 0.628658, 0.502926], 'p_i': 40, 'u_i': 1.7494},
        {'id': 5, 'e_m': 1.951142, 'e_o_k': [0.198287, 0.158629, 0.126904, 0.101523], 'p_i': 10, 'u_i': 4.2042},
        {'id': 6, 'e_m': 20.857754, 'e_o_k': [2.564478, 2.051582, 1.641266], 'p_i': 80, 'u_i': 1.0373},
        {'id': 7, 'e_m': 10.844471, 'e_o_k': [1.807412, 1.445930], 'p_i': 40, 'u_i': 1.4059},
    ]
    B_BUDGET = 239.200007
    return processors, tasks, B_BUDGET
