"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319986, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319986, "H": 80, "J": 37, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.356926, 'e_o_k': [0.209660, 0.125796, 0.075478, 0.045287, 0.027172, 0.016303], 'p_i': 10, 'u_i': 4.1639},
        {'id': 1, 'e_m': 0.051417, 'e_o_k': [0.033081, 0.019849, 0.011909, 0.007145], 'p_i': 20, 'u_i': 2.0315},
        {'id': 2, 'e_m': 2.806103, 'e_o_k': [1.703914, 1.022348, 0.613409, 0.368045, 0.220827], 'p_i': 40, 'u_i': 1.5871},
        {'id': 3, 'e_m': 1.927874, 'e_o_k': [1.686890, 1.012134], 'p_i': 80, 'u_i': 1.8711},
        {'id': 4, 'e_m': 0.136822, 'e_o_k': [0.119719, 0.071831], 'p_i': 20, 'u_i': 4.9538},
        {'id': 5, 'e_m': 2.021725, 'e_o_k': [1.227626, 0.736576, 0.441945, 0.265167, 0.159100], 'p_i': 10, 'u_i': 2.3994},
        {'id': 6, 'e_m': 0.792114, 'e_o_k': [0.693099, 0.415860], 'p_i': 40, 'u_i': 1.5904},
        {'id': 7, 'e_m': 0.386691, 'e_o_k': [0.276208, 0.165725, 0.099435], 'p_i': 10, 'u_i': 2.4893},
    ]
    B_BUDGET = 88.319986
    return processors, tasks, B_BUDGET
