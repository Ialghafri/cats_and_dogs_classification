import streamlit as st
import torch
import torchvision.models as models
from PIL import Image
from torchvision import transforms
from torchvision import models
import matplotlib.pyplot as plt


device = (
    "cpu"
    # if torch.cuda.is_available()
    # else "mps"
    # if torch.backends.mps.is_available()
    # else "cpu"
)

@st.cache_data()  # Cache the model to avoid reloading every time
def load_model():
    model = models.vgg16(pretrained=False)  # Define the model architecture
    model = torch.load('VGG16_Model.pth', weights_only=False)  
    model.eval()
    return model 

model = load_model()

transform = transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=3), # Convert grayscale to RGB
    transforms.Resize((224, 224)),  # Resize all images to 224x224
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

st.title("Cats and Dogs Classification")
st.write("Upload an image and classifiy it as a cat or as a dog!")

uploaded_file = st.file_uploader(("Upload an image"), type = ["jpeg", "jpg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="uploaded image", use_column_width= True)
    st.write("Classifying...")

    image_transformed = transform(image)

    image_transformed = image_transformed.unsqueeze(0)

    image_transformed = image_transformed.to(device)

    # model.eval()

    with torch.no_grad():
        output = model(image_transformed)

    _, predicted_class = torch.max(output, 1)

    if predicted_class.item() == 0:
        st.write('This is a cat')
        plt.imshow(image) 
        plt.show()
    else:
        st.write('This is a dog')
        plt.imshow(image) 
        plt.show()

        