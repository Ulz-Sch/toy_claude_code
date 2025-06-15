from google.genai import types

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_files_content, get_file_content
from functions.write_file_content import schema_write_file, write_file
from functions.run_python import schema_run_python, run_python_file

available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_files_content,
            schema_write_file,
            schema_run_python
        ]
    )

def call_function(function_call_part):

    work_dir = "./calculator"

    match function_call_part.name:
        case "get_files_info":
            result = get_files_info(work_dir,**function_call_part.args)
        case "get_file_content":
            result = get_file_content(work_dir,**function_call_part.args)
        case "write_file":
            result = write_file(work_dir,**function_call_part.args)
        case "run_python_file":
            result = run_python_file(work_dir,**function_call_part.args)
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"error": f"Unknown function: {function_call_part.name}"},
                    )
                ],
            )
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )
