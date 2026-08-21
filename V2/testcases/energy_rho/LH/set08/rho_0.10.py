"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 41.952, "H": 80, "J": 37, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.1, "seed": 1008, "set": 8, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.10"}
"""

_SPEC = '{"B": 41.952, "H": 80, "J": 37, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.1, "seed": 1008, "set": 8, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.356926, 'e_o_k': [0.135445, 0.108356, 0.086685, 0.069348, 0.055478, 0.044383], 'p_i': 10, 'u_i': 4.1639},
        {'id': 1, 'e_m': 0.051417, 'e_o_k': [0.024385, 0.019508, 0.015606, 0.012485], 'p_i': 20, 'u_i': 2.0315},
        {'id': 2, 'e_m': 2.806103, 'e_o_k': [1.168653, 0.934922, 0.747938, 0.598350, 0.478680], 'p_i': 40, 'u_i': 1.5871},
        {'id': 3, 'e_m': 1.927874, 'e_o_k': [1.499457, 1.199566], 'p_i': 80, 'u_i': 1.8711},
        {'id': 4, 'e_m': 0.136822, 'e_o_k': [0.106417, 0.085134], 'p_i': 20, 'u_i': 4.9538},
        {'id': 5, 'e_m': 2.021725, 'e_o_k': [0.841985, 0.673588, 0.538870, 0.431096, 0.344877], 'p_i': 10, 'u_i': 2.3994},
        {'id': 6, 'e_m': 0.792114, 'e_o_k': [0.616088, 0.492871], 'p_i': 40, 'u_i': 1.5904},
        {'id': 7, 'e_m': 0.386691, 'e_o_k': [0.221872, 0.177498, 0.141998], 'p_i': 10, 'u_i': 2.4893},
    ]
    B_BUDGET = 41.952000
    return processors, tasks, B_BUDGET
