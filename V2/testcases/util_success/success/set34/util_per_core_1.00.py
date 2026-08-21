"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199987, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199987, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.278189, 'e_o_k': [0.713032, 0.570425], 'p_i': 10, 'u_i': 4.9296},
        {'id': 1, 'e_m': 5.357209, 'e_o_k': [0.435630, 0.348504, 0.278803, 0.223043, 0.178434, 0.142747], 'p_i': 20, 'u_i': 4.5772},
        {'id': 2, 'e_m': 16.102866, 'e_o_k': [1.437072, 1.149657, 0.919726, 0.735781, 0.588625], 'p_i': 40, 'u_i': 4.4816},
        {'id': 3, 'e_m': 19.447356, 'e_o_k': [1.976357, 1.581086, 1.264869, 1.011895], 'p_i': 80, 'u_i': 1.1432},
        {'id': 4, 'e_m': 3.021476, 'e_o_k': [0.307061, 0.245648, 0.196519, 0.157215], 'p_i': 20, 'u_i': 4.4630},
        {'id': 5, 'e_m': 2.633036, 'e_o_k': [0.267585, 0.214068, 0.171254, 0.137003], 'p_i': 10, 'u_i': 3.8428},
        {'id': 6, 'e_m': 2.620850, 'e_o_k': [0.233893, 0.187114, 0.149692, 0.119753, 0.095803], 'p_i': 20, 'u_i': 4.3035},
        {'id': 7, 'e_m': 2.264743, 'e_o_k': [0.184161, 0.147329, 0.117863, 0.094291, 0.075432, 0.060346], 'p_i': 20, 'u_i': 1.7239},
    ]
    B_BUDGET = 239.199987
    return processors, tasks, B_BUDGET
