# fleetqual

**FleetQual** is a command-line tool for validating and reporting on system hardware and firmware, built for infrastructure and hardware engineers who manage data center fleets.

## 🔧 Features

- Scan system specs: CPU, RAM, firmware versions, etc.
- Validate against expected configurations (customizable YAML rules)
- Generate clean Markdown reports
- Built with Python and runs on Linux-based systems

## 📁 Project Structure

```

fleetqual/
├── fleetqual.py             # Main CLI script
├── modules/
│   ├── scan.py              # System scanner
│   ├── validate.py          # Validation logic
│   └── report.py            # Report generator
├── data/
│   ├── sample_system_info.json
│   └── validation_rules.yaml
├── tests/
│   └── test_validate.py
├── README.md
└── system_diagram.png

````

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/ELew-Dev/fleetqual.git
cd fleetqual

# Run the main script
python3 fleetqual.py --help
````

## 📦 Requirements

* Python 3.10+
* Linux (recommended)
* [psutil](https://pypi.org/project/psutil/), [PyYAML](https://pypi.org/project/PyYAML/)

Once `requirements.txt` is added:

```bash
pip install -r requirements.txt
```

## 🛠️ Future Plans

* Auto-detect system misconfigurations
* Integrate with IPMI / Redfish / PXE tools
* Export reports to JSON, HTML
* Add system diagram and CLI autocomplete

## 🧪 Testing

```bash
python3 -m unittest tests/test_validate.py
```

## 📜 License

MIT

````

Now save it and commit:

```bash
git add README.md
git commit -m "Add clean and formatted README"
git push
````