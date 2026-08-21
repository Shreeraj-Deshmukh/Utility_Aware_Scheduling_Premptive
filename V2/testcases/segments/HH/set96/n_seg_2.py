"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640016, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640016, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.505787, 'e_o_k': [0.393390, 0.314712], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.195219, 'e_o_k': [0.151837, 0.121469], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 10.184228, 'e_o_k': [7.921066, 6.336853], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 6.561179, 'e_o_k': [5.103139, 4.082511], 'p_i': 80, 'u_i': 1.1592},
        {'id': 4, 'e_m': 4.539403, 'e_o_k': [3.530646, 2.824517], 'p_i': 20, 'u_i': 2.2796},
        {'id': 5, 'e_m': 6.765491, 'e_o_k': [5.262049, 4.209639], 'p_i': 80, 'u_i': 4.8637},
        {'id': 6, 'e_m': 1.084629, 'e_o_k': [0.843600, 0.674880], 'p_i': 20, 'u_i': 2.9768},
        {'id': 7, 'e_m': 0.372698, 'e_o_k': [0.289876, 0.231901], 'p_i': 10, 'u_i': 1.8410},
    ]
    B_BUDGET = 176.640016
    return processors, tasks, B_BUDGET
