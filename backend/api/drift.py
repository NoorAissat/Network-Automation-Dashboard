from fastapi import APIRouter
from modules.drift import detect_drift

router = APIRouter()

@router.get("")
def drift():
    file, changed, err = detect_drift()
    return {
        "report_file": file,
        "drift_found": changed,
        "error": err
    }
