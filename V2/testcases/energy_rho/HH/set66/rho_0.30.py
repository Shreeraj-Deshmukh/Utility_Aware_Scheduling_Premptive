"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 104.512, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.3, "seed": 1066, "set": 66, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.30"}
"""

_SPEC = '{"B": 104.512, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.3, "seed": 1066, "set": 66, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.134282, 'e_o_k': [0.063684, 0.050947, 0.040758, 0.032606], 'p_i': 10, 'u_i': 3.0491},
        {'id': 1, 'e_m': 1.595105, 'e_o_k': [0.664311, 0.531449, 0.425159, 0.340127, 0.272102], 'p_i': 20, 'u_i': 3.9469},
        {'id': 2, 'e_m': 4.086998, 'e_o_k': [2.344999, 1.875999, 1.500799], 'p_i': 40, 'u_i': 1.2331},
        {'id': 3, 'e_m': 10.112241, 'e_o_k': [5.802105, 4.641684, 3.713347], 'p_i': 80, 'u_i': 3.8857},
        {'id': 4, 'e_m': 1.915959, 'e_o_k': [1.490191, 1.192153], 'p_i': 20, 'u_i': 4.4773},
        {'id': 5, 'e_m': 1.005364, 'e_o_k': [0.781950, 0.625560], 'p_i': 10, 'u_i': 2.4546},
        {'id': 6, 'e_m': 1.093498, 'e_o_k': [0.518597, 0.414877, 0.331902, 0.265522], 'p_i': 80, 'u_i': 1.1544},
        {'id': 7, 'e_m': 21.458838, 'e_o_k': [12.312448, 9.849958, 7.879967], 'p_i': 80, 'u_i': 4.0204},
    ]
    B_BUDGET = 104.512000
    return processors, tasks, B_BUDGET
