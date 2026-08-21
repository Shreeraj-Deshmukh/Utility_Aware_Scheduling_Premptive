"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200005, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200005, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.104679, 'e_o_k': [0.187828, 0.150263, 0.120210, 0.096168, 0.076934], 'p_i': 10, 'u_i': 4.4317},
        {'id': 1, 'e_m': 5.057021, 'e_o_k': [0.513925, 0.411140, 0.328912, 0.263130], 'p_i': 20, 'u_i': 3.9967},
        {'id': 2, 'e_m': 8.726856, 'e_o_k': [0.778813, 0.623050, 0.498440, 0.398752, 0.319002], 'p_i': 40, 'u_i': 3.7464},
        {'id': 3, 'e_m': 33.804577, 'e_o_k': [4.156300, 3.325040, 2.660032], 'p_i': 80, 'u_i': 2.1384},
        {'id': 4, 'e_m': 2.600707, 'e_o_k': [0.319759, 0.255807, 0.204646], 'p_i': 20, 'u_i': 4.1214},
        {'id': 5, 'e_m': 3.568481, 'e_o_k': [0.594747, 0.475798], 'p_i': 10, 'u_i': 3.7942},
        {'id': 6, 'e_m': 11.950028, 'e_o_k': [1.066459, 0.853167, 0.682534, 0.546027, 0.436822], 'p_i': 80, 'u_i': 2.9007},
        {'id': 7, 'e_m': 10.387746, 'e_o_k': [1.055665, 0.844532, 0.675626, 0.540501], 'p_i': 40, 'u_i': 1.2150},
    ]
    B_BUDGET = 239.200005
    return processors, tasks, B_BUDGET
