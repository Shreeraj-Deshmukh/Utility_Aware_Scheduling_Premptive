"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759989, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759989, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.001394, 'e_o_k': [0.000232, 0.000186], 'p_i': 10, 'u_i': 1.4564},
        {'id': 1, 'e_m': 0.772659, 'e_o_k': [0.078522, 0.062818, 0.050254, 0.040203], 'p_i': 20, 'u_i': 1.4719},
        {'id': 2, 'e_m': 0.374980, 'e_o_k': [0.046104, 0.036883, 0.029507], 'p_i': 40, 'u_i': 1.0831},
        {'id': 3, 'e_m': 2.477859, 'e_o_k': [0.221132, 0.176906, 0.141525, 0.113220, 0.090576], 'p_i': 80, 'u_i': 3.5025},
        {'id': 4, 'e_m': 12.574266, 'e_o_k': [1.022498, 0.817998, 0.654398, 0.523519, 0.418815, 0.335052], 'p_i': 40, 'u_i': 3.4020},
        {'id': 5, 'e_m': 1.273911, 'e_o_k': [0.212319, 0.169855], 'p_i': 20, 'u_i': 4.4776},
        {'id': 6, 'e_m': 0.142112, 'e_o_k': [0.011556, 0.009245, 0.007396, 0.005917, 0.004733, 0.003787], 'p_i': 10, 'u_i': 3.0661},
        {'id': 7, 'e_m': 1.286164, 'e_o_k': [0.104587, 0.083669, 0.066935, 0.053548, 0.042839, 0.034271], 'p_i': 10, 'u_i': 2.9486},
    ]
    B_BUDGET = 71.759989
    return processors, tasks, B_BUDGET
