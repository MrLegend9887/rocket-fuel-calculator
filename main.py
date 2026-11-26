import sys
from models import RocketStage,Rocket
from calculations import calculate_required_propellant


def display_menu():
    print("=" * 40)
    print("       ROCKET FUEL CALCULATOR")
    print("=" * 40)
    print("1. Calculate Single-Stage Delta-v")
    print("2. Calculate Required Propellant")
    print("3. Build a Multi-Stage Rocket")
    print("4. Exit")
    print("=" * 40)
    choice = input("Enter your choice: ")
    return choice

def single_stage_calculator():
    dry_mass = float(input("Enter dry mass: "))
    propellant_mass = float(input("Enter propellant mass: "))
    isp = float(input("Enter isp: "))
    payload_mass = float(input("Enter payload mass: "))
    rocket_stage = RocketStage(dry_mass, propellant_mass, isp, payload_mass)
    delta_v = rocket_stage.calculate_delta_v()
    print(f"Calculated Delta-v: {delta_v:.2f} m/s")
    input("\nPress Enter to return to the menu...")

def required_propellant():
    final_mass = float(input("Enter final mass: "))
    target_delta_v = float(input("Enter target Delta-v: "))
    isp = float(input("Enter isp: "))
    required_propellant = calculate_required_propellant(final_mass, target_delta_v, isp)
    print(f"Required propellant: {required_propellant:.2f} kg")
    input("\nPress Enter to return to the menu...")

def multi_stage_rocket_builder():
    payload_mass = float(input("Enter total payload mass: "))
    stage_count = int(input("How many stages you want to create? :"))
    stages = []
    for i in range(stage_count):
        dry_mass = float(input(f"Enter dry mass for stage{i+1}: "))
        propellant_mass = float(input(f"Enter propellant mass for stage{i+1}: "))
        isp = float(input(f"Enter isp for stage{i+1}: "))
        stage = RocketStage(dry_mass, propellant_mass, isp, 0)
        stages.append(stage)
    rocket = Rocket(stages, payload_mass)
    rocket.calculate_payload()
    stage_delta_v = rocket.calculate_delta_v()
    total_delta_v = rocket.total_delta_v()
    # Display All Stages With There Delta V
    for stage, delta_v in enumerate(stage_delta_v):
        print(f"Stage {stage + 1} Delta-v: {delta_v:.2f} m/s")
    # Display Total Delta V 
    print(f"Total Delta-v: {total_delta_v:.2f} m/s")
    input("\nPress Enter to return to the menu...")

while True:

    user_choice = display_menu()
    if user_choice == "1":
        single_stage_calculator()

    elif user_choice == "2":
        required_propellant()

    elif user_choice == "3":
        multi_stage_rocket_builder()

    elif user_choice == "4":
        print("Exiting Rocket Fuel Calculator")
        sys.exit()

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        input("\nPress Enter to return to the menu...")