"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32001, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.32001, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.786850, 'e_o_k': [0.611995, 0.489596], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 0.744352, 'e_o_k': [0.578940, 0.463152], 'p_i': 20, 'u_i': 4.7122},
        {'id': 2, 'e_m': 0.568045, 'e_o_k': [0.441813, 0.353450], 'p_i': 40, 'u_i': 2.7870},
        {'id': 3, 'e_m': 6.876570, 'e_o_k': [5.348443, 4.278755], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 2.991189, 'e_o_k': [2.326481, 1.861185], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 0.337006, 'e_o_k': [0.262116, 0.209693], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 0.443917, 'e_o_k': [0.345269, 0.276215], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 5.148870, 'e_o_k': [4.004677, 3.203742], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 88.320010
    return processors, tasks, B_BUDGET
