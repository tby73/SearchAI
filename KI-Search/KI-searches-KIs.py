# pip install openai==0.28
import requests
import openai

# === Configuration ===
GOOGLE_API_KEY = "AIzaSyCCTtud8DuE2-UUSip6HehdWJ4VltUIldc"  # Your Google API key
CUSTOM_SEARCH_ENGINE_ID = "117017048ee1b4217"  # Your Custom Search Engine ID (cx)
OPENAI_API_KEY = "REPLACE-WITH-YOUR-OPENAI-API-KEY"
# =======================

def generate_search_keywords(query_description, openai_api_key):
    """
    Uses the gpt-4o-mini model to generate effective Google search keywords
    for finding official AI solutions only, excluding YouTube and video content.
    """
    openai.api_key = openai_api_key
    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert search query generator who only provides effective "
                "Google search keywords that lead to official AI solutions, product pages, "
                "company homepages, or research projects. Do not include terms that might result "
                "in video tutorials, blog articles, or YouTube content. Return a concise list."
            )
        },
        {
            "role": "user",
            "content": f"Generate search keywords to find official AI solutions (excluding video tutorials or YouTube) for the following request: '{query_description}'."
        }
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.5,
            max_tokens=60
        )
        search_keywords = response.choices[0].message.content.strip()
        return search_keywords
    except Exception as e:
        print("Error generating search keywords:", str(e))
        return query_description  # fallback to the original query if error occurs

def get_google_search_results(query, google_api_key, cx, count=5):
    """
    Retrieve search results from the Google Custom Search JSON API using the provided keys.
    Also filter out results that are likely to be video content (e.g., YouTube).
    """
    if not google_api_key or not cx:
        print("Error: Google API key and Custom Search Engine ID are required.")
        return None

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": google_api_key,
        "cx": cx,
        "q": query,
        "num": count  # Google API allows up to 10 results per query
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error retrieving search results from Google:", response.status_code, response.text)
        return None

    results = response.json()
    # Filter out items with YouTube (or similar video) links
    if "items" in results:
        filtered_items = []
        for item in results["items"]:
            link = item.get("link", "").lower()
            if ("youtube.com" in link) or ("youtu.be" in link):
                continue
            filtered_items.append(item)
        results["items"] = filtered_items

    return results

def summarize_results_with_chatgpt(search_results, original_query, openai_api_key):
    """
    Uses the gpt-4o-mini model to summarize the search results and list useful official links.
    The summary is forced to only include official AI solutions, excluding video tutorials or YouTube pages.
    """
    if not openai_api_key:
        print("Error: No OpenAI API key provided.")
        return None

    openai.api_key = openai_api_key

    snippets = []
    if "items" in search_results and search_results["items"]:
        for item in search_results["items"]:
            title = item.get("title", "")
            snippet = item.get("snippet", "")
            link = item.get("link", "")
            # Include the link with the title and snippet.
            snippets.append(f"Name: {title}\nSnippet: {snippet}\nURL: {link}")
    else:
        snippets.append("No suitable search results found.")

    search_context = "\n\n".join(snippets)

    prompt = (
        f"The original request is: '{original_query}'.\n\n"
        f"Below are Google search results (filtered for official AI solutions) related to the request:\n\n"
        f"{search_context}\n\n"
        "Based on the above search results, please provide an objective summary of available AI solutions related to the request. "
        "Only include official product pages, company websites, or research projects that are actual AI solutions, and ignore "
        "any video tutorials, YouTube content, or non-AI tools. For each solution mentioned, include the name and a useful link."
    )

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant summarizing search results and only listing official AI solutions with useful links."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.3,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("Error calling ChatGPT API:", str(e))
        return None

def main():
    query_description = input("Enter the purpose for which you want to search available AI solutions: ").strip()

    # Generate effective search keywords using the AI.
    print("\nGenerating effective search keywords...")
    search_keywords = generate_search_keywords(query_description, OPENAI_API_KEY)
    print("Generated search keywords:", search_keywords)

    # Use the generated keywords to perform the Google search.
    print("\nSearching for available AI solutions using Google Custom Search JSON API...")
    search_results = get_google_search_results(search_keywords, GOOGLE_API_KEY, CUSTOM_SEARCH_ENGINE_ID, count=5)
    if not search_results:
        return

    # Summarize the search results.
    print("Summarizing search results with ChatGPT...")
    final_summary = summarize_results_with_chatgpt(search_results, query_description, OPENAI_API_KEY)
    if final_summary:
        print("\nFinal Summary of AI Solutions:")
        print(final_summary)
    else:
        print("Could not generate summary.")

if __name__ == "__main__":
    main()