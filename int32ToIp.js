/*
int32 to IPv4

Take the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.

status: solved */


function int32ToIp(int32){
    let binaryStr = int32.toString(2)
    while (binaryStr.length< 32){
        binaryStr = "0" + binaryStr
    }
    let str1 = binaryStr.substring(0,8)
    let str2 = binaryStr.substring(8, 16)
    let str3 = binaryStr.substring(16, 24)
    let str4=  binaryStr.substring(24, 32)
    str1 = parseInt(str1, 2).toString()
    str2 = parseInt(str2, 2).toString()
    str3 = parseInt(str3, 2).toString()
    str4 = parseInt(str4, 2).toString()
    return str1 + "." + str2 + "." + str3 + "." + str4
  }