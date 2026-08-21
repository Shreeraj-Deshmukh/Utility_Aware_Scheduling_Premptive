"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280007, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280007, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.182618, 'e_o_k': [0.120185, 0.096148, 0.076918, 0.061535], 'p_i': 10, 'u_i': 2.0211},
        {'id': 1, 'e_m': 3.905370, 'e_o_k': [0.480168, 0.384135, 0.307308], 'p_i': 20, 'u_i': 3.1521},
        {'id': 2, 'e_m': 1.554592, 'e_o_k': [0.126414, 0.101131, 0.080905, 0.064724, 0.051779, 0.041423], 'p_i': 40, 'u_i': 4.6880},
        {'id': 3, 'e_m': 22.544520, 'e_o_k': [1.833245, 1.466596, 1.173277, 0.938622, 0.750897, 0.600718], 'p_i': 80, 'u_i': 3.7723},
        {'id': 4, 'e_m': 4.566447, 'e_o_k': [0.761074, 0.608860], 'p_i': 20, 'u_i': 2.0383},
        {'id': 5, 'e_m': 35.253867, 'e_o_k': [3.582710, 2.866168, 2.292934, 1.834348], 'p_i': 80, 'u_i': 4.5751},
        {'id': 6, 'e_m': 8.698655, 'e_o_k': [1.449776, 1.159821], 'p_i': 20, 'u_i': 3.4615},
        {'id': 7, 'e_m': 0.618700, 'e_o_k': [0.050311, 0.040248, 0.032199, 0.025759, 0.020607, 0.016486], 'p_i': 10, 'u_i': 4.4330},
    ]
    B_BUDGET = 215.280007
    return processors, tasks, B_BUDGET
