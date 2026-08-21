"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.106037, 'e_o_k': [0.307233, 0.245786], 'p_i': 10, 'u_i': 4.4310},
        {'id': 1, 'e_m': 1.049824, 'e_o_k': [0.291618, 0.233294], 'p_i': 20, 'u_i': 4.5357},
        {'id': 2, 'e_m': 0.127751, 'e_o_k': [0.035486, 0.028389], 'p_i': 40, 'u_i': 3.5135},
        {'id': 3, 'e_m': 3.081106, 'e_o_k': [0.855863, 0.684690], 'p_i': 80, 'u_i': 3.8723},
        {'id': 4, 'e_m': 1.628628, 'e_o_k': [0.452397, 0.361917], 'p_i': 80, 'u_i': 1.1816},
        {'id': 5, 'e_m': 0.896350, 'e_o_k': [0.248986, 0.199189], 'p_i': 40, 'u_i': 3.3631},
        {'id': 6, 'e_m': 7.298706, 'e_o_k': [2.027418, 1.621935], 'p_i': 80, 'u_i': 2.0216},
        {'id': 7, 'e_m': 0.611971, 'e_o_k': [0.169992, 0.135993], 'p_i': 10, 'u_i': 3.3728},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET
