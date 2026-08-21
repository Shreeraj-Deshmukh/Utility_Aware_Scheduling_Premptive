"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360007, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360007, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.147402, 'e_o_k': [0.280884, 0.224707, 0.179766, 0.143813, 0.115050], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 2.977407, 'e_o_k': [0.242113, 0.193690, 0.154952, 0.123962, 0.099169, 0.079336], 'p_i': 20, 'u_i': 1.3163},
        {'id': 2, 'e_m': 2.272180, 'e_o_k': [0.230913, 0.184730, 0.147784, 0.118227], 'p_i': 40, 'u_i': 1.2768},
        {'id': 3, 'e_m': 27.506279, 'e_o_k': [3.381920, 2.705536, 2.164429], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 11.964758, 'e_o_k': [1.471077, 1.176861, 0.941489], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 1.348023, 'e_o_k': [0.120302, 0.096242, 0.076993, 0.061595, 0.049276], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 1.775668, 'e_o_k': [0.295945, 0.236756], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 20.595481, 'e_o_k': [1.838007, 1.470406, 1.176324, 0.941060, 0.752848], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 191.360007
    return processors, tasks, B_BUDGET
