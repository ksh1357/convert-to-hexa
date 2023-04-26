def dec_to_hex(decimal):
    """
    10진수를 16진수로 변환
    Args:
        decimal(int, float): 10진수
    Returns:
        str: 16진수 문자열
    """
    answer = ""
    hex_digits = "0123456789abcdef"
    hex_str = ""
    # float인 경우 int로 형 변환
    if isinstance(decimal, (int, float)):
        decimal = int(decimal)
    elif isinstance(decimal, str) and decimal.isdigit():
        decimal = int(decimal)
    # input type이 올바르지 않은 경우
    else:
        raise ValueError("Invalid decimal number")
    # 음수인 경우
    if decimal < 0:
        # 32-bit binary string으로 변환
        binary_str = bin(decimal & 0xffffffff)[2:]
        complement_str = "".join(["1" if b == "0" else "0" for b in binary_str])
        decimal = int(complement_str, 2) + 1
        answer = "-"
    while decimal > 0:
        remainder = decimal % 16
        hex_str = hex_digits[remainder] + hex_str
        decimal //= 16
    answer += "0x" + hex_str
    return answer
