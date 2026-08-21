"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.279536, 'e_o_k': [0.057282, 0.045826, 0.036660], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 0.807491, 'e_o_k': [0.165469, 0.132376, 0.105900], 'p_i': 20, 'u_i': 1.2645},
        {'id': 2, 'e_m': 3.179023, 'e_o_k': [0.651439, 0.521151, 0.416921], 'p_i': 40, 'u_i': 2.2756},
        {'id': 3, 'e_m': 7.775197, 'e_o_k': [1.593278, 1.274622, 1.019698], 'p_i': 80, 'u_i': 2.5093},
        {'id': 4, 'e_m': 0.001832, 'e_o_k': [0.000375, 0.000300, 0.000240], 'p_i': 10, 'u_i': 3.6510},
        {'id': 5, 'e_m': 1.937647, 'e_o_k': [0.397059, 0.317647, 0.254118], 'p_i': 80, 'u_i': 3.1983},
        {'id': 6, 'e_m': 0.361320, 'e_o_k': [0.074041, 0.059233, 0.047386], 'p_i': 10, 'u_i': 4.3627},
        {'id': 7, 'e_m': 3.778825, 'e_o_k': [0.774349, 0.619479, 0.495584], 'p_i': 40, 'u_i': 4.4103},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
