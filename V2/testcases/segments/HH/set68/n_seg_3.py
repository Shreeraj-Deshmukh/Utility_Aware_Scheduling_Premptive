"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64002, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.64002, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.930633, 'e_o_k': [0.533970, 0.427176, 0.341741], 'p_i': 10, 'u_i': 3.1458},
        {'id': 1, 'e_m': 3.264279, 'e_o_k': [1.872947, 1.498357, 1.198686], 'p_i': 20, 'u_i': 4.9683},
        {'id': 2, 'e_m': 2.777130, 'e_o_k': [1.593435, 1.274748, 1.019798], 'p_i': 40, 'u_i': 2.4718},
        {'id': 3, 'e_m': 8.264281, 'e_o_k': [4.741801, 3.793441, 3.034752], 'p_i': 80, 'u_i': 3.8875},
        {'id': 4, 'e_m': 2.998873, 'e_o_k': [1.720665, 1.376532, 1.101226], 'p_i': 80, 'u_i': 3.3599},
        {'id': 5, 'e_m': 0.395365, 'e_o_k': [0.226849, 0.181479, 0.145183], 'p_i': 40, 'u_i': 3.9269},
        {'id': 6, 'e_m': 2.545753, 'e_o_k': [1.460678, 1.168542, 0.934834], 'p_i': 10, 'u_i': 3.4836},
        {'id': 7, 'e_m': 2.761829, 'e_o_k': [1.584656, 1.267725, 1.014180], 'p_i': 40, 'u_i': 2.8974},
    ]
    B_BUDGET = 176.640020
    return processors, tasks, B_BUDGET
