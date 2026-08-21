"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439994, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439994, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.801912, 'e_o_k': [0.071565, 0.057252, 0.045802, 0.036641, 0.029313], 'p_i': 10, 'u_i': 1.3802},
        {'id': 1, 'e_m': 2.972580, 'e_o_k': [0.365481, 0.292385, 0.233908], 'p_i': 20, 'u_i': 1.3476},
        {'id': 2, 'e_m': 4.942747, 'e_o_k': [0.823791, 0.659033], 'p_i': 40, 'u_i': 4.5157},
        {'id': 3, 'e_m': 20.584091, 'e_o_k': [2.530831, 2.024665, 1.619732], 'p_i': 80, 'u_i': 4.4957},
        {'id': 4, 'e_m': 0.544460, 'e_o_k': [0.044274, 0.035419, 0.028335, 0.022668, 0.018135, 0.014508], 'p_i': 10, 'u_i': 4.5672},
        {'id': 5, 'e_m': 2.964192, 'e_o_k': [0.301239, 0.240991, 0.192793, 0.154234], 'p_i': 40, 'u_i': 4.7861},
        {'id': 6, 'e_m': 2.244340, 'e_o_k': [0.182502, 0.146002, 0.116801, 0.093441, 0.074753, 0.059802], 'p_i': 10, 'u_i': 1.1886},
        {'id': 7, 'e_m': 17.493007, 'e_o_k': [1.777745, 1.422196, 1.137757, 0.910205], 'p_i': 40, 'u_i': 4.3925},
    ]
    B_BUDGET = 167.439994
    return processors, tasks, B_BUDGET
