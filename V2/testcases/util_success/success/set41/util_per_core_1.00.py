"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199997, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199997, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.966526, 'e_o_k': [0.364737, 0.291789, 0.233432], 'p_i': 10, 'u_i': 3.2904},
        {'id': 1, 'e_m': 0.946882, 'e_o_k': [0.116420, 0.093136, 0.074509], 'p_i': 20, 'u_i': 1.8156},
        {'id': 2, 'e_m': 16.823639, 'e_o_k': [1.501396, 1.201117, 0.960893, 0.768715, 0.614972], 'p_i': 40, 'u_i': 1.9365},
        {'id': 3, 'e_m': 2.197555, 'e_o_k': [0.270191, 0.216153, 0.172922], 'p_i': 80, 'u_i': 2.3606},
        {'id': 4, 'e_m': 6.937803, 'e_o_k': [0.705061, 0.564049, 0.451239, 0.360991], 'p_i': 40, 'u_i': 2.6705},
        {'id': 5, 'e_m': 31.651361, 'e_o_k': [3.891561, 3.113249, 2.490599], 'p_i': 80, 'u_i': 4.9899},
        {'id': 6, 'e_m': 4.692372, 'e_o_k': [0.418762, 0.335010, 0.268008, 0.214406, 0.171525], 'p_i': 20, 'u_i': 3.2939},
        {'id': 7, 'e_m': 16.169486, 'e_o_k': [1.314849, 1.051879, 0.841503, 0.673203, 0.538562, 0.430850], 'p_i': 40, 'u_i': 2.4697},
    ]
    B_BUDGET = 239.199997
    return processors, tasks, B_BUDGET
