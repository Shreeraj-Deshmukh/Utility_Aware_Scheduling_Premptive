"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359995, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359995, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.195224, 'e_o_k': [0.178508, 0.142807, 0.114245, 0.091396, 0.073117, 0.058494], 'p_i': 10, 'u_i': 1.2398},
        {'id': 1, 'e_m': 2.795869, 'e_o_k': [0.284133, 0.227306, 0.181845, 0.145476], 'p_i': 20, 'u_i': 1.6455},
        {'id': 2, 'e_m': 4.860563, 'e_o_k': [0.493960, 0.395168, 0.316134, 0.252907], 'p_i': 40, 'u_i': 1.3745},
        {'id': 3, 'e_m': 3.609439, 'e_o_k': [0.443783, 0.355027, 0.284021], 'p_i': 80, 'u_i': 1.5038},
        {'id': 4, 'e_m': 3.839499, 'e_o_k': [0.472070, 0.377656, 0.302125], 'p_i': 10, 'u_i': 4.4242},
        {'id': 5, 'e_m': 3.469005, 'e_o_k': [0.578168, 0.462534], 'p_i': 10, 'u_i': 1.3856},
        {'id': 6, 'e_m': 5.068521, 'e_o_k': [0.844754, 0.675803], 'p_i': 40, 'u_i': 2.4453},
        {'id': 7, 'e_m': 8.659542, 'e_o_k': [0.772805, 0.618244, 0.494595, 0.395676, 0.316541], 'p_i': 40, 'u_i': 2.4405},
    ]
    B_BUDGET = 191.359995
    return processors, tasks, B_BUDGET
