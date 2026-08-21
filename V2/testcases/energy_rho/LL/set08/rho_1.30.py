"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 60.720016, "H": 80, "J": 37, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.3, "seed": 1008, "set": 8, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.30"}
"""

_SPEC = '{"B": 60.720016, "H": 80, "J": 37, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.3, "seed": 1008, "set": 8, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.356926, 'e_o_k': [0.048373, 0.038699, 0.030959, 0.024767, 0.019814, 0.015851], 'p_i': 10, 'u_i': 4.1639},
        {'id': 1, 'e_m': 0.051417, 'e_o_k': [0.008709, 0.006967, 0.005574, 0.004459], 'p_i': 20, 'u_i': 2.0315},
        {'id': 2, 'e_m': 2.806103, 'e_o_k': [0.417376, 0.333901, 0.267121, 0.213697, 0.170957], 'p_i': 40, 'u_i': 1.5871},
        {'id': 3, 'e_m': 1.927874, 'e_o_k': [0.535521, 0.428416], 'p_i': 80, 'u_i': 1.8711},
        {'id': 4, 'e_m': 0.136822, 'e_o_k': [0.038006, 0.030405], 'p_i': 20, 'u_i': 4.9538},
        {'id': 5, 'e_m': 2.021725, 'e_o_k': [0.300709, 0.240567, 0.192454, 0.153963, 0.123170], 'p_i': 10, 'u_i': 2.3994},
        {'id': 6, 'e_m': 0.792114, 'e_o_k': [0.220032, 0.176025], 'p_i': 40, 'u_i': 1.5904},
        {'id': 7, 'e_m': 0.386691, 'e_o_k': [0.079240, 0.063392, 0.050714], 'p_i': 10, 'u_i': 2.4893},
    ]
    B_BUDGET = 60.720016
    return processors, tasks, B_BUDGET
