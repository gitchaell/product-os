import os
import json

changelog_data = [
    {"id": "v2-0-0-release.md", "title": "Version 2.0.0 Release", "version": "v2.0.0", "date": "2024-03-01", "type": "Feature", "author": "Alice"},
    {"id": "v1-5-0-update.md", "title": "UI Overhaul", "version": "v1.5.0", "date": "2024-02-15", "type": "Improvement", "author": "Bob"}
]

roadmap_data = [
    {"id": "analytics-dashboard.md", "title": "Analytics Dashboard", "status": "In Development", "category": "Analytics", "progress": 60, "priority": "High"},
    {"id": "new-auth-system.md", "title": "OAuth 2.0 Integration", "status": "Planned", "category": "Security", "progress": 0, "priority": "Medium"}
]

docs_data = [
    {"id": "authentication-guide.mdx", "title": "Authentication Guide", "description": "Learn how to authenticate with the API.", "category": "Core API", "author": "Alice", "updated_at": "2024-03-10"},
    {"id": "webhooks-setup.mdx", "title": "Webhooks Setup", "description": "Configure webhooks for real-time events.", "category": "Webhooks", "author": "Charlie", "updated_at": "2024-03-12"}
]

def write_md(folder, item):
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, item['id'])
    content = "---\n"
    for k, v in item.items():
        if k != 'id':
            if isinstance(v, str):
                content += f'{k}: "{v}"\n'
            else:
                content += f'{k}: {v}\n'
    content += "---\n\n"
    content += f"This is the content for {item['title']}."
    with open(filepath, 'w') as f:
        f.write(content)

for item in changelog_data: write_md('src/content/changelog', item)
for item in roadmap_data: write_md('src/content/roadmap', item)
for item in docs_data: write_md('src/content/docs', item)
