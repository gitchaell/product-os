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
    },
    {
        "id": "v2-1-0-release.md",
        "title": "Advanced Reporting & Exporting",
        "version": "v2.1.0",
        "date": "2024-04-15",
        "type": "Feature",
        "author": "Charlie Data",
        "content": """
Our latest update introduces comprehensive reporting features that allow you to extract maximum value from your data.

## 📊 Detailed Reports

Generate in-depth reports covering user engagement, API usage, and system performance over custom date ranges.

## 📥 Export Options

You can now export reports and raw data to CSV and PDF formats directly from the dashboard.

## 🔔 Scheduled Deliveries

Set up automated report deliveries to your email on a daily, weekly, or monthly basis.
        """
    },
    {
        "id": "v2-1-1-patch.md",
        "title": "Minor Fixes and Enhancements",
        "version": "v2.1.1",
        "date": "2024-04-20",
        "type": "Bugfix",
        "author": "Dana Support",
        "content": """
This patch addresses several minor bugs reported by our community and includes a few quality-of-life enhancements.

- Fixed an issue where the date picker would occasionally reset.
- Improved loading speeds on the billing page.
- Clarified error messages during failed API requests.
        """
    },
    {
        "id": "v2-2-0-integrations.md",
        "title": "New Third-Party Integrations",
        "version": "v2.2.0",
        "date": "2024-05-10",
        "type": "Feature",
        "author": "Eve Connect",
        "content": """
We're expanding our ecosystem! You can now seamlessly connect Product OS with your favorite tools.

## 🔗 Supported Integrations

- **Slack:** Receive real-time notifications directly in your team's channel.
- **Jira:** Automatically create tickets from flagged issues.
- **GitHub:** Link commits to specific feature deployments.

Explore the new Integrations tab in your settings to get started.
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
    },
    {
        "id": "dark-mode-support.md",
        "title": "Comprehensive Dark Mode",
        "status": "Launched",
        "category": "UI/UX",
        "progress": 100,
        "priority": "Medium",
        "content": """
We have successfully rolled out full dark mode support across the entire platform.

Users can now toggle between light and dark themes, or set it to respect their system preferences automatically.
        """
    },
    {
        "id": "mobile-app.md",
        "title": "Native Mobile App (iOS & Android)",
        "status": "Under Consideration",
        "category": "UI/UX",
        "progress": 0,
        "priority": "Low",
        "content": """
We are evaluating the feasibility of developing a native mobile application to allow users to manage their workspace on the go.

Current considerations include feature parity with the web application and offline capabilities.
        """
    },
    {
        "id": "ai-insights.md",
        "title": "AI-Powered Data Insights",
        "status": "In Development",
        "category": "AI",
        "progress": 30,
        "priority": "High",
        "content": """
Integrating machine learning models to automatically highlight trends and anomalies in your data.

This feature will proactively alert you to significant changes, reducing the need for manual data analysis.
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
    },
    {
        "id": "rate-limits.mdx",
        "title": "Understanding Rate Limits",
        "description": "Details on how rate limiting works and how to handle HTTP 429 responses.",
        "category": "Core API",
        "author": "Alice API Team",
        "updated_at": "2024-03-25",
        "content": """
To ensure system stability, we enforce rate limits on API requests.

## Standard Limits

Most endpoints are limited to 100 requests per minute per user.

## Handling 429 Errors

If you exceed the limit, the API will respond with an `HTTP 429 Too Many Requests` error.

You should implement an exponential backoff strategy in your application to retry requests gracefully.
        """
    },
    {
        "id": "pagination.mdx",
        "title": "API Pagination",
        "description": "How to navigate through large datasets returned by the API.",
        "category": "Core API",
        "author": "Alice API Team",
        "updated_at": "2024-04-05",
        "content": """
Endpoints that return collections use cursor-based pagination.

## Requesting Pages

Use the `limit` parameter to specify the number of items per page. The response will include a `next_cursor` value if there are more items.

Pass the `next_cursor` value as the `cursor` parameter in your subsequent request.
        """
    },
    {
        "id": "error-handling.mdx",
        "title": "Error Handling best practices",
        "description": "A guide on interpreting and handling API errors effectively.",
        "category": "Core API",
        "author": "David Support",
        "updated_at": "2024-04-10",
        "content": """
Our API uses conventional HTTP response codes to indicate the success or failure of an API request.

## Common Error Codes

- **400 Bad Request:** The request was invalid or cannot be otherwise served.
- **401 Unauthorized:** Missing or incorrect authentication credentials.
- **403 Forbidden:** The authenticated user does not have access to the requested resource.
- **404 Not Found:** The requested resource could not be found.
- **500 Internal Server Error:** Something went wrong on our end.
        """
    }
]


def write_md(folder, item):
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, item['id'])
    content = "---\n"
    for k, v in item.items():
        if k not in ['id', 'content']:
            if isinstance(v, str) and k != 'date' and k != 'updated_at':
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
