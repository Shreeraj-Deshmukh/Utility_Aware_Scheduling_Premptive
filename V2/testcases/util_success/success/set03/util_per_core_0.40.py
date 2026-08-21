"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679986, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679986, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.759727, 'e_o_k': [0.077208, 0.061766, 0.049413, 0.039531], 'p_i': 10, 'u_i': 3.3255},
        {'id': 1, 'e_m': 2.267234, 'e_o_k': [0.184364, 0.147491, 0.117993, 0.094394, 0.075515, 0.060412], 'p_i': 20, 'u_i': 3.8694},
        {'id': 2, 'e_m': 1.540180, 'e_o_k': [0.256697, 0.205357], 'p_i': 40, 'u_i': 3.5739},
        {'id': 3, 'e_m': 8.351708, 'e_o_k': [0.679133, 0.543307, 0.434645, 0.347716, 0.278173, 0.222538], 'p_i': 80, 'u_i': 3.1864},
        {'id': 4, 'e_m': 8.673789, 'e_o_k': [0.881483, 0.705186, 0.564149, 0.451319], 'p_i': 80, 'u_i': 1.9174},
        {'id': 5, 'e_m': 24.118641, 'e_o_k': [1.961248, 1.568998, 1.255199, 1.004159, 0.803327, 0.642662], 'p_i': 80, 'u_i': 3.2100},
        {'id': 6, 'e_m': 0.384822, 'e_o_k': [0.047314, 0.037851, 0.030281], 'p_i': 10, 'u_i': 2.5681},
        {'id': 7, 'e_m': 0.775086, 'e_o_k': [0.129181, 0.103345], 'p_i': 40, 'u_i': 3.1630},
    ]
    B_BUDGET = 95.679986
    return processors, tasks, B_BUDGET
