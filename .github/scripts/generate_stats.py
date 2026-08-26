import json
import os
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from html import escape


USERNAME = os.environ["GITHUB_USERNAME"]
TOKEN = os.environ["GITHUB_TOKEN"]
OUTPUT_FILE = "assets/github-stats.svg"


def github_request(url, method="GET", data=None):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "shin0biX-profile-stats",
    }

    request = urllib.request.Request(
        url,
        data=data,
        headers=headers,
        method=method,
    )

    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode())


def graphql(query, variables=None):
    payload = json.dumps({
        "query": query,
        "variables": variables or {},
    }).encode()

    return github_request(
        "https://api.github.com/graphql",
        method="POST",
        data=payload,
    )


def get_profile_data():
    query = """
    query($username: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $username) {
        repositories(
          first: 100
          ownerAffiliations: OWNER
          privacy: PUBLIC
        ) {
          totalCount
          nodes {
            name
            isFork
            stargazerCount
            languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
              edges {
                size
                node {
                  name
                }
              }
            }
          }
        }
        contributionsCollection(from: $from, to: $to) {
          contributionCalendar {
            totalContributions
          }
        }
      }
    }
    """

    now = datetime.utcnow()
    year_ago = now - timedelta(days=365)

    result = graphql(
        query,
        {
            "username": USERNAME,
            "from": year_ago.isoformat() + "Z",
            "to": now.isoformat() + "Z",
        },
    )

    if "errors" in result:
        raise RuntimeError(result["errors"])

    user = result["data"]["user"]
    repositories = user["repositories"]

    total_stars = 0
    languages = {}

    for repo in repositories["nodes"]:
        if repo["isFork"]:
            continue

        total_stars += repo["stargazerCount"]

        for language in repo["languages"]["edges"]:
            name = language["node"]["name"]
            size = language["size"]
            languages[name] = languages.get(name, 0) + size

    top_languages = sorted(
        languages.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    return {
        "contributions": user["contributionsCollection"]["contributionCalendar"][
            "totalContributions"
        ],
        "repositories": repositories["totalCount"],
        "stars": total_stars,
        "languages": [language[0] for language in top_languages[:3]],
    }


def generate_svg(stats):
    contributions = stats["contributions"]
    repositories = stats["repositories"]
    stars = stats["stars"]

    languages = stats["languages"]
    language_text = " · ".join(languages) if languages else "Exploring"

    updated = datetime.utcnow().strftime("%d %b %Y")

    svg = f"""<svg width="1100" height="230" viewBox="0 0 1100 230"
xmlns="http://www.w3.org/2000/svg" role="img"
aria-label="GitHub activity for {escape(USERNAME)}">

<defs>
  <linearGradient id="accent" x1="0" y1="0" x2="1100" y2="0">
    <stop offset="0%" stop-color="#58A6FF"/>
    <stop offset="50%" stop-color="#A371F7"/>
    <stop offset="100%" stop-color="#58A6FF"/>
  </linearGradient>

  <filter id="glow">
    <feGaussianBlur stdDeviation="3" result="blur"/>
    <feMerge>
      <feMergeNode in="blur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
</defs>

<!-- Background -->
<rect width="1100" height="230" rx="14" fill="#0D1117"/>
<rect x="1" y="1" width="1098" height="228" rx="14"
      fill="none" stroke="#30363D"/>

<!-- Header -->
<circle cx="42" cy="38" r="5" fill="#3FB950" filter="url(#glow)">
  <animate attributeName="opacity"
           values="1;0.35;1"
           dur="2s"
           repeatCount="indefinite"/>
</circle>

<text x="58" y="43"
      fill="#8B949E"
      font-family="monospace"
      font-size="13"
      letter-spacing="1">
  ACTIVITY // LIVE
</text>

<text x="1058" y="43"
      text-anchor="end"
      fill="#484F58"
      font-family="monospace"
      font-size="11">
  UPDATED {updated.upper()}
</text>

<line x1="32" y1="65" x2="1068" y2="65"
      stroke="#21262D"/>

<!-- Stats -->
<g font-family="monospace">

  <!-- Contributions -->
  <text x="170" y="125"
        text-anchor="middle"
        fill="#C9D1D9"
        font-size="34"
        font-weight="bold">{contributions}</text>

  <text x="170" y="155"
        text-anchor="middle"
        fill="#8B949E"
        font-size="11"
        letter-spacing="1">CONTRIBUTIONS / 365D</text>

  <!-- Repositories -->
  <text x="410" y="125"
        text-anchor="middle"
        fill="#58A6FF"
        font-size="34"
        font-weight="bold">{repositories}</text>

  <text x="410" y="155"
        text-anchor="middle"
        fill="#8B949E"
        font-size="11"
        letter-spacing="1">PUBLIC REPOSITORIES</text>

  <!-- Stars -->
  <text x="650" y="125"
        text-anchor="middle"
        fill="#A371F7"
        font-size="34"
        font-weight="bold">{stars}</text>

  <text x="650" y="155"
        text-anchor="middle"
        fill="#8B949E"
        font-size="11"
        letter-spacing="1">TOTAL STARS</text>

  <!-- Languages -->
  <text x="900" y="119"
        text-anchor="middle"
        fill="#C9D1D9"
        font-size="18"
        font-weight="bold">{escape(language_text)}</text>

  <text x="900" y="155"
        text-anchor="middle"
        fill="#8B949E"
        font-size="11"
        letter-spacing="1">TOP LANGUAGES</text>

</g>

<!-- Vertical separators -->
<line x1="290" y1="88" x2="290" y2="165" stroke="#21262D"/>
<line x1="530" y1="88" x2="530" y2="165" stroke="#21262D"/>
<line x1="770" y1="88" x2="770" y2="165" stroke="#21262D"/>

<!-- Bottom system line -->
<line x1="32" y1="194" x2="1068" y2="194"
      stroke="url(#accent)" stroke-width="1" opacity="0.5"/>

<circle r="3" fill="#58A6FF">
  <animateMotion
    path="M32,194 L1068,194"
    dur="6s"
    repeatCount="indefinite"/>
</circle>

<text x="550" y="215"
      text-anchor="middle"
      fill="#484F58"
      font-family="monospace"
      font-size="10"
      letter-spacing="2">
  SHIN0BIX // BUILD • UNDERSTAND • IMPROVE
</text>

</svg>
"""

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(svg)


if __name__ == "__main__":
    stats = get_profile_data()
    generate_svg(stats)

    print("GitHub stats generated successfully!")
    print(stats)
