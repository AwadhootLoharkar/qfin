<h1 style='text-align: center;'>Backend for QFin</h1>
<h2 style='text-align: center;'>A quantum finance application for your better future</h2>

<h3>Backend Setup</h3>

<p><b>NOTE: </b> You don't need to follow these steps and create an enviornment if you have already created enviornment in the root folder.</p>

0. Install `uv`: an extremely fast Python package installer and resolver, written in Rust.
```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# With pip.
pip install uv

# With pipx.
pipx install uv

# With Homebrew.
brew install uv

# With Pacman.
pacman -S uv
```

1. To create an evnvirnment, run the following command:
```bash
uv venv
```
2. To activate the environment, run the following command:
```bash
# On macOS and Linux.
source .venv/bin/activate

# On Windows.
.venv\Scripts\activate
```
3. To install the required packages, run the following command:
```bash
uv pip install -r requirements.txt
```

3. The usage of all scripts is given in the `scripts/usage.ipynb` file.