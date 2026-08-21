"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.40001, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.40001, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.505787, 'e_o_k': [0.140496, 0.112397], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.195219, 'e_o_k': [0.054227, 0.043382], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 10.184228, 'e_o_k': [2.828952, 2.263162], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 6.561179, 'e_o_k': [1.822550, 1.458040], 'p_i': 80, 'u_i': 1.1592},
        {'id': 4, 'e_m': 4.539403, 'e_o_k': [1.260945, 1.008756], 'p_i': 20, 'u_i': 2.2796},
        {'id': 5, 'e_m': 6.765491, 'e_o_k': [1.879303, 1.503442], 'p_i': 80, 'u_i': 4.8637},
        {'id': 6, 'e_m': 1.084629, 'e_o_k': [0.301286, 0.241029], 'p_i': 20, 'u_i': 2.9768},
        {'id': 7, 'e_m': 0.372698, 'e_o_k': [0.103527, 0.082822], 'p_i': 10, 'u_i': 1.8410},
    ]
    B_BUDGET = 110.400010
    return processors, tasks, B_BUDGET
