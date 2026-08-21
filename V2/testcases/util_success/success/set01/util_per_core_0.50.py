"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599992, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599992, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.319552, 'e_o_k': [0.025985, 0.020788, 0.016630, 0.013304, 0.010643, 0.008515], 'p_i': 10, 'u_i': 4.5169},
        {'id': 1, 'e_m': 7.293670, 'e_o_k': [1.215612, 0.972489], 'p_i': 20, 'u_i': 3.9484},
        {'id': 2, 'e_m': 1.287537, 'e_o_k': [0.114904, 0.091923, 0.073539, 0.058831, 0.047065], 'p_i': 40, 'u_i': 3.8598},
        {'id': 3, 'e_m': 1.656297, 'e_o_k': [0.134685, 0.107748, 0.086198, 0.068958, 0.055167, 0.044133], 'p_i': 80, 'u_i': 3.9484},
        {'id': 4, 'e_m': 24.209845, 'e_o_k': [2.976620, 2.381296, 1.905037], 'p_i': 80, 'u_i': 4.6365},
        {'id': 5, 'e_m': 0.495732, 'e_o_k': [0.040311, 0.032249, 0.025799, 0.020639, 0.016511, 0.013209], 'p_i': 40, 'u_i': 4.7054},
        {'id': 6, 'e_m': 4.032910, 'e_o_k': [0.672152, 0.537721], 'p_i': 80, 'u_i': 3.2554},
        {'id': 7, 'e_m': 3.700828, 'e_o_k': [0.616805, 0.493444], 'p_i': 20, 'u_i': 3.5452},
    ]
    B_BUDGET = 119.599992
    return processors, tasks, B_BUDGET
