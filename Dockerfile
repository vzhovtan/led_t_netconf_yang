# Use the official image as a parent image.
FROM centos:latest

# Create and set the working directory.
RUN mkdir /led-t 
WORKDIR /led-t

# Copy the file from your host to your current location.
COPY netconf_yang_loopback.py .
COPY openconfig-interfaces.yang .

# Run the command inside your image filesystem.
RUN yum -y install epel-release python3 python-pip
RUN pip3 install --upgrade pip
RUN pip3 install ncclient
RUN pip3 install pyang

# Run the specified command within the container.
CMD [ "/bin/bash" ]