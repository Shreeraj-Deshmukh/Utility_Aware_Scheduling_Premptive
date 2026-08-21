"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439998, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439998, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.627073, 'e_o_k': [0.132308, 0.105847, 0.084677, 0.067742, 0.054193, 0.043355], 'p_i': 10, 'u_i': 2.4783},
        {'id': 1, 'e_m': 0.099536, 'e_o_k': [0.008094, 0.006475, 0.005180, 0.004144, 0.003315, 0.002652], 'p_i': 20, 'u_i': 1.9438},
        {'id': 2, 'e_m': 4.591989, 'e_o_k': [0.765332, 0.612265], 'p_i': 40, 'u_i': 1.5728},
        {'id': 3, 'e_m': 7.830677, 'e_o_k': [1.305113, 1.044090], 'p_i': 80, 'u_i': 1.5110},
        {'id': 4, 'e_m': 4.111919, 'e_o_k': [0.685320, 0.548256], 'p_i': 20, 'u_i': 4.3454},
        {'id': 5, 'e_m': 18.450230, 'e_o_k': [1.875023, 1.500019, 1.200015, 0.960012], 'p_i': 40, 'u_i': 2.7253},
        {'id': 6, 'e_m': 0.599298, 'e_o_k': [0.099883, 0.079906], 'p_i': 10, 'u_i': 1.4714},
        {'id': 7, 'e_m': 5.857024, 'e_o_k': [0.976171, 0.780937], 'p_i': 20, 'u_i': 2.9160},
    ]
    B_BUDGET = 167.439998
    return processors, tasks, B_BUDGET
