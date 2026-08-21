"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64001, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.64001, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.384353, 'e_o_k': [0.656536, 0.525229, 0.420183, 0.336146], 'p_i': 10, 'u_i': 1.0669},
        {'id': 1, 'e_m': 1.854864, 'e_o_k': [0.879678, 0.703742, 0.562994, 0.450395], 'p_i': 20, 'u_i': 2.5210},
        {'id': 2, 'e_m': 1.794964, 'e_o_k': [1.029897, 0.823918, 0.659134], 'p_i': 40, 'u_i': 3.1907},
        {'id': 3, 'e_m': 17.552391, 'e_o_k': [8.324305, 6.659444, 5.327555, 4.262044], 'p_i': 80, 'u_i': 4.8710},
        {'id': 4, 'e_m': 3.295999, 'e_o_k': [2.563555, 2.050844], 'p_i': 20, 'u_i': 3.8865},
        {'id': 5, 'e_m': 1.397426, 'e_o_k': [1.086887, 0.869510], 'p_i': 10, 'u_i': 3.2848},
    ]
    B_BUDGET = 176.640010
    return processors, tasks, B_BUDGET
