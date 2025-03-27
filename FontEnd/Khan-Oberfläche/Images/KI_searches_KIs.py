# pip install openai==0.28
import requests
import openai

# === Configuration ===
GOOGLE_API_KEY = "AIzaSyCCTtud8DuE2-UUSip6HehdWJ4VltUIldc"  # Your Google API key
CUSTOM_SEARCH_ENGINE_ID = "117017048ee1b4217"  # Your Custom Search Engine ID (cx)
OPENAI_API_KEY = "YOUR-OPENAI-API-KEY"
# =======================

def generate_search_keywords(query_description, openai_api_key):
    """
    Uses the gpt-4o-mini model to generate a broad Google search query string
    for AI solutions related to voice cloning and text-to-speech. The prompt instructs the model
    to return a natural plain-English query without enclosing it in quotes or adding overly strict boolean operators.
    """
    openai.api_key = openai_api_key
    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert search query generator. Generate a natural, broad Google search query in plain English "
                "that, when used, will return a range of relevant pages—including official product pages and company websites—"
                "for AI voice cloning and text-to-speech solutions. Do not enclose the query in quotes and do not include unnecessary punctuation."
            )
        },
        {
            "role": "user",
            "content": f"Generate a search query for the request: '{query_description}'."
        }
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.5,
            max_tokens=60
        )
        search_keywords_raw = response.choices[0].message.content.strip()
        # Clean up to form a single-line string
        search_keywords = " ".join(search_keywords_raw.split())
        return search_keywords
    except Exception as e:
        print("Error generating search keywords:", str(e))
        return query_description

def get_google_search_results(query, google_api_key, cx, count=5):
    """
    Retrieve search results from the Google Custom Search JSON API using the provided keys.
    This version also filters out pages that are obviously not official AI tool pages—such as blog posts.
    """
    if not google_api_key or not cx:
        print("Error: Google API key and Custom Search Engine ID are required.")
        return None

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": google_api_key,
        "cx": cx,
        "q": query,
        "num": count  # up to 10 results per query
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error retrieving search results from Google:", response.status_code)
        try:
            error_details = response.json()
            print("Error details:", error_details)
        except Exception:
            print("Response content:", response.text)
        return None

    results = response.json()

    # Debug: print the full JSON response (optional)
    print("Full Google API Response:", results)

    # Light filtering: remove results that are clearly not official tool pages.
    if "items" in results:
        filtered_items = []
        for item in results["items"]:
            link = item.get("link", "").lower()
            # Filter out common video sites
            if "youtube.com" in link or "youtu.be" in link:
                continue
            # Filter out blog posts (assuming product pages rarely include '/blog/' in the URL)
            if "/blog/" in link:
                continue
            filtered_items.append(item)
        results["items"] = filtered_items

    return results

def summarize_results_with_chatgpt(search_results, original_query, openai_api_key):
    """
    Uses the gpt-4o-mini model to summarize the search results.
    This version instructs the model to only list actual AI tools (official product pages or company websites)
    that provide solutions for the user's query, excluding blog posts, reviews, and comparisons.
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
            snippets.append(f"Name: {title}\nSnippet: {snippet}\nURL: {link}")
    else:
        snippets.append("No search results found.")

    search_context = "\n\n".join(snippets)

    prompt = (
        f"The original request is: '{original_query}'.\n\n"
        "Below are Google search results related to the request:\n\n"
        f"{search_context}\n\n"
        f"Based on the above search results, please provide an objective summary listing only the actual AI tools or products that can help with '{original_query}'. "
        "Only include official product pages or company websites that directly offer an AI solution, and do not include blog posts, review articles, or comparison pages. "
        "For each tool, list its name, a brief description, and the URL. If no official tool is found, state that explicitly. "
        "Format the output so that 'Description' and 'URL' are not treated as list items."
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant summarizing search results and listing only official AI tool solutions. "
                "Do not include aggregated blog posts, reviews, or comparisons."
            )
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