from datetime import date
from pathlib import Path

def ensure_log_entry(day_number: int = 1) -> None:
    """Create or update STREAK_LOG.md with today's streak entry."""
    today = date.today().isoformat()
    log = Path("STREAK_LOG.md")

    if not log.exists():
        log.write_text("# GitHub Streak Log\n\n")
    
    content = log.read_text()

    # If today's entry is missing, append it
    if today not in content:
        entry = f"- {today}: Day {day_number} – Bootstrapped the streak with a simple Python script.\n"
        log.write_text(content + entry)
        print(f"Logged: {entry.strip()}")
    else:
        print("Today's entry already exists. You're covered!")

if __name__ == "__main__":
    ensure_log_entry(day_number=1)
