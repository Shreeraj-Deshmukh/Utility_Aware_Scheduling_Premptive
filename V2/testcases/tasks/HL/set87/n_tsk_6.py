"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.202831, 'e_o_k': [0.451400, 0.361120, 0.288896], 'p_i': 10, 'u_i': 1.0870},
        {'id': 1, 'e_m': 0.431270, 'e_o_k': [0.058449, 0.046759, 0.037407, 0.029926, 0.023941, 0.019153], 'p_i': 20, 'u_i': 2.0773},
        {'id': 2, 'e_m': 1.727609, 'e_o_k': [0.256962, 0.205570, 0.164456, 0.131565, 0.105252], 'p_i': 40, 'u_i': 2.9699},
        {'id': 3, 'e_m': 18.665343, 'e_o_k': [3.824865, 3.059892, 2.447914], 'p_i': 80, 'u_i': 1.6736},
        {'id': 4, 'e_m': 3.502419, 'e_o_k': [0.520945, 0.416756, 0.333405, 0.266724, 0.213379], 'p_i': 20, 'u_i': 2.6796},
        {'id': 5, 'e_m': 4.261019, 'e_o_k': [0.873160, 0.698528, 0.558822], 'p_i': 40, 'u_i': 2.5270},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET
