"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440011, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440011, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.698600, 'e_o_k': [0.151589, 0.121271, 0.097017, 0.077613, 0.062091], 'p_i': 10, 'u_i': 1.8657},
        {'id': 1, 'e_m': 5.115269, 'e_o_k': [0.456503, 0.365202, 0.292162, 0.233730, 0.186984], 'p_i': 20, 'u_i': 1.6547},
        {'id': 2, 'e_m': 1.942331, 'e_o_k': [0.197391, 0.157913, 0.126330, 0.101064], 'p_i': 40, 'u_i': 3.2690},
        {'id': 3, 'e_m': 6.385072, 'e_o_k': [0.785050, 0.628040, 0.502432], 'p_i': 80, 'u_i': 2.0883},
        {'id': 4, 'e_m': 1.811452, 'e_o_k': [0.222720, 0.178176, 0.142541], 'p_i': 10, 'u_i': 2.4453},
        {'id': 5, 'e_m': 17.719133, 'e_o_k': [1.581312, 1.265050, 1.012040, 0.809632, 0.647706], 'p_i': 40, 'u_i': 4.4841},
        {'id': 6, 'e_m': 8.560793, 'e_o_k': [1.052557, 0.842045, 0.673636], 'p_i': 40, 'u_i': 2.2759},
        {'id': 7, 'e_m': 0.628916, 'e_o_k': [0.104819, 0.083855], 'p_i': 80, 'u_i': 4.2544},
    ]
    B_BUDGET = 167.440011
    return processors, tasks, B_BUDGET
