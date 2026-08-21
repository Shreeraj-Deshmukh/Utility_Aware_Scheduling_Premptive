"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.559072, 'e_o_k': [0.339478, 0.203687, 0.122212, 0.073327, 0.043996], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 1.614981, 'e_o_k': [0.948650, 0.569190, 0.341514, 0.204908, 0.122945, 0.073767], 'p_i': 20, 'u_i': 1.1622},
        {'id': 2, 'e_m': 6.358045, 'e_o_k': [4.541461, 2.724877, 1.634926], 'p_i': 40, 'u_i': 4.1752},
        {'id': 3, 'e_m': 15.550394, 'e_o_k': [10.004849, 6.002909, 3.601746, 2.161047], 'p_i': 80, 'u_i': 1.9420},
        {'id': 4, 'e_m': 0.003664, 'e_o_k': [0.003206, 0.001923], 'p_i': 10, 'u_i': 2.5093},
        {'id': 5, 'e_m': 3.875294, 'e_o_k': [2.768067, 1.660840, 0.996504], 'p_i': 80, 'u_i': 3.6510},
        {'id': 6, 'e_m': 0.722639, 'e_o_k': [0.464933, 0.278960, 0.167376, 0.100426], 'p_i': 10, 'u_i': 3.1983},
        {'id': 7, 'e_m': 7.557649, 'e_o_k': [4.862458, 2.917475, 1.750485, 1.050291], 'p_i': 40, 'u_i': 4.3627},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET
