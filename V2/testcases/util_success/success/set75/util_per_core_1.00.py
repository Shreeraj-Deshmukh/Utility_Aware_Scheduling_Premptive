"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200001, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200001, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.454608, 'e_o_k': [0.409101, 0.327281], 'p_i': 10, 'u_i': 1.8412},
        {'id': 1, 'e_m': 1.931566, 'e_o_k': [0.196297, 0.157038, 0.125630, 0.100504], 'p_i': 20, 'u_i': 1.2830},
        {'id': 2, 'e_m': 17.436121, 'e_o_k': [1.556056, 1.244844, 0.995876, 0.796700, 0.637360], 'p_i': 40, 'u_i': 3.0625},
        {'id': 3, 'e_m': 35.891445, 'e_o_k': [4.412883, 3.530306, 2.824245], 'p_i': 80, 'u_i': 1.6371},
        {'id': 4, 'e_m': 1.836375, 'e_o_k': [0.149328, 0.119462, 0.095570, 0.076456, 0.061165, 0.048932], 'p_i': 20, 'u_i': 3.9678},
        {'id': 5, 'e_m': 1.742030, 'e_o_k': [0.141656, 0.113325, 0.090660, 0.072528, 0.058022, 0.046418], 'p_i': 10, 'u_i': 1.3120},
        {'id': 6, 'e_m': 8.973106, 'e_o_k': [1.103251, 0.882601, 0.706080], 'p_i': 20, 'u_i': 2.6546},
        {'id': 7, 'e_m': 1.174756, 'e_o_k': [0.104839, 0.083871, 0.067097, 0.053678, 0.042942], 'p_i': 20, 'u_i': 1.0495},
    ]
    B_BUDGET = 239.200001
    return processors, tasks, B_BUDGET
