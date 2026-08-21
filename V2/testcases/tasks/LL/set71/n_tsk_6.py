"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.419192, 'e_o_k': [0.394220, 0.315376], 'p_i': 10, 'u_i': 1.9248},
        {'id': 1, 'e_m': 0.272690, 'e_o_k': [0.036957, 0.029566, 0.023652, 0.018922, 0.015138, 0.012110], 'p_i': 20, 'u_i': 3.6832},
        {'id': 2, 'e_m': 0.719531, 'e_o_k': [0.121872, 0.097497, 0.077998, 0.062398], 'p_i': 40, 'u_i': 2.0214},
        {'id': 3, 'e_m': 14.541944, 'e_o_k': [1.970838, 1.576670, 1.261336, 1.009069, 0.807255, 0.645804], 'p_i': 80, 'u_i': 3.5232},
        {'id': 4, 'e_m': 0.153738, 'e_o_k': [0.042705, 0.034164], 'p_i': 10, 'u_i': 1.0606},
        {'id': 5, 'e_m': 2.344799, 'e_o_k': [0.397154, 0.317723, 0.254179, 0.203343], 'p_i': 80, 'u_i': 3.4010},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
