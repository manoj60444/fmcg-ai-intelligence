"""
Layer 4: Conversational AI
Integrates with Google Gemini to provide intelligent, context-aware responses.
"""

import google.generativeai as genai
from config.settings import GEMINI_API_KEY, GEMINI_MODEL

# Configure Gemini
if GEMINI_API_KEY and GEMINI_API_KEY != "YOUR_GEMINI_API_KEY_HERE":
    # Show first 4 characters for debugging (safe)
    print(f"DEBUG: Using Gemini Key starting with: {GEMINI_API_KEY[:4]}...")
else:
    print("DEBUG: Gemini API Key NOT FOUND or placeholder used.")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)

def get_demo_responses(alert, ops_count):
    """
    Return a dict of keyword-pattern → response for the chat layer.
    Used for quick-button suggestions.
    """
    zone = alert['Zone']
    responses = {
        f"why is {zone.lower()} zone performance dropping": f"Analyzing the multi-factor decline in {zone}...",
        "what happens if no action is taken": "Modeling the 30-60-90 day risk projections...",
        "what corrective action do you recommend": "Generating high-impact mitigation strategies..."
    }
    return responses

def match_response(user_input, demo_responses, alert):
    """
    Calls Google Gemini to provide real-time intelligence based on context.
    """
    try:
        # Create a detailed system prompt with the current alert context
        system_prompt = f"""
        You are the FMCG Operational Intelligence Oracle. 
        Analyze the anomaly in the {alert['Zone']} Zone.
        
        CONTEXT:
        - Zone: {alert['Zone']}
        - Cluster: {alert['Cluster']}
        - Distributors Affected: {alert['Distributors_Affected']}
        - Sales Drop: {alert['Sales_Drop']}
        - Credit Days Increase: {alert['Credit_Increase']}
        - Confidence Score: {alert['Confidence']}
        - Projected Revenue Risk: {alert['Projected_Risk']}
        
        YOUR ROLE:
        - Provide high-end, professional, and data-driven answers.
        - Use metrics and professional FMCG terminology.
        - Format your response using clean Markdown.
        """

        # Generate content using Gemini
        msg = f"{system_prompt}\n\nUSER QUESTION: {user_input}"
        response = model.generate_content(msg)
        
        return response.text

    except Exception as e:
        return f"⚠️ **AI Connection Error (Gemini):** {str(e)}\n\n*Please ensure your API key is valid.*"
