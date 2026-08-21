"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.44, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.44, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.416103, 'e_o_k': [0.037134, 0.029708, 0.023766, 0.019013, 0.015210], 'p_i': 10, 'u_i': 4.9795},
        {'id': 1, 'e_m': 4.030593, 'e_o_k': [0.495565, 0.396452, 0.317161], 'p_i': 20, 'u_i': 4.9448},
        {'id': 2, 'e_m': 13.243015, 'e_o_k': [1.181849, 0.945479, 0.756384, 0.605107, 0.484085], 'p_i': 40, 'u_i': 4.4554},
        {'id': 3, 'e_m': 35.162814, 'e_o_k': [3.138043, 2.510434, 2.008347, 1.606678, 1.285342], 'p_i': 80, 'u_i': 2.2591},
        {'id': 4, 'e_m': 0.384251, 'e_o_k': [0.047244, 0.037795, 0.030236], 'p_i': 10, 'u_i': 2.7803},
        {'id': 5, 'e_m': 17.451905, 'e_o_k': [1.419131, 1.135305, 0.908244, 0.726595, 0.581276, 0.465021], 'p_i': 80, 'u_i': 3.4160},
        {'id': 6, 'e_m': 5.437258, 'e_o_k': [0.668515, 0.534812, 0.427850], 'p_i': 80, 'u_i': 3.4712},
        {'id': 7, 'e_m': 1.234197, 'e_o_k': [0.110144, 0.088115, 0.070492, 0.056394, 0.045115], 'p_i': 20, 'u_i': 4.3322},
    ]
    B_BUDGET = 167.440000
    return processors, tasks, B_BUDGET
