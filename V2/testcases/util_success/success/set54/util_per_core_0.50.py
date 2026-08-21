"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.60002, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.60002, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.575111, 'e_o_k': [0.316612, 0.253290, 0.202632], 'p_i': 10, 'u_i': 3.7892},
        {'id': 1, 'e_m': 0.423782, 'e_o_k': [0.043067, 0.034454, 0.027563, 0.022050], 'p_i': 20, 'u_i': 2.5683},
        {'id': 2, 'e_m': 19.808991, 'e_o_k': [2.013109, 1.610487, 1.288390, 1.030712], 'p_i': 40, 'u_i': 1.2577},
        {'id': 3, 'e_m': 2.203616, 'e_o_k': [0.196658, 0.157326, 0.125861, 0.100689, 0.080551], 'p_i': 80, 'u_i': 3.4086},
        {'id': 4, 'e_m': 0.981238, 'e_o_k': [0.120644, 0.096515, 0.077212], 'p_i': 40, 'u_i': 3.2935},
        {'id': 5, 'e_m': 1.018033, 'e_o_k': [0.103459, 0.082767, 0.066214, 0.052971], 'p_i': 10, 'u_i': 4.9988},
        {'id': 6, 'e_m': 0.206816, 'e_o_k': [0.018457, 0.014766, 0.011812, 0.009450, 0.007560], 'p_i': 20, 'u_i': 2.8879},
        {'id': 7, 'e_m': 1.237096, 'e_o_k': [0.125721, 0.100577, 0.080462, 0.064369], 'p_i': 20, 'u_i': 4.7528},
    ]
    B_BUDGET = 119.600020
    return processors, tasks, B_BUDGET
