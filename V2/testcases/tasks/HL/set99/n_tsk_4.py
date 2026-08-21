"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.084132, 'e_o_k': [0.427076, 0.341661, 0.273329], 'p_i': 10, 'u_i': 2.9415},
        {'id': 1, 'e_m': 5.951899, 'e_o_k': [1.653305, 1.322644], 'p_i': 20, 'u_i': 4.1135},
        {'id': 2, 'e_m': 2.652369, 'e_o_k': [0.359470, 0.287576, 0.230061, 0.184048, 0.147239, 0.117791], 'p_i': 40, 'u_i': 3.4980},
        {'id': 3, 'e_m': 18.214611, 'e_o_k': [5.059614, 4.047691], 'p_i': 80, 'u_i': 2.1751},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
