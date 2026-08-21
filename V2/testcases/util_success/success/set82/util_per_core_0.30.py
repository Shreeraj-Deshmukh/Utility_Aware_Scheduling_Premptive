"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760003, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760003, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.267355, 'e_o_k': [0.113103, 0.090482, 0.072386, 0.057909, 0.046327], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.266377, 'e_o_k': [0.044396, 0.035517], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 2.150315, 'e_o_k': [0.218528, 0.174822, 0.139858, 0.111886], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 2.623293, 'e_o_k': [0.437216, 0.349772], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 10.372548, 'e_o_k': [0.843461, 0.674769, 0.539815, 0.431852, 0.345482, 0.276385], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 2.326148, 'e_o_k': [0.236397, 0.189118, 0.151294, 0.121035], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.166711, 'e_o_k': [0.027785, 0.022228], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 2.215226, 'e_o_k': [0.180135, 0.144108, 0.115286, 0.092229, 0.073783, 0.059027], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 71.760003
    return processors, tasks, B_BUDGET
