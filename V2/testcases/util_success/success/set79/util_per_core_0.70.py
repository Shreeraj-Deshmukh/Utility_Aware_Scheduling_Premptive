"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439998, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439998, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.190286, 'e_o_k': [0.106225, 0.084980, 0.067984, 0.054387, 0.043510], 'p_i': 10, 'u_i': 4.9110},
        {'id': 1, 'e_m': 2.957243, 'e_o_k': [0.240473, 0.192379, 0.153903, 0.123122, 0.098498, 0.078798], 'p_i': 20, 'u_i': 1.5555},
        {'id': 2, 'e_m': 0.909327, 'e_o_k': [0.111802, 0.089442, 0.071554], 'p_i': 40, 'u_i': 1.9189},
        {'id': 3, 'e_m': 31.665308, 'e_o_k': [5.277551, 4.222041], 'p_i': 80, 'u_i': 3.1608},
        {'id': 4, 'e_m': 8.767139, 'e_o_k': [1.461190, 1.168952], 'p_i': 80, 'u_i': 1.3239},
        {'id': 5, 'e_m': 3.422879, 'e_o_k': [0.347854, 0.278283, 0.222626, 0.178101], 'p_i': 80, 'u_i': 4.3282},
        {'id': 6, 'e_m': 18.813396, 'e_o_k': [3.135566, 2.508453], 'p_i': 40, 'u_i': 3.0285},
        {'id': 7, 'e_m': 7.347965, 'e_o_k': [0.746744, 0.597396, 0.477916, 0.382333], 'p_i': 80, 'u_i': 4.7214},
    ]
    B_BUDGET = 167.439998
    return processors, tasks, B_BUDGET
