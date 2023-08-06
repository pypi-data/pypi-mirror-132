FROM ubuntu:21.10 as ubuntu_base

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -yq \
&& apt-get install -yq --no-install-recommends \
    ca-certificates \
    build-essential \
    cmake \
    libboost-all-dev \
    libboost-python-dev \
    libx11-dev \
    libxrandr-dev \
    libxinerama-dev \
    libxcursor-dev \
    libasound2-dev \
    libcurl4-openssl-dev \
    libfreetype-dev \
    libgtk-4-dev \
    libwebkit2gtk-4.0-dev \
    python3 \
    python3.9-dev \
&& update-ca-certificates \
&& apt-get clean -y

RUN apt-get install -yq python3-pip git libopencv-dev
RUN pip install numpy matplotlib

# clone repo
#RUN git clone https://github.com/galchinsky/
## or copy:
WORKDIR /aptest
COPY pyproject.toml .
COPY setup.py .
COPY dryjuce dryjuce
COPY source source
COPY CMakeLists.txt .

#WORKDIR /aptest/build
#RUN cmake .. -DCMAKE_BUILD_TYPE=Debug
#RUN make -j6

RUN pip install .
