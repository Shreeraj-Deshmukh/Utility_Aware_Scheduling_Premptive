"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 24, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 24, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.721674, 'e_o_k': [0.300554, 0.240444, 0.192355, 0.153884, 0.123107], 'p_i': 10, 'u_i': 3.4325},
        {'id': 1, 'e_m': 2.496139, 'e_o_k': [1.941441, 1.553153], 'p_i': 20, 'u_i': 2.7085},
        {'id': 2, 'e_m': 0.886501, 'e_o_k': [0.508648, 0.406918, 0.325535], 'p_i': 40, 'u_i': 2.7857},
        {'id': 3, 'e_m': 2.410461, 'e_o_k': [1.143173, 0.914538, 0.731630, 0.585304], 'p_i': 80, 'u_i': 3.1834},
        {'id': 4, 'e_m': 2.948362, 'e_o_k': [1.227899, 0.982320, 0.785856, 0.628685, 0.502948], 'p_i': 40, 'u_i': 3.1028},
        {'id': 5, 'e_m': 4.596887, 'e_o_k': [3.575357, 2.860285], 'p_i': 80, 'u_i': 2.9295},
        {'id': 6, 'e_m': 0.004759, 'e_o_k': [0.002257, 0.001806, 0.001445, 0.001156], 'p_i': 40, 'u_i': 2.9225},
        {'id': 7, 'e_m': 0.388865, 'e_o_k': [0.223119, 0.178495, 0.142796], 'p_i': 20, 'u_i': 3.3922},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
