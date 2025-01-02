
# setting Base Image
FROM python:3.10-slim

# set the Working Directory
WORKDIR /app

# copy Dependencies
COPY requirements.txt .

# install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the Application Code
COPY main.py . 
COPY VGG16_CPU.pth .

# expose the Port for Streamlit
EXPOSE 8501

# define the Command to Run the App
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]



# # setting Base Image
# # FROM nvidia/mps:latest
# FROM --platform=linux/arm64 nvidia/mps:latest


# # set the Working Directory
# WORKDIR /app
 
# # copy Dependencies
# COPY requirements.txt .
 
# # Add repository and install Python 3.10
 
# # RUN apt-get update 

# # RUN apt-get update && apt-get install -y --no-install-recommends \
# #     software-properties-common \
# #     && add-apt-repository ppa:deadsnakes/ppa \
# #     && apt-get update && apt-get install -y --no-install-recommends \
# #         python3.10 \
# #         python3.10-venv \
# #         python3.10-dev \
# #         python3.10-distutils \
# #     && rm -rf /var/lib/apt/lists/*
 
 
# # install Dependencies
# # RUN pip install --no-cache-dir -r requirements.txt
 
# # copy the Application Code
# COPY . .
 
# # expose the Port for Streamlit
# EXPOSE 8501
 
# # define the Command to Run the App
# CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]