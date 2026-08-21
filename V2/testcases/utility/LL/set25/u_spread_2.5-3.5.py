"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200003, "H": 80, "J": 31, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 55.200003, "H": 80, "J": 31, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.799720, 'e_o_k': [0.222144, 0.177716], 'p_i': 10, 'u_i': 2.8385},
        {'id': 1, 'e_m': 2.592762, 'e_o_k': [0.531304, 0.425043, 0.340034], 'p_i': 20, 'u_i': 3.3989},
        {'id': 2, 'e_m': 1.461112, 'e_o_k': [0.247478, 0.197983, 0.158386, 0.126709], 'p_i': 40, 'u_i': 3.2511},
        {'id': 3, 'e_m': 3.792245, 'e_o_k': [1.053401, 0.842721], 'p_i': 80, 'u_i': 2.6132},
        {'id': 4, 'e_m': 0.519494, 'e_o_k': [0.070406, 0.056325, 0.045060, 0.036048, 0.028838, 0.023071], 'p_i': 40, 'u_i': 3.4895},
        {'id': 5, 'e_m': 0.710845, 'e_o_k': [0.096339, 0.077071, 0.061657, 0.049326, 0.039461, 0.031568], 'p_i': 20, 'u_i': 2.7700},
        {'id': 6, 'e_m': 1.584893, 'e_o_k': [0.440248, 0.352199], 'p_i': 40, 'u_i': 2.5616},
        {'id': 7, 'e_m': 0.183071, 'e_o_k': [0.037515, 0.030012, 0.024009], 'p_i': 10, 'u_i': 3.1826},
    ]
    B_BUDGET = 55.200003
    return processors, tasks, B_BUDGET
