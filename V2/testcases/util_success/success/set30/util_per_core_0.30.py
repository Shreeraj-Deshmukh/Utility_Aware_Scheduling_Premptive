"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759985, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759985, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.036767, 'e_o_k': [0.004520, 0.003616, 0.002893], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 1.582052, 'e_o_k': [0.128647, 0.102918, 0.082334, 0.065867, 0.052694, 0.042155], 'p_i': 20, 'u_i': 1.5905},
        {'id': 2, 'e_m': 2.022860, 'e_o_k': [0.337143, 0.269715], 'p_i': 40, 'u_i': 4.0467},
        {'id': 3, 'e_m': 3.744734, 'e_o_k': [0.380562, 0.304450, 0.243560, 0.194848], 'p_i': 80, 'u_i': 4.3793},
        {'id': 4, 'e_m': 14.324660, 'e_o_k': [1.455758, 1.164607, 0.931685, 0.745348], 'p_i': 80, 'u_i': 2.7000},
        {'id': 5, 'e_m': 0.062240, 'e_o_k': [0.006325, 0.005060, 0.004048, 0.003238], 'p_i': 10, 'u_i': 2.7208},
        {'id': 6, 'e_m': 1.094055, 'e_o_k': [0.111184, 0.088948, 0.071158, 0.056926], 'p_i': 80, 'u_i': 2.5904},
        {'id': 7, 'e_m': 4.417643, 'e_o_k': [0.543153, 0.434522, 0.347618], 'p_i': 20, 'u_i': 1.1735},
    ]
    B_BUDGET = 71.759985
    return processors, tasks, B_BUDGET
