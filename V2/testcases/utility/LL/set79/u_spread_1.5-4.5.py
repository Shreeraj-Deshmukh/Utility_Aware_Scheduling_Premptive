"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.20001, "H": 80, "J": 20, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 55.20001, "H": 80, "J": 20, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.340082, 'e_o_k': [0.050583, 0.040467, 0.032373, 0.025899, 0.020719], 'p_i': 10, 'u_i': 4.4332},
        {'id': 1, 'e_m': 0.844927, 'e_o_k': [0.114511, 0.091609, 0.073287, 0.058630, 0.046904, 0.037523], 'p_i': 20, 'u_i': 1.9166},
        {'id': 2, 'e_m': 0.259808, 'e_o_k': [0.053239, 0.042591, 0.034073], 'p_i': 40, 'u_i': 2.1892},
        {'id': 3, 'e_m': 9.047231, 'e_o_k': [2.513120, 2.010496], 'p_i': 80, 'u_i': 3.1206},
        {'id': 4, 'e_m': 2.504897, 'e_o_k': [0.695805, 0.556644], 'p_i': 80, 'u_i': 1.7429},
        {'id': 5, 'e_m': 0.977966, 'e_o_k': [0.165645, 0.132516, 0.106013, 0.084810], 'p_i': 80, 'u_i': 3.9961},
        {'id': 6, 'e_m': 5.375256, 'e_o_k': [1.493127, 1.194501], 'p_i': 40, 'u_i': 3.0214},
        {'id': 7, 'e_m': 2.099419, 'e_o_k': [0.355593, 0.284474, 0.227579, 0.182063], 'p_i': 80, 'u_i': 4.2911},
    ]
    B_BUDGET = 55.200010
    return processors, tasks, B_BUDGET
