"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199997, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199997, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.518196, 'e_o_k': [0.154288, 0.123431, 0.098744, 0.078996], 'p_i': 10, 'u_i': 1.7812},
        {'id': 1, 'e_m': 9.014497, 'e_o_k': [0.804483, 0.643586, 0.514869, 0.411895, 0.329516], 'p_i': 20, 'u_i': 3.4338},
        {'id': 2, 'e_m': 1.024179, 'e_o_k': [0.091401, 0.073121, 0.058497, 0.046797, 0.037438], 'p_i': 40, 'u_i': 1.4372},
        {'id': 3, 'e_m': 25.780570, 'e_o_k': [3.169742, 2.535794, 2.028635], 'p_i': 80, 'u_i': 1.0760},
        {'id': 4, 'e_m': 6.780451, 'e_o_k': [0.605109, 0.484087, 0.387270, 0.309816, 0.247853], 'p_i': 20, 'u_i': 3.9613},
        {'id': 5, 'e_m': 1.019247, 'e_o_k': [0.125317, 0.100254, 0.080203], 'p_i': 10, 'u_i': 4.3968},
        {'id': 6, 'e_m': 15.731920, 'e_o_k': [1.279267, 1.023414, 0.818731, 0.654985, 0.523988, 0.419190], 'p_i': 40, 'u_i': 1.2846},
        {'id': 7, 'e_m': 2.153487, 'e_o_k': [0.192184, 0.153747, 0.122998, 0.098398, 0.078719], 'p_i': 10, 'u_i': 3.8310},
    ]
    B_BUDGET = 239.199997
    return processors, tasks, B_BUDGET
