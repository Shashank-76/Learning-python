# A virtual environment is basically an isolated Python setup for a specific project.
# The problem it solves
# When you install a library like pandas or flask using pip install, it gets installed globally — meaning all your projects share the same libraries.
# This causes problems when:

# Project A needs flask version 1.0
# Project B needs flask version 3.0
# They conflict with each other!


# What virtual environment does

# It creates a separate isolated box for each project with its own libraries and versions:
# C:\learning_python\
#     └── venv\          ← virtual environment folder
#         ├── flask 1.0  ← only for this project
#         └── pandas 2.0 ← only for this project
# So Project A and Project B can have completely different library versions without conflicting.

# How to create one
# python -m venv venv
# Activate it:

# venv\Scripts\activate

# We'll see (venv) appear in your terminal — that means you're inside the virtual environment.
# Install libraries inside it:

# pip install flask