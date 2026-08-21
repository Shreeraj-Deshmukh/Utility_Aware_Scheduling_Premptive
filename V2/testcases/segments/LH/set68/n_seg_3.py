"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31999, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.31999, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.465316, 'e_o_k': [0.266985, 0.213588, 0.170870], 'p_i': 10, 'u_i': 3.1458},
        {'id': 1, 'e_m': 1.632139, 'e_o_k': [0.936473, 0.749179, 0.599343], 'p_i': 20, 'u_i': 4.9683},
        {'id': 2, 'e_m': 1.388565, 'e_o_k': [0.796717, 0.637374, 0.509899], 'p_i': 40, 'u_i': 2.4718},
        {'id': 3, 'e_m': 4.132141, 'e_o_k': [2.370900, 1.896720, 1.517376], 'p_i': 80, 'u_i': 3.8875},
        {'id': 4, 'e_m': 1.499437, 'e_o_k': [0.860332, 0.688266, 0.550613], 'p_i': 80, 'u_i': 3.3599},
        {'id': 5, 'e_m': 0.197682, 'e_o_k': [0.113424, 0.090739, 0.072592], 'p_i': 40, 'u_i': 3.9269},
        {'id': 6, 'e_m': 1.272876, 'e_o_k': [0.730339, 0.584271, 0.467417], 'p_i': 10, 'u_i': 3.4836},
        {'id': 7, 'e_m': 1.380915, 'e_o_k': [0.792328, 0.633862, 0.507090], 'p_i': 40, 'u_i': 2.8974},
    ]
    B_BUDGET = 88.319990
    return processors, tasks, B_BUDGET
