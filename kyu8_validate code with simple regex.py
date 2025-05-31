import re
def validate_code(code):
    return True if re.match(r"^[123]",str(code)) else False