# Rocket Fuel Calculator

A Python-based rocket performance calculator that uses the ideal rocket equation to calculate single-stage delta-v, estimate required propellant mass, and evaluate the ideal delta-v of a multi-stage rocket.

The project combines mathematical calculations, object-oriented design, input validation, automated testing, and an interactive command-line interface (CLI).

## Features

- **Single-Stage Delta-v Calculation:** Calculates the ideal velocity change of a rocket stage using its dry mass, propellant mass, payload mass, and specific impulse.
- **Required Propellant Calculation:** Estimates the propellant mass required to achieve a specified target delta-v for a given final mass and specific impulse.
- **Multi-Stage Rocket Analysis:** Creates a multi-stage rocket model and calculates the ideal delta-v of individual stages and the combined vehicle.
- **Input Validation:** Validates numerical inputs, rejects Boolean and invalid values, and handles several numerical safety conditions.
- **Interactive CLI:** Provides a menu-based interface for accessing the calculator's functionality.
- **Automated Testing:** Includes automated tests using Python's built-in `unittest` framework.

## Physics

The calculator uses the ideal Tsiolkovsky rocket equation:

\[
\Delta v = I_{sp}g_0\ln\left(\frac{m_0}{m_f}\right)
\]

Where:

- \(\Delta v\) = velocity change (m/s)
- \(I_{sp}\) = specific impulse (seconds)
- \(g_0\) = standard gravitational acceleration (9.80665 m/s²)
- \(m_0\) = initial mass (kg)
- \(m_f\) = final mass (kg)

The required propellant calculation uses the inverse form of the ideal rocket equation.

All calculations assume ideal conditions and do not account for real-world flight losses.

## Project Structure

```text
P4_Rocket_Fuel_Calculator/
│
├── calculations.py
├── models.py
├── main.py
├── README.md
├── ROADMAP.md
│
└── tests/
    ├── test_calculations.py
    ├── test_models.py
    └── test_rocket.py
```

### Modules

| File | Responsibility |
|---|---|
| `calculations.py` | Mathematical calculations, including delta-v and required propellant. |
| `models.py` | RocketStage and Rocket classes, mass properties, payload relationships and performance calculations. |
| `main.py` | Interactive CLI, user input, menu navigation and result display. |
| `tests/` | Automated tests covering calculations and rocket models. |
| `ROADMAP.md` | Project milestones and development roadmap. |

## Requirements

- Python 3.x
- No external Python packages are required.

## Running the Program

Clone the repository:

```bash
git clone <https://github.com/MrLegend9887/rocket-fuel-calculator>
```

Navigate to the project directory:

```bash
cd P4_Rocket_Fuel_Calculator
```

Run the program:

```bash
python main.py
```

## CLI Options

The program provides the following menu options:

1. Calculate Single-Stage Delta-v
2. Calculate Required Propellant
3. Build a Multi-Stage Rocket
4. Exit

## Running Tests

The project uses Python's built-in `unittest` framework.

Run the test suite from the project root:

```bash
python -m unittest discover -s tests -v
```

## Model Limitations

This calculator uses simplified ideal rocket physics. Its calculations do not account for:

- Atmospheric drag
- Gravity losses during ascent
- Aerodynamic effects
- Thrust variation during flight
- Trajectory optimization
- Steering losses
- Orbital mechanics and mission-specific trajectory requirements
- Real engine performance variations

The multi-stage calculation represents ideal stage performance under the assumptions implemented in the model. The resulting delta-v is not a prediction of actual flight performance or achievable orbital insertion.

## Project Goals

This project was developed to strengthen understanding of:

- Python programming
- Object-oriented programming
- Mathematical modeling
- Rocket propulsion fundamentals
- Input validation
- Numerical safety
- Automated testing
- Software architecture
- Git and GitHub workflows

## Status

This project is an educational Python project focused on implementing fundamental rocket performance calculations and software engineering practices.

---

**Disclaimer:** This calculator is intended for educational purposes and simplified theoretical analysis. It should not be used for real-world rocket design, engineering decisions, flight planning, or safety-critical applications.