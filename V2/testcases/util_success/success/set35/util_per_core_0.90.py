"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279999, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279999, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.409782, 'e_o_k': [0.277272, 0.221818, 0.177454, 0.141963, 0.113571, 0.090857], 'p_i': 10, 'u_i': 3.9981},
        {'id': 1, 'e_m': 6.203946, 'e_o_k': [0.630482, 0.504386, 0.403509, 0.322807], 'p_i': 20, 'u_i': 1.1221},
        {'id': 2, 'e_m': 8.925153, 'e_o_k': [1.097355, 0.877884, 0.702307], 'p_i': 40, 'u_i': 1.0173},
        {'id': 3, 'e_m': 19.095047, 'e_o_k': [3.182508, 2.546006], 'p_i': 80, 'u_i': 4.7591},
        {'id': 4, 'e_m': 8.892261, 'e_o_k': [0.903685, 0.722948, 0.578358, 0.462687], 'p_i': 80, 'u_i': 4.6573},
        {'id': 5, 'e_m': 23.578512, 'e_o_k': [2.898997, 2.319198, 1.855358], 'p_i': 80, 'u_i': 3.1574},
        {'id': 6, 'e_m': 2.364835, 'e_o_k': [0.192301, 0.153840, 0.123072, 0.098458, 0.078766, 0.063013], 'p_i': 10, 'u_i': 2.6010},
        {'id': 7, 'e_m': 0.892789, 'e_o_k': [0.109769, 0.087815, 0.070252], 'p_i': 20, 'u_i': 2.4102},
    ]
    B_BUDGET = 215.279999
    return processors, tasks, B_BUDGET
