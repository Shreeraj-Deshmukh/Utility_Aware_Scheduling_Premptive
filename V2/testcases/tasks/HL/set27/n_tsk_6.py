"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.330983, 'e_o_k': [1.203051, 0.962441], 'p_i': 10, 'u_i': 4.6007},
        {'id': 1, 'e_m': 0.177947, 'e_o_k': [0.026468, 0.021174, 0.016939, 0.013551, 0.010841], 'p_i': 20, 'u_i': 4.4928},
        {'id': 2, 'e_m': 2.652215, 'e_o_k': [0.359449, 0.287559, 0.230047, 0.184038, 0.147230, 0.117784], 'p_i': 40, 'u_i': 4.0915},
        {'id': 3, 'e_m': 1.218905, 'e_o_k': [0.165195, 0.132156, 0.105725, 0.084580, 0.067664, 0.054131], 'p_i': 80, 'u_i': 4.3648},
        {'id': 4, 'e_m': 3.803019, 'e_o_k': [1.056394, 0.845115], 'p_i': 80, 'u_i': 3.7706},
        {'id': 5, 'e_m': 4.578499, 'e_o_k': [0.620514, 0.496411, 0.397129, 0.317703, 0.254162, 0.203330], 'p_i': 20, 'u_i': 4.9150},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
