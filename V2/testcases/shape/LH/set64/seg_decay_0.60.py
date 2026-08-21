"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.721674, 'e_o_k': [0.438213, 0.262928, 0.157757, 0.094654, 0.056792], 'p_i': 10, 'u_i': 4.7302},
        {'id': 1, 'e_m': 2.496139, 'e_o_k': [2.184121, 1.310473], 'p_i': 20, 'u_i': 1.8342},
        {'id': 2, 'e_m': 0.886501, 'e_o_k': [0.633215, 0.379929, 0.227957], 'p_i': 40, 'u_i': 2.1428},
        {'id': 3, 'e_m': 2.410461, 'e_o_k': [1.550848, 0.930509, 0.558305, 0.334983], 'p_i': 80, 'u_i': 3.7337},
        {'id': 4, 'e_m': 2.948362, 'e_o_k': [1.790296, 1.074178, 0.644507, 0.386704, 0.232022], 'p_i': 40, 'u_i': 3.4112},
        {'id': 5, 'e_m': 4.596887, 'e_o_k': [4.022276, 2.413366], 'p_i': 80, 'u_i': 2.7179},
        {'id': 6, 'e_m': 0.004759, 'e_o_k': [0.003062, 0.001837, 0.001102, 0.000661], 'p_i': 40, 'u_i': 2.6898},
        {'id': 7, 'e_m': 0.388865, 'e_o_k': [0.277761, 0.166656, 0.099994], 'p_i': 20, 'u_i': 4.5690},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
