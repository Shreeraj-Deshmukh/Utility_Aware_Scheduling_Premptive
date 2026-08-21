"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759999, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759999, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.229970, 'e_o_k': [0.023371, 0.018697, 0.014957, 0.011966], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.222554, 'e_o_k': [0.018097, 0.014478, 0.011582, 0.009266, 0.007413, 0.005930], 'p_i': 20, 'u_i': 2.3478},
        {'id': 2, 'e_m': 3.405335, 'e_o_k': [0.418689, 0.334951, 0.267961], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 10.913516, 'e_o_k': [0.973957, 0.779166, 0.623333, 0.498666, 0.398933], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 4.020752, 'e_o_k': [0.670125, 0.536100], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 2.202159, 'e_o_k': [0.179072, 0.143258, 0.114606, 0.091685, 0.073348, 0.058678], 'p_i': 40, 'u_i': 2.1935},
        {'id': 6, 'e_m': 0.854822, 'e_o_k': [0.105101, 0.084081, 0.067265], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 0.454903, 'e_o_k': [0.075817, 0.060654], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 71.759999
    return processors, tasks, B_BUDGET
