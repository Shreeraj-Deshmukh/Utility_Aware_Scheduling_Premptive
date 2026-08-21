"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359994, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359994, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.422552, 'e_o_k': [0.570425, 0.456340], 'p_i': 10, 'u_i': 4.9296},
        {'id': 1, 'e_m': 4.285767, 'e_o_k': [0.348504, 0.278803, 0.223043, 0.178434, 0.142747, 0.114198], 'p_i': 20, 'u_i': 4.5772},
        {'id': 2, 'e_m': 12.882293, 'e_o_k': [1.149657, 0.919726, 0.735781, 0.588625, 0.470900], 'p_i': 40, 'u_i': 4.4816},
        {'id': 3, 'e_m': 15.557885, 'e_o_k': [1.581086, 1.264869, 1.011895, 0.809516], 'p_i': 80, 'u_i': 1.1432},
        {'id': 4, 'e_m': 2.417181, 'e_o_k': [0.245648, 0.196519, 0.157215, 0.125772], 'p_i': 20, 'u_i': 4.4630},
        {'id': 5, 'e_m': 2.106429, 'e_o_k': [0.214068, 0.171254, 0.137003, 0.109603], 'p_i': 10, 'u_i': 3.8428},
        {'id': 6, 'e_m': 2.096680, 'e_o_k': [0.187114, 0.149692, 0.119753, 0.095803, 0.076642], 'p_i': 20, 'u_i': 4.3035},
        {'id': 7, 'e_m': 1.811794, 'e_o_k': [0.147329, 0.117863, 0.094291, 0.075432, 0.060346, 0.048277], 'p_i': 20, 'u_i': 1.7239},
    ]
    B_BUDGET = 191.359994
    return processors, tasks, B_BUDGET
