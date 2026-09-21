# URL Risk Analyzer — Initial Design

## Purpose

URL Risk Analyzer is an educational tool that evaluates basic risk signals in a URL. It does not visit, scan, or attack the URL.

## Input

The analyzer receives one URL as text.

Example:

```text
https://example.com/login
```

## Output

The analyzer returns:

- The original URL.
- A numeric risk score.
- A risk level: `low`, `medium`, or `high`.
- A list of reasons that explain the score.

Example:

```json
{
  "url": "http://192.168.1.1/login",
  "risk_score": 50,
  "risk_level": "high",
  "reasons": [
    "The URL does not use HTTPS",
    "The host is an IP address"
  ]
}
```

## Initial Risk Rules

| Signal | Score | Reason |
|---|---:|---|
| The URL does not use HTTPS | 20 | The URL does not use HTTPS |
| The host is an IP address | 30 | The host is an IP address |
| The URL is longer than 100 characters | 15 | The URL is unusually long |
| The URL has more than three subdomains | 15 | The URL has many subdomains |
| The URL contains `@` | 25 | The URL contains an at sign |
| The URL contains encoded characters such as `%` | 10 | The URL contains encoded characters |

The final score is the sum of all applicable rules.

## Risk Levels

| Score | Level |
|---:|---|
| 0–19 | low |
| 20–49 | medium |
| 50 or more | high |

## Limitations

This tool uses simple, rule-based checks. It does not guarantee that a URL is safe or malicious. A URL with a low score can still be dangerous, and a URL with a high score can be legitimate.

## Examples

### Example 1

Input:

```text
https://www.python.org
```

Prediction:

```json
{
  "url": "https://www.python.org",
  "risk_score": 0,
  "risk_level": "low",
  "reasons": []
}
```

Explanation: it uses HTTPS, has a normal domain, and does not trigger any initial rule.

### Example 2

Input:

```text
http://192.168.1.1/login
```

Prediction:

```json
{
  "url": "http://192.168.1.1/login",
  "risk_score": 50,
  "risk_level": "high",
  "reasons": [
    "The URL does not use HTTPS",
    "The host is an IP address"
  ]
}
```

Explanation: `http` adds 20 points and using an IP address as the host adds 30 points.

### Example 3

Input:

```text
https://user@very.long.example.com/path
```

Prediction:

```json
{
  "url": "https://user@very.long.example.com/path",
  "risk_score": 25,
  "risk_level": "medium",
  "reasons": [
    "The URL contains an at sign"
  ]
}
```

Explanation: the `@` symbol can visually mislead users about the real destination. The actual host in this example is `very.long.example.com`.
