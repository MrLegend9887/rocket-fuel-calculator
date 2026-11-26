import sys
from models import RocketStage, Rocket
from calculations import calculate_required_propellant


def display_menu():
    # Display the application's main menu and collect the user's selection.
    # This function handles menu presentation, not the calculations themselves.
    print("=" * 40)
    print("       ROCKET FUEL CALCULATOR")
    print("=" * 40)
    print("1. Calculate Single-Stage Delta-v")
    print("2. Calculate Required Propellant")
    print("3. Build a Multi-Stage Rocket")
    print("4. Exit")
    print("=" * 40)

    # input() returns a string, which is compared against menu options below.
    choice = input("Enter your choice: ")
    return choice


def single_stage_calculator():
    # Collect the physical parameters required to model a single rocket stage.
    # float() converts the user's text input into a numeric value.
    dry_mass = float(input("Enter dry mass: "))
    propellant_mass = float(input("Enter propellant mass: "))
    isp = float(input("Enter isp: "))
    payload_mass = float(input("Enter payload mass: "))

    # Create a RocketStage object, which stores the input values and
    # validates them during initialization.
    rocket_stage = RocketStage(dry_mass, propellant_mass, isp, payload_mass)

    # Calculate the stage's theoretical delta-v using the rocket equation.
    delta_v = rocket_stage.calculate_delta_v()

    # Display the result with two decimal places and the unit m/s.
    print(f"Calculated Delta-v: {delta_v:.2f} m/s")

    # Pause the program so the user can read the result before returning.
    input("\nPress Enter to return to the menu...")


def required_propellant():
    # Collect the final mass, desired delta-v and specific impulse.
    # Final mass refers to the mass remaining after propellant is consumed.
    final_mass = float(input("Enter final mass: "))
    target_delta_v = float(input("Enter target Delta-v: "))
    isp = float(input("Enter isp: "))

    # Call the inverse rocket equation to estimate the propellant
    # required to achieve the specified delta-v.
    required_propellant = calculate_required_propellant(final_mass, target_delta_v, isp)

    # Display the calculated propellant mass in kilograms.
    print(f"Required propellant: {required_propellant:.2f} kg")

    # Pause before returning to the main menu.
    input("\nPress Enter to return to the menu...")


def multi_stage_rocket_builder():
    # Collect the payload mass that the complete rocket must carry.
    payload_mass = float(input("Enter total payload mass: "))

    # Determine how many stages the user wants to model.
    stage_count = int(input("How many stages you want to create? :"))

    # Store all created RocketStage objects in a list.
    # The list order is important: stages are expected from the bottom
    # (first stage) to the top (final stage).
    stages = []

    # Collect physical properties for each stage.
    for i in range(stage_count):
        dry_mass = float(input(f"Enter dry mass for stage{i+1}: "))
        propellant_mass = float(input(f"Enter propellant mass for stage{i+1}: "))
        isp = float(input(f"Enter isp for stage{i+1}: "))

        # Payload mass is initially set to zero because the Rocket object
        # will calculate how much mass each stage carries after all stages
        # have been created.
        stage = RocketStage(dry_mass, propellant_mass, isp, 0)
        stages.append(stage)

    # Create a Rocket object containing the complete stage list and payload.
    rocket = Rocket(stages, payload_mass)

    # Assign the correct carried mass to each stage based on the stages
    # above it and the payload, accounting for the staged configuration.
    rocket.calculate_payload()

    # Calculate the delta-v produced by each individual stage.
    stage_delta_v = rocket.calculate_delta_v()

    # Calculate the theoretical delta-v of the complete rocket by summing
    # the contributions of its individual stages.
    total_delta_v = rocket.total_delta_v()

    # Display the delta-v of every stage individually.
    for stage, delta_v in enumerate(stage_delta_v):
        print(f"Stage {stage + 1} Delta-v: {delta_v:.2f} m/s")

    # Display the total ideal delta-v of the complete rocket.
    print(f"Total Delta-v: {total_delta_v:.2f} m/s")

    # Pause before returning to the menu.
    input("\nPress Enter to return to the menu...")


# Main program loop:
# Repeatedly display the menu and execute the selected operation
# until the user chooses to exit.
while True:

    user_choice = display_menu()

    if user_choice == "1":
        # Run the single-stage delta-v calculator.
        single_stage_calculator()

    elif user_choice == "2":
        # Run the inverse rocket equation calculator.
        required_propellant()

    elif user_choice == "3":
        # Build and calculate the performance of a multi-stage rocket.
        multi_stage_rocket_builder()

    elif user_choice == "4":
        # Terminate the program when the user chooses the exit option.
        print("Exiting Rocket Fuel Calculator")
        sys.exit()

    else:
        # Handle selections that do not correspond to a menu option.
        print("Invalid choice. Please select 1, 2, 3, or 4.")

        # Pause to allow the user to read the error message.
        input("\nPress Enter to return to the menu...")