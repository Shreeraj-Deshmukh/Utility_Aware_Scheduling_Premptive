"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.44001, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.44001, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.957162, 'e_o_k': [0.263907, 0.211125, 0.168900, 0.135120, 0.108096], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.621546, 'e_o_k': [0.103591, 0.082873], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 5.017401, 'e_o_k': [0.509898, 0.407919, 0.326335, 0.261068], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 6.121017, 'e_o_k': [1.020170, 0.816136], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 24.202612, 'e_o_k': [1.968076, 1.574461, 1.259569, 1.007655, 0.806124, 0.644899], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 5.427679, 'e_o_k': [0.551593, 0.441275, 0.353020, 0.282416], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.388992, 'e_o_k': [0.064832, 0.051866], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 5.168860, 'e_o_k': [0.420315, 0.336252, 0.269001, 0.215201, 0.172161, 0.137729], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 167.440010
    return processors, tasks, B_BUDGET
