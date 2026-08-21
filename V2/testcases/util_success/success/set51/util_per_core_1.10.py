"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120007, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120007, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.049942, 'e_o_k': [0.508324, 0.406659], 'p_i': 10, 'u_i': 2.8825},
        {'id': 1, 'e_m': 4.797379, 'e_o_k': [0.428134, 0.342507, 0.274005, 0.219204, 0.175364], 'p_i': 20, 'u_i': 1.7316},
        {'id': 2, 'e_m': 14.728584, 'e_o_k': [2.454764, 1.963811], 'p_i': 40, 'u_i': 1.0632},
        {'id': 3, 'e_m': 23.879126, 'e_o_k': [1.941771, 1.553417, 1.242734, 0.994187, 0.795349, 0.636280], 'p_i': 80, 'u_i': 2.0111},
        {'id': 4, 'e_m': 12.323652, 'e_o_k': [1.002118, 0.801695, 0.641356, 0.513085, 0.410468, 0.328374], 'p_i': 40, 'u_i': 1.5370},
        {'id': 5, 'e_m': 7.830689, 'e_o_k': [0.795802, 0.636641, 0.509313, 0.407450], 'p_i': 20, 'u_i': 4.6443},
        {'id': 6, 'e_m': 3.370060, 'e_o_k': [0.274042, 0.219234, 0.175387, 0.140310, 0.112248, 0.089798], 'p_i': 20, 'u_i': 3.4741},
        {'id': 7, 'e_m': 4.812177, 'e_o_k': [0.489042, 0.391234, 0.312987, 0.250390], 'p_i': 40, 'u_i': 1.2909},
    ]
    B_BUDGET = 263.120007
    return processors, tasks, B_BUDGET
