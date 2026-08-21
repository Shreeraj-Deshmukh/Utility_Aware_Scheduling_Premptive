"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439997, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439997, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.511968, 'e_o_k': [0.356907, 0.285526, 0.228421, 0.182737], 'p_i': 10, 'u_i': 2.9329},
        {'id': 1, 'e_m': 0.251755, 'e_o_k': [0.025585, 0.020468, 0.016374, 0.013099], 'p_i': 20, 'u_i': 4.3550},
        {'id': 2, 'e_m': 7.639246, 'e_o_k': [0.681751, 0.545401, 0.436321, 0.349056, 0.279245], 'p_i': 40, 'u_i': 2.2741},
        {'id': 3, 'e_m': 3.362008, 'e_o_k': [0.413362, 0.330689, 0.264551], 'p_i': 80, 'u_i': 2.5808},
        {'id': 4, 'e_m': 5.896407, 'e_o_k': [0.526214, 0.420971, 0.336777, 0.269422, 0.215537], 'p_i': 40, 'u_i': 4.5356},
        {'id': 5, 'e_m': 2.454235, 'e_o_k': [0.301750, 0.241400, 0.193120], 'p_i': 20, 'u_i': 4.4130},
        {'id': 6, 'e_m': 11.929971, 'e_o_k': [1.466800, 1.173440, 0.938752], 'p_i': 80, 'u_i': 1.1305},
        {'id': 7, 'e_m': 3.839626, 'e_o_k': [0.390206, 0.312165, 0.249732, 0.199785], 'p_i': 10, 'u_i': 4.7707},
    ]
    B_BUDGET = 167.439997
    return processors, tasks, B_BUDGET
