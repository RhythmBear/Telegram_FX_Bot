import requests
import json

def call_openai_api(prompt):
    # Define the API endpoint and header information
    api_endpoint = "https://api.openai.com/v1/engines/text-davinci-002/jobs"
    api_key = "YOUR_API_KEY"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Define the request data
    data = {
        "prompt": prompt,
        "max_tokens": 100,
        "n": 1,
        "stop": None,
        "temperature": 0.5
    }

    # Send the request and get the response
    response = requests.post(api_endpoint, headers=headers, json=data)

    if response.status_code == 200:
        response_json = response.json()
        return response_json["choices"][0]["text"]
    else:
        raise Exception(f"Request failed with status code {response.status_code}")

def signal_to_json_pip_builder(signal_str):
    # Split the signal string into individual properties
    properties = signal_str.split("\n")
    signal = {}
    for prop in properties:
        key, value = prop.split(": ")
        if key == "Take Profit":
            value = [float(x) for x in value.split(" ")]
        else:
            value = float(value) if "." in value and value.replace(".", "").isdigit() else value
        signal[key] = value

    return json.dumps(signal)
    
def parse_trade_info_goldscalper(trade_text):
    trade_lines = trade_text.strip().split("\n")
    # print(trade_lines)
    trade = {}
    currency_pair, order_type = trade_lines[0].split(" ")[:2]
    trade["CurrencyPair"] = currency_pair
    trade["OrderType"] = order_type
    # print(trade)
    buy_order = trade_lines[0].split(" ")[3:]
    # print(buy_order)
    # buy_order = buy_order[0].split(" - ")
    # print(buy_order)
    trade["BuyOrder"] = {"From": float(buy_order[0]), "To": float(buy_order[2])}
    # print(trade)
    for line in trade_lines[1:]:
        if line != '':
                
            key, value = line.split(": ")
            if key == "SL":
                trade["StopLoss"] = float(value)
            elif key.startswith("TP"):
                trade.setdefault("TakeProfits", []).append({key: float(value)})
        else: 
            continue
    return trade

# trade_text = """GBPJPY BUY NOW: 158.850-158.550
# SL: 158.250
# TP1:  159.050
# TP2:  159.250"""

# trade = parse_trade_info_goldscalper(trade_text)
# print(trade)


# prompt = "Can you trade this Signal USDJPY-Short\nOpen Price: 136.81\nSL: 137.10\nMinimum TP 136.65\nBase TP 136.50\nMaximum TP 136.35\nRef#: USDJPY136.81"
# response = call_openai_api(prompt)
# print(response)
