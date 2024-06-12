def extract_dtc(can_message):
    # Assuming can_message is a hexadecimal string representing the CAN message
    # This is a simplified example and may not work directly for your specific CANbus protocol

    # Example parsing assuming DTCs are stored in bytes 2 and 3 of the message
    dtc_bytes = can_message[4:8]  # Assuming the DTCs are in bytes 2 and 3
    dtc_code = int(dtc_bytes, 16)  # Convert hexadecimal to integer

    return dtc_code

# Example usage
can_message = "18DAF11000000000"  # Example CAN message
dtc = extract_dtc(can_message)
print("DTC:", dtc)
