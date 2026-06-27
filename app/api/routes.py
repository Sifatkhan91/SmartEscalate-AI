from fastapi import APIRouter, HTTPException
import requests

from app.core.config import get_settings
from app.models.decision import DecisionRequest
from app.services.decision_service import DecisionService

router = APIRouter()

settings = get_settings()

decision_service = DecisionService()


@router.get("/")
def home():
    return {
        "application": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "running"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/decision")
def analyze(request: DecisionRequest):
    """
    Analyze a risky action and determine whether
    human approval is required.
    """
    return decision_service.analyze(request)

@router.get("/api/voice-token")
@router.post("/api/voice-token")
def get_voice_token():

    """
    Proxy endpoint used by the VocalBridge React SDK.

    React
        ↓
    GET /api/voice-token
        ↓
    SmartEscalate Backend
        ↓
    POST https://vocalbridgeai.com/api/v1/token
        ↓
    Return LiveKit credentials
    """

    if not settings.VOCALBRIDGE_API_KEY:

        raise HTTPException(
            status_code=500,
            detail="VOCALBRIDGE_API_KEY not configured."
        )

    try:

        response = requests.post(

            settings.VOCALBRIDGE_API_URL,

            headers={
                "X-API-Key": settings.VOCALBRIDGE_API_KEY,
                "X-Agent-Id": settings.VOCALBRIDGE_AGENT_ID,
                "Content-Type": "application/json"
            },

            json={
                "participant_name": "Sifat"
            },

            timeout=30

        )

        if response.status_code != 200:

            raise HTTPException(
                status_code=response.status_code,
                detail=response.text
            )

        return response.json()

    except requests.RequestException as ex:

        raise HTTPException(
            status_code=500,
            detail=f"Unable to contact VocalBridge: {str(ex)}"
        )


@router.post("/decision-response")
def decision_response(response: dict):
    """
    Placeholder endpoint.

    Later the voice agent will call this endpoint
    after the human approves or rejects the action.
    """

    return {
        "status": "received",
        "response": response
    }