"""
Layer 4: Conversational AI
Integrates with OpenAI ChatGPT to provide intelligent, context-aware responses.
"""

from openai import OpenAI
from config.settings import OPENAI_API_KEY, OPENAI_MODEL

# Initialize OpenAI Client
client = OpenAI(api_key=OPENAI_API_KEY)

def get_demo_responses(alert, ops_count):
    """
    Return a dict of keyword-pattern → response for the chat layer.
    These are still used for quick-button suggestions.
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
    Calls OpenAI GPT-4o to provide real-time intelligence based on the app's context.
    """
    try:
        # Create a detailed system prompt with the current alert context
        system_prompt = f"""
        You are the FMCG Operational Intelligence Oracle. 
        You are currently analyzing an anomaly in the {alert['Zone']} Zone.
        
        CONTEXT DATA:
        - Zone: {alert['Zone']}
        - Cluster: {alert['Cluster']}
        - Distributors Affected: {alert['Distributors_Affected']}
        - Sales Drop: {alert['Sales_Drop']}
        - Credit Days Increase: {alert['Credit_Increase']}
        - Confidence Score: {alert['Confidence']}
        - Projected Revenue Risk: {alert['Projected_Risk']}
        
        BEHAVIOUR SIGNATURE:
        The system has detected synchronized sales drops linked to scheme deactivations, 
        increased competitor pricing, and distributor credit stress.
        
        YOUR MISSION:
        - Provide high-end, professional, and data-driven answers.
        - Use professional metrics and FMCG terminology.
        - Be concise but insightful.
        - Format your response using clean Markdown.
        - If the user asks for corrective actions, focus on Scheme Reactivation, Field Force Deployment, and Credit Restructuring.
        """

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=800
        )
        
        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ **AI Connection Error:** {str(e)}\n\n*Please ensure your API key is valid and you have an active internet connection.*"
