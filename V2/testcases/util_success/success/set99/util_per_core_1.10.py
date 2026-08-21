"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119993, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119993, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.231552, 'e_o_k': [0.109908, 0.087926, 0.070341, 0.056273, 0.045018], 'p_i': 10, 'u_i': 1.3465},
        {'id': 1, 'e_m': 8.306481, 'e_o_k': [1.021289, 0.817031, 0.653625], 'p_i': 20, 'u_i': 2.7919},
        {'id': 2, 'e_m': 17.090237, 'e_o_k': [1.736813, 1.389450, 1.111560, 0.889248], 'p_i': 40, 'u_i': 4.9231},
        {'id': 3, 'e_m': 26.348713, 'e_o_k': [3.239596, 2.591677, 2.073341], 'p_i': 80, 'u_i': 3.9978},
        {'id': 4, 'e_m': 2.459126, 'e_o_k': [0.219460, 0.175568, 0.140455, 0.112364, 0.089891], 'p_i': 10, 'u_i': 3.4220},
        {'id': 5, 'e_m': 3.516127, 'e_o_k': [0.586021, 0.468817], 'p_i': 10, 'u_i': 1.4805},
        {'id': 6, 'e_m': 23.093041, 'e_o_k': [2.839308, 2.271447, 1.817157], 'p_i': 80, 'u_i': 2.3014},
        {'id': 7, 'e_m': 0.748699, 'e_o_k': [0.124783, 0.099827], 'p_i': 40, 'u_i': 3.2394},
    ]
    B_BUDGET = 263.119993
    return processors, tasks, B_BUDGET
