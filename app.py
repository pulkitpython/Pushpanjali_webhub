from select import select
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import webbrowser
from streamlit_option_menu import option_menu
import base64
import os
import io

# ---- web page seing ----
st.set_page_config(page_title="Pushpanjali's Webhub", layout="wide", page_icon="images/3.ico")

# --- lottiefiles ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Helper function to convert image to base64
def image_to_base64(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Image list from static folder
image_files = ["static/2.jpg", "static/1.jpg", "static/3.jpg"]
base64_images = []

for img_path in image_files:
    if os.path.exists(img_path):
        base64_images.append(image_to_base64(img_path))
    else:
        st.error(f"Image not found: {img_path}")


# ---- Load Assets ---- 
lottie_coding = load_lottieurl("https://lottie.host/dfc447af-fc56-4d83-a133-4d54c4afd929/8j6MBv6XQ7.json")
lottie_contactnow = load_lottieurl("https://lottie.host/94501369-16f8-49c3-ac00-7ad1219bbaf3/hiTrv91g09.json")
image_Porche = Image.open("images/8.png")
image_BMW = Image.open("images/12.png")
image_logo = Image.open("images/3.png")
product_images = ["static/1.jpg", "static/2.jpg", "static/4.jpg"]  # your images

# Construct HTML
image_tags = "".join(
    f'<img src="data:image/jpeg;base64,{img}" class="carousel-image" />' for img in base64_images
)

carousel_html = f"""
<link rel="stylesheet" href="static/slider.css">
<div class="carousel-container">
     <div class="carousel-slide" id="carousel-slide">
          {image_tags}
     </div>
     <button class="carousel-button left" id="left-btn">&#10094;</button>
     <button class="carousel-button right" id="right-btn">&#10095;</button>
</div>
<script>
     document.addEventListener("DOMContentLoaded", function () {{
          let currentIndex = 0;
          const slide = document.getElementById('carousel-slide');
          const totalImages = slide.children.length;

          function moveSlide(step) {{
               currentIndex = (currentIndex + step + totalImages) % totalImages;
               slide.style.transform = `translateX(-$${{currentIndex * 100}}%)`;
          }}

          document.getElementById('left-btn').addEventListener('click', () => moveSlide(-1));
          document.getElementById('right-btn').addEventListener('click', () => moveSlide(1));
     }});
</script>
     """
# Load CSS
with open("styles/button.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def local_css(file_name):
      with open(file_name) as f:
           st.markdown(f"<style>{f.read()}</styles>", unsafe_allow_html=True)
local_css("styles/style.css")

with open("styles/carousel.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;  /* Adjust this value as needed */
        }
    </style>
    """,
    unsafe_allow_html=True
)

 # ---- home menue ----
selected = option_menu(
     menu_title=None,
     options=["Home", "Products", "Contact"], 
     icons=["house", "box-seam", "envelope"],
     orientation="horizontal"
)



if selected == "Home":
     # ---- Header Setting ----
     with st.container():
      st.write("---")
     left_column, right_column = st.columns((2,1))     
     with left_column:
               st.subheader(
                    """
                    Welcome dear users,

                    A spiritual shop to get the right product you need

                    """
               )
               st.title("This website is maded by Dr Pushpanjali Maithil")
               st.write("For any quieries please DM us for information")
               st.markdown(
                    """
                    <div class="button-container">
                        <a href="https://www.instagram.com/tarotpushpanjali/" target="_blank" class="custom-button">
                            Instagram DM
                        </a>
                    </div>        
                    """,
                    unsafe_allow_html=True
               )
                    
                    

     with right_column:
          st.image(image_logo, width=400) 
          


     # ---- Hwo I Am ----
     with st.container():
      st.write("---")
      left_column, right_column = st.columns((2,1))
     with left_column:
          st.write("A Little detail about the devloper Pulkit Maithil")
          st.write(
               """
               I maded this website using Python and streamlit:
               - Streamlit is a very good software when combines with Python
               - How mUch would you rate my website.


               to see my old Youtube videos click on the link below

               """
          )
          st.markdown(
               """
               <div class="button-container">
                    <a href="https://www.instagram.com/tarotpushpanjali/" target="_blank" class="custom-button">
                         Youtube Channel
                    </a>
               </div> 
               """,
               unsafe_allow_html=True
          )

     with right_column:
          st_lottie(lottie_coding, height=300, key="coding", speed = 200)

if selected == "Products":
     with st.container():
          st.write("---")
          st.write("##")
          image_column, text_column = st.columns((2,1))
          with image_column:
               st.markdown(carousel_html, unsafe_allow_html=True)

          with text_column:
               st.markdown("### Magnetic Bracelet")
               st.markdown("This Product Is Very Good")
               st.markdown("₹30,000/-")

     with st.container():
          st.write("---")
          st.write("##")
          image_column, text_column = st.columns((1,2))
          with image_column:
               st.image(image_BMW)

          with text_column:
               st.subheader("A BMW kinda looks cool")
               st.write(
                    """
                    So if you want to lear more about pyhon,

                    just contact me through instagram
                    """
               )
               st.markdown("[Click here for instagram](https://www.instagram.com/notpulkitatall)")

if selected == "Contact":
     with st.container():
               st.title("Contact Me Now To Learn More")
               st.write("##")

               contact_form =  """
               <form action="https://formsubmit.co/pulkitpushpanjali@gmail.com" method="POST">
               <input type="hidden" name="_captcha" value="false">
               <input type="text" name="name" placeholder="Your name" required>
               <input type="email" name="email" placeholder="Your email" required>
               <textarea name="message" placeholder="Your message here" required></textarea> 
               <button type="submit">Send</button>
          </form>
               """

               left_column, right_column = st.columns((2,1))
               with left_column:
                    st.markdown(contact_form, unsafe_allow_html=True)
               with right_column:
                    st_lottie(lottie_contactnow, height=300, key="contact", speed = 200)

          
     
     

    
