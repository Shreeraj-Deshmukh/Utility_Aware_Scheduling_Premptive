"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200005, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200005, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.318768, 'e_o_k': [0.530996, 0.424797, 0.339838], 'p_i': 10, 'u_i': 2.7456},
        {'id': 1, 'e_m': 4.121960, 'e_o_k': [0.506798, 0.405439, 0.324351], 'p_i': 20, 'u_i': 1.4781},
        {'id': 2, 'e_m': 8.837815, 'e_o_k': [0.718662, 0.574929, 0.459944, 0.367955, 0.294364, 0.235491], 'p_i': 40, 'u_i': 4.2271},
        {'id': 3, 'e_m': 10.140185, 'e_o_k': [1.030507, 0.824405, 0.659524, 0.527619], 'p_i': 80, 'u_i': 2.1613},
        {'id': 4, 'e_m': 2.433886, 'e_o_k': [0.247346, 0.197877, 0.158302, 0.126641], 'p_i': 10, 'u_i': 3.4475},
        {'id': 5, 'e_m': 3.113229, 'e_o_k': [0.518872, 0.415097], 'p_i': 10, 'u_i': 3.7603},
        {'id': 6, 'e_m': 4.421469, 'e_o_k': [0.543623, 0.434899, 0.347919], 'p_i': 10, 'u_i': 4.2692},
        {'id': 7, 'e_m': 0.698762, 'e_o_k': [0.116460, 0.093168], 'p_i': 40, 'u_i': 2.3975},
    ]
    B_BUDGET = 239.200005
    return processors, tasks, B_BUDGET
