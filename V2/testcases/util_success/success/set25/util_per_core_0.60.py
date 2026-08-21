"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519999, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519999, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.399160, 'e_o_k': [0.399860, 0.319888], 'p_i': 10, 'u_i': 2.3541},
        {'id': 1, 'e_m': 7.778285, 'e_o_k': [0.956346, 0.765077, 0.612062], 'p_i': 20, 'u_i': 4.5958},
        {'id': 2, 'e_m': 4.383336, 'e_o_k': [0.445461, 0.356369, 0.285095, 0.228076], 'p_i': 40, 'u_i': 4.0042},
        {'id': 3, 'e_m': 11.376736, 'e_o_k': [1.896123, 1.516898], 'p_i': 80, 'u_i': 1.4529},
        {'id': 4, 'e_m': 1.558481, 'e_o_k': [0.126730, 0.101384, 0.081107, 0.064886, 0.051909, 0.041527], 'p_i': 40, 'u_i': 4.9580},
        {'id': 5, 'e_m': 2.132535, 'e_o_k': [0.173411, 0.138729, 0.110983, 0.088786, 0.071029, 0.056823], 'p_i': 20, 'u_i': 2.0799},
        {'id': 6, 'e_m': 4.754680, 'e_o_k': [0.792447, 0.633957], 'p_i': 40, 'u_i': 1.2465},
        {'id': 7, 'e_m': 0.549214, 'e_o_k': [0.067526, 0.054021, 0.043217], 'p_i': 10, 'u_i': 3.7304},
    ]
    B_BUDGET = 143.519999
    return processors, tasks, B_BUDGET
