from datetime import date
from pathlib import Path
import re

def ensure_log_entry() -> None:
    """Create or update STREAK_LOG.md with today's streak entry."""
    today = date.today().isoformat()
    log = Path("STREAK_LOG.md")

    # If the log doesn't exist, create it
    if not log.exists():
        log.write_text("# GitHub Streak Log\n\n")

    content = log.read_text()

    # Extract the highest Day number so far
    days = re.findall(r"Day (\d+)", content)
    last_day = int(days[-1]) if days else 0
    new_day = last_day + 1

    # If today's entry is missing, append it
    if today not in content:
        entry = f"- {today}: Day {new_day} – Continued the streak with another Python update.\n"
        log.write_text(content + entry)
        print(f"Logged: {entry.strip()}")
    else:
        print("Today's entry already exists. You're covered!")

if __name__ == "__main__":
    ensure_log_entry()
