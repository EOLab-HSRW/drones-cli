from dataclasses import dataclass

COMPONENTS = [
    "radiomaster_tx16s"
]

@dataclass
class Drone:
    url: str
    id: int
    px4_version: str
    vendor: str
    model: str
    default_fw_version: str
    default_components: list[str]
    compatible_components: list[str]

DRONES = {
    "phoenix": Drone(
        url= "https://github.com/EOLab-HSRW/fw-phoenix",
        id= 22101,
        px4_version= "v1.15.0",
        vendor="px4",
        model="fmu-v3",
        default_fw_version= "latest",
        default_components= ["radiomaster_tx16s"],
        compatible_components= ["radiomaster_tx16s"],
    ),
    "platypus": Drone(
        url= "https://github.com/EOLab-HSRW/fw-platypus",
        id= 22102,
        px4_version= "v1.15.0",
        vendor="px4",
        model="fmu-v3",
        default_fw_version= "latest",
        default_components= ["radiomaster_tx16s"],
        compatible_components= ["radiomaster_tx16s"],
    ),
    "sar": Drone(
        url= "https://github.com/EOLab-HSRW/fw-sar",
        id= 22103,
        px4_version= "v1.15.0",
        vendor="px4",
        model="fmu-v6x",
        default_fw_version= "latest",
        default_components= ["radiomaster_tx16s"],
        compatible_components= ["radiomaster_tx16s"],
    ),
}
