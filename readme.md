1. read_test.py [ GATT Read Test Program ]
 => read_test.py "Device Name" "SERVICE_UUID" "CHARACTERISTIC_UUID"
 => ex) python3 read_test.py "Unknown" "00001800-0000-1000-8000-00805f9b34fb" "00002a00-0000-1000-8000-00805f9b34fb"

2. write_test.py [ GATT Write Test Program ]
=> write_test.py "SERVICE_UUID" "CHARACTERISTIC_UUID" "WRITE_VALUE" NEED_RESPONSE
=> ex) python3 read_test.py "Unknown" "00001800-0000-1000-8000-00805f9b34fb" "00002a00-0000-1000-8000-00805f9b34fb" "Hello_World" 1
