"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759997, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759997, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.366330, 'e_o_k': [0.061055, 0.048844], 'p_i': 10, 'u_i': 1.2408},
        {'id': 1, 'e_m': 0.693492, 'e_o_k': [0.070477, 0.056381, 0.045105, 0.036084], 'p_i': 20, 'u_i': 2.7274},
        {'id': 2, 'e_m': 1.716245, 'e_o_k': [0.153163, 0.122531, 0.098024, 0.078420, 0.062736], 'p_i': 40, 'u_i': 3.7398},
        {'id': 3, 'e_m': 3.492908, 'e_o_k': [0.429456, 0.343565, 0.274852], 'p_i': 80, 'u_i': 1.4758},
        {'id': 4, 'e_m': 0.108576, 'e_o_k': [0.008829, 0.007063, 0.005651, 0.004520, 0.003616, 0.002893], 'p_i': 10, 'u_i': 1.9890},
        {'id': 5, 'e_m': 0.105716, 'e_o_k': [0.012998, 0.010398, 0.008319], 'p_i': 40, 'u_i': 1.7667},
        {'id': 6, 'e_m': 3.693505, 'e_o_k': [0.454119, 0.363296, 0.290636], 'p_i': 20, 'u_i': 2.7743},
        {'id': 7, 'e_m': 2.439492, 'e_o_k': [0.247916, 0.198333, 0.158666, 0.126933], 'p_i': 10, 'u_i': 3.3191},
    ]
    B_BUDGET = 71.759997
    return processors, tasks, B_BUDGET
