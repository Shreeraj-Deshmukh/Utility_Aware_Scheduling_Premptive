"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.097419, 'e_o_k': [1.138172, 0.910538], 'p_i': 10, 'u_i': 3.2108},
        {'id': 1, 'e_m': 3.168359, 'e_o_k': [0.880100, 0.704080], 'p_i': 20, 'u_i': 1.2189},
        {'id': 2, 'e_m': 2.648778, 'e_o_k': [0.358983, 0.287186, 0.229749, 0.183799, 0.147039, 0.117632], 'p_i': 40, 'u_i': 1.4602},
        {'id': 3, 'e_m': 13.249655, 'e_o_k': [3.680460, 2.944368], 'p_i': 80, 'u_i': 2.5890},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET
