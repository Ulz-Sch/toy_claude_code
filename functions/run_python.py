import os
import subprocess
import time

from google.genai import types

def run_python_file(working_directory, file_path,args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            timeout=30,
            capture_output=True,
            text=True,
            cwd=abs_working_dir,
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        
        if output:
            return "\n".join(output)
        else:
            return "No output produced."
        
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python = types.FunctionDeclaration(
        name="run_python_file",
        description="Run a python script with arguments, if provided, in the specified directory, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file path to run the script from, relative to the working directory.",
                ),
                "args": types.Schema(
                    type=types.Type.STRING,
                    description="The arguments to run the scripts. If not provided, None is set as default by the function.",
                ),
            },
        ),
    )
    










    