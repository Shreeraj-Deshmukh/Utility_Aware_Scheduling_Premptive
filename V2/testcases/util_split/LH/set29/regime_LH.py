"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31999, "H": 80, "J": 28, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_split", "util_per_core": 0.2, "value": "LH"}
"""

_SPEC = '{"B": 88.31999, "H": 80, "J": 28, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_split", "util_per_core": 0.2, "value": "LH"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.277588, 'e_o_k': [0.131647, 0.105318, 0.084254, 0.067403], 'p_i': 10, 'u_i': 2.4751},
        {'id': 1, 'e_m': 0.425730, 'e_o_k': [0.177303, 0.141842, 0.113474, 0.090779, 0.072623], 'p_i': 20, 'u_i': 3.6644},
        {'id': 2, 'e_m': 1.697852, 'e_o_k': [0.707101, 0.565681, 0.452545, 0.362036, 0.289629], 'p_i': 40, 'u_i': 2.2976},
        {'id': 3, 'e_m': 1.741157, 'e_o_k': [0.725137, 0.580109, 0.464087, 0.371270, 0.297016], 'p_i': 80, 'u_i': 4.8639},
        {'id': 4, 'e_m': 2.016691, 'e_o_k': [1.568538, 1.254830], 'p_i': 40, 'u_i': 4.5045},
        {'id': 5, 'e_m': 1.394673, 'e_o_k': [0.800222, 0.640178, 0.512142], 'p_i': 80, 'u_i': 1.0020},
        {'id': 6, 'e_m': 1.783638, 'e_o_k': [0.845899, 0.676719, 0.541375, 0.433100], 'p_i': 40, 'u_i': 4.9529},
        {'id': 7, 'e_m': 1.743023, 'e_o_k': [1.355685, 1.084548], 'p_i': 10, 'u_i': 2.3587},
    ]
    B_BUDGET = 88.319990
    return processors, tasks, B_BUDGET
