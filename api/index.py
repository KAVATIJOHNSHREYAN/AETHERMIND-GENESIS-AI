import os
import sys
import subprocess

# Add project root directory to python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import run_app if hasattr(__import__('app'), 'run_app') else None

def handler(request, response):
    return {
        "statusCode": 200,
        "body": "AetherMind Genesis Engine Active"
    }
