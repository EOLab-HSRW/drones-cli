import sys
from argparse import ArgumentParser, Namespace
from drones_cli.commands import Command
from drones_cli.config import CATALOG

class BuildCommand(Command):

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument("drone", type=str.lower, choices=CATALOG["drones"].keys(), help="Name of the drone.")
        parser.add_argument("--fw-version", type=str.lower, help="Version of the drone firmware to build (this is different from the px4 version).")
        parser.add_argument("--fw-components", help="Components to add to the firmware")
        parser.add_argument("--px4-version", type=str.lower, help="PX4 Autopilot version")
        parser.add_argument("--vendor", type=str.lower, help="Board vendor. E.g. `px4`")
        parser.add_argument("--model", type=str.lower, help="Model of the board vendor. E.g `fmu-v6x` or `fmu-v3`")

    def execute(self, args: Namespace) -> None:

        if False:
            drone = DRONES[args.drone]
            drone_name = args.drone
            drone_wd = DRONES_DIR / drone_name

            print(f"Checking out PX4 firmware version: {drone.px4_version}")
            run_command("git fetch --all --tags", PX4_DIR)
            run_command(f"git checkout {drone.px4_version}", PX4_DIR)
            run_command("git submodule sync --recursive", PX4_DIR)
            run_command("git submodule update --init --recursive", PX4_DIR)

            temp_tag = f"{drone.px4_version}-"

            if args.fw_version == "latest":
                tag = get_latest_git_tag(drone_wd)
            else:
                tag = args.fw_version

            temp_tag += tag.lstrip('v')

            # working out the tags for the custom firmware version format
            run_command(f"git tag -f -a {temp_tag} -m {temp_tag}", PX4_DIR)

            run_command("bash ./Tools/setup/ubuntu.sh --no-sim-tools", PX4_DIR)
            run_command("sudo apt -y install gcc-arm-none-eabi", PX4_DIR)


            print(f"Checking out {drone_name} firmware version: {tag}")
            run_command("git fetch --all --tags", drone_wd)
            run_command(f"git checkout {tag}", drone_wd)

            airframe_base = drone_wd / "airframe"
            if not airframe_base.exists():
                print(f"could not find the file `airframe` under {drone_wd}. This file is mandatory to build the firmware.")
                sys.exit(1)

            modules_base = drone_wd / "modules"
            if not modules_base.exists():
                print(f"could not find the file `modules` under {drone_wd}. This file is mandatory to build the firmware.")
                sys.exit(1)

            airframe = f"{drone.id}_eolab_{drone_name}"
