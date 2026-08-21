"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.043017, 'e_o_k': [0.289727, 0.231782], 'p_i': 10, 'u_i': 2.9022},
        {'id': 1, 'e_m': 3.136325, 'e_o_k': [0.466493, 0.373194, 0.298555, 0.238844, 0.191076], 'p_i': 20, 'u_i': 3.0103},
        {'id': 2, 'e_m': 2.217270, 'e_o_k': [0.375554, 0.300443, 0.240354, 0.192284], 'p_i': 40, 'u_i': 4.4931},
        {'id': 3, 'e_m': 12.826047, 'e_o_k': [1.738286, 1.390629, 1.112503, 0.890002, 0.712002, 0.569602], 'p_i': 80, 'u_i': 4.6084},
        {'id': 4, 'e_m': 1.766330, 'e_o_k': [0.490647, 0.392518], 'p_i': 10, 'u_i': 3.5739},
        {'id': 5, 'e_m': 5.859667, 'e_o_k': [0.794148, 0.635318, 0.508255, 0.406604, 0.325283, 0.260226], 'p_i': 40, 'u_i': 3.1864},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
