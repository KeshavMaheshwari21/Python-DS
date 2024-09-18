import streamlit as st
from PIL import Image
from io import BytesIO
from rembg import remove

# Streamlit app
st.title("Background Removal App")

# User can upload images for background removal
st.subheader("Upload the image to remove the background")

# Upload foreground image
uploaded_file = st.file_uploader("Upload the foreground image", type=["jpg", "png", "jpeg"])
if uploaded_file:
    img = Image.open(uploaded_file)

# If foreground image is provided
if 'img' in locals():
    st.image(img, caption="Original Image", use_column_width=True)

    # Remove background from the image
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    removed_bg = remove(img_bytes.getvalue())

    # Display the image without background
    removed_bg_img = Image.open(BytesIO(removed_bg))
    st.image(removed_bg_img, caption="Image with background removed", use_column_width=True)

    # Provide download option for the background-removed image
    removed_bg_img_bytes = BytesIO()
    removed_bg_img.save(removed_bg_img_bytes, format='PNG')
    st.download_button(
        label="Download Image with Background Removed",
        data=removed_bg_img_bytes.getvalue(),
        file_name="image_with_background_removed.png",
        mime="image/png"
    )

    # Ask for background image
    st.subheader("Upload a background image")

    bg_file = st.file_uploader("Upload a background image", type=["jpg", "png", "jpeg"], key='bg')
    if bg_file:
        bg_img = Image.open(bg_file)

    # If background image is provided
    if 'bg_img' in locals():
        # Resize the background image to match the foreground size
        bg_img = bg_img.resize(removed_bg_img.size)

        # Ensure background has an alpha channel
        if bg_img.mode != 'RGBA':
            bg_img = bg_img.convert('RGBA')

        # Overlay the foreground (with transparent background) onto the new background
        final_img = bg_img.copy()
        final_img.paste(removed_bg_img, (0, 0), removed_bg_img)

        # Display the final image
        st.image(final_img, caption="Final Image", use_column_width=True)

        # Provide download option for the final image
        final_img_bytes = BytesIO()
        final_img.save(final_img_bytes, format='PNG')
        st.download_button(
            label="Download Final Image",
            data=final_img_bytes.getvalue(),
            file_name="final_image.png",
            mime="image/png"
        )
