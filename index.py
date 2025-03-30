import json
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler

data = [
  { "name": "3hC", "marks": 96 },
  { "name": "E4XaBjcGjr", "marks": 96 },
  { "name": "H3Zl9ns", "marks": 68 },
  { "name": "tywOk", "marks": 47 },
  { "name": "HkxkUOkz", "marks": 0 },
  { "name": "PwENC02Jad", "marks": 67 },
  { "name": "uvQ", "marks": 74 },
  { "name": "apFc8fIk", "marks": 12 },
  { "name": "kRDHh5SUI", "marks": 60 },
  { "name": "gOLi", "marks": 92 },
  { "name": "Xh3e", "marks": 74 },
  { "name": "XY2", "marks": 9 },
  { "name": "ijDnnLG", "marks": 53 },
  { "name": "Fa75SVNiV", "marks": 61 },
  { "name": "eADmV", "marks": 91 },
  { "name": "Mp2HlL3", "marks": 37 },
  { "name": "wwRRQ", "marks": 77 },
  { "name": "yKGtJSf0", "marks": 18 },
  { "name": "5r9i", "marks": 17 },
  { "name": "7u", "marks": 62 },
  { "name": "qK", "marks": 78 },
  { "name": "i", "marks": 16 },
  { "name": "z", "marks": 89 },
  { "name": "uIQvh", "marks": 42 },
  { "name": "RBKEyU", "marks": 16 },
  { "name": "Q", "marks": 11 },
  { "name": "y", "marks": 28 },
  { "name": "Ml8Yg4k3g", "marks": 32 },
  { "name": "Zu1VsDLx", "marks": 14 },
  { "name": "Bp68OTFU", "marks": 74 },
  { "name": "oz8M8Z3Gw", "marks": 27 },
  { "name": "kPlvw6vZ1V", "marks": 48 },
  { "name": "wXRYi0nai", "marks": 3 },
  { "name": "McT96PgH9", "marks": 84 },
  { "name": "vYadv9GWq1", "marks": 42 },
  { "name": "9PX", "marks": 70 },
  { "name": "ab", "marks": 14 },
  { "name": "29aEEfo", "marks": 11 },
  { "name": "a4", "marks": 88 },
  { "name": "5", "marks": 59 },
  { "name": "uYWXyj", "marks": 13 },
  { "name": "Ut5906zRiY", "marks": 56 },
  { "name": "ss5ud", "marks": 15 },
  { "name": "aoTl5gy", "marks": 46 },
  { "name": "M4", "marks": 68 },
  { "name": "b8xukP", "marks": 59 },
  { "name": "66I1Yep", "marks": 15 },
  { "name": "o8V4BCcX7", "marks": 0 },
  { "name": "ANi0wx", "marks": 46 },
  { "name": "0fZ", "marks": 79 },
  { "name": "MqvK", "marks": 92 },
  { "name": "Lv", "marks": 35 },
  { "name": "sxo", "marks": 55 },
  { "name": "6", "marks": 64 },
  { "name": "Kz0XVKabR", "marks": 62 },
  { "name": "I73SabYCOE", "marks": 17 },
  { "name": "7", "marks": 23 },
  { "name": "q", "marks": 84 },
  { "name": "DwVquNi", "marks": 25 },
  { "name": "2sMwjn5S", "marks": 83 },
  { "name": "b57RhiX", "marks": 32 },
  { "name": "i9EHj", "marks": 18 },
  { "name": "etnbJt", "marks": 52 },
  { "name": "6hznA", "marks": 27 },
  { "name": "cdauL", "marks": 20 },
  { "name": "7Tf", "marks": 12 },
  { "name": "zb2Fd7P", "marks": 17 },
  { "name": "tF", "marks": 38 },
  { "name": "ApaSN", "marks": 41 },
  { "name": "lHwFFf", "marks": 47 },
  { "name": "LsHg1jV", "marks": 64 },
  { "name": "Ce5Rmc", "marks": 18 },
  { "name": "pn2", "marks": 72 },
  { "name": "kp", "marks": 44 },
  { "name": "G3", "marks": 87 },
  { "name": "ZLIVpmRFKx", "marks": 50 },
  { "name": "wtXlh0GS", "marks": 32 },
  { "name": "rMDJcd", "marks": 4 },
  { "name": "FChT", "marks": 36 },
  { "name": "pqFZ", "marks": 44 },
  { "name": "Wd6ASlh", "marks": 83 },
  { "name": "2xl6m7", "marks": 85 },
  { "name": "OOKMhNlN6s", "marks": 0 },
  { "name": "RLyJ", "marks": 95 },
  { "name": "md", "marks": 38 },
  { "name": "dryD5M", "marks": 94 },
  { "name": "DacoAzOQ", "marks": 87 },
  { "name": "S5", "marks": 28 },
  { "name": "mA", "marks": 54 },
  { "name": "NP6p6Jnm", "marks": 48 },
  { "name": "MueVR1", "marks": 98 },
  { "name": "6R", "marks": 26 },
  { "name": "URAjW", "marks": 71 },
  { "name": "ESsgwMoqiN", "marks": 41 },
  { "name": "QN1jZMP", "marks": 67 },
  { "name": "jqnu", "marks": 59 },
  { "name": "Z5zjAPq0", "marks": 41 },
  { "name": "EpXXcas", "marks": 74 },
  { "name": "Pnf", "marks": 54 },
  { "name": "rrX9Mfp", "marks": 90 }
]
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters from the URL
        query_params = parse_qs(urlparse(self.path).query)
        names = query_params.get('name', [])  # Extract 'name' parameters as a list

        # Filter and maintain order based on the 'name' parameters
        if names:
            filtered_data = []
            for name in names:
                for item in data:
                    if item['name'] == name:
                        filtered_data.append(item)
                        break
        else:
            filtered_data = data  # Return all data if no filter is provided

        # Extract marks into a list while maintaining the order
        marks_list = [item["marks"] for item in filtered_data]

        # Respond with only the JSON object
        response = {"marks": marks_list}

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return
