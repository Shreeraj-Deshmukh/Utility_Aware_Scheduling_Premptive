"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119991, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119991, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.806290, 'e_o_k': [0.467715, 0.374172], 'p_i': 10, 'u_i': 3.2561},
        {'id': 1, 'e_m': 7.248073, 'e_o_k': [0.589389, 0.471511, 0.377209, 0.301767, 0.241414, 0.193131], 'p_i': 20, 'u_i': 2.1809},
        {'id': 2, 'e_m': 17.502799, 'e_o_k': [1.778740, 1.422992, 1.138393, 0.910715], 'p_i': 40, 'u_i': 2.1482},
        {'id': 3, 'e_m': 28.664685, 'e_o_k': [4.777447, 3.821958], 'p_i': 80, 'u_i': 2.8260},
        {'id': 4, 'e_m': 2.580016, 'e_o_k': [0.230249, 0.184199, 0.147359, 0.117887, 0.094310], 'p_i': 10, 'u_i': 1.7178},
        {'id': 5, 'e_m': 2.712110, 'e_o_k': [0.452018, 0.361615], 'p_i': 20, 'u_i': 4.0325},
        {'id': 6, 'e_m': 6.636789, 'e_o_k': [0.815999, 0.652799, 0.522239], 'p_i': 20, 'u_i': 1.8661},
        {'id': 7, 'e_m': 1.425691, 'e_o_k': [0.175290, 0.140232, 0.112185], 'p_i': 40, 'u_i': 4.3460},
    ]
    B_BUDGET = 263.119991
    return processors, tasks, B_BUDGET
