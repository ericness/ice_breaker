import requests


def script_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn proviles,
    Manually scrpe the information from the LinkedIn profile"""
    api_endpoint = "https://gist.githubusercontent.com/ericness/f6b5169b437bf9c2e8929af699043376/raw/7c8e563be9498dd7b2aacbdd2a6c7ca4c40e9501/eric_ness_linkedin_profile.json"
    response = requests.get(api_endpoint)

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k
        in [
            "experiences",
            "education",
        ]
    }
    data["experiences"] = data["experiences"][:3]
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
