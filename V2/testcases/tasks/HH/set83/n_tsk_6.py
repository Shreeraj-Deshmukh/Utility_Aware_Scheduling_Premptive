"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.112793, 'e_o_k': [1.643283, 1.314627], 'p_i': 10, 'u_i': 3.4799},
        {'id': 1, 'e_m': 1.985293, 'e_o_k': [0.826812, 0.661449, 0.529159, 0.423328, 0.338662], 'p_i': 20, 'u_i': 2.9893},
        {'id': 2, 'e_m': 1.603759, 'e_o_k': [0.667915, 0.534332, 0.427465, 0.341972, 0.273578], 'p_i': 40, 'u_i': 3.6030},
        {'id': 3, 'e_m': 19.251871, 'e_o_k': [14.973677, 11.978942], 'p_i': 80, 'u_i': 4.7122},
        {'id': 4, 'e_m': 13.207286, 'e_o_k': [10.272333, 8.217867], 'p_i': 80, 'u_i': 2.7870},
        {'id': 5, 'e_m': 1.744905, 'e_o_k': [1.001175, 0.800940, 0.640752], 'p_i': 40, 'u_i': 1.7506},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
