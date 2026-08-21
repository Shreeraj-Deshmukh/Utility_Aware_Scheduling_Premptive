"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.939509, 'e_o_k': [0.288480, 0.230784, 0.184627, 0.147702, 0.118161], 'p_i': 10, 'u_i': 2.8937},
        {'id': 1, 'e_m': 2.763818, 'e_o_k': [0.468126, 0.374501, 0.299601, 0.239681], 'p_i': 20, 'u_i': 3.5048},
        {'id': 2, 'e_m': 0.413834, 'e_o_k': [0.056086, 0.044869, 0.035895, 0.028716, 0.022973, 0.018378], 'p_i': 40, 'u_i': 4.5166},
        {'id': 3, 'e_m': 2.175525, 'e_o_k': [0.368483, 0.294787, 0.235829, 0.188663], 'p_i': 80, 'u_i': 1.0922},
        {'id': 4, 'e_m': 8.790579, 'e_o_k': [2.441828, 1.953462], 'p_i': 40, 'u_i': 2.4300},
        {'id': 5, 'e_m': 4.211078, 'e_o_k': [0.626350, 0.501080, 0.400864, 0.320691, 0.256553], 'p_i': 20, 'u_i': 4.3958},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET
