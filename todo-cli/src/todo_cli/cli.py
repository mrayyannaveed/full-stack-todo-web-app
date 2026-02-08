"""
CLI interface for the Todo CLI application using Click
"""
import click
import logging
from typing import Optional
from datetime import datetime
from getpass import getpass
from .service import task_service
from .models import CreateTaskRequest, UpdateTaskRequest, User, Priority
from .state import task_store
from .auth import auth_manager


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def authenticate_user() -> str:
    """
    Authenticate user by prompting for username and password
    """
    while True:
        username = click.prompt('Login username', type=str)

        # Check if user exists
        if auth_manager.user_exists(username):
            # User exists, authenticate
            password = getpass('Password: ')
            user = auth_manager.authenticate_user(username, password)
            if user:
                click.echo(f"Welcome to CLI Todo App")
                click.echo(f"Hi, {username}")
                click.echo(f"Total tasks: {task_service.get_total_task_count(username)}")
                return username
            else:
                click.echo("Invalid password. Please try again.")
                continue
        else:
            # User is new, create account
            click.echo("New account detected. Creating account...")
            password = getpass('Create password: ')
            confirm_password = getpass('Confirm password: ')

            if password != confirm_password:
                click.echo("Passwords do not match. Please try again.")
                continue

            # Register new user
            success = auth_manager.register_user(username, password)
            if success:
                click.echo(f"Welcome to CLI Todo App")
                click.echo(f"Hi, {username}")
                click.echo(f"Total tasks: {task_service.get_total_task_count(username)}")
                return username
            else:
                click.echo("Error creating account. Username may already exist. Please try again.")
                continue


def display_menu():
    """
    Display the main menu options
    """
    click.echo("\n--- Main Menu ---")
    click.echo("1. Add Tasks")
    click.echo("2. View Tasks")
    click.echo("3. Update Tasks")
    click.echo("4. Delete Tasks")
    click.echo("5. Mark as Complete / Incomplete")
    click.echo("6. Search / Filter Tasks")
    click.echo("7. Help")
    click.echo("8. Exit")
    click.echo("------------------")


def add_task_flow(username):
    """
    Interactive flow for adding a new task
    """
    try:
        title = click.prompt('Task title', type=str)

        # Prompt for priority
        priority_choice = click.prompt(
            'Priority (1: High, 2: Medium, 3: Low)',
            type=click.Choice(['1', '2', '3']),
            default='2'
        )
        priority_map = {'1': Priority.HIGH, '2': Priority.MEDIUM, '3': Priority.LOW}
        priority = priority_map[priority_choice]

        # Optional description
        description = click.prompt('Description (optional, press Enter to skip)', default='', show_default=False)
        if not description:
            description = None

        # Optional due date
        due_date_str = click.prompt('Due date (YYYY-MM-DD, optional, press Enter to skip)', default='', show_default=False)
        if not due_date_str:
            due_date_str = None

        # Create the request
        request = CreateTaskRequest(
            title=title,
            priority=priority,
            description=description,
            due_date=due_date_str
        )

        # Create the task - need to pass username here
        # Since we don't have the username in this context, we'll need to update the function call
        # This will be handled by updating the calling function to pass the username
        new_task = task_service.create_task(request, username)

        # Calculate remaining time
        remaining_time = new_task.get_remaining_time()
        remaining_str = f" (due in {remaining_time.days} days)" if remaining_time and remaining_time.days > 0 else ""

        click.echo(f"Successfully created task #{new_task.id}: {new_task.title}")
        click.echo(f"Details: Priority={new_task.priority}, Status=[{new_task.status}] {remaining_str}")

        logger.info(f"Successfully added task with ID: {new_task.id}")

    except Exception as e:
        logger.error(f"Error adding task: {e}")
        click.echo(f"Error: {e}")


def view_tasks_flow(username):
    """
    Display all tasks
    """
    try:
        tasks = task_service.get_all_tasks(username)
        if not tasks:
            click.echo("No tasks found.")
            logger.info("No tasks found in the store")
            return

        click.echo(f"\n--- All Tasks ({len(tasks)} total) ---")
        for task in tasks:
            status = '[completed]' if task.status == 'completed' else '[pending]'
            due_date_str = task.due_date.strftime('%Y-%m-%d') if task.due_date else 'No due date'
            description = f" - {task.description}" if task.description else ""
            remaining_time = task.get_remaining_time()
            remaining_str = f" (due in {remaining_time.days} days)" if remaining_time and remaining_time.days > 0 else ""

            click.echo(f"#{task.id} | {due_date_str} | {status} | {task.priority} | {task.title}{description}{remaining_str}")
        click.echo("-----------------------------")

        logger.info(f"Successfully listed {len(tasks)} tasks")
    except Exception as e:
        logger.error(f"An error occurred while listing tasks: {e}")
        click.echo(f"An error occurred: {e}")


def update_task_flow(username):
    """
    Interactive flow for updating an existing task
    """
    try:
        task_id = click.prompt('Enter task ID to update', type=int)

        # Get the current task to show current values
        current_task = task_service.get_task(task_id, username)
        if not current_task:
            click.echo(f"Task with ID {task_id} not found")
            logger.warning(f"Task with ID {task_id} not found for update")
            return

        click.echo(f"Current task: #{current_task.id} - {current_task.title}")

        # Get new values (with current values as defaults)
        new_title = click.prompt(f'New title (current: "{current_task.title}", press Enter to keep current)', default=current_task.title, show_default=False)
        new_description = click.prompt(f'New description (current: "{current_task.description or "None"}", press Enter to keep current)', default=current_task.description or '', show_default=False)

        # If the default value was an empty string and user pressed Enter, keep it as None
        if current_task.description is None and new_description == '':
            new_description = None

        # Update the task
        updated_task = task_service.update_task(task_id, username, new_title if new_title != current_task.title else None,
                                              new_description if new_description != current_task.description else None)

        if updated_task:
            click.echo(f"Updated task: #{updated_task.id} - {updated_task.title} [{'x' if updated_task.status == 'completed' else ' '}]")
            logger.info(f"Successfully updated task with ID: {updated_task.id}")
        else:
            click.echo(f"Task with ID {task_id} not found")
            logger.warning(f"Task with ID {task_id} not found for update")
    except Exception as e:
        logger.error(f"Error updating task: {e}")
        click.echo(f"Error: {e}")


def delete_task_flow(username):
    """
    Interactive flow for deleting a task
    """
    try:
        task_id = click.prompt('Enter task ID to delete', type=int)

        success = task_service.delete_task(task_id, username)
        if success:
            click.echo(f"Deleted task with ID: {task_id}")
            logger.info(f"Successfully deleted task with ID: {task_id}")
        else:
            click.echo(f"Task with ID {task_id} not found")
            logger.warning(f"Task with ID {task_id} not found for deletion")
    except Exception as e:
        logger.error(f"An error occurred while deleting task: {e}")
        click.echo(f"An error occurred: {e}")


def mark_complete_incomplete_flow(username):
    """
    Interactive flow for marking a task as complete/incomplete
    """
    try:
        task_id = click.prompt('Enter task ID to toggle completion status', type=int)

        # Get current task to check current status
        current_task = task_service.get_task(task_id, username)
        if not current_task:
            click.echo(f"Task with ID {task_id} not found")
            logger.warning(f"Task with ID {task_id} not found for completion toggle")
            return

        if current_task.status == 'completed':
            # Mark as incomplete
            updated_task = task_service.mark_incomplete(task_id, username)
            action = "incomplete"
        else:
            # Mark as complete
            updated_task = task_service.mark_complete(task_id, username)
            action = "complete"

        if updated_task:
            click.echo(f"Marked task as {action}: #{updated_task.id} - {updated_task.title}")
            logger.info(f"Successfully marked task as {action} with ID: {updated_task.id}")
        else:
            click.echo(f"Task with ID {task_id} not found")
            logger.warning(f"Task with ID {task_id} not found for completion toggle")
    except Exception as e:
        logger.error(f"An error occurred while toggling task completion: {e}")
        click.echo(f"An error occurred: {e}")


def search_tasks_flow(username):
    """
    Interactive flow for searching/filtering tasks
    """
    try:
        search_term = click.prompt('Enter search term (ID or title)', type=str)

        # Try to convert to int to see if it's an ID search
        try:
            task_id = int(search_term)
            search_by = "id"
        except ValueError:
            # It's a title search
            search_by = "title"

        results = task_service.search_tasks(search_term, username, search_by)

        if not results:
            click.echo(f"No tasks found matching '{search_term}'")
            return

        click.echo(f"\n--- Search Results ({len(results)} found) ---")
        for task in results:
            status = '[completed]' if task.status == 'completed' else '[pending]'
            due_date_str = task.due_date.strftime('%Y-%m-%d') if task.due_date else 'No due date'
            description = f" - {task.description}" if task.description else ""
            remaining_time = task.get_remaining_time()
            remaining_str = f" (due in {remaining_time.days} days)" if remaining_time and remaining_time.days > 0 else ""

            click.echo(f"#{task.id} | {due_date_str} | {status} | {task.priority} | {task.title}{description}{remaining_str}")
        click.echo("-----------------------------")

    except Exception as e:
        logger.error(f"An error occurred while searching tasks: {e}")
        click.echo(f"An error occurred: {e}")


def help_flow():
    """
    Display help information about the application
    """
    click.echo("\n--- Todo CLI Application Help ---")
    click.echo("This application helps you manage your tasks efficiently.")
    click.echo("\nAvailable Features:")
    click.echo("• Add Tasks: Create new tasks with title, priority, description, and due date")
    click.echo("• View Tasks: See all your tasks with their status and details")
    click.echo("• Update Tasks: Modify existing task title or description")
    click.echo("• Delete Tasks: Remove tasks that are no longer needed")
    click.echo("• Mark Complete/Incomplete: Update task completion status")
    click.echo("• Search/Filter Tasks: Find specific tasks by ID or title")
    click.echo("• User Authentication: Secure login with username/password")
    click.echo("\nPriority Levels:")
    click.echo("• High: Urgent tasks that need immediate attention")
    click.echo("• Medium: Regular tasks with normal priority")
    click.echo("• Low: Tasks that can wait")
    click.echo("\nTask Status:")
    click.echo("• Pending: Tasks that need to be completed")
    click.echo("• Completed: Tasks that have been finished")
    click.echo("\nFor support, contact: todo-cli-support@example.com")
    click.echo("-----------------------------------")


def main_menu_loop(username: str):
    """
    Main menu loop for the application
    """
    while True:
        display_menu()

        try:
            choice = click.prompt('Select an option', type=click.Choice(['1', '2', '3', '4', '5', '6', '7', '8']), default='8')

            if choice == '1':
                add_task_flow(username)
            elif choice == '2':
                view_tasks_flow(username)
            elif choice == '3':
                update_task_flow(username)
            elif choice == '4':
                delete_task_flow(username)
            elif choice == '5':
                mark_complete_incomplete_flow(username)
            elif choice == '6':
                search_tasks_flow(username)
            elif choice == '7':
                help_flow()
            elif choice == '8':
                click.echo("Goodbye!")
                break
        except KeyboardInterrupt:
            click.echo("\nGoodbye!")
            break
        except Exception as e:
            logger.error(f"An error occurred in main menu: {e}")
            click.echo(f"An error occurred: {e}")


def main():
    """
    Main entry point for the CLI application
    """
    try:
        # Authenticate user
        username = authenticate_user()

        # Enter main menu loop
        main_menu_loop(username)

    except KeyboardInterrupt:
        click.echo("\nGoodbye!")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        click.echo(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()