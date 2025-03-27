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
    Uses the gpt-4o-mini model to generate a simple, direct Google search query string
    for AI tools related to the user's request.
    """
    openai.api_key = openai_api_key
    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert search query generator. Generate a SIMPLE and DIRECT Google search query to find AI tools/products for the user's request. "
                "Focus on core keywords plus 'AI tool' or 'AI platform'. Avoid complex operators or excessive negative keywords unless absolutely essential for clarity. "
                "Example: If the request is 'financial advice', generate something like 'AI financial advice tool' or 'AI financial planning platform'."
            )
        },
        {
            "role": "user",
            "content": f"Generate a simple, direct search query for AI tools/products that provide: '{query_description}'."
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

def get_google_search_results(query, google_api_key, cx, count=10):
    """
    Retrieve search results from the Google Custom Search JSON API using the provided keys.
    This version uses strong filtering on the results of a simpler query.
    """
    if not google_api_key or not cx:
        print("Error: Google API key and Custom Search Engine ID are required.")
        return None

    # Ensure basic AI terms are present if not already implied by the generated query
    if not any(term in query.lower() for term in ["ai", "artificial intelligence", "machine learning", "robo-advisor"]):
         query = f"{query} AI"

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": google_api_key,
        "cx": cx,
        "q": query, # Use the simpler query
        "num": count
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

    # Filtering logic remains largely the same to catch unwanted results
    if "items" in results:
        filtered_items = []
        for item in results["items"]:
            link = item.get("link", "").lower()
            title = item.get("title", "").lower()
            snippet = item.get("snippet", "").lower()
            content = title + " " + snippet

            # Skip obvious non-product sites by URL
            if any(site in link for site in ["youtube.com", "youtu.be", "wikipedia.org", ".gov", ".edu"]):
                continue

            # Skip obvious article pages, listicles, and educational content by title
            if any(term in title for term in ["top 10", "best ai", "best tools", "how to", "what is", "guide to", "introduction", "review of", " vs ", " comparison", " trends", " future of", " list of", " examples of"]):
                continue

            # Skip academic papers
            if any(file_type in link for file_type in ["/paper/", "/publication/"]):
                 continue

            # Check for blog/news indicators
            blog_indicators = ["/blog/", "/article/", "/news/", "/post/", "forbes.com", "medium.com", "investopedia.com", "techcrunch.com", "venturebeat.com", "businessinsider.com", "barrons.com", "finextra.com", "dakota.com", "bdb-bh.com"]
            is_blog_or_news = any(indicator in link for indicator in blog_indicators)

            # Define product/advisor terms
            product_indicators = ["tool", "platform", "app", "software", "solution", "product", "service", "suite", "advisor", "robo-advisor"]
            ai_terms = ["ai", "artificial intelligence", "machine learning", "ml"]
            advisory_terms = ["advice", "advisor", "planning", "guidance", "recommendation", "robo-advisor", "financial plan"]

            # Check if the content mentions a relevant product type
            mentions_product_type = any(indicator in content for indicator in product_indicators)
            mentions_ai = any(term in content for term in ai_terms)
            mentions_advisory = any(term in content for term in advisory_terms)

            # If it's a blog/news article, only keep it if it clearly mentions a relevant product type
            # Allow if title mentions product/advisory terms even if URL is newsy
            if is_blog_or_news and not (mentions_product_type or mentions_advisory):
                continue

            # Require product-specific terms OR advisory terms
            if not (mentions_product_type or mentions_advisory):
                continue

            # Must mention AI capabilities if not explicitly an advisor/robo-advisor
            if not mentions_advisory and not mentions_ai:
                 continue

            # If advice was requested, apply stricter checks
            # Check original_query passed to this function if available, otherwise check the generated query 'q'
            # For simplicity, let's assume 'query' reflects the intent reasonably well here
            original_query_needs_advice = any(advice_term in query.lower() for advice_term in ["advice", "planning", "guidance", "recommendation"])
            if original_query_needs_advice:
                non_advisory_terms = ["tracker", "tracking", "screener", "portfolio management", "analytics"]
                has_only_non_advisory = not mentions_advisory and any(term in content for term in non_advisory_terms)

                # Skip if it only mentions non-advisory terms when advice is needed
                if has_only_non_advisory:
                    continue

            # Keep the result if it passes all filters
            filtered_items.append(item)

        results["items"] = filtered_items

    return results

def summarize_results_with_chatgpt(search_results, original_query, openai_api_key):
    """
    Uses the gpt-4o-mini model to summarize the search results.
    This version strictly focuses on direct AI products providing the specific function requested (e.g., advice).
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
        f"Based ONLY on the provided search results, identify and list specific AI tools or products that directly provide the functionality for '{original_query}'. "
        f"CRITICAL: If '{original_query}' involves 'advice', 'planning', or 'guidance', ONLY list tools that explicitly offer these advisory functions (like robo-advisors or AI financial planners). Do NOT list tools that only track, analyze, or manage portfolios unless they also provide personalized advice/recommendations. "
        "News articles mentioning specific tools (e.g., acquisitions of robo-advisors like WealthNavi, Nutmeg, NextCapital) ARE valid evidence if the tool itself fits the request. Extract the tool name and URL if possible, even from news. "
        "Exclude general articles, lists, educational content, and general websites. Focus solely on named AI products the user can access. "
        "For each AI tool found, present it as follows using Markdown (use exactly this format, including the bullet point, bold labels, and <br> tags for line breaks):\n"
        "*   **Name:** [Tool Name]<br>\n"
        "    **Description:** [Brief description focusing on how it fulfills the '{original_query}' request (especially advisory features if relevant)]<br>\n"
        "    **URL:** [Direct URL or 'URL not directly available']\n\n"
        "List each tool as a separate bullet point. Ensure the Name, Description, and URL for a single tool are grouped under one bullet point, separated by <br> tags."
        "If no tools matching the specific request (especially the advisory function, if applicable) are found in the results, state 'No specific AI tools found for {original_query}' and suggest a more targeted search query."
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are a highly discerning AI product finder. Your sole task is to identify specific, named AI tools/products from the provided search results that DIRECTLY match the user's request. "
                "If the user asks for 'advice' or 'planning', you MUST verify the tool provides this function (e.g., robo-advisor, AI planner), not just related analysis or tracking. "
                "Interpret news about specific, named tools (like acquisitions) as valid mentions. "
                "Be extremely strict: NO general articles, NO listicles, NO educational content, NO general websites. Only list actual, usable AI products with names and URLs. "
                "Format the output using Markdown bullet points for each tool, with bold labels for Name, Description, and URL within each bullet point, using <br> tags for line breaks as specified in the user prompt. "
                "If the results don't contain tools matching the specific request (especially advisory functions when requested), state that clearly."
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
    search_results = get_google_search_results(search_keywords, GOOGLE_API_KEY, CUSTOM_SEARCH_ENGINE_ID, count=10)
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