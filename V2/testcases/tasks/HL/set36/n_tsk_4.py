"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.028401, 'e_o_k': [0.563445, 0.450756], 'p_i': 10, 'u_i': 1.1535},
        {'id': 1, 'e_m': 1.732749, 'e_o_k': [0.293487, 0.234790, 0.187832, 0.150266], 'p_i': 20, 'u_i': 2.8332},
        {'id': 2, 'e_m': 2.718634, 'e_o_k': [0.755176, 0.604141], 'p_i': 40, 'u_i': 2.4233},
        {'id': 3, 'e_m': 35.404529, 'e_o_k': [4.798298, 3.838638, 3.070911, 2.456729, 1.965383, 1.572306], 'p_i': 80, 'u_i': 4.2523},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET
