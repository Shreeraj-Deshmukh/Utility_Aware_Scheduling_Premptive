"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399991, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399991, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.201488, 'e_o_k': [0.043695, 0.026217, 0.015730, 0.009438, 0.005663], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 1.441830, 'e_o_k': [0.302478, 0.181487, 0.108892, 0.065335, 0.039201, 0.023521], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 8.661890, 'e_o_k': [2.706841, 1.624104], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 8.902172, 'e_o_k': [2.781929, 1.669157], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 5.993625, 'e_o_k': [1.873008, 1.123805], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 4.342413, 'e_o_k': [0.910985, 0.546591, 0.327955, 0.196773, 0.118064, 0.070838], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 1.301354, 'e_o_k': [0.406673, 0.244004], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 3.654332, 'e_o_k': [0.932227, 0.559336, 0.335602], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 110.399991
    return processors, tasks, B_BUDGET
