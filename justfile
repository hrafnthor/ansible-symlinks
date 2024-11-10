# -----------------------------------------------------------------------------
# Variable section
# -----------------------------------------------------------------------------

python_test_path := justfile_directory() + "/tests/jsonschema"

# Path to Python venv directory
venv_dir_path := justfile_directory() + "/venv"

# Path to Python3 in venv environment
venv_python3_path := venv_dir_path + "/bin/python3"

# Indicates if directory ./venv exists or not. 
venv_dir_exists := path_exists(venv_dir_path)

# Only way to get conditional check to work in tasks is to have 
venv_dir_missing := if path_exists(venv_dir_path) == "true" { "false" } else { "true" }

# -----------------------------------------------------------------------------
# Command section
# -----------------------------------------------------------------------------

# Default behaviour when running 'just' without input.
default:
    @just --choose

# Lists the commands without prompting for selection.
list:
    @just -l

# Sets up the environment and installs dependendencies
setup:
    if {{venv_dir_missing}}; then python3 -m venv {{venv_dir_path}}; fi
    {{venv_python3_path}} -m pip install -r requirements.in

# Runs unit tests
test:
    if {{venv_dir_missing}}; then just setup; fi
    {{venv_python3_path}} -m pytest {{python_test_path}}
