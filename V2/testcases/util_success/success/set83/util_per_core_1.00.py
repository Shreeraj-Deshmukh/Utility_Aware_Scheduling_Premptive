"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199995, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199995, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.934252, 'e_o_k': [0.351105, 0.280884, 0.224707, 0.179766, 0.143813], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 3.721759, 'e_o_k': [0.302641, 0.242113, 0.193690, 0.154952, 0.123962, 0.099169], 'p_i': 20, 'u_i': 1.3163},
        {'id': 2, 'e_m': 2.840225, 'e_o_k': [0.288641, 0.230913, 0.184730, 0.147784], 'p_i': 40, 'u_i': 1.2768},
        {'id': 3, 'e_m': 34.382849, 'e_o_k': [4.227399, 3.381920, 2.705536], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 14.955947, 'e_o_k': [1.838846, 1.471077, 1.176861], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 1.685029, 'e_o_k': [0.150377, 0.120302, 0.096242, 0.076993, 0.061595], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 2.219585, 'e_o_k': [0.369931, 0.295945], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 25.744352, 'e_o_k': [2.297509, 1.838007, 1.470406, 1.176324, 0.941060], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 239.199995
    return processors, tasks, B_BUDGET
