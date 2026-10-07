from urllib.parse import urlparse
import ipaddress


def get_risk_level(score: int) -> str:
    if score >= 50:
        return "high"
    if score >= 20:
        return "medium"
    return "low"

def is_ip_address(host: str | None) -> bool:
    if not host:
        return False
    
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False
    
def count_subdomains(host: str | None) -> int:
    if not host or is_ip_address(host):
        return 0
    
    parts = host.split(".")
    return max(0, len(parts) - 2)    


def analyze_url(url: str) -> dict:
    """
    Analyze a URL and return its risk score, level, and reasons.
    """
    parsed_url = urlparse(url)
    risk_score = 0
    reasons = []

    if parsed_url.scheme != "https":
        risk_score += 20
        reasons.append("The URL does not use HTTPS")

    if is_ip_address(parsed_url.hostname):
        risk_score += 30
        reasons.append("The host is an IP address")
        
    if len (url) > 100:
        risk_score += 15
        reasons.append("The URL is unusually long")
        
    if "@" in url:
        risk_score += 25
        reasons.append("The URL contains an at sign")
    
    if count_subdomains(parsed_url.hostname) > 3:
            
            risk_score += 15
            reasons.append("The URL has many subdomains")    
    
    if "%" in url:
        risk_score += 10
        reasons.append("The URl contains encoded characteres")

    return {
        "url": url,
        "risk_score": risk_score,
        "risk_level": get_risk_level(risk_score),
        "reasons": reasons,
    }
    


if __name__ == "__main__":
    example_url = "http://192.168.1.1/login%20admin"
    print(analyze_url(example_url))