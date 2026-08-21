"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.28002, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.28002, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.469627, 'e_o_k': [0.200822, 0.160658, 0.128526, 0.102821, 0.082257, 0.065805], 'p_i': 10, 'u_i': 1.2398},
        {'id': 1, 'e_m': 3.145353, 'e_o_k': [0.319650, 0.255720, 0.204576, 0.163661], 'p_i': 20, 'u_i': 1.6455},
        {'id': 2, 'e_m': 5.468134, 'e_o_k': [0.555705, 0.444564, 0.355651, 0.284521], 'p_i': 40, 'u_i': 1.3745},
        {'id': 3, 'e_m': 4.060618, 'e_o_k': [0.499256, 0.399405, 0.319524], 'p_i': 80, 'u_i': 1.5038},
        {'id': 4, 'e_m': 4.319437, 'e_o_k': [0.531078, 0.424863, 0.339890], 'p_i': 10, 'u_i': 4.4242},
        {'id': 5, 'e_m': 3.902631, 'e_o_k': [0.650439, 0.520351], 'p_i': 10, 'u_i': 1.3856},
        {'id': 6, 'e_m': 5.702086, 'e_o_k': [0.950348, 0.760278], 'p_i': 40, 'u_i': 2.4453},
        {'id': 7, 'e_m': 9.741984, 'e_o_k': [0.869406, 0.695525, 0.556420, 0.445136, 0.356109], 'p_i': 40, 'u_i': 2.4405},
    ]
    B_BUDGET = 215.280020
    return processors, tasks, B_BUDGET
