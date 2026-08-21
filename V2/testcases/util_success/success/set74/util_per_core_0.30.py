"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759995, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759995, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.178330, 'e_o_k': [0.015915, 0.012732, 0.010185, 0.008148, 0.006519], 'p_i': 10, 'u_i': 4.9795},
        {'id': 1, 'e_m': 1.727397, 'e_o_k': [0.212385, 0.169908, 0.135926], 'p_i': 20, 'u_i': 4.9448},
        {'id': 2, 'e_m': 5.675578, 'e_o_k': [0.506507, 0.405205, 0.324164, 0.259332, 0.207465], 'p_i': 40, 'u_i': 4.4554},
        {'id': 3, 'e_m': 15.069777, 'e_o_k': [1.344875, 1.075900, 0.860720, 0.688576, 0.550861], 'p_i': 80, 'u_i': 2.2591},
        {'id': 4, 'e_m': 0.164679, 'e_o_k': [0.020247, 0.016198, 0.012958], 'p_i': 10, 'u_i': 2.7803},
        {'id': 5, 'e_m': 7.479388, 'e_o_k': [0.608199, 0.486559, 0.389247, 0.311398, 0.249118, 0.199295], 'p_i': 80, 'u_i': 3.4160},
        {'id': 6, 'e_m': 2.330253, 'e_o_k': [0.286507, 0.229205, 0.183364], 'p_i': 80, 'u_i': 3.4712},
        {'id': 7, 'e_m': 0.528942, 'e_o_k': [0.047204, 0.037764, 0.030211, 0.024169, 0.019335], 'p_i': 20, 'u_i': 4.3322},
    ]
    B_BUDGET = 71.759995
    return processors, tasks, B_BUDGET
