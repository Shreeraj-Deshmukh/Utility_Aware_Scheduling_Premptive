"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279985, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279985, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.895823, 'e_o_k': [0.815970, 0.652776], 'p_i': 10, 'u_i': 2.8688},
        {'id': 1, 'e_m': 2.381155, 'e_o_k': [0.396859, 0.317487], 'p_i': 20, 'u_i': 1.9991},
        {'id': 2, 'e_m': 6.678162, 'e_o_k': [0.678675, 0.542940, 0.434352, 0.347482], 'p_i': 40, 'u_i': 2.9592},
        {'id': 3, 'e_m': 6.770644, 'e_o_k': [0.550566, 0.440453, 0.352362, 0.281890, 0.225512, 0.180410], 'p_i': 80, 'u_i': 1.9155},
        {'id': 4, 'e_m': 4.815745, 'e_o_k': [0.489405, 0.391524, 0.313219, 0.250575], 'p_i': 20, 'u_i': 1.4935},
        {'id': 5, 'e_m': 11.424182, 'e_o_k': [1.404613, 1.123690, 0.898952], 'p_i': 40, 'u_i': 1.7848},
        {'id': 6, 'e_m': 11.227819, 'e_o_k': [1.002007, 0.801605, 0.641284, 0.513027, 0.410422], 'p_i': 80, 'u_i': 3.9231},
        {'id': 7, 'e_m': 10.921332, 'e_o_k': [1.109891, 0.887913, 0.710331, 0.568264], 'p_i': 40, 'u_i': 3.8764},
    ]
    B_BUDGET = 215.279985
    return processors, tasks, B_BUDGET
