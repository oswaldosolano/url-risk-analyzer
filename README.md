# URL Risk Analyzer

An educational API that analyzes URLs for basic phishing and security risk signals.

## Problem

Suspicious URLs can use simple patterns to mislead users. This project will identify selected, non-invasive indicators of risk without visiting or scanning the provided URL.

## Planned features

- Analyze whether a URL uses HTTPS.
- Detect IP addresses used as hosts.
- Flag unusually long URLs, many subdomains, and suspicious characters.
- Return a risk score, risk level, and human-readable reasons.
- Expose the analysis through a Python API.
- Store analysis history in PostgreSQL.

## Planned technologies

- Python
- FastAPI
- PostgreSQL
- Pytest
- Git and GitHub

## Status

In development.

## Safety note

This is an educational project. It does not visit, scan, or attack URLs, and it is not a replacement for a real security solution.