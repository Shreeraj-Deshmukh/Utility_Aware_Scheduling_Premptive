"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.097167, 'e_o_k': [0.853352, 0.682682], 'p_i': 10, 'u_i': 1.7789},
        {'id': 1, 'e_m': 0.357025, 'e_o_k': [0.204850, 0.163880, 0.131104], 'p_i': 20, 'u_i': 1.0831},
        {'id': 2, 'e_m': 9.722762, 'e_o_k': [4.049223, 3.239378, 2.591502, 2.073202, 1.658562], 'p_i': 40, 'u_i': 3.5025},
        {'id': 3, 'e_m': 19.820506, 'e_o_k': [7.521443, 6.017154, 4.813723, 3.850979, 3.080783, 2.464626], 'p_i': 80, 'u_i': 3.4020},
        {'id': 4, 'e_m': 1.788974, 'e_o_k': [1.391424, 1.113139], 'p_i': 10, 'u_i': 4.4776},
        {'id': 5, 'e_m': 0.108372, 'e_o_k': [0.041125, 0.032900, 0.026320, 0.021056, 0.016845, 0.013476], 'p_i': 40, 'u_i': 3.0661},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
