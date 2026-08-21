"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400013, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400013, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.567714, 'e_o_k': [0.679396, 0.543517, 0.434813, 0.347851, 0.278281], 'p_i': 10, 'u_i': 1.7421},
        {'id': 1, 'e_m': 2.660477, 'e_o_k': [0.360569, 0.288455, 0.230764, 0.184611, 0.147689, 0.118151], 'p_i': 20, 'u_i': 1.9951},
        {'id': 2, 'e_m': 4.513749, 'e_o_k': [1.253819, 1.003055], 'p_i': 40, 'u_i': 1.2617},
        {'id': 3, 'e_m': 7.788884, 'e_o_k': [1.055610, 0.844488, 0.675591, 0.540472, 0.432378, 0.345902], 'p_i': 80, 'u_i': 4.5683},
    ]
    B_BUDGET = 110.400013
    return processors, tasks, B_BUDGET
