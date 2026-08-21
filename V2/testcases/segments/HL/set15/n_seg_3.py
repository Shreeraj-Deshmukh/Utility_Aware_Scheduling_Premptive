"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.212074, 'e_o_k': [0.453294, 0.362635, 0.290108], 'p_i': 10, 'u_i': 4.4310},
        {'id': 1, 'e_m': 2.099648, 'e_o_k': [0.430256, 0.344205, 0.275364], 'p_i': 20, 'u_i': 4.5357},
        {'id': 2, 'e_m': 0.255502, 'e_o_k': [0.052357, 0.041886, 0.033508], 'p_i': 40, 'u_i': 3.5135},
        {'id': 3, 'e_m': 6.162213, 'e_o_k': [1.262749, 1.010199, 0.808159], 'p_i': 80, 'u_i': 3.8723},
        {'id': 4, 'e_m': 3.257255, 'e_o_k': [0.667470, 0.533976, 0.427181], 'p_i': 80, 'u_i': 1.1816},
        {'id': 5, 'e_m': 1.792700, 'e_o_k': [0.367357, 0.293885, 0.235108], 'p_i': 40, 'u_i': 3.3631},
        {'id': 6, 'e_m': 14.597411, 'e_o_k': [2.991273, 2.393018, 1.914415], 'p_i': 80, 'u_i': 2.0216},
        {'id': 7, 'e_m': 1.223941, 'e_o_k': [0.250808, 0.200646, 0.160517], 'p_i': 10, 'u_i': 3.3728},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
