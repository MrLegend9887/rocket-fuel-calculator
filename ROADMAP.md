
# Project 4: Rocket Fuel Calculator

## Project Objective
Build a Python-based rocket performance calculator capable of calculating single-stage and multi-stage rocket performance using the Tsiolkovsky rocket equation.

The project aims to develop practical programming skills in:
- Python programming
- Object-oriented programming
- Mathematical computation
- Input validation
- Automated testing
- Software architecture
- CLI development
- Engineering software design

---

## Progress

- [x] Milestone 1: Understand the Rocket Equation
- [x] Milestone 2: Define Physical Quantities and Units
- [x] Milestone 3: Implement Mass-Ratio Calculation
- [x] Milestone 4: Implement Single-Stage Δv Calculation
- [x] Milestone 5: Implement Inverse Calculation for Required Propellant
- [x] Milestone 6: Design the RocketStage Model
- [x] Milestone 7: Validate Stage Data
- [x] Milestone 8: Calculate Stage Mass Properties
- [x] Milestone 9: Calculate Stage Performance
- [x] Milestone 10: Design the Multi-Stage Rocket Model
- [x] Milestone 11: Calculate Stage-by-Stage Δv
- [x] Milestone 12: Calculate Total Vehicle Δv
- [x] Milestone 13: Calculate Required Propellant for a Target Δv
- [x] Milestone 14: Handle Payload and Staging Relationships
- [x] Milestone 15: Input Validation
- [x] Milestone 16: Edge Cases and Numerical Safety
- [x] Milestone 17: Automated Testing
- [x] Milestone 18: Refactoring and Project Structure
- [x] Milestone 19: Reporting and CLI Usability
- [ ] Milestone 20: Documentation and Final Architecture Review

---

# Phase 1: Mathematical Foundation

### Milestone 1: Understand the Rocket Equation
Understand the physics and mathematical foundation of the Tsiolkovsky rocket equation.

### Milestone 2: Define Physical Quantities and Units
Define the physical quantities, units and assumptions used throughout the project.

### Milestone 3: Implement Mass-Ratio Calculation
Implement the mass-ratio calculation.

### Milestone 4: Implement Single-Stage Δv Calculation
Calculate ideal single-stage delta-v.

### Milestone 5: Implement Inverse Calculation for Required Propellant
Calculate the required propellant mass for a target delta-v.

---

# Phase 2: Domain Modeling

### Milestone 6: Design the RocketStage Model
Create the RocketStage class and define its properties.

### Milestone 7: Validate Stage Data
Validate stage inputs and ensure invalid values are rejected.

### Milestone 8: Calculate Stage Mass Properties
Calculate initial mass, final mass and mass ratio.

### Milestone 9: Calculate Stage Performance
Calculate individual stage delta-v.

### Milestone 10: Design the Multi-Stage Rocket Model
Create a Rocket model capable of managing multiple rocket stages.

---

# Phase 3: Multi-Stage Calculations

### Milestone 11: Calculate Stage-by-Stage Δv
Calculate the delta-v of each stage within the rocket.

### Milestone 12: Calculate Total Vehicle Δv
Calculate the total ideal delta-v of the vehicle.

### Milestone 13: Calculate Required Propellant for a Target Δv
Extend inverse calculations to the appropriate rocket model.

### Milestone 14: Handle Payload and Staging Relationships
Manage payload distribution and stage separation relationships.

---

# Phase 4: Reliability

### Milestone 15: Input Validation
Implement validation for user inputs and model data.

### Milestone 16: Edge Cases and Numerical Safety
Protect calculations against invalid values, numerical overflow and unsafe arithmetic.

### Milestone 17: Automated Testing
Build an automated testing system to verify the correctness and reliability of the project.

### Milestone 18: Refactoring and Project Structure
Improve the code structure, organization, maintainability and separation of responsibilities.

---

# Phase 5: Engineering Usability

### Milestone 19: Reporting and CLI Usability
Develop a usable command-line interface and structured calculation reports.

### Milestone 20: Documentation and Final Architecture Review
Document the project, review the architecture and finalize the project.

---

# Physics Model

The project uses the Tsiolkovsky rocket equation:

Δv = Isp × g₀ × ln(m₀ / mf)

Where:

- Δv = Change in velocity (m/s)
- Isp = Specific impulse (seconds)
- g₀ = Standard gravitational acceleration (9.80665 m/s²)
- m₀ = Initial mass (kg)
- mf = Final mass (kg)

## Simplified Model Assumptions

- Ideal rocket equation
- No atmospheric drag
- No gravity losses
- No steering losses
- No trajectory simulation
- Ideal stage separation

---

# Development Rules

- Complete one task at a time.
- Understand the reasoning behind implementations.
- Avoid unnecessary complexity.
- Test functionality before proceeding.
- Do not introduce unplanned scope.
- Keep the code readable and maintainable.
- Commit completed milestones to Git.
- Track progress in this roadmap.