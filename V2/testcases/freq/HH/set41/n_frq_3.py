"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 25, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "freq", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 25, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "freq", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.7, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.7, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.878081, 'e_o_k': [0.503817, 0.403054, 0.322443], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 1.760389, 'e_o_k': [0.668029, 0.534423, 0.427538, 0.342031, 0.273624, 0.218900], 'p_i': 20, 'u_i': 3.7145},
        {'id': 2, 'e_m': 15.213605, 'e_o_k': [11.832804, 9.466243], 'p_i': 40, 'u_i': 2.6488},
        {'id': 3, 'e_m': 1.221415, 'e_o_k': [0.463500, 0.370800, 0.296640, 0.237312, 0.189850, 0.151880], 'p_i': 80, 'u_i': 4.3024},
        {'id': 4, 'e_m': 1.867670, 'e_o_k': [1.071614, 0.857291, 0.685833], 'p_i': 20, 'u_i': 4.8206},
        {'id': 5, 'e_m': 1.951144, 'e_o_k': [0.740416, 0.592333, 0.473866, 0.379093, 0.303274, 0.242619], 'p_i': 20, 'u_i': 3.2508},
        {'id': 6, 'e_m': 1.842208, 'e_o_k': [1.057004, 0.845604, 0.676483], 'p_i': 80, 'u_i': 3.3334},
        {'id': 7, 'e_m': 1.167704, 'e_o_k': [0.908214, 0.726572], 'p_i': 80, 'u_i': 2.1081},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
