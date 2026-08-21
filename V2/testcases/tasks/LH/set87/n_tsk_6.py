"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320012, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320012, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.101415, 'e_o_k': [0.631960, 0.505568, 0.404454], 'p_i': 10, 'u_i': 1.0870},
        {'id': 1, 'e_m': 0.215635, 'e_o_k': [0.081829, 0.065463, 0.052370, 0.041896, 0.033517, 0.026814], 'p_i': 20, 'u_i': 2.0773},
        {'id': 2, 'e_m': 0.863805, 'e_o_k': [0.359747, 0.287798, 0.230238, 0.184191, 0.147352], 'p_i': 40, 'u_i': 2.9699},
        {'id': 3, 'e_m': 9.332672, 'e_o_k': [5.354812, 4.283849, 3.427079], 'p_i': 80, 'u_i': 1.6736},
        {'id': 4, 'e_m': 1.751210, 'e_o_k': [0.729323, 0.583459, 0.466767, 0.373414, 0.298731], 'p_i': 20, 'u_i': 2.6796},
        {'id': 5, 'e_m': 2.130510, 'e_o_k': [1.222424, 0.977939, 0.782351], 'p_i': 40, 'u_i': 2.5270},
    ]
    B_BUDGET = 88.320012
    return processors, tasks, B_BUDGET
