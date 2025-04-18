import os
import httpx

async def create_retell_agent(request):
    payload = {
        "agent_name": request.agent_name,
        "llm_websocket_url": request.llm["websocket_url"],
        "voice_id": request.voice["id"],
        "initial_message": request.behavior["initial_message"],
        "prompt": request.behavior["instructions"]
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.retellai.com/create-agent",
            headers={"Authorization": f"Bearer {os.getenv('RETELL_API_KEY')}"},
            json=payload
        )
        response.raise_for_status()
        return response.json()
