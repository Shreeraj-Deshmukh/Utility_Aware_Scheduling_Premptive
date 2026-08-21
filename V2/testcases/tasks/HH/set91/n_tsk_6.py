"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639986, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639986, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.480132, 'e_o_k': [0.561677, 0.449342, 0.359473, 0.287579, 0.230063, 0.184050], 'p_i': 10, 'u_i': 3.3094},
        {'id': 1, 'e_m': 0.550568, 'e_o_k': [0.315900, 0.252720, 0.202176], 'p_i': 20, 'u_i': 3.8452},
        {'id': 2, 'e_m': 16.779335, 'e_o_k': [6.367386, 5.093909, 4.075127, 3.260102, 2.608081, 2.086465], 'p_i': 40, 'u_i': 1.8919},
        {'id': 3, 'e_m': 7.849433, 'e_o_k': [2.978686, 2.382949, 1.906359, 1.525087, 1.220070, 0.976056], 'p_i': 80, 'u_i': 3.0558},
        {'id': 4, 'e_m': 0.184203, 'e_o_k': [0.087359, 0.069887, 0.055910, 0.044728], 'p_i': 10, 'u_i': 1.4898},
        {'id': 5, 'e_m': 3.537470, 'e_o_k': [1.677662, 1.342130, 1.073704, 0.858963], 'p_i': 40, 'u_i': 1.5566},
    ]
    B_BUDGET = 176.639986
    return processors, tasks, B_BUDGET
