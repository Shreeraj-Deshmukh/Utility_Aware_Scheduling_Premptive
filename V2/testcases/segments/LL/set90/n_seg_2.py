"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.427962, 'e_o_k': [0.118878, 0.095103], 'p_i': 10, 'u_i': 3.1824},
        {'id': 1, 'e_m': 1.031123, 'e_o_k': [0.286423, 0.229138], 'p_i': 20, 'u_i': 3.8670},
        {'id': 2, 'e_m': 0.898123, 'e_o_k': [0.249479, 0.199583], 'p_i': 40, 'u_i': 1.6834},
        {'id': 3, 'e_m': 0.364547, 'e_o_k': [0.101263, 0.081010], 'p_i': 80, 'u_i': 3.8684},
        {'id': 4, 'e_m': 1.110849, 'e_o_k': [0.308569, 0.246855], 'p_i': 40, 'u_i': 4.7513},
        {'id': 5, 'e_m': 6.962867, 'e_o_k': [1.934130, 1.547304], 'p_i': 40, 'u_i': 4.4932},
        {'id': 6, 'e_m': 2.975430, 'e_o_k': [0.826508, 0.661207], 'p_i': 40, 'u_i': 1.6064},
        {'id': 7, 'e_m': 0.024091, 'e_o_k': [0.006692, 0.005353], 'p_i': 10, 'u_i': 2.2133},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
