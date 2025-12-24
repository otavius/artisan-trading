from decouple import config

BUY = 1
SELL = -1 
NONE = 0

SECURE_HEADER = {
    "Authorization": f"Bearer {config("OANDA_API_KEY")}",
    "Content-Type": "application/json"
}