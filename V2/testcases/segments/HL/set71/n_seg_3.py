"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.149966, 'e_o_k': [0.440567, 0.352454, 0.281963], 'p_i': 10, 'u_i': 1.0606},
        {'id': 1, 'e_m': 0.415795, 'e_o_k': [0.085204, 0.068163, 0.054530], 'p_i': 20, 'u_i': 3.4010},
        {'id': 2, 'e_m': 1.011654, 'e_o_k': [0.207306, 0.165845, 0.132676], 'p_i': 40, 'u_i': 1.6455},
        {'id': 3, 'e_m': 23.962531, 'e_o_k': [4.910355, 3.928284, 3.142627], 'p_i': 80, 'u_i': 1.3745},
        {'id': 4, 'e_m': 1.255643, 'e_o_k': [0.257304, 0.205843, 0.164674], 'p_i': 40, 'u_i': 1.5038},
        {'id': 5, 'e_m': 6.392981, 'e_o_k': [1.310037, 1.048030, 0.838424], 'p_i': 40, 'u_i': 4.4242},
        {'id': 6, 'e_m': 1.712311, 'e_o_k': [0.350883, 0.280707, 0.224565], 'p_i': 40, 'u_i': 1.3856},
        {'id': 7, 'e_m': 0.107345, 'e_o_k': [0.021997, 0.017598, 0.014078], 'p_i': 20, 'u_i': 2.4453},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET
