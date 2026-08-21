"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639991, "H": 80, "J": 20, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639991, "H": 80, "J": 20, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.680163, 'e_o_k': [0.390258, 0.312206, 0.249765], 'p_i': 10, 'u_i': 4.9110},
        {'id': 1, 'e_m': 1.689853, 'e_o_k': [0.969588, 0.775670, 0.620536], 'p_i': 20, 'u_i': 2.4171},
        {'id': 2, 'e_m': 0.519615, 'e_o_k': [0.298140, 0.238512, 0.190810], 'p_i': 40, 'u_i': 4.5639},
        {'id': 3, 'e_m': 18.094462, 'e_o_k': [10.382068, 8.305654, 6.644524], 'p_i': 80, 'u_i': 3.1608},
        {'id': 4, 'e_m': 5.009794, 'e_o_k': [2.874472, 2.299577, 1.839662], 'p_i': 80, 'u_i': 1.3239},
        {'id': 5, 'e_m': 1.955931, 'e_o_k': [1.122255, 0.897804, 0.718244], 'p_i': 80, 'u_i': 4.3282},
        {'id': 6, 'e_m': 10.750512, 'e_o_k': [6.168327, 4.934661, 3.947729], 'p_i': 40, 'u_i': 3.0285},
        {'id': 7, 'e_m': 4.198837, 'e_o_k': [2.409169, 1.927335, 1.541868], 'p_i': 80, 'u_i': 4.7214},
    ]
    B_BUDGET = 176.639991
    return processors, tasks, B_BUDGET
