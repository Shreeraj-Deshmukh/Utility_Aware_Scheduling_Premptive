"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200016, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.200016, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.464878, 'e_o_k': [0.038740, 0.038740, 0.038740, 0.038740, 0.038740, 0.038740], 'p_i': 10, 'u_i': 2.4783},
        {'id': 1, 'e_m': 0.028439, 'e_o_k': [0.002370, 0.002370, 0.002370, 0.002370, 0.002370, 0.002370], 'p_i': 20, 'u_i': 1.9438},
        {'id': 2, 'e_m': 1.311997, 'e_o_k': [0.327999, 0.327999], 'p_i': 40, 'u_i': 1.5728},
        {'id': 3, 'e_m': 2.237336, 'e_o_k': [0.559334, 0.559334], 'p_i': 80, 'u_i': 1.5110},
        {'id': 4, 'e_m': 1.174834, 'e_o_k': [0.293709, 0.293709], 'p_i': 20, 'u_i': 4.3454},
        {'id': 5, 'e_m': 5.271494, 'e_o_k': [0.658937, 0.658937, 0.658937, 0.658937], 'p_i': 40, 'u_i': 2.7253},
        {'id': 6, 'e_m': 0.171228, 'e_o_k': [0.042807, 0.042807], 'p_i': 10, 'u_i': 1.4714},
        {'id': 7, 'e_m': 1.673435, 'e_o_k': [0.418359, 0.418359], 'p_i': 20, 'u_i': 2.9160},
    ]
    B_BUDGET = 55.200016
    return processors, tasks, B_BUDGET
