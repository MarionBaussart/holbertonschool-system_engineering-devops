# 0x07-networking_basics

## 0. OSI model
![Getting Started](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/4e6a0ad87a65d7054248.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220225%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220225T123039Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=46c82dd8de411a8c2f304fc76c293860b8af19d80a642f0d09f40207540a5ff2)

![Getting Started](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/0fc96bd99faa7941b18bcae4c5f90c6acd11791d.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220225%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220225T123039Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=12dc6a0f0f79ae3356e15b3f640aa31de4ec5cf40bda0390c2c32d9ef81b06f9)

Questions:

What is the OSI model?

1. Set of specifications that network hardware manufacturers must respect
2. The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

How is the OSI model organized?

1. Alphabetically
2. From the lowest to the highest level
3. Randomly

## 1. Types of network
![Getting Started](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/4b995d4f8078b44afa968d68a98035d2bd7e8fac.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220225%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220225T123039Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=da78f563ecbbe0cc9a616d575bc03f580f20fbe6750e4c079ca90e54a7ea19a1)

LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

Questions:

What type of network a computer in local is connected to?

1. Internet
2. WAN
3. LAN

What type of network could connect an office in one building to another office in a building a few streets away?

1. Internet
2. WAN
3. LAN

What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

1. Internet
2. WAN
3. LAN

## 2. MAC and IP address
![Getting Started](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/1e348ba3bcbb094b02922f821ffeb3d8c5438b7b.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220225%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220225T123039Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3bb7b22b293737da57bb06d7eb3fae3fd8a02706ffb8f2a82dbb852006d7188e)

Questions:

What is a MAC address?

1. The name of a network interface
2. The unique identifier of a network interface
3. A network interface

What is an IP address?

1. Is to devices connected to a network what postal address is to houses
2. The unique identifier of a network interface
3. Is a number that network devices use to connect to networks

## 3. UDP and TCP
![Getting Started](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/3d92e3c4a470f8ecf4c73db511fcbbadaa002e1c.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220225%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220225T123039Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=800506d59b2bcf031e2024c9c34defe4930164711daddebfb9d9290ffcf3b92d)

Let’s fill the empty parts in the drawing above.

Questions:

Which statement is correct for the TCP box:
1. It is a protocol that is transferring data in a slow way but surely
2. It is a protocol that is transferring data in a fast way and might loss data along in the process

Which statement is correct for the UDP box:
1. It is a protocol that is transferring data in a slow way but surely
2. It is a protocol that is transferring data in a fast way and might loss data along in the process

Which statement is correct for the TCP worker:
1. Have you received boxes x, y, z?
2. May I increase the rate at which I am sending you boxes?

## 4. TCP and UDP ports
Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:

* 22 for SSH
* 80 for HTTP
* 443 for HTTPS

Note that a specific IP + port = socket.

Write a Bash script that displays listening ports:

* That only shows listening sockets
* That shows the PID and name of the program to which each socket belongs