---
title: "Core API v2"
status: "Planned"
category: "Core API"
assignees:
  - name: "Alice Smith"
    initials: "AS"
progress: 10
priority: "High"
---

# Core API v2 Development

The next major version of the Core API, introducing full GraphQL support, enhanced payload limits, and a completely rewritten caching layer designed to improve throughput by 40%.

## Key Features Planned

- **GraphQL Support:** Implement a robust GraphQL schema to allow clients to fetch only the exact data they need, reducing over-fetching and under-fetching.
- **Enhanced Payload Limits:** Increase the maximum payload size for bulk operations from 5MB to 20MB to support larger dataset processing.
- **Caching Layer Rewrite:** Replace the current caching mechanism with a Redis-backed distributed cache, optimizing response times for frequently accessed resources.
- **Improved Rate Limiting:** Introduce dynamic rate limiting based on tiered usage plans to ensure fair resource allocation.

## Milestones

1. **Schema Design:** Define the GraphQL schema and mutations.
2. **Backend Integration:** Connect GraphQL resolvers to existing services.
3. **Caching Migration:** Implement and test the new Redis caching layer.
4. **Performance Testing:** Benchmark API v2 against API v1.

We are currently in the early planning stages and gathering feedback from key stakeholders.
