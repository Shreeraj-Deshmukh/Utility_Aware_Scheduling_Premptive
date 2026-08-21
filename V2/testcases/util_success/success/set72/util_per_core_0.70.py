"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440006, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440006, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.403269, 'e_o_k': [0.032793, 0.026234, 0.020987, 0.016790, 0.013432, 0.010745], 'p_i': 10, 'u_i': 2.8095},
        {'id': 1, 'e_m': 3.011232, 'e_o_k': [0.370233, 0.296187, 0.236949], 'p_i': 20, 'u_i': 2.2645},
        {'id': 2, 'e_m': 8.307524, 'e_o_k': [0.741390, 0.593112, 0.474490, 0.379592, 0.303673], 'p_i': 40, 'u_i': 4.9290},
        {'id': 3, 'e_m': 9.605737, 'e_o_k': [1.181033, 0.944827, 0.755861], 'p_i': 80, 'u_i': 2.8289},
        {'id': 4, 'e_m': 4.598887, 'e_o_k': [0.410419, 0.328336, 0.262668, 0.210135, 0.168108], 'p_i': 20, 'u_i': 2.4039},
        {'id': 5, 'e_m': 3.546909, 'e_o_k': [0.316538, 0.253230, 0.202584, 0.162067, 0.129654], 'p_i': 10, 'u_i': 2.7593},
        {'id': 6, 'e_m': 21.569864, 'e_o_k': [1.924964, 1.539971, 1.231977, 0.985582, 0.788465], 'p_i': 80, 'u_i': 4.9185},
        {'id': 7, 'e_m': 2.167454, 'e_o_k': [0.266490, 0.213192, 0.170554], 'p_i': 80, 'u_i': 1.9966},
    ]
    B_BUDGET = 167.440006
    return processors, tasks, B_BUDGET
