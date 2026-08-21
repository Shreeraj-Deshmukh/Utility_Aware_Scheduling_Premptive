"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.713852, 'e_o_k': [0.149757, 0.089854, 0.053913, 0.032348, 0.019409, 0.011645], 'p_i': 10, 'u_i': 4.1639},
        {'id': 1, 'e_m': 0.102835, 'e_o_k': [0.023629, 0.014178, 0.008507, 0.005104], 'p_i': 20, 'u_i': 2.0315},
        {'id': 2, 'e_m': 5.612205, 'e_o_k': [1.217081, 0.730249, 0.438149, 0.262890, 0.157734], 'p_i': 40, 'u_i': 1.5871},
        {'id': 3, 'e_m': 3.855748, 'e_o_k': [1.204921, 0.722953], 'p_i': 80, 'u_i': 1.8711},
        {'id': 4, 'e_m': 0.273644, 'e_o_k': [0.085514, 0.051308], 'p_i': 20, 'u_i': 4.9538},
        {'id': 5, 'e_m': 4.043450, 'e_o_k': [0.876876, 0.526126, 0.315675, 0.189405, 0.113643], 'p_i': 10, 'u_i': 2.3994},
        {'id': 6, 'e_m': 1.584227, 'e_o_k': [0.495071, 0.297043], 'p_i': 40, 'u_i': 1.5904},
        {'id': 7, 'e_m': 0.773382, 'e_o_k': [0.197291, 0.118375, 0.071025], 'p_i': 10, 'u_i': 2.4893},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
