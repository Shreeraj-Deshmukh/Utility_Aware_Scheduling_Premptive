"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759999, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759999, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.936902, 'e_o_k': [0.115193, 0.092154, 0.073723], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 0.916341, 'e_o_k': [0.152723, 0.122179], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 4.632472, 'e_o_k': [0.470780, 0.376624, 0.301299, 0.241039], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 6.070228, 'e_o_k': [1.011705, 0.809364], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 0.556563, 'e_o_k': [0.049669, 0.039736, 0.031788, 0.025431, 0.020345], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 4.873082, 'e_o_k': [0.396263, 0.317010, 0.253608, 0.202887, 0.162309, 0.129847], 'p_i': 40, 'u_i': 3.0218},
        {'id': 6, 'e_m': 0.567112, 'e_o_k': [0.050611, 0.040489, 0.032391, 0.025913, 0.020730], 'p_i': 20, 'u_i': 2.6468},
        {'id': 7, 'e_m': 8.376513, 'e_o_k': [0.681150, 0.544920, 0.435936, 0.348749, 0.278999, 0.223199], 'p_i': 80, 'u_i': 1.1768},
    ]
    B_BUDGET = 71.759999
    return processors, tasks, B_BUDGET
