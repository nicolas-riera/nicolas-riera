from datetime import datetime, timezone

BIRTH = datetime(2006, 9, 8, 11, 30, tzinfo=timezone.utc)

now = datetime.now(timezone.utc)
hours = int((now - BIRTH).total_seconds() // 3600)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

start = "<!-- AGE_START -->"
end = "<!-- AGE_END -->"

before = content.split(start)[0]
after = content.split(end)[1]

new_block = f"""{start}
I was born {hours:,} hours ago
{end}"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(before + new_block + after)
