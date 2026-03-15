import os
import json

changelog_data = [
    {
        "id": "v2-0-0-release.md",
        "title": "Product OS v2.0.0 is Here! 🚀",
        "version": "v2.0.0",
        "date": "2024-03-01",
        "type": "Feature",
        "author": "Alice Engineering",
        "content": """
We are thrilled to announce the official release of Product OS v2.0.0! This release brings major improvements to our core architecture, providing unparalleled performance and scalability.

## 🌟 What's New?

### Revamped Analytics Dashboard

The new analytics dashboard gives you real-time insights into your application's performance. Monitor API usage, user growth, and system health seamlessly.

- **Real-time Data:** Metrics update instantly as they happen.
- **Customizable Widgets:** Tailor your dashboard with the widgets that matter most to you.
- **Advanced Filtering:** Slice and dice your data precisely.

### Enhanced Security Measures

Security is our top priority. v2.0.0 includes new features to keep your data safe.

1.  **OAuth 2.0 Integration:** We now fully support OAuth 2.0 for third-party integrations.
2.  **MFA Enforcement:** Admins can now mandate Multi-Factor Authentication for all users in an organization.

### Infrastructure Upgrades

Under the hood, we've migrated to a new distributed architecture.

```javascript
// Example of connecting to our new edge API
const client = new ProductOSClient({
  endpoint: 'https://edge.product-os.io',
  apiKey: process.env.API_KEY,
  region: 'us-east'
});

const response = await client.metrics.getOverview();
console.log(response);
```

Thank you for your continued feedback and support!
        """
    },
    {
        "id": "v1-5-0-update.md",
        "title": "UI Overhaul & Accessibility Updates",
        "version": "v1.5.0",
        "date": "2024-02-15",
        "type": "Improvement",
        "author": "Bob Design",
        "content": """
In this update, we focused heavily on refining the user interface and ensuring our platform is accessible to everyone.

## ✨ UI Refinements

- Updated the color palette for better contrast.
- Introduced a new set of clear, recognizable icons.
- Improved the layout of the settings pages to group related configurations.

## ♿ Accessibility Improvements

We've made significant strides in meeting WCAG guidelines.

- Added ARIA labels to all interactive elements.
- Ensured keyboard navigation is fully supported across all primary workflows.
- Improved screen reader compatibility for complex data tables.

*We believe great software should be usable by all.*
        """
    }
]

roadmap_data = [
    {
        "id": "analytics-dashboard.md",
        "title": "Next-Gen Analytics Dashboard",
        "status": "In Development",
        "category": "Analytics",
        "progress": 65,
        "priority": "High",
        "content": """
We are currently building the next generation of our analytics dashboard.

## Goals

1.  Provide near real-time metric updates (latency < 1s).
2.  Allow users to create custom charts and save them to dashboards.
3.  Implement anomaly detection alerts.

Our engineering team is finalizing the data pipeline architecture to support the high throughput required for real-time updates. We are on track for a beta release next quarter.
        """
    },
    {
        "id": "new-auth-system.md",
        "title": "OAuth 2.0 and SAML SSO Integration",
        "status": "Planned",
        "category": "Security",
        "progress": 0,
        "priority": "Critical",
        "content": """
Enterprise customers need robust authentication mechanisms. We are planning a complete overhaul of our authentication system.

## Planned Features

- **OAuth 2.0 Provider:** Allow users to build applications on top of our API.
- **SAML SSO:** Seamless integration with enterprise identity providers (Okta, Azure AD, etc.).
- **Granular Permissions:** Introduce fine-grained access control lists (ACLs).

This project is currently in the design phase, and we are gathering requirements from our enterprise design partners.
        """
    }
]

docs_data = [
    {
        "id": "authentication-guide.mdx",
        "title": "API Authentication Guide",
        "description": "Learn how to securely authenticate your applications with the Product OS API.",
        "category": "Core API",
        "author": "Alice API Team",
        "updated_at": "2024-03-10",
        "content": """
To interact with the Product OS API, you must authenticate your requests. We offer two primary methods: API Keys and Bearer Tokens.

## Using API Keys

API Keys are the simplest way to get started. You can generate an API key in your account settings.

### Including the Key in Requests

Include your API key in the `Authorization` header of your HTTP requests.

```bash
curl -X GET "https://api.product-os.io/v1/users" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

> **Warning**: Never share your API key or commit it to version control. If your key is compromised, revoke it immediately and generate a new one.

## Using Bearer Tokens (OAuth)

For applications acting on behalf of a user, use OAuth 2.0 to obtain a Bearer Token.

See the [OAuth Integration Guide](/docs/oauth-integration) for detailed instructions on the authorization flow.
        """
    },
    {
        "id": "webhooks-setup.mdx",
        "title": "Configuring Webhooks",
        "description": "Set up webhooks to receive real-time notifications when events occur in your account.",
        "category": "Webhooks",
        "author": "Charlie Integration Team",
        "updated_at": "2024-03-12",
        "content": """
Webhooks allow your system to receive HTTP POST payloads whenever specific events occur within Product OS.

## 1. Create an Endpoint

First, create a public HTTP endpoint on your server that can accept POST requests.

```javascript
const express = require('express');
const app = express();
app.use(express.json());

app.post('/webhook', (req, res) => {
  const event = req.body;
  console.log(`Received event: ${event.type}`);
  // Process the event...
  res.status(200).send('Webhook received');
});

app.listen(3000, () => console.log('Webhook server listening on port 3000'));
```

## 2. Register the Webhook

Navigate to **Settings > Webhooks** in the Product OS dashboard and click **Add Webhook**.

Provide your endpoint URL and select the events you want to subscribe to (e.g., `user.created`, `invoice.paid`).

## 3. Verify Signatures

For security, we sign all webhook payloads. You should verify the signature to ensure the request originated from Product OS.

Check the `X-ProductOS-Signature` header against your webhook secret.
        """
    }
]


def write_md(folder, item):
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, item['id'])
    content = "---\n"
    for k, v in item.items():
        if k not in ['id', 'content']:
            if isinstance(v, str):
                content += f'{k}: "{v}"\n'
            else:
                content += f'{k}: {v}\n'
    content += "---\n\n"
    content += item.get('content', '')
    with open(filepath, 'w') as f:
        f.write(content)

for item in changelog_data: write_md('src/content/changelog', item)
for item in roadmap_data: write_md('src/content/roadmap', item)
for item in docs_data: write_md('src/content/docs', item)
