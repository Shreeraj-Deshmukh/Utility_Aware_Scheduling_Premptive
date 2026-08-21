"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600003, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600003, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.987116, 'e_o_k': [0.100317, 0.080253, 0.064203, 0.051362], 'p_i': 10, 'u_i': 4.2289},
        {'id': 1, 'e_m': 0.306618, 'e_o_k': [0.051103, 0.040882], 'p_i': 20, 'u_i': 3.6434},
        {'id': 2, 'e_m': 4.138493, 'e_o_k': [0.336529, 0.269223, 0.215378, 0.172303, 0.137842, 0.110274], 'p_i': 40, 'u_i': 4.1771},
        {'id': 3, 'e_m': 2.035649, 'e_o_k': [0.206875, 0.165500, 0.132400, 0.105920], 'p_i': 80, 'u_i': 4.0903},
        {'id': 4, 'e_m': 2.563940, 'e_o_k': [0.260563, 0.208450, 0.166760, 0.133408], 'p_i': 20, 'u_i': 2.9627},
        {'id': 5, 'e_m': 0.137937, 'e_o_k': [0.014018, 0.011214, 0.008971, 0.007177], 'p_i': 80, 'u_i': 1.9286},
        {'id': 6, 'e_m': 4.029635, 'e_o_k': [0.409516, 0.327613, 0.262090, 0.209672], 'p_i': 10, 'u_i': 3.5955},
        {'id': 7, 'e_m': 8.966595, 'e_o_k': [0.800208, 0.640166, 0.512133, 0.409706, 0.327765], 'p_i': 40, 'u_i': 1.8182},
    ]
    B_BUDGET = 119.600003
    return processors, tasks, B_BUDGET
