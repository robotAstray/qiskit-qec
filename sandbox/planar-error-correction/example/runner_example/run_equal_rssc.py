from plerco.pec_python.simulation_runner.runner import Runner

pin = {
    3: [
        0.0001,
        0.00015,
        0.0002,
        0.00025,
        0.0003,
        0.00035,
        0.0004,
        0.00045,
        0.0005,
        0.00055,
        0.0006,
        0.00065,
        0.0007,
        0.00075,
        0.0008,
        0.00085,
        0.0009,
        0.00095,
        0.001,
        0.0015,
        0.002,
        0.0025,
        0.003,
        0.0035,
        0.004,
        0.0045,
    ],
    5: [
        0.0001,
        0.00015,
        0.0002,
        0.00025,
        0.0003,
        0.00035,
        0.0004,
        0.00045,
        0.0005,
        0.00055,
        0.0006,
        0.00065,
        0.0007,
        0.00075,
        0.0008,
        0.00085,
        0.0009,
        0.00095,
        0.001,
        0.0015,
        0.002,
        0.0025,
        0.003,
        0.0035,
        0.004,
        0.0045,
    ],
    7: [
        0.0002,
        0.00025,
        0.0003,
        0.00035,
        0.0004,
        0.00045,
        0.0005,
        0.00055,
        0.0006,
        0.00065,
        0.0007,
        0.00075,
        0.0008,
        0.00085,
        0.0009,
        0.00095,
        0.001,
        0.0015,
        0.002,
        0.0025,
        0.003,
        0.0035,
        0.004,
        0.0045,
    ],
    9: [
        0.0004,
        0.00045,
        0.0005,
        0.00055,
        0.0006,
        0.00065,
        0.0007,
        0.00075,
        0.0008,
        0.00085,
        0.0009,
        0.00095,
        0.001,
        0.0015,
        0.002,
        0.0025,
        0.003,
        0.0035,
        0.004,
        0.0045,
    ],
    11: [
        0.0006,
        0.00065,
        0.0007,
        0.00075,
        0.0008,
        0.00085,
        0.0009,
        0.00095,
        0.001,
        0.0015,
        0.002,
        0.0025,
        0.003,
        0.0035,
        0.004,
        0.0045,
    ],
}
r = Runner()
for d in [3, 5, 7, 9, 11]:
    for rounds in [12, 6, 4]:
        round_schedule = {12: "zx", 6: "zzxx", 4: "zzzxxx"}
        r.add_experiment(
            "rssc_hex", "equal", d, rounds, round_schedule[rounds], "z", pin[d]
        )
        r.add_experiment(
            "rssc_hex", "equal", d, rounds, round_schedule[rounds], "x", pin[d]
        )
r.run_experiments()
print("DONE")
print(r.results)
