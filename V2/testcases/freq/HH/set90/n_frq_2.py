"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639988, "H": 80, "J": 29, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "freq", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639988, "H": 80, "J": 29, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "freq", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 1.0]},
        {'id': 1, 'frequencies': [0.4, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.855925, 'e_o_k': [0.356466, 0.285172, 0.228138, 0.182510, 0.146008], 'p_i': 10, 'u_i': 3.1824},
        {'id': 1, 'e_m': 2.062245, 'e_o_k': [0.782576, 0.626061, 0.500849, 0.400679, 0.320543, 0.256435], 'p_i': 20, 'u_i': 3.3367},
        {'id': 2, 'e_m': 1.796246, 'e_o_k': [1.030633, 0.824506, 0.659605], 'p_i': 40, 'u_i': 4.5472},
        {'id': 3, 'e_m': 0.729094, 'e_o_k': [0.345776, 0.276621, 0.221297, 0.177038], 'p_i': 80, 'u_i': 1.6834},
        {'id': 4, 'e_m': 2.221698, 'e_o_k': [1.727987, 1.382390], 'p_i': 40, 'u_i': 3.8684},
        {'id': 5, 'e_m': 13.925733, 'e_o_k': [10.831126, 8.664901], 'p_i': 40, 'u_i': 4.7513},
        {'id': 6, 'e_m': 5.950860, 'e_o_k': [2.258220, 1.806576, 1.445261, 1.156208, 0.924967, 0.739973], 'p_i': 40, 'u_i': 2.4512},
        {'id': 7, 'e_m': 0.048181, 'e_o_k': [0.037474, 0.029980], 'p_i': 10, 'u_i': 1.4858},
    ]
    B_BUDGET = 176.639988
    return processors, tasks, B_BUDGET
