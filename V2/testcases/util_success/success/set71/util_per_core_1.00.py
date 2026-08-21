"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199987, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199987, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.744030, 'e_o_k': [0.223135, 0.178508, 0.142807, 0.114245, 0.091396, 0.073117], 'p_i': 10, 'u_i': 1.2398},
        {'id': 1, 'e_m': 3.494836, 'e_o_k': [0.355166, 0.284133, 0.227306, 0.181845], 'p_i': 20, 'u_i': 1.6455},
        {'id': 2, 'e_m': 6.075704, 'e_o_k': [0.617450, 0.493960, 0.395168, 0.316134], 'p_i': 40, 'u_i': 1.3745},
        {'id': 3, 'e_m': 4.511798, 'e_o_k': [0.554729, 0.443783, 0.355027], 'p_i': 80, 'u_i': 1.5038},
        {'id': 4, 'e_m': 4.799374, 'e_o_k': [0.590087, 0.472070, 0.377656], 'p_i': 10, 'u_i': 4.4242},
        {'id': 5, 'e_m': 4.336257, 'e_o_k': [0.722709, 0.578168], 'p_i': 10, 'u_i': 1.3856},
        {'id': 6, 'e_m': 6.335652, 'e_o_k': [1.055942, 0.844754], 'p_i': 40, 'u_i': 2.4453},
        {'id': 7, 'e_m': 10.824427, 'e_o_k': [0.966007, 0.772805, 0.618244, 0.494595, 0.395676], 'p_i': 40, 'u_i': 2.4405},
    ]
    B_BUDGET = 239.199987
    return processors, tasks, B_BUDGET
