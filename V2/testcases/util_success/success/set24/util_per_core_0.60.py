"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520003, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520003, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.381381, 'e_o_k': [0.063563, 0.050851], 'p_i': 10, 'u_i': 2.4482},
        {'id': 1, 'e_m': 7.346022, 'e_o_k': [0.746547, 0.597238, 0.477790, 0.382232], 'p_i': 20, 'u_i': 4.8654},
        {'id': 2, 'e_m': 9.890211, 'e_o_k': [1.648368, 1.318695], 'p_i': 40, 'u_i': 2.4832},
        {'id': 3, 'e_m': 7.455467, 'e_o_k': [0.757669, 0.606136, 0.484908, 0.387927], 'p_i': 80, 'u_i': 1.7299},
        {'id': 4, 'e_m': 0.443340, 'e_o_k': [0.054509, 0.043607, 0.034886], 'p_i': 10, 'u_i': 4.6595},
        {'id': 5, 'e_m': 0.334978, 'e_o_k': [0.034043, 0.027234, 0.021787, 0.017430], 'p_i': 10, 'u_i': 1.6443},
        {'id': 6, 'e_m': 2.456511, 'e_o_k': [0.409419, 0.327535], 'p_i': 10, 'u_i': 1.9160},
        {'id': 7, 'e_m': 1.306293, 'e_o_k': [0.106223, 0.084979, 0.067983, 0.054386, 0.043509, 0.034807], 'p_i': 10, 'u_i': 1.4840},
    ]
    B_BUDGET = 143.520003
    return processors, tasks, B_BUDGET
