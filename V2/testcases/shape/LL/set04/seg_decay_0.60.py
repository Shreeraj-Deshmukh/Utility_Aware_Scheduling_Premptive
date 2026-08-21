"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200003, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.200003, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.464878, 'e_o_k': [0.097526, 0.058515, 0.035109, 0.021066, 0.012639, 0.007584], 'p_i': 10, 'u_i': 2.4783},
        {'id': 1, 'e_m': 0.028439, 'e_o_k': [0.005966, 0.003580, 0.002148, 0.001289, 0.000773, 0.000464], 'p_i': 20, 'u_i': 1.9438},
        {'id': 2, 'e_m': 1.311997, 'e_o_k': [0.409999, 0.245999], 'p_i': 40, 'u_i': 1.5728},
        {'id': 3, 'e_m': 2.237336, 'e_o_k': [0.699168, 0.419501], 'p_i': 80, 'u_i': 1.5110},
        {'id': 4, 'e_m': 1.174834, 'e_o_k': [0.367136, 0.220281], 'p_i': 20, 'u_i': 4.3454},
        {'id': 5, 'e_m': 5.271494, 'e_o_k': [1.211281, 0.726769, 0.436061, 0.261637], 'p_i': 40, 'u_i': 2.7253},
        {'id': 6, 'e_m': 0.171228, 'e_o_k': [0.053509, 0.032105], 'p_i': 10, 'u_i': 1.4714},
        {'id': 7, 'e_m': 1.673435, 'e_o_k': [0.522949, 0.313769], 'p_i': 20, 'u_i': 2.9160},
    ]
    B_BUDGET = 55.200003
    return processors, tasks, B_BUDGET
