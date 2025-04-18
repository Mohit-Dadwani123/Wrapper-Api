import os
import httpx

async def create_vapi_agent(request):
    payload = {
        "model": request.llm["model"],
        "name": request.agent_name,
        "instructions": request.behavior["instructions"],
        "voice": request.voice,
        "firstMessage": request.behavior["initial_message"],
        "interruptionsEnabled": request.behavior.get("allow_interruptions", False)
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.vapi.ai/v1/assistant",
            headers={"Authorization": f"Bearer {os.getenv('VAPI_API_KEY')}"},
            json=payload
        )
        response.raise_for_status()
        return response.json()