FROM debian:bullseye-slim as dev-env

# Install system tools
RUN apt-get update \
    #
    # install the things we want
    && apt-get install -y sudo git python3 python3-tk\
    #
    # clean up apt-get files
    && apt-get clean  \
    && rm -rf /var/lib/apt/lists/

# Add non-root user
ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # add non-root user to sudoers
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Install user-mode dev tools
USER $USERNAME
