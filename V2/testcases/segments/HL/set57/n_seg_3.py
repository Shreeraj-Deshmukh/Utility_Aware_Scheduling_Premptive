"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.40002, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.40002, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.201488, 'e_o_k': [0.041289, 0.033031, 0.026425], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 1.441830, 'e_o_k': [0.295457, 0.236366, 0.189092], 'p_i': 20, 'u_i': 1.1969},
        {'id': 2, 'e_m': 8.661890, 'e_o_k': [1.774978, 1.419982, 1.135986], 'p_i': 40, 'u_i': 4.6056},
        {'id': 3, 'e_m': 8.902172, 'e_o_k': [1.824216, 1.459373, 1.167498], 'p_i': 80, 'u_i': 2.0280},
        {'id': 4, 'e_m': 5.993625, 'e_o_k': [1.228202, 0.982562, 0.786049], 'p_i': 40, 'u_i': 3.8591},
        {'id': 5, 'e_m': 4.342413, 'e_o_k': [0.889839, 0.711871, 0.569497], 'p_i': 80, 'u_i': 4.1547},
        {'id': 6, 'e_m': 1.301354, 'e_o_k': [0.266671, 0.213337, 0.170669], 'p_i': 10, 'u_i': 4.9057},
        {'id': 7, 'e_m': 3.654332, 'e_o_k': [0.748838, 0.599071, 0.479257], 'p_i': 80, 'u_i': 4.2009},
    ]
    B_BUDGET = 110.400020
    return processors, tasks, B_BUDGET
