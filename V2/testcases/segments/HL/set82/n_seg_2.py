"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.689807, 'e_o_k': [0.469391, 0.375513], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.355169, 'e_o_k': [0.098658, 0.078927], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 2.867086, 'e_o_k': [0.796413, 0.637130], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 3.497724, 'e_o_k': [0.971590, 0.777272], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 13.830064, 'e_o_k': [3.841684, 3.073348], 'p_i': 80, 'u_i': 2.3882},
        {'id': 5, 'e_m': 3.101531, 'e_o_k': [0.861536, 0.689229], 'p_i': 20, 'u_i': 4.1284},
        {'id': 6, 'e_m': 0.222281, 'e_o_k': [0.061745, 0.049396], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 2.953634, 'e_o_k': [0.820454, 0.656363], 'p_i': 20, 'u_i': 3.2846},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET
