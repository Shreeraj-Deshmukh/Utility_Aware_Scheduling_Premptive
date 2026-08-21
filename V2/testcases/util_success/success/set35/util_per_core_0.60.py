"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520014, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520014, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.459940, 'e_o_k': [0.046742, 0.037393, 0.029915, 0.023932], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.445107, 'e_o_k': [0.036195, 0.028956, 0.023165, 0.018532, 0.014825, 0.011860], 'p_i': 20, 'u_i': 2.3478},
        {'id': 2, 'e_m': 6.810670, 'e_o_k': [0.837377, 0.669902, 0.535922], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 21.827032, 'e_o_k': [1.947915, 1.558332, 1.246665, 0.997332, 0.797866], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 8.041505, 'e_o_k': [1.340251, 1.072201], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 4.404317, 'e_o_k': [0.358144, 0.286516, 0.229212, 0.183370, 0.146696, 0.117357], 'p_i': 40, 'u_i': 2.1935},
        {'id': 6, 'e_m': 1.709644, 'e_o_k': [0.210202, 0.168162, 0.134529], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 0.909807, 'e_o_k': [0.151634, 0.121308], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 143.520014
    return processors, tasks, B_BUDGET
