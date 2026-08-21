"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280025, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280025, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.672491, 'e_o_k': [0.271595, 0.217276, 0.173821, 0.139056], 'p_i': 10, 'u_i': 4.7936},
        {'id': 1, 'e_m': 5.532936, 'e_o_k': [0.922156, 0.737725], 'p_i': 20, 'u_i': 3.8633},
        {'id': 2, 'e_m': 17.483199, 'e_o_k': [2.149574, 1.719659, 1.375727], 'p_i': 40, 'u_i': 3.6436},
        {'id': 3, 'e_m': 26.882109, 'e_o_k': [2.399046, 1.919237, 1.535389, 1.228312, 0.982649], 'p_i': 80, 'u_i': 2.9643},
        {'id': 4, 'e_m': 0.051955, 'e_o_k': [0.004637, 0.003709, 0.002967, 0.002374, 0.001899], 'p_i': 10, 'u_i': 2.7604},
        {'id': 5, 'e_m': 7.408265, 'e_o_k': [0.910852, 0.728682, 0.582945], 'p_i': 20, 'u_i': 2.8703},
        {'id': 6, 'e_m': 0.017494, 'e_o_k': [0.002151, 0.001721, 0.001377], 'p_i': 10, 'u_i': 2.8894},
        {'id': 7, 'e_m': 8.451180, 'e_o_k': [1.039079, 0.831264, 0.665011], 'p_i': 80, 'u_i': 1.0820},
    ]
    B_BUDGET = 215.280025
    return processors, tasks, B_BUDGET
