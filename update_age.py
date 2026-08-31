from datetime import datetime
from zoneinfo import ZoneInfo

PARIS_TZ = ZoneInfo("Europe/Paris")
BIRTH = datetime(2006, 9, 8, 11, 30, tzinfo=PARIS_TZ)

now = datetime.now(PARIS_TZ)
hours = int((now - BIRTH).total_seconds() // 3600)

emoji = "🎂" if (now.month, now.day) == (BIRTH.month, BIRTH.day) else "🎈"

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start = "<!-- AGE_START -->"
end = "<!-- AGE_END -->"

before = content.split(start)[0]
after = content.split(end)[1]

new_block = f"""{start}
- {emoji} I was born {hours:,} hours ago
{end}"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(before + new_block + after)
