# Models of Computation Simulator

A Python-based interactive simulator for exploring **formal models of
computation** --- including **DFAs**, **NFAs**, **PDAs**, and **Turing
Machines** --- through an easy-to-use GUI.

This tool is designed for students and instructors studying **Automata
Theory** and **Formal Languages**.\
It allows users to **create**, **edit**, and **test** computational
models using JSON definitions and visual testing interfaces.

---

## Features

- **Graphical Menu System (Tkinter)**
  - Choose to **Create**, **Test**, or **Quit** the application.
- **Model Creation Interface**
  - Input fields for `model`, `Q`, `sigma`, `delta`, `q0`, and `F`.
  - Built-in scrollable/wrappable help window for formatting the
    `delta` transition function.
- **JSON-Based Model Storage**
  - Models are saved in a consistent JSON schema compatible with all
    automaton types.
- **Simulator Framework**
  - Supports deterministic and nondeterministic automata, with
    planned support for PDAs and TMs.

---

## Project Structure

    Models-of-Computation-Simulator/
    ├── gui_main_menu.py         # Main Tkinter menu (Create, Test, Quit)
    ├── utils_parse_relaxed_json.py  # Parser for user input → valid JSON model
    ├── Model.py                 # Abstract base class for computational models
    ├── DFA.py, NFA.py, PDA.py, TM.py  # Individual model implementations
    ├── utils.py                 # Shared helper functions
    ├── data/                    # Example model files (.json)
    └── README.md                # Project documentation (this file)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/reissko/Models-of-Computation-Simulator.git
cd Models-of-Computation-Simulator
```

### 2. Set up your environment

This project requires **Python 3.10+** and uses only the standard
library.

To confirm:

```bash
python3 --version
```

### 3. Run the simulator

```bash
python main.py
```

---

## JSON Model Format

Each model is stored in a JSON file like the following:

```json
{
  "model": "NFA",
  "Q": ["q0", "q1", "q2"],
  "sigma": ["a", "b"],
  "delta": {
    "q0": { "a": ["q0", "q1"], "b": ["q0"], "epsilon": [] },
    "q1": { "a": ["q2"], "b": [], "epsilon": [] },
    "q2": { "a": [], "b": [], "epsilon": [] }
  },
  "q0": "q0",
  "F": ["q2"]
}
```

### Notes for creating models

- `Q`: list of all states\
- `sigma`: alphabet symbols\
- `delta`: transitions (`state → symbol → next states`)\
- `q0`: start state\
- `F`: accepting states

Relaxed formatting (e.g., `{ q0: { a: [q1] } }`) is allowed; the system
converts it to valid JSON.

---

## GUI Components

### Main Menu

- **TEST a model** --- Placeholder for testing interface
- **CREATE a model** --- Opens the detailed delta-format help window
- **QUIT** --- Exits with confirmation

---

## Future Roadmap

- [ ] Full model creation UI
- [ ] Recent model tracking

---

## Contributing

Pull requests are welcome!\
Steps: 1. Fork the repo\
2. Create a branch (`feature/my-feature`)\
3. Commit changes\
4. Open a PR

---

## License

MIT License.

---

## Author

**Reiss Oliveros**\
University of Portland --- Models of Computation Project
