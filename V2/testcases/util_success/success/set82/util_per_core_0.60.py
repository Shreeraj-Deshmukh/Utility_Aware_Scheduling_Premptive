"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520005, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520005, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.534710, 'e_o_k': [0.226206, 0.180965, 0.144772, 0.115817, 0.092654], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.532754, 'e_o_k': [0.088792, 0.071034], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 4.300629, 'e_o_k': [0.437056, 0.349645, 0.279716, 0.223773], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 5.246586, 'e_o_k': [0.874431, 0.699545], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 20.745096, 'e_o_k': [1.686922, 1.349538, 1.079630, 0.863704, 0.690963, 0.552771], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 4.652296, 'e_o_k': [0.472794, 0.378235, 0.302588, 0.242071], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.333422, 'e_o_k': [0.055570, 0.044456], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 4.430451, 'e_o_k': [0.360270, 0.288216, 0.230573, 0.184458, 0.147566, 0.118053], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 143.520005
    return processors, tasks, B_BUDGET
