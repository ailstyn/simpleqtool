# SimpleQTool - EverQuest Real-Time Buff Tracker

Native Linux EverQuest tool for real-time buff tracking, spell timers, and zone mapping.

## Features

- 📊 **Real-time Buff Tracking** - Monitor active buffs with countdown timers
- 🗺️ **Zone Map Display** - See your location on zone maps
- ⏱️ **Spell Timer Tracking** - Track spell cast times based on spellcaster level
- 🎨 **Color-Coded Warnings** - Green (safe), Yellow (warning), Red (expiring soon)
- 🐧 **Native Linux** - No WINE/Proton required
- 💻 **Cross-Platform** - Works on Linux, Windows, and macOS

## Quick Start

### Prerequisites
- Python 3.10 or higher
- Debian/Ubuntu Linux (or compatible)
- EverQuest with logs enabled
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/ailstyn/simpleqtool.git
cd simpleqtool

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python3 main.py
```

## Usage

1. Launch EverQuest and log in to your character
2. Type `/loc` in the game chat to enable location tracking
3. Run SimpleQTool: `python3 main.py`
4. Two windows will appear:
   - **Buff Tracker** - Shows active buffs with countdown timers
   - **Zone Map** - Displays your current location on the zone map

## Project Structure

```
simpleqtool/
├── main.py                 # Application entry point
├── log_parser.py          # Real-time log parsing and buff tracking
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── LICENSE                # MIT License
├── .gitignore             # Git configuration
└── ui/
    ├── __init__.py
    ├── buff_window.py     # Buff timer UI
    └── map_window.py      # Zone map display
```

## Requirements

### System
- Python 3.10+
- PyQt5
- watchdog (file monitoring)

### Game
- EverQuest installed with logs enabled
- Logs located in: `~/EverQuest/Logs/`

### Install Dependencies

```bash
pip install -r requirements.txt
```

Which installs:
- `PyQt5==5.15.9` - GUI framework
- `watchdog==3.0.0` - File system monitoring

## Configuration

Configuration files will be created in the `data/` directory:
- `config.ini` - User settings
- `spells.json` - Spell durations database
- `zones.json` - Zone coordinate mappings

## Troubleshooting

### "No EQ logs found"
**Problem**: Application can't find your log files.

**Solution**:
1. Verify EverQuest is installed: `ls -la ~/EverQuest/Logs/`
2. Generate a log entry: Run `/loc` in EverQuest
3. Check that logs exist: `ls eqlog_*.txt`

### ModuleNotFoundError: No module named 'PyQt5'
**Problem**: PyQt5 not installed in virtual environment.

**Solution**:
```bash
source venv/bin/activate
pip install PyQt5
```

### Map not displaying
**Problem**: Zone maps not found.

**Solution**:
1. Zone maps need to be populated in `assets/maps/`
2. Maps can be extracted from the original EqTool project

### Buff timers not updating
**Problem**: Buffs parsed but not showing in window.

**Solution**:
1. Verify log entries: `tail -f ~/EverQuest/Logs/eqlog_*.txt`
2. Check spell names match in spells.json
3. Ensure buff cast format is recognized

## Development

### Contributing
Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Commit: `git commit -am 'Add my feature'`
5. Push: `git push origin feature/my-feature`
6. Open a Pull Request

### Project Roadmap
- [ ] Extract zone maps from EqTool repository
- [ ] Build comprehensive spell database
- [ ] Add zone calibration for accurate map positioning
- [ ] Implement buff duration formulas for P99
- [ ] UI improvements and customization
- [ ] Debian package creation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Original EqTool: [smasherprog/EqTool](https://github.com/smasherprog/EqTool)
- EverQuest: Daybreak Games Company
- PyQt5: Riverbank Computing Limited

## Support

For issues, questions, or suggestions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Open an [Issue](https://github.com/ailstyn/simpleqtool/issues)
3. Submit a [Discussion](https://github.com/ailstyn/simpleqtool/discussions)

---

**Status**: Active Development 🚀

Last Updated: April 5, 2026
