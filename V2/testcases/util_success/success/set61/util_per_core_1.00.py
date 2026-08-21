"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200001, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200001, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.569180, 'e_o_k': [0.315883, 0.252706, 0.202165], 'p_i': 10, 'u_i': 2.8354},
        {'id': 1, 'e_m': 2.669114, 'e_o_k': [0.217043, 0.173635, 0.138908, 0.111126, 0.088901, 0.071121], 'p_i': 20, 'u_i': 4.4570},
        {'id': 2, 'e_m': 11.849419, 'e_o_k': [1.974903, 1.579922], 'p_i': 40, 'u_i': 1.7617},
        {'id': 3, 'e_m': 6.026791, 'e_o_k': [0.490079, 0.392063, 0.313650, 0.250920, 0.200736, 0.160589], 'p_i': 80, 'u_i': 3.9855},
        {'id': 4, 'e_m': 14.045184, 'e_o_k': [1.427356, 1.141885, 0.913508, 0.730806], 'p_i': 40, 'u_i': 4.2888},
        {'id': 5, 'e_m': 13.200703, 'e_o_k': [1.073437, 0.858750, 0.687000, 0.549600, 0.439680, 0.351744], 'p_i': 40, 'u_i': 4.5823},
        {'id': 6, 'e_m': 21.545622, 'e_o_k': [2.189596, 1.751677, 1.401341, 1.121073], 'p_i': 80, 'u_i': 2.7900},
        {'id': 7, 'e_m': 11.503540, 'e_o_k': [0.935430, 0.748344, 0.598675, 0.478940, 0.383152, 0.306522], 'p_i': 40, 'u_i': 1.8324},
    ]
    B_BUDGET = 239.200001
    return processors, tasks, B_BUDGET
