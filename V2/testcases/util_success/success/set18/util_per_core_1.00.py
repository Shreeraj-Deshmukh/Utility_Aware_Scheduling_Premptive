"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199999, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199999, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.634162, 'e_o_k': [0.272360, 0.217888], 'p_i': 10, 'u_i': 1.3844},
        {'id': 1, 'e_m': 7.007309, 'e_o_k': [0.712125, 0.569700, 0.455760, 0.364608], 'p_i': 20, 'u_i': 1.0170},
        {'id': 2, 'e_m': 10.897001, 'e_o_k': [0.886108, 0.708886, 0.567109, 0.453687, 0.362950, 0.290360], 'p_i': 40, 'u_i': 2.5161},
        {'id': 3, 'e_m': 0.851993, 'e_o_k': [0.069281, 0.055425, 0.044340, 0.035472, 0.028378, 0.022702], 'p_i': 80, 'u_i': 4.5643},
        {'id': 4, 'e_m': 9.526556, 'e_o_k': [0.850180, 0.680144, 0.544116, 0.435292, 0.348234], 'p_i': 40, 'u_i': 3.3807},
        {'id': 5, 'e_m': 7.940768, 'e_o_k': [0.806989, 0.645591, 0.516473, 0.413178], 'p_i': 20, 'u_i': 1.8594},
        {'id': 6, 'e_m': 19.820331, 'e_o_k': [2.436926, 1.949541, 1.559633], 'p_i': 40, 'u_i': 2.0030},
        {'id': 7, 'e_m': 5.794628, 'e_o_k': [0.517131, 0.413705, 0.330964, 0.264771, 0.211817], 'p_i': 80, 'u_i': 2.5190},
    ]
    B_BUDGET = 239.199999
    return processors, tasks, B_BUDGET
