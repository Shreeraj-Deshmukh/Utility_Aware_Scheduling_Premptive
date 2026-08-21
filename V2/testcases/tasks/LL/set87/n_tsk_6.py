"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200009, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200009, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.101415, 'e_o_k': [0.225700, 0.180560, 0.144448], 'p_i': 10, 'u_i': 1.0870},
        {'id': 1, 'e_m': 0.215635, 'e_o_k': [0.029225, 0.023380, 0.018704, 0.014963, 0.011970, 0.009576], 'p_i': 20, 'u_i': 2.0773},
        {'id': 2, 'e_m': 0.863805, 'e_o_k': [0.128481, 0.102785, 0.082228, 0.065782, 0.052626], 'p_i': 40, 'u_i': 2.9699},
        {'id': 3, 'e_m': 9.332672, 'e_o_k': [1.912433, 1.529946, 1.223957], 'p_i': 80, 'u_i': 1.6736},
        {'id': 4, 'e_m': 1.751210, 'e_o_k': [0.260473, 0.208378, 0.166702, 0.133362, 0.106690], 'p_i': 20, 'u_i': 2.6796},
        {'id': 5, 'e_m': 2.130510, 'e_o_k': [0.436580, 0.349264, 0.279411], 'p_i': 40, 'u_i': 2.5270},
    ]
    B_BUDGET = 55.200009
    return processors, tasks, B_BUDGET
