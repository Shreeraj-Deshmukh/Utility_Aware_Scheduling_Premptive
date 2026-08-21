"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320041, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.320041, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.464878, 'e_o_k': [0.108472, 0.108472, 0.108472, 0.108472, 0.108472, 0.108472], 'p_i': 10, 'u_i': 2.4783},
        {'id': 1, 'e_m': 0.028439, 'e_o_k': [0.006636, 0.006636, 0.006636, 0.006636, 0.006636, 0.006636], 'p_i': 20, 'u_i': 1.9438},
        {'id': 2, 'e_m': 1.311997, 'e_o_k': [0.918398, 0.918398], 'p_i': 40, 'u_i': 1.5728},
        {'id': 3, 'e_m': 2.237336, 'e_o_k': [1.566135, 1.566135], 'p_i': 80, 'u_i': 1.5110},
        {'id': 4, 'e_m': 1.174834, 'e_o_k': [0.822384, 0.822384], 'p_i': 20, 'u_i': 4.3454},
        {'id': 5, 'e_m': 5.271494, 'e_o_k': [1.845023, 1.845023, 1.845023, 1.845023], 'p_i': 40, 'u_i': 2.7253},
        {'id': 6, 'e_m': 0.171228, 'e_o_k': [0.119860, 0.119860], 'p_i': 10, 'u_i': 1.4714},
        {'id': 7, 'e_m': 1.673435, 'e_o_k': [1.171405, 1.171405], 'p_i': 20, 'u_i': 2.9160},
    ]
    B_BUDGET = 88.320041
    return processors, tasks, B_BUDGET
