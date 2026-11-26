# Project 4: Rocket Fuel Calculator

## Objective

Build a Python-based Rocket Fuel Calculator that applies the Tsiolkovsky rocket equation to calculate theoretical delta-v and required propellant for single-stage and multi-stage rockets.

The project focuses on mathematical implementation, object-oriented programming, validation, testing, modular architecture and CLI usability.

---

## Physics Model

The project uses the ideal rocket equation:

\[
\Delta v = I_{sp}g_0\ln\left(\frac{m_0}{m_f}\right)
\]

Where:

- \(\Delta v\) = change in velocity (m/s)
- \(I_{sp}\) = specific impulse (seconds)
- \(g_0\) = standard gravitational acceleration (9.80665 m/s²)
- \(m_0\) = initial mass
- \(m_f\) = final mass

The project also implements the inverse equation for calculating required propellant mass.

---

## Development Rules

- Build incrementally, milestone by milestone.
- Understand the mathematics before implementing it.
- Maintain modular code.
- Use object-oriented programming where appropriate.
- Validate inputs and handle numerical edge cases.
- Write automated tests.
- Maintain Git version control.
- Document the project and its limitations.
- Avoid unnecessary features and scope creep.

---

## Phase 1: Mathematical Foundation

- [x] Milestone 1: Understand the Rocket Equation
- [x] Milestone 2: Define Physical Quantities and Units
- [x] Milestone 3: Implement Mass-Ratio Calculation
- [x] Milestone 4: Implement Single-Stage Delta-v Calculation
- [x] Milestone 5: Implement Inverse Required-Propellant Calculation

## Phase 2: Object-Oriented Stage Modeling

- [x] Milestone 6: Design `RocketStage`
- [x] Milestone 7: Validate Stage Data
- [x] Milestone 8: Calculate Stage Mass Properties
- [x] Milestone 9: Calculate Stage Performance

## Phase 3: Multi-Stage Rocket Modeling

- [x] Milestone 10: Design Multi-Stage Rocket Model
- [x] Milestone 11: Calculate Stage-by-Stage Delta-v
- [x] Milestone 12: Calculate Total Vehicle Delta-v
- [x] Milestone 13: Calculate Required Propellant for Target Delta-v
- [x] Milestone 14: Handle Payload and Staging Relationships

## Phase 4: Validation and Reliability

- [x] Milestone 15: Input Validation
- [x] Milestone 16: Edge Cases and Numerical Safety
- [x] Milestone 17: Automated Testing

## Phase 5: Software Structure and Completion

- [x] Milestone 18: Refactoring and Project Structure
- [x] Milestone 19: Reporting and CLI Usability
- [x] Milestone 20: Documentation and Final Architecture Review

---

## Project Status

**Status: Completed**

All 20 milestones have been completed.

- Mathematical calculations implemented.
- Single-stage calculation implemented.
- Multi-stage rocket modeling implemented.
- Payload distribution implemented.
- Input validation implemented.
- Numerical safety implemented.
- Automated tests implemented and passed.
- CLI implemented.
- README documentation completed.
- Code comments added.
- Final architecture review completed.

