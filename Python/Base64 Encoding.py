import base64

def to_base_64(string):
    return base64.b64encode(string).strip("=");
    
def from_base_64(string):
    return base64.b64decode(string + "===");