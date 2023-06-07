from beacon_enum import Beacon

def filter_beacon_name(received_entry):
    mac_add = received_entry.split("device=")[1].split(",")[0]
    return _get_beacon_enum(mac_add)
    

def _get_beacon_enum(mac_add):
    for member in Beacon.__members__.values():
        if member.value == mac_add:
            return member
    raise ValueError(f"No Beacon with mac addr '{mac_add}' found.")