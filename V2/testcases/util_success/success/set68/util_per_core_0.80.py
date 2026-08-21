"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360003, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360003, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.018169, 'e_o_k': [0.002234, 0.001787, 0.001430], 'p_i': 10, 'u_i': 3.5457},
        {'id': 1, 'e_m': 0.814383, 'e_o_k': [0.072678, 0.058143, 0.046514, 0.037211, 0.029769], 'p_i': 20, 'u_i': 2.0812},
        {'id': 2, 'e_m': 11.290924, 'e_o_k': [0.918140, 0.734512, 0.587610, 0.470088, 0.376070, 0.300856], 'p_i': 40, 'u_i': 3.4962},
        {'id': 3, 'e_m': 14.855601, 'e_o_k': [1.826508, 1.461207, 1.168965], 'p_i': 80, 'u_i': 3.6650},
        {'id': 4, 'e_m': 33.948650, 'e_o_k': [3.029687, 2.423749, 1.939000, 1.551200, 1.240960], 'p_i': 80, 'u_i': 4.9498},
        {'id': 5, 'e_m': 0.590224, 'e_o_k': [0.059982, 0.047986, 0.038389, 0.030711], 'p_i': 10, 'u_i': 3.9677},
        {'id': 6, 'e_m': 24.605097, 'e_o_k': [2.000805, 1.600644, 1.280515, 1.024412, 0.819530, 0.655624], 'p_i': 80, 'u_i': 3.6488},
        {'id': 7, 'e_m': 23.884124, 'e_o_k': [2.427248, 1.941799, 1.553439, 1.242751], 'p_i': 80, 'u_i': 3.0676},
    ]
    B_BUDGET = 191.360003
    return processors, tasks, B_BUDGET
