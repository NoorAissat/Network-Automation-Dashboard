def run_command(conn, command):
    try:
        output = conn.send_command(command)
        return output
    except Exception as e:
        return f"Error running command: {e}"
