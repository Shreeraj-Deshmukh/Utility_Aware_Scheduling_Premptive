"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320006, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320006, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.560596, 'e_o_k': [0.321653, 0.257323, 0.205858], 'p_i': 10, 'u_i': 2.9208},
        {'id': 1, 'e_m': 2.273229, 'e_o_k': [1.304312, 1.043449, 0.834760], 'p_i': 20, 'u_i': 4.6519},
        {'id': 2, 'e_m': 5.286614, 'e_o_k': [3.033303, 2.426643, 1.941314], 'p_i': 40, 'u_i': 4.9020},
        {'id': 3, 'e_m': 1.840129, 'e_o_k': [1.055812, 0.844649, 0.675720], 'p_i': 80, 'u_i': 4.4826},
        {'id': 4, 'e_m': 0.311968, 'e_o_k': [0.178998, 0.143198, 0.114559], 'p_i': 80, 'u_i': 1.3844},
        {'id': 5, 'e_m': 1.580366, 'e_o_k': [0.906768, 0.725414, 0.580331], 'p_i': 40, 'u_i': 3.8571},
        {'id': 6, 'e_m': 2.375437, 'e_o_k': [1.362956, 1.090365, 0.872292], 'p_i': 80, 'u_i': 3.6185},
        {'id': 7, 'e_m': 0.040206, 'e_o_k': [0.023069, 0.018455, 0.014764], 'p_i': 20, 'u_i': 1.1495},
    ]
    B_BUDGET = 88.320006
    return processors, tasks, B_BUDGET
