import sys
import traceback
from src.todo_cli.cli import authenticate_user

try:
    print("Attempting to call authenticate_user function...")
    result = authenticate_user()
    print(f"Result: {result}")
except Exception as e:
    print(f"Error occurred: {e}")
    print("Full traceback:")
    traceback.print_exc()
    print(f"Exception type: {type(e)}")