"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31999, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.31999, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.216718, 'e_o_k': [0.698117, 0.558494, 0.446795], 'p_i': 10, 'u_i': 3.4259},
        {'id': 1, 'e_m': 0.839332, 'e_o_k': [0.481584, 0.385267, 0.308214], 'p_i': 20, 'u_i': 1.3819},
        {'id': 2, 'e_m': 1.348859, 'e_o_k': [0.773935, 0.619148, 0.495319], 'p_i': 40, 'u_i': 1.7445},
        {'id': 3, 'e_m': 2.791709, 'e_o_k': [1.601800, 1.281440, 1.025152], 'p_i': 80, 'u_i': 2.0127},
        {'id': 4, 'e_m': 0.479983, 'e_o_k': [0.275400, 0.220320, 0.176256], 'p_i': 10, 'u_i': 4.7864},
        {'id': 5, 'e_m': 0.600183, 'e_o_k': [0.344367, 0.275494, 0.220395], 'p_i': 10, 'u_i': 1.7550},
        {'id': 6, 'e_m': 0.097664, 'e_o_k': [0.056037, 0.044829, 0.035863], 'p_i': 10, 'u_i': 2.9364},
        {'id': 7, 'e_m': 1.998429, 'e_o_k': [1.146640, 0.917312, 0.733849], 'p_i': 40, 'u_i': 1.0429},
    ]
    B_BUDGET = 88.319990
    return processors, tasks, B_BUDGET
