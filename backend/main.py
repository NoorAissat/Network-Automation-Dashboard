import sys
import os
# Ensure project root is in module search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.health import router as health_router
from backend.api.services import router as services_router
from backend.api.wireguard import router as wg_router
from backend.api.backup import router as backup_router
from backend.api.drift import router as drift_router

app = FastAPI(
    title="Network Automation API",
    description="Backend API for your monitoring dashboard",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/api/health")
app.include_router(services_router, prefix="/api/services")
app.include_router(wg_router, prefix="/api/wireguard")
app.include_router(backup_router, prefix="/api/backup")
app.include_router(drift_router, prefix="/api/drift")
