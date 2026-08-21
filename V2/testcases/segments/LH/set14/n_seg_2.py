"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 20, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 20, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.361229, 'e_o_k': [0.280956, 0.224765], 'p_i': 10, 'u_i': 1.0216},
        {'id': 1, 'e_m': 1.543444, 'e_o_k': [1.200456, 0.960365], 'p_i': 20, 'u_i': 4.0085},
        {'id': 2, 'e_m': 5.606336, 'e_o_k': [4.360484, 3.488387], 'p_i': 40, 'u_i': 1.9931},
        {'id': 3, 'e_m': 2.233033, 'e_o_k': [1.736803, 1.389443], 'p_i': 80, 'u_i': 2.4773},
        {'id': 4, 'e_m': 0.084420, 'e_o_k': [0.065660, 0.052528], 'p_i': 80, 'u_i': 3.1022},
        {'id': 5, 'e_m': 0.994040, 'e_o_k': [0.773142, 0.618514], 'p_i': 40, 'u_i': 1.7440},
        {'id': 6, 'e_m': 3.955611, 'e_o_k': [3.076586, 2.461269], 'p_i': 80, 'u_i': 1.2190},
        {'id': 7, 'e_m': 3.462576, 'e_o_k': [2.693114, 2.154491], 'p_i': 80, 'u_i': 2.8489},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
