states_needed= set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["ktree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

best_station = None
states_covered = set()
for stations, states_for_stations in stations.items():
    covered = states_needed & states_for_stations
    if len(covered) > len(states_covered):
        best_station = stations
        states_covered = covered

print(best_station)