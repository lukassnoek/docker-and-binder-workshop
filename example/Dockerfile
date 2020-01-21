# Base image
FROM ubuntu:20.04

# Install vim and htop as an example
# Note the 'apt-get update', necessary to update
# the package register and the -y flag after install,
# which skips the y/n prompt when installing
RUN apt-get update && apt-get install -y vim
RUN apt-get install -y htop

# Define what the container should run when started
ENTRYPOINT ["/bin/echo", "Hello,"]

# Add default argument, which can be overridden when
# adding custom arguments to the "docker run" call.
CMD ["John Doe"]