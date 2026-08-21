"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360015, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360015, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.455015, 'e_o_k': [0.424797, 0.339838, 0.271870], 'p_i': 10, 'u_i': 2.7456},
        {'id': 1, 'e_m': 3.297568, 'e_o_k': [0.405439, 0.324351, 0.259481], 'p_i': 20, 'u_i': 1.4781},
        {'id': 2, 'e_m': 7.070252, 'e_o_k': [0.574929, 0.459944, 0.367955, 0.294364, 0.235491, 0.188393], 'p_i': 40, 'u_i': 4.2271},
        {'id': 3, 'e_m': 8.112148, 'e_o_k': [0.824405, 0.659524, 0.527619, 0.422095], 'p_i': 80, 'u_i': 2.1613},
        {'id': 4, 'e_m': 1.947109, 'e_o_k': [0.197877, 0.158302, 0.126641, 0.101313], 'p_i': 10, 'u_i': 3.4475},
        {'id': 5, 'e_m': 2.490583, 'e_o_k': [0.415097, 0.332078], 'p_i': 10, 'u_i': 3.7603},
        {'id': 6, 'e_m': 3.537175, 'e_o_k': [0.434899, 0.347919, 0.278335], 'p_i': 10, 'u_i': 4.2692},
        {'id': 7, 'e_m': 0.559010, 'e_o_k': [0.093168, 0.074535], 'p_i': 40, 'u_i': 2.3975},
    ]
    B_BUDGET = 191.360015
    return processors, tasks, B_BUDGET
